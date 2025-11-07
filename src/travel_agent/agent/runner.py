from typing import Dict, Any
import logging

from .state import ConversationState
from ..llm.client import LLMClient
from ..llm.toolspecs import ALL_TOOLS
from .router import dispatch_tool_call

logger = logging.getLogger(__name__)

class AgentRunner:
    """Single interface to run one step of the travel agent."""

    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client
        self.state = ConversationState()

    def handle_user_input(self, user_text: str) -> str:
        """Process user input and return agent response."""
        self.state.add_user_message(user_text)

        llm_response = self.llm_client.call_with_tools(
            messages=self.state.messages,
            tools=ALL_TOOLS,
        )

        if llm_response["type"] == "assistant_final":
            content = llm_response["content"]
            self.state.add_assistant_message(content)
            return content

        if llm_response["type"] == "tool_call":
            tool_name = llm_response["tool_name"]
            tool_args = llm_response["tool_args"]
            logger.info("Model requested tool '%s' with args=%s", tool_name, tool_args)

            tool_output = dispatch_tool_call(tool_name, tool_args)
            self.state.add_tool_message(tool_name, tool_output)

            llm_response_2 = self.llm_client.call_with_tools(
                messages=self.state.messages,
                tools=ALL_TOOLS,
            )
            if llm_response_2["type"] == "assistant_final":
                content = llm_response_2["content"]
                self.state.add_assistant_message(content)
                return content

            content = "I had trouble interpreting the tool result. Please rephrase your request."
            self.state.add_assistant_message(content)
            return content

        content = "I am not sure how to respond. Please try again."
        self.state.add_assistant_message(content)
        return content
