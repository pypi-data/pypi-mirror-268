import asyncio
import logging
from decimal import Decimal
from typing import (
    Dict,
    Optional
)

from komoutils.core import KomoBase, safe_ensure_future, PublishQueue
from web3 import Web3
from web3.contract import Contract
from web3.middleware import geth_poa_middleware

from aporacle import conf
from aporacle.connectors.evm_chain import FlareChain
from aporacle.connectors.oracle.contracts.submission.submission_contract import SubmissionContract
from aporacle.connectors.oracle.contracts.submission.submission_watcher import SubmissionWatcher
from aporacle.connectors.oracle.contracts.tso_contract_base import TsoContractBase
from aporacle.connectors.watcher.websocket_watcher import WSNewBlocksWatcher
from aporacle.network.network_base import NetworkStatus

s_decimal_0 = Decimal(0)


class Web3WalletBackend(KomoBase):
    def __init__(self,
                 rpc_url: str,
                 websocket_url: str,
                 event_output_queue: Optional[asyncio.Queue],
                 chain: FlareChain = FlareChain.SONGBIRD):
        super().__init__()

        self._chain = chain
        # Initialize Web3, accounts and contracts.
        self._w3: Web3 = Web3(Web3.HTTPProvider(rpc_url))
        self._w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        self._chain: FlareChain = chain
        self._websocket_url = websocket_url
        self._event_output_queue = event_output_queue

        # Contracts
        self._flare_v2_contracts: Dict[str, TsoContractBase] = {}

        # Blockchain data
        self._local_nonce: int = -1

        # Watchers
        self._new_blocks_watcher: Optional[WSNewBlocksWatcher] = None
        self._submission_watcher: Optional[SubmissionWatcher] = None

        self._blocks_publishing_queue: PublishQueue = PublishQueue()

        # Network
        self._check_network_task: Optional[asyncio.Task] = None
        self._network_status: NetworkStatus = NetworkStatus.STOPPED

        self.set_chain_contracts()

    @property
    def block_number(self) -> int:
        return self._new_blocks_watcher.block_number if self._new_blocks_watcher is not None else -1

    @property
    def chain(self) -> FlareChain:
        return self._chain

    @property
    def flare_v2_contracts(self) -> Dict[str, TsoContractBase]:
        return self._flare_v2_contracts

    @property
    def started(self) -> bool:
        return self._check_network_task is not None

    @property
    def network_status(self) -> NetworkStatus:
        return self._network_status

    @property
    def contracts(self) -> Dict[str, Contract]:
        return {name: contract.contract for name, contract
                in self.flare_v2_contracts.items()}

    def set_chain_contracts(self):
        self.log_with_clock(log_level=logging.INFO, msg=f"Updating chain contracts. ")

        # Initialize price provider contract data structures.
        self._flare_v2_contracts = {
            # "flare_systems_manager": FlareSystemsManagerContract(w3=self._w3,
            #                                                      address=conf.flare_systems_manager_address),
            "contract": SubmissionContract(w3=self._w3, address=conf.submission_address),
        }

    def start(self):
        if self.started:
            self.stop()

        self._check_network_task = safe_ensure_future(self._check_network_loop())
        self._network_status = NetworkStatus.NOT_CONNECTED

    def stop(self):
        if self._check_network_task is not None:
            self._check_network_task.cancel()
            self._check_network_task = None
        safe_ensure_future(self.stop_network())
        self._network_status = NetworkStatus.STOPPED

    async def start_network(self):
        self.log_with_clock(log_level=logging.INFO, msg=f"Starting back end.")
        # Create event watchers.
        self._new_blocks_watcher = WSNewBlocksWatcher(self._w3, self._websocket_url)
        self._submission_watcher = SubmissionWatcher(
            w3=self._w3,
            contract=self._flare_v2_contracts["contract"],
            blocks_watcher=self._new_blocks_watcher,
            event_output_queue=self._event_output_queue
        )

        await self._new_blocks_watcher.start_network()
        await self._submission_watcher.start_network()

    async def stop_network(self):
        # Stop the event watchers.
        if self._new_blocks_watcher is not None:
            await self._new_blocks_watcher.stop_network()
            self._new_blocks_watcher = None
            del self._new_blocks_watcher
        if self._submission_watcher is not None:
            await self._submission_watcher.stop_network()

    async def check_network(self) -> NetworkStatus:
        # Assume connected if received new blocks in last 2 minutes
        # if time.time() - self._last_timestamp_received_blocks < 60 * 2:
        return NetworkStatus.CONNECTED

        try:
            await self._update_gas_price()
        except asyncio.CancelledError:
            raise
        except Exception:
            return NetworkStatus.NOT_CONNECTED
        return NetworkStatus.CONNECTED

    async def _check_network_loop(self):
        while True:
            try:
                new_status = await asyncio.wait_for(self.check_network(), timeout=10.0)
            except asyncio.CancelledError:
                raise
            except asyncio.TimeoutError:
                new_status = NetworkStatus.NOT_CONNECTED
            except Exception:
                self.log_with_clock(log_level=logging.ERROR,
                                    msg="Unexpected error while checking for network status.", exc_info=True)
                new_status = NetworkStatus.NOT_CONNECTED

            self._network_status = new_status
            await asyncio.sleep(5.0)
