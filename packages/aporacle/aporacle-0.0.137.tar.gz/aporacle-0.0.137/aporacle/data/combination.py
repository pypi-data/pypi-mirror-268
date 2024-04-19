import asyncio
import logging
from typing import List, Optional, Dict

import pandas as pd
from komoutils.core import KomoBase, safe_ensure_future

from aporacle.data.asset import AssetData
from aporacle.data.gcp import download_csv_from_gcp_return_df
from aporacle.data.symbols import SymbolData


class Combination(KomoBase):
    def __init__(self, feed: str, symbols: List[str] = None):
        self.feed: str = feed
        self.symbols: Optional[list] = symbols
        self.collected: Dict[str, pd.DataFrame] = {}
        self.combined: Optional[pd.DataFrame] = None

    def combine(self, data: List[pd.DataFrame]):
        self.combined = pd.concat(data, axis=1).sort_index(axis=0)
        return self.combined

    async def symbol_data_collection_task(self, symbol: str):
        df = download_csv_from_gcp_return_df(bucket_name=self.feed, symbol=symbol)
        prefix = f'{symbol}_x_'
        df.columns = [prefix + col for col in df.columns]  # Modify columns in-place
        self.collected[symbol] = df

    async def collect_symbol_data(self):
        self.collected = {}
        await asyncio.gather(*[self.symbol_data_collection_task(symbol) for symbol in self.symbols])

    async def get(self):
        safe_ensure_future(self.collect_symbol_data())
        while True:
            if set(self.collected.keys()) == set(self.symbols):
                return self.combine(list(self.collected.values()))

            await asyncio.sleep(0.1)
