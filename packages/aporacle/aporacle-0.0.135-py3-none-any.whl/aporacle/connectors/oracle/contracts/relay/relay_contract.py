import json
import os

from web3 import Web3

from chain_data_collector.chain.oracle.contracts.tso_contract_base import TsoContractBase


class RelayContract(TsoContractBase):

    def __init__(self,
                 w3: Web3,
                 address: str):
        super().__init__(w3, address)

    @property
    def name(self):
        return 'relay_contract'

    @property
    def abi(self):
        chain = os.getenv("CHAIN")
        with open(
                os.path.join(os.path.dirname(__file__), f'{self.name}_abi.{chain}.json')) as contract_abi:
            data: dict = json.load(contract_abi)
        return data["abi"]
