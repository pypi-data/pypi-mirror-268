import logging
import os
from os.path import basename, dirname, abspath
from typing import Optional

from komoutils.core.time import the_time_in_iso_now_is
from komoutils.logger import KomoLogger

class SharedSetup:
    _shared_instance: "SharedSetup" = None
    _logger: Optional[KomoLogger] = None

    @classmethod
    def get_instance(cls) -> "SharedSetup":
        if cls._shared_instance is None:
            cls._shared_instance = SharedSetup()
        return cls._shared_instance

    @classmethod
    def logger(cls) -> KomoLogger:
        if cls._logger is None:
            cls._logger = logging.getLogger(__name__)
        return cls._logger

    def log_with_clock(self, log_level: int, msg: str, **kwargs):
        self.logger().log(log_level, f"{self.__class__.__name__} {msg} [clock={str(the_time_in_iso_now_is())}]",
                          **kwargs)

    def __init__(self):
        self.algorithm_name: str = ""
        self.environment: str = os.getenv("ENVIRONMENT")
        self.trades_streamer_endpoint: str = f'ws://{os.getenv("TRADES_STREAMER_ENDPOINT")}'
        print(self.trades_streamer_endpoint)

    def start(self):
        self.log_with_clock(log_level=logging.INFO, msg=f"Shared algorithm setup service started. ")

        try:
            # Get the name of the algorithm for dir name
            self.algorithm_name = str(basename(dirname(abspath(__file__)))).replace("_", "-")

        except Exception as e:
            raise e

        self.log_with_clock(log_level=logging.INFO, msg=f"Shared algorithm setup service successfully started. ")
