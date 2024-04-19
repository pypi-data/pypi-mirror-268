from aporacle.connectors.rpc.flarepy.api import flarerpc

caller = flarerpc.get_caller()


def get_current_validators(subnet_id=None, node_ids=None):
    data = {}

    if subnet_id:
        data["subnetID"] = subnet_id

    if node_ids:
        data["nodeIDs"] = node_ids

    return caller("platform.getCurrentValidators", data)
