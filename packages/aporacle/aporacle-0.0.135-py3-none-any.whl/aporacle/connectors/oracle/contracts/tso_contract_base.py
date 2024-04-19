import asyncio
import logging
from typing import List, Coroutine, Union, Optional

from komoutils.core import safe_gather
from komoutils.logger import KomoLogger
from web3 import Web3
from web3.contract import Contract

from aporacle.core.utils.async_call_scheduler import AsyncCallScheduler


class TsoContractBase:
    _tso_contract_logger: Optional[KomoLogger] = None

    @classmethod
    def logger(cls) -> KomoLogger:
        if cls._tso_contract_logger is None:
            cls._tso_contract_logger = logging.getLogger(__name__)
        return cls._tso_contract_logger

    def __init__(self,
                 w3: Web3,
                 address: str):
        self._w3: Web3 = w3
        self._address: str = address
        self._name: str = ""
        self._contract: Contract = self._w3.eth.contract(address=self._address, abi=self.abi)

    @property
    def name(self):
        return NotImplementedError

    @property
    def abi(self):
        return NotImplementedError

    @classmethod
    def get_name_from_contract(cls, contract: Contract) -> str:
        raw_name: Union[str, bytes] = contract.functions.name().call()
        if isinstance(raw_name, bytes):
            retval: str = raw_name.split(b"\x00")[0].decode("utf8")
        else:
            retval: str = raw_name
        return retval

    @property
    def address(self) -> str:
        return self._address

    @property
    def contract(self) -> Contract:
        return self._contract

    async def _get_contract_info(self):
        if self._name is not None:
            return

        tasks: List[Coroutine] = [
            AsyncCallScheduler.shared_instance().call_async(func, *args)
            for func, args in [
                (self.get_name_from_contract, [self._contract]),
            ]
        ]

        try:
            name = await safe_gather(*tasks)
            self._name = name
            # self._decimals = decimals
        except asyncio.CancelledError as e:
            raise e
        except Exception:
            self.logger().network(f"Error fetching price contract info for {self._contract.address}.",
                                  exc_info=True,
                                  app_warning_msg=f"Error fetching price contract info for {self._contract.address}. "
                                                  f"Check wallet network connection")

    async def get_name(self) -> str:
        if self._name is None:
            await self._get_contract_info()
        return self._name
