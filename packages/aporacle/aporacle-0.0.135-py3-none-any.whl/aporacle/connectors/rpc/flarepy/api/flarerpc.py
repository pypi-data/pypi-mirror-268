import inspect
import requests

from aporacle.connectors.rpc.flarepy.api.apimeta import api_endpoints

host = "flare-api.flare.network"
# jsonrpc_port = "9650"
protocol = "https"
# jsonrpc_url = "{}://{}:{}".format(jsonrpc_prot, jsonrpc_host, jsonrpc_port)
url = "{}://{}".format(protocol, host)

urls = {k: ("{}" + v).format(url) for k, v in api_endpoints.items()}

# print(f"URLS {urls}")


def chain_call(url, method, params=None):
    payload = {
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 1
    }
    print(url)
    print(payload)

    # return
    # url = 'https://flare-api.flare.network/ext/bc/P'
    # payload = {"jsonrpc": "2.0", "method": "platform.getCurrentValidators", "params": {}, "id": 1}

    response = requests.post(url, json=payload).json()

    if "error" in response:
        print(response["error"]["message"])
        return

    return response["result"]


def chain_post(url, params=None):
    return requests.post(url, params)


def make_caller(url):
    def f(method, data):
        return chain_call(url, method, data)

    return f


def make_poster(url):
    def f(data):
        return chain_post(url, data)

    return f


def get_caller():
    """
    Uses the source caller's module name to determine
    which caller to return.
    Will fail if source is __main__. Do not call module
    functions directly from command line.
    """
    src_caller = inspect.stack()[1]
    module_name = str(inspect.getmodule(src_caller[0]).__name__).split('.')[-1]
    print(str(inspect.getmodule(src_caller[0]).__name__))
    return make_caller(urls[module_name])


def get_poster():
    src_caller = inspect.stack()[1]
    module_name = inspect.getmodule(src_caller[0])
    return make_poster(urls[module_name])
