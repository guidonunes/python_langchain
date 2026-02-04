import argparse
import sys
from langchain_classic.agents import AgentExecutor
from orchestrator import Orchestrator


def main():
    agent = Orchestrator()
    orchestrator = AgentExecutor(
        agent=agent.agent,
        tools=agent.tools,
        verbose=True
    )

    user_input = (
        """
        Check the latest price and news for BTC."
        THEN, use the Financial Analyst tool to write a strategic sentiment report "
        based on that news. I need both the price and the strategy."
        """
    )


    response =orchestrator.invoke({"input": user_input})

    print("\nFinal Response from Agent:")
    print(response)


if __name__ == "__main__":
    main()
