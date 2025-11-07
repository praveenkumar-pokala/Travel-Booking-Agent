from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class AppConfig(BaseModel):
    openai_api_key: str
    model_name: str = "gpt-4.1-mini"
    debug: bool = True

    @classmethod
    def from_env(cls) -> "AppConfig":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set. Please configure your .env file.")
        return cls(openai_api_key=api_key)
