from decimal import Decimal
from typing import Dict

from komoutils.core import KomoBase


class WalletBase(KomoBase):
    @property
    def address(self) -> str:
        raise NotImplementedError

    def get_balance(self, asset_name: str) -> Decimal:
        raise NotImplementedError

    def get_raw_balance(self, asset_name: str) -> int:
        raise NotImplementedError

    def get_all_balances(self) -> Dict[str, Decimal]:
        raise NotImplementedError

    def send(self, address: str, asset_name: str, amount: Decimal) -> str:
        raise NotImplementedError

    def to_nominal(self, asset_name: str, raw_amount: int) -> Decimal:
        raise NotImplementedError

    def to_raw(self, asset_name: str, nominal_amount: Decimal) -> int:
        raise NotImplementedError