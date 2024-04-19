#!/usr/bin/env python
#!/usr/bin/env python
import asyncio
import logging
from decimal import Decimal
from typing import (
    List,
    Optional
)

import pendulum
from komoutils.core import safe_ensure_future
from web3 import Web3
from web3.datastructures import AttributeDict

from aporacle import conf
from aporacle.connectors import VotingRound
from aporacle.connectors.oracle.contracts.tso_contract_base import TsoContractBase
from aporacle.connectors.watcher.base_watcher import BaseWatcher
from aporacle.connectors.watcher.contract_event_logs import ContractEventLogger
from aporacle.connectors.watcher.websocket_watcher import WSNewBlocksWatcher

s_decimal_0 = Decimal(0)

NEW_VOTING_ROUND_INITIATED_EVENT_NAME = 'NewVotingRoundInitiated'


class FlareSystemsManagerWatcher(BaseWatcher):
    def __init__(self,
                 w3: Web3,
                 contract: TsoContractBase,
                 blocks_watcher: WSNewBlocksWatcher,
                 event_output_queue: Optional[asyncio.Queue],
                 ):
        super().__init__(w3)
        self._blocks_watcher: WSNewBlocksWatcher = blocks_watcher
        self._contract = contract.contract
        self._contract_event_logger = ContractEventLogger(w3, contract.address, contract.abi)
        self._event_output_queue = event_output_queue

        self._new_blocks_queue: asyncio.Queue = self._blocks_watcher.blocks_publishing_queue.register()
        self._poll_logs_task: Optional[asyncio.Task] = None

    async def start_network(self):
        self._poll_logs_task = asyncio.ensure_future(self.poll_logs_loop())

    async def stop_network(self):
        if self._poll_logs_task is not None:
            self._poll_logs_task.cancel()
            self._poll_logs_task = None

    def did_receive_new_blocks(self, new_blocks: List[AttributeDict]):
        self._new_blocks_queue.put_nowait(new_blocks)

    async def poll_logs_loop(self):
        while True:
            try:
                new_blocks: List[AttributeDict] = await self._new_blocks_queue.get()
                # Process Events
                new_voting_entries = await self._contract_event_logger.get_new_entries_from_logs(
                    NEW_VOTING_ROUND_INITIATED_EVENT_NAME,
                    new_blocks
                )
                for new_voting_entry in new_voting_entries:
                    await self._handle_event_data(new_voting_entry)

            except asyncio.CancelledError:
                raise
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                print(e)

    async def _handle_event_data(self, event_data: AttributeDict):
        event_type: str = event_data["event"]
        if event_type == NEW_VOTING_ROUND_INITIATED_EVENT_NAME:
            self.handle_new_voting_round_event(event_data)

    def handle_new_voting_round_event(self, event_data: AttributeDict):
        stamp = pendulum.now("UTC").int_timestamp

        vr: VotingRound = VotingRound(
            event='new_voting_round_initiated',
            voting_round=stamp,
            voting_round_start=stamp,
            voting_round_end=stamp + conf.chain_voting_round_duration,
            block_number=event_data["blockNumber"],
            timestamp=pendulum.now("UTC").to_iso8601_string()
        )
        safe_ensure_future(self._event_output_queue.put(vr.model_dump()))
        self.log_with_clock(log_level=logging.INFO, msg=f"New voting round issued at block - {vr.block_number}. ")
