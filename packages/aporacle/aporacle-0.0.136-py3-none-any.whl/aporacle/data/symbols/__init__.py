import pandas as pd
from cachetools import TTLCache, cached
from komoutils.core import KomoBase

from aporacle import conf
from aporacle.data.db.crud import Crud


class SymbolData(KomoBase):
    def __init__(self):
        self.crud: Crud = Crud(uri=conf.mongo_database_uri, db_name=conf.mongo_database_name)

    @cached(cache=TTLCache(maxsize=1024, ttl=3600))
    def get_symbol(self, symbol: str) -> list:
        filters = {"asset": symbol}
        return self.crud.read_symbol_data(filters)

    def get(self, symbol: str) -> pd.DataFrame:
        df = pd.DataFrame(self.get_symbol(symbol))
        return df
