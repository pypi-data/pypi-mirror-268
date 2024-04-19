import pandas as pd
from cachetools import TTLCache, cached
from komoutils.core import KomoBase

from aporacle import MONGODB_URI, MONGODB_NAME
from aporacle.data.db.crud import Crud


class AssetData(KomoBase):
    def __init__(self):
        self.crud: Crud = Crud(uri=MONGODB_URI, db_name=MONGODB_NAME)

    @cached(cache=TTLCache(maxsize=1024, ttl=3600))
    def get_asset(self, asset: str) -> list:
        filters = {"asset": asset}
        return self.crud.read_symbol_data(filters)

    def get(self, asset: str):
        df = pd.DataFrame(self.get_asset(asset))
        return df
