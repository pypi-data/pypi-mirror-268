import os
from concurrent.futures import ThreadPoolExecutor

_shared_executor = None


def get_executor() -> ThreadPoolExecutor:
    global _shared_executor
    if _shared_executor is None:
        _shared_executor = ThreadPoolExecutor()
    return _shared_executor