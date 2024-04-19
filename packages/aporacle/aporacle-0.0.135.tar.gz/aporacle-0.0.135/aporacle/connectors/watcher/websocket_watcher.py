import asyncio
import json
import logging
from contextlib import suppress
from typing import Optional, Dict, AsyncIterable, Any

import websockets
from cachetools import TTLCache
from hexbytes import HexBytes
from komoutils.core import PublishQueue, safe_ensure_future
from komoutils.core.time import the_time_now_is
from web3 import Web3
from web3.datastructures import AttributeDict
from web3.exceptions import BlockNotFound
from websockets.exceptions import ConnectionClosed

from aporacle.connectors.watcher.base_watcher import BaseWatcher


class WSNewBlocksWatcher(BaseWatcher):
    MESSAGE_TIMEOUT = 30.0
    PING_TIMEOUT = 10.0

    def __init__(self,
                 w3: Web3,
                 websocket_url: str):
        super().__init__(w3)
        self._network_on = False
        self._nonce: int = 0
        self._current_block_number: int = -1
        self._websocket_url = websocket_url
        self._node_address = None
        self._client: Optional[websockets.WebSocketClientProtocol] = None
        self._fetch_new_blocks_task: Optional[asyncio.Task] = None
        self._block_cache = TTLCache(maxsize=60, ttl=60)
        self._blocks_to_mend: list = []

        self.blocks_publishing_queue: PublishQueue = PublishQueue()

    @property
    def block_number(self) -> int:
        return self._current_block_number

    @property
    def block_cache(self) -> Dict[HexBytes, AttributeDict]:
        cache_dict: Dict[HexBytes, AttributeDict] = dict([(key, self._block_cache[key])
                                                          for key in self._block_cache.keys()])
        return cache_dict

    async def start_network(self):
        if self._fetch_new_blocks_task is not None:
            await self.stop_network()
        else:
            try:
                self._current_block_number = await self.call_async(getattr, self._w3.eth, "block_number")
            except asyncio.CancelledError:
                raise
            except Exception:
                self.log_with_clock(log_level=logging.INFO, msg="Error fetching newest Ethereum block number.",
                                    exc_info=True)
            await self.connect()
            await self.subscribe(["newHeads"])
            self._fetch_new_blocks_task: asyncio.Task = safe_ensure_future(self.fetch_new_blocks_loop())
            self._network_on = True

    async def stop_network(self):
        if self._fetch_new_blocks_task is not None:
            await self.disconnect()
            self._fetch_new_blocks_task.cancel()
            self._fetch_new_blocks_task = None
            self._network_on = False

    async def connect(self):
        try:
            self.log_with_clock(log_level=logging.INFO, msg=f"WS URL - {self._websocket_url}")
            self._client = await websockets.connect(uri=self._websocket_url)
            return self._client
        except Exception as e:
            self.log_with_clock(log_level=logging.ERROR, msg=f"ERROR in connection: {e}")

    async def disconnect(self):
        try:
            await self._client.close()
            self._client = None
        except Exception as e:
            self.log_with_clock(log_level=logging.ERROR, msg=f"ERROR in disconnection: {e}")

    async def _send(self, emit_data) -> int:
        if self._client is None:
            while True:
                await self.connect()
                if self._client is not None:
                    break
                else:
                    self.log_with_clock(log_level=logging.ERROR, msg=f"Websocket client has a value of NONE. "
                                                                     f"Will attempt to reconnect in 10 seconds. ")
                    await asyncio.sleep(10)

        self._nonce += 1
        emit_data["id"] = self._nonce
        await self._client.send(json.dumps(emit_data))
        return self._nonce

    async def subscribe(self, params) -> bool:
        emit_data = {
            "method": "eth_subscribe",
            "params": params
        }
        nonce = await self._send(emit_data)
        raw_message = await self._client.recv()
        if raw_message is not None:
            resp = json.loads(raw_message)
            if resp.get("id", None) == nonce:
                self._node_address = resp.get("result")
                return True
        return False

    async def _messages(self) -> AsyncIterable[Any]:
        try:
            while True:
                try:
                    raw_msg_str: str = await asyncio.wait_for(self._client.recv(), self.MESSAGE_TIMEOUT)
                    yield raw_msg_str
                except asyncio.TimeoutError:
                    pong_waiter = await self._client.ping()
                    await asyncio.wait_for(pong_waiter, timeout=self.PING_TIMEOUT)
        except asyncio.TimeoutError:
            self.log_with_clock(log_level=logging.WARNING, msg="WebSocket ping timed out. Going to reconnect...")
            return
        except ConnectionClosed:
            return
        finally:
            await self.disconnect()
            # Reconnect and subscribe in case a disconnect happens
            await self.connect()
            await self.subscribe(["newHeads"])

    async def fetch_new_blocks_loop(self):
        while True:
            try:
                async for raw_message in self._messages():
                    message_json = json.loads(raw_message) if raw_message is not None else None
                    if message_json.get("method", None) == "eth_subscription":
                        subscription_result_params = message_json.get("params", None)
                        incoming_block = subscription_result_params.get("result", None) \
                            if subscription_result_params is not None else None
                        if incoming_block is not None:
                            with suppress(BlockNotFound):
                                try:
                                    new_block: AttributeDict = await self.call_async(self._w3.eth.get_block,
                                                                                     incoming_block.get("hash"), True)
                                    self._current_block_number = new_block.get("number")
                                    # print(new_block.get("hash"))
                                    self.log_with_clock(log_level=logging.DEBUG,
                                                        msg=f"Block number - {self._current_block_number}. ")
                                    self._block_cache[new_block.get("hash")] = new_block
                                    # print(new_block)
                                    self.blocks_publishing_queue.publish([new_block])
                                    # self.trigger_event(NewBlocksWatcherEvent.NewBlocks, [new_block])
                                except Exception as e:
                                    self.log_with_clock(log_level=logging.ERROR, msg=f"ERROR - {e}")

            except asyncio.TimeoutError:
                self.log_with_clock(log_level=logging.ERROR, msg="Timed out fetching new block.", exc_info=True)
                await asyncio.sleep(30.0)
                await self.start_network()
            except asyncio.CancelledError as e:
                self.log_with_clock(log_level=logging.ERROR, msg=f"A Cancel Error fetching new block: {e}",
                                    exc_info=True)
                await asyncio.sleep(30.0)
                await self.start_network()
            except Exception as e:
                self.log_with_clock(log_level=logging.ERROR, msg=f"Error fetching new block: {e}", exc_info=True)
                await asyncio.sleep(5.0)
                await self.start_network()

    async def get_timestamp_for_block(self, block_hash: HexBytes, max_tries: Optional[int] = 10) -> int:
        counter = 0
        block: AttributeDict = None
        if block_hash in self._block_cache.keys():
            block = self._block_cache.get(block_hash)
        else:
            return int(the_time_now_is())
            # while block is None:
            #     if counter == max_tries:
            #         raise ValueError(f"Block hash {block_hash.hex()} does not exist.")
            #     counter += 1
            #     block = self._block_cache.get(block_hash)
            #     await asyncio.sleep(0.5)
        return block.get("timestamp")
