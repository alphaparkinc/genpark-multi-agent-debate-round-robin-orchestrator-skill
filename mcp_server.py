import json, sys
from client import MultiAgentDebateRoundRobinOrchestratorClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "debate-round-robin", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "orchestrate_round_robin_debate", "description": "Orchestrates turn-based multi-agent debate and measures truth convergence."}]}}
    elif method == "tools/call":
        client = MultiAgentDebateRoundRobinOrchestratorClient()
        res = client.orchestrate_round_robin_debate()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = MultiAgentDebateRoundRobinOrchestratorClient()
        print(json.dumps(client.orchestrate_round_robin_debate(), indent=2))
