from .base import BaseModel


class MockModel(BaseModel):

    def complete(self, system_prompt: str, user_prompt: str):
        message = user_prompt.split("\n")[-1]
        return message
