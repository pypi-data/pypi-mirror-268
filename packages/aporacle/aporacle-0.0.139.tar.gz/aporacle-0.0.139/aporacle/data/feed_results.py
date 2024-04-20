import asyncio
from typing import List, Optional

import pandas as pd
from komoutils.core import KomoBase

from aporacle.data.gcp import download_csv_from_gcp_return_df


class FeedResults(KomoBase):
    def __init__(self, feed: str, source: Optional[str] = "gcp"):
        self.feed: str = str(feed).replace('/', '_')
        self.source: str = source
        self.collected: Optional[pd.DataFrame] = None

    async def data_collection_task(self):
        if self.source == "gcp":
            df = download_csv_from_gcp_return_df(bucket_name=self.feed, file_name=f'{self.feed}_results'.lower())
        else:
            raise Exception("Unsupported data source specified. ")

        self.collected = df
        self.collected.set_index('voting_round', inplace=True)

    def get(self):
        asyncio.run(self.data_collection_task())
        return self.collected
