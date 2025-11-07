from typing import List, Dict, Any
from dataclasses import dataclass, field

@dataclass
class ConversationState:
    messages: List[Dict[str, Any]] = field(default_factory=list)

    def add_user_message(self, content: str) -> None:
        self.messages.append({"role": "user", "content": content})

    def add_assistant_message(self, content: str) -> None:
        self.messages.append({"role": "assistant", "content": content})

    def add_tool_message(self, tool_name: str, content: str) -> None:
        self.messages.append({"role": "tool", "name": tool_name, "content": content})
