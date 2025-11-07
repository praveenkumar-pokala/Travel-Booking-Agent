import logging

from travel_agent.config import AppConfig
from travel_agent.logging_utils import setup_logging
from travel_agent.llm.client import LLMClient
from travel_agent.agent.runner import AgentRunner

def main() -> None:
    setup_logging(logging.INFO)
    config = AppConfig.from_env()
    llm_client = LLMClient(config)
    agent = AgentRunner(llm_client)

    print("=== Travel Booking Agent ===")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if user_text.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        reply = agent.handle_user_input(user_text)
        print("Agent:\n" + reply + "\n")

if __name__ == "__main__":
    main()
