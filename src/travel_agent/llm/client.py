from typing import List, Dict, Any
from openai import OpenAI
from ..config import AppConfig

class LLMClient:
    def __init__(self, config: AppConfig):
        self.config = config
        self.client = OpenAI(api_key=config.openai_api_key)

    def call_with_tools(
        self,
        messages: List[Dict[str, Any]],
        tools: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        response = self.client.responses.create(
            model=self.config.model_name,
            input=messages,
            tools=[{"type": "function", "function": t} for t in tools],
        )
        msg = response.output[0].content[0]
        if msg.type == "tool_call":
            tool_call = msg.tool_call
            return {
                "type": "tool_call",
                "tool_name": tool_call.function.name,
                "tool_args": tool_call.function.arguments,
            }
        content = getattr(msg, "text", str(msg))
        return {"type": "assistant_final", "content": content}
