import argparse
import sys
from langchain_classic.agents import AgentExecutor
from orchestrator import Orchestrator


def main():
    parser = argparse.ArgumentParser(description="AI Finance Agent - CLI")
    parser.add_argument(
        "tickers",
        nargs="*",
        help="Stock tickers to analyze (e.g., AAPL MSFT GOOGL)",
        default=["BTC-USD"]
    )
    args = parser.parse_args()

    print("Starting AI Finance Agent...")
    orchestrator_setup = Orchestrator()
    agent_executor = AgentExecutor(
        agent=orchestrator_setup.agent,
        tools=orchestrator_setup.tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=3
    )

    print(f"📊 Processing tickers: {args.tickers}\n" + "="*40)

    for ticker in args.tickers:
        print(f"\n🔎 Analyzing {ticker}...")

        # Construct the "Task" dynamically
        task_prompt = (
            f"Check the latest price and news for {ticker}. "
            "THEN, use the Financial Analyst tool to write a strategic sentiment report "
            "based on that news. I need both the price and the strategy."
        )

        try:
            # Run the agent for this specific ticker
            result = agent_executor.invoke({"input": task_prompt})

            # Print a clean separator
            print(f"\n✅ Report for {ticker} Ready:")
            print("-" * 20)
            print(result['output'])
            print("=" * 40)

        except Exception as e:
            print(f"❌ Failed to analyze {ticker}: {e}")

if __name__ == "__main__":
    main()
