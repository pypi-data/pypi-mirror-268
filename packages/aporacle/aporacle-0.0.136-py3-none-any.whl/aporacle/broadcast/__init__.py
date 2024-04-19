import asyncio
import json
import logging
from typing import Optional

import websockets
from komoutils.core import KomoBase, safe_ensure_future
from komoutils.core.time import the_time_in_iso_now_is

from aporacle import conf
from aporacle.conf import WS, streams


class DataBroadcaster(KomoBase):
    def __init__(self, stream: str = 'utilities'):
        self.stream: str = stream
        self.url: str = f"{conf.WS}{streams[stream]}/ingest"
        self.broadcast_stream: asyncio.Queue = asyncio.Queue()
        self._broadcast_data_stream_task: Optional[asyncio.Task] = None

    @property
    def name(self):
        return "data_broadcaster"

    def start(self):
        self._broadcast_data_stream_task = safe_ensure_future(self._broadcast_data_stream_loop())

    async def _broadcast_data_stream_loop(self):
        self.log_with_clock(log_level=logging.INFO, msg=f"Establishing a connection to {self.url}. ")
        try:
            async with websockets.connect(self.url) as websocket:
                self.log_with_clock(log_level=logging.INFO, msg=f"Connection to {self.url} for {self.stream} data "
                                                                f"is now active. ")
                while True:
                    message = await self.broadcast_stream.get()
                    message['time_created'] = the_time_in_iso_now_is()
                    await websocket.send(json.dumps(message))
                    self.broadcast_stream.task_done()

        except Exception as e:
            self.log_with_clock(log_level=logging.ERROR, msg=f"Connection was closed. Will retry {e}")
            await asyncio.sleep(5)
            safe_ensure_future(self._broadcast_data_stream_loop())
