from langchain_classic.agents import AgentExecutor
from orchestrator import Orchestrator


def main():
    agent = Orchestrator()
    orchestrator = AgentExecutor(
        agent=agent.agent,
        tools=agent.tools,
        verbose=True
    )

    user_input = "What is the current status of AAPL and TSLA stocks?"

    response =orchestrator.invoke({"input": user_input})

    print("\nFinal Response from Agent:")
    print(response)


if __name__ == "__main__":
    main()
