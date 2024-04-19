from typing import Any, Dict, Optional

from eth_account import Account
from eth_account.messages import defunct_hash_message
from eth_account.signers.local import LocalAccount
from komoutils.core import KomoBase
from web3 import Web3
from web3.contract.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.exceptions import BlockNotFound
from web3.middleware import geth_poa_middleware

from chain_data_collector.chain.evm_chain import FlareChain
from chain_data_collector.chain.watcher.websocket_watcher import WSNewBlocksWatcher
from chain_data_collector.core.utils.async_call_scheduler import AsyncCallScheduler


class OracleWallet(KomoBase):
    def __init__(self,
                 private_key: Any,
                 evm_rpc_url: str,
                 evm_chain_ws: str,
                 chain: FlareChain = FlareChain.SONGBIRD):
        super().__init__()

        # Initialize Web3, accounts and contracts.
        self._evm_rpc_url: str = evm_rpc_url
        self._evm_ws_url: str = evm_chain_ws

        self._w3: Web3 = Web3(Web3.HTTPProvider(evm_rpc_url))
        self._w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        self._chain: FlareChain = chain
        self._account: LocalAccount = Account.from_key(private_key)

        self._new_blocks_watcher: Optional[WSNewBlocksWatcher] = None


    @property
    def address(self) -> str:
        return self._account.address

    @property
    def get_block(self):
        block = self._w3.eth.get_block('latest')
        return block

    @property
    def block_number(self) -> int:
        return self._new_blocks_watcher.block_number if self._new_blocks_watcher is not None else -1

    @property
    def gas_price(self) -> int:
        """
        Warning: This property causes network access, even though it's synchronous.

        :return: Gas price in wei
        """
        # TODO: The gas price from Parity is not reliable. Convert to use internal gas price calculator
        return self._gas_price

    @property
    def nonce(self) -> int:
        """
        Warning: This property causes network access, even though it's synchronous.

        :return: Gas price in wei
        """
        remote_nonce: int = self.get_remote_nonce()
        retval: int = max(remote_nonce, self._local_nonce)
        self._local_nonce = retval
        return retval

    @property
    def chain(self) -> FlareChain:
        return self._chain

    def sign_hash(self, text: str = None, hexstr: str = None) -> str:
        msg_hash: str = defunct_hash_message(hexstr=hexstr, text=text)
        signature_dict: AttributeDict = self._account.signHash(msg_hash)
        signature: str = signature_dict["signature"].hex()
        return signature

    def execute_transaction(self, contract_function: ContractFunction, **kwargs) -> str:
        """
        This function WILL result in immediate network calls (e.g. to get the gas price, nonce and gas cost), even
        though it is written in sync manner.

        :param contract_function:
        :param kwargs:
        :return:
        """
        # if self._network_status is not NetworkStatus.CONNECTED:
        #     raise EnvironmentError("Cannot send transactions when network status is not connected.")

        # print(f"BACKEND ADDRESS {self.address}")
        gas_price: int = self.gas_price
        print(f"Submitted Gas price {gas_price}")
        transaction_args: Dict[str, Any] = {
            "from": self.address,
            "nonce": self.nonce,
            # "chainId": self.chain.value,
            "gasPrice": gas_price
        }
        transaction_args.update(kwargs)
        transaction: Dict[str, Any] = contract_function.buildTransaction(transaction_args)
        if "gas" not in transaction:
            estimate_gas: int = 1000000
            try:
                estimate_gas = self._w3.eth.estimateGas(transaction)
            except ValueError:
                self.logger().error("Failed to estimate gas. Using default of 1000000.")
            transaction["gas"] = estimate_gas
        signed_transaction: AttributeDict = self._account.signTransaction(transaction)
        tx_hash: str = signed_transaction.hash.hex()
        self.schedule_eth_transaction(signed_transaction, gas_price)
        return tx_hash

    async def _update_gas_price(self):
        async_scheduler: AsyncCallScheduler = AsyncCallScheduler.shared_instance()
        new_gas_price: int = await async_scheduler.call_async(getattr, self._w3.eth, "gasPrice")
        self._gas_price = new_gas_price

    def get_remote_nonce(self):
        try:
            remote_nonce = self._w3.eth.getTransactionCount(self.address, block_identifier="pending")
            return remote_nonce
        except BlockNotFound:
            return None
