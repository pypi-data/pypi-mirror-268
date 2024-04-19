from ai_flare_research_assistant.connectors.rpc.flarepy.api.apimeta import api_endpoints

host = "flare-api.flare.network"
# jsonrpc_port = "9650"
protocol = "https"
# jsonrpc_url = "{}://{}:{}".format(jsonrpc_prot, jsonrpc_host, jsonrpc_port)
url = "{}://{}".format(protocol, host)

urls = {k: ("{}" + v).format(url) for k, v in api_endpoints.items()}
