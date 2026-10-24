import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import MultiAgentDebateRoundRobinOrchestratorClient

def main():
    client = MultiAgentDebateRoundRobinOrchestratorClient()
    res = client.orchestrate_round_robin_debate()
    print("=== Multi-Agent Debate Round Robin Orchestrator Output ===")
    print(f"Proposition: {res['proposition']}")
    print(f"Convergence: {res['initial_convergence_score']*100}% -> {res['final_convergence_score']*100}% (Consensus: {res['consensus_achieved']})")
    print(f"Verdict: {res['synthesized_consensus_verdict']}")
    print("\nDebate Rounds Progression:")
    for r in res['rounds_log']:
        print(f"  Round {r['round']} (Score: {r['convergence_score']}):")
        print(f"    Pro: {r['proponent_arg'][:60]}...")
        print(f"    Con: {r['opponent_arg'][:60]}...")

if __name__ == '__main__':
    main()
