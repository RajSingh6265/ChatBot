from phi.agent import Agent, RunResponse

def perform_search(agent: Agent, query: str) -> str:
    run: RunResponse = agent.run(query)
    return run.content