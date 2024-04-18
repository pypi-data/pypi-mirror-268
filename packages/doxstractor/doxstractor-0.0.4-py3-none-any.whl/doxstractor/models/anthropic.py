import anthropic
from .base import BaseModel
from typing import Optional


class AnthropicAPIModel(BaseModel):
    def __init__(
        self,
        model: Optional[str] = "claude-3-haiku-20240307",
        temperature: float = 0.0,
        max_tokens: int = 0,
    ) -> None:
        super().__init__(model=model, temperature=temperature, max_tokens=max_tokens)

        self.client = anthropic.Anthropic()

    def complete(self, system_prompt: str, user_prompt: str):
        message = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_prompt,
                        }
                    ],
                }
            ],
        )
        return message.content[0].text
