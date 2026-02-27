import os

from openai import OpenAI

from app.services.prompt_builder import DISCLAIMER


class AIClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("OPENAI_MODEL", "gpt-5")

    def chat(self, system_prompt: str, message: str) -> str:
        if not os.getenv("OPENAI_API_KEY"):
            return f"{DISCLAIMER} Focus on risk limits, stop-loss usage, and journaling each trade."
        response = self.client.responses.create(
            model=self.model,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message},
            ],
        )
        return f"{response.output_text}\n\n{DISCLAIMER}"
