import json
import os

from web3 import Web3

from aporacle.connectors.oracle.contracts.tso_contract_base import TsoContractBase


class FtsoRewardOffersContract(TsoContractBase):

    def __init__(self,
                 w3: Web3,
                 address: str):
        super().__init__(w3, address)

    @property
    def name(self):
        return 'ftso_reward_offers_manager_contract'

    @property
    def abi(self):
        chain = os.getenv("CHAIN")
        with open(
                os.path.join(os.path.dirname(__file__), f'{self.name}_abi.{chain}.json')) as contract_abi:
            data: dict = json.load(contract_abi)
        return data["abi"]
