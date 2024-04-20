import asyncio
from typing import List, Optional, Dict

import pandas as pd
from komoutils.core import KomoBase

from aporacle.data.gcp import download_csv_from_gcp_return_df


class Combination(KomoBase):
    def __init__(self, feed: str, symbols: List[str] = None, source: Optional[str] = "gcp"):
        self.feed: str = str(feed).replace('/', '_')
        self.symbols: Optional[list] = symbols
        self.source: str = source
        self.collected: Dict[str, pd.DataFrame] = {}
        self.combined: Optional[pd.DataFrame] = None

    def combine(self, data: List[pd.DataFrame]):
        self.combined = pd.concat(data, axis=1).sort_index(axis=0)
        return self.combined

    async def symbol_data_collection_task(self, symbol: str):
        if self.source == "gcp":
            df = download_csv_from_gcp_return_df(bucket_name=self.feed, file_name=symbol)
        else:
            raise Exception("Unsupported data source specified. ")

        prefix = f'{symbol}_x_'
        df.columns = [prefix + col for col in df.columns]  # Modify columns in-place
        df.set_index('voting_round', inplace=True)

        self.collected[symbol] = df

    async def collect_symbol_data(self):
        self.collected = {}
        await asyncio.gather(*[self.symbol_data_collection_task(symbol) for symbol in self.symbols])

    def get(self):
        asyncio.run(self.collect_symbol_data())
        sorted_dict = dict(sorted(self.collected.items(), key=lambda item: item[0]))
        return self.combine(data=list(sorted_dict.values()))
