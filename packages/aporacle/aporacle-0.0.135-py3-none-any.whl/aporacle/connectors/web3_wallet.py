from typing import Dict

from web3 import Web3
from web3.middleware import geth_poa_middleware

from aporacle import conf
from aporacle.connectors.evm_chain import FlareChain
from aporacle.connectors.oracle.contracts.flare_system_manager.flare_systems_manager_contract import \
    FlareSystemsManagerContract
from aporacle.connectors.oracle.contracts.submission.submission_contract import SubmissionContract
from aporacle.connectors.oracle.contracts.tso_contract_base import TsoContractBase
from aporacle.connectors.wallet_base import WalletBase


class Web3Wallet(WalletBase):
    BACKEND_SELECTION_INTERVAL = 15.0
    WALLET_EVENT_DEDUP_WINDOW_SIZE = 1024

    def __init__(self,
                 rpc_url: list,
                 chain: FlareChain = FlareChain.SONGBIRD):
        super().__init__()

        self._w3: Web3 = Web3(Web3.HTTPProvider(rpc_url[0]))
        self._w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self._chain: FlareChain = chain

        # Initialize price provider contract data structures.
        self._flare_contracts = {
            "flare_systems_manager": FlareSystemsManagerContract(w3=self._w3, address=conf.flare_systems_manager_address),
            "contract": SubmissionContract(w3=self._w3, address=conf.submission_address),
        }

    @property
    def w3(self) -> Web3:
        return self._w3

    @property
    def chain(self) -> FlareChain:
        return self._chain

    @property
    def reward_epoch(self) -> int:
        return self._flare_contracts["contract"].reward_epoch

    @property
    def current_voting_round(self) -> int:
        return self._flare_contracts["contract"].current_voting_round

    @property
    def flare_contracts(self) -> Dict[str, TsoContractBase]:
        return self._flare_contracts.copy()

    def get_asset_price(self, asset: str) -> float:
        return self._flare_contracts["contract"].get_asset_price(asset)

