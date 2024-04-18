from .utils import parseNumber, most_common
from .models import BaseModel
from typing import List


class BaseExtractor:
    def __init__(
        self,
        name: str,  # Has to be unique within graph as it identifies extractor
        query: str,
        model: BaseModel,
        max_chunk_size: float = 10_000,
    ) -> None:
        self.max_chunk_size = max_chunk_size
        self.model = model
        self.query = query
        self.name = name

    def _chunk_text(self, doc_text: str) -> List[str]:
        chunks = doc_text.split("\n")

        merged_chunks = [""]
        for chunk in chunks:
            prev_chunk = merged_chunks[-1]
            if (len(prev_chunk) + len(chunk)) < (self.max_chunk_size - 1):
                merged_chunks[-1] = prev_chunk + "\n" + chunk
            else:
                merged_chunks.append(chunk)

        return merged_chunks

    def extract(self, doc_text: str):
        raise NotImplementedError


class NumericExtractor(BaseExtractor):

    def extract(self, doc_text: str) -> float:

        merged_chunks = self._chunk_text(doc_text)
        snip_messages = []
        for snippet in merged_chunks:

            message = self.model.complete(
                system_prompt='Your job is to extract numerical values in document. Respond with a single number and no other text. If there is no relevant information in the text provided, respond with "NA". Do not make things up.',
                user_prompt=f"{self.query} \n Use the information given below. \n {snippet}",
            )
            snip_messages.append(message)

            valid_answers = [m for m in snip_messages if m != "NA"]
            # TODO: We would probably want a bigger LLM to pick the winner, but we will just pick the most common valid answer.
            consensus = most_common(valid_answers)

            return parseNumber(consensus)


class CategoryExtractor(BaseExtractor):
    def __init__(
        self,
        name: str,
        query: str,
        categories: List[str],
        model: BaseModel,
        max_chunk_size: float = 10_000,
    ) -> None:
        super().__init__(
            name=name, query=query, max_chunk_size=max_chunk_size, model=model
        )
        self.categories = categories

    def extract(self, doc_text: str) -> str:
        merged_chunks = self._chunk_text(doc_text)
        categories_str = "The possible categories are " + ", ".join(
            [f'"{w}"' for w in self.categories]
        )
        snip_messages = []
        for snippet in merged_chunks:

            message = self.model.complete(
                system_prompt='Your job is to provide a categorial answer based on provided text. Answer only with the category, and no other text. If there is no relevant information in the text provided, respond with "NA". Do not make things up.',
                user_prompt=f"{self.query} \n Valid categories are: {categories_str} \n Use the information below: \n {snippet}",
            )
            snip_messages.append(message)

        valid_answers = [
            m for m in snip_messages if (m != "NA") and (m in self.categories)
        ]

        return most_common(valid_answers)


class TextExtractor(BaseExtractor):

    def extract(self, doc_text: str) -> str:
        merged_chunks = self._chunk_text(doc_text)
        snip_messages = []
        for snippet in merged_chunks:

            message = self.model.complete(
                system_prompt='Your job is to precisely answer the query, with as little text as possible. Answer only with the relevant text snippet you have found below, and no other text. Do not explain your answer or provide any context.  If there is no relevant information in the text provided, respond with "NA". Do not make things up.',
                user_prompt=f"{self.query} \n Use the information given below. \n {snippet}",
            )
            snip_messages.append(message)

        valid_answers = [m for m in snip_messages if (m != "NA")]

        return most_common(valid_answers)
