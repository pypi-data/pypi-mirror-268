from aporacle.connectors.rpc.flarepy.api import flarerpc

caller = flarerpc.get_caller()


def get_health():
    data = {}

    ret = caller("health.health", data)
    return ret
