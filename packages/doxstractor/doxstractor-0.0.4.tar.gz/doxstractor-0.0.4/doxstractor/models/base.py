from typing import Optional


class BaseModel:
    def __init__(
        self, model: Optional[str] = None, temperature: float = 0.0, max_tokens: int = 0
    ) -> None:
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def complete(self, system_prompt: str, user_prompt: str):
        raise NotImplementedError
