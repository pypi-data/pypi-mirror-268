from openai import AsyncAzureOpenAI
import asyncio
from tqdm import tqdm
from .chat_client import ChatClient
from typing import Iterable, Generator
from dotenv import load_dotenv
from math import ceil
from .constants import OPENAI_SYSTEM_PROMPT


class OpenAIClient(ChatClient):

    def __init__(self):
        super().__init__()
        load_dotenv()
        self.client = AsyncAzureOpenAI(api_version="2023-09-01-preview")

    def batch_invoke(
        self, msgs: Iterable, model_name: str = "gpt-4", batch_size: int = 50
    ) -> Generator:
        for chunk in self._chunk(msgs, batch_size):
            coros = [
                self.client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": OPENAI_SYSTEM_PROMPT},
                        {"role": "user", "content": msg},
                    ],
                    temperature=0,
                )
                for msg in chunk
            ]

            yield [
                completion.choices[0].message.content
                for completion in self.loop.run_until_complete(asyncio.gather(*coros))
            ]

    def batch_embed(
        self,
        texts: Iterable,
        model_name: str = "text-embedding-ada-002",
        batch_size: int = 50,
        texts_per_request: int = 50,
    ) -> Generator:
        # split text into {batch_size}-size batches, i.e. {batch_size} number of texts per request
        splits = self._chunk(texts, texts_per_request)
        # further split batches into {batch_size}-size superbatches, i.e. {batch_size} number of requests fired
        for chunk in self._chunk(splits, batch_size):
            coros = [
                self.client.embeddings.create(input=texts, model=model_name)
                for texts in chunk
            ]
            yield [
                d.embedding
                for response in self.loop.run_until_complete(asyncio.gather(*coros))
                for d in response.data
            ]

    # wrapper for acummulating results from batch_invoke
    def invoke(
        self, msgs: list[str], model_name: str = "gpt-4", batch_size: int = 50
    ) -> list:
        return [
            res
            for batch_res in tqdm(
                self.batch_invoke(iter(msgs), model_name, batch_size),
                total=ceil(len(msgs) / batch_size),
            )
            for res in batch_res
        ]

    # wrapper for acummulating results from batch_embed
    def embed(
        self,
        texts: list,
        model_name: str = "text-embedding-ada-002",
        batch_size: int = 50,
        texts_per_request: int = 50,
    ) -> list:
        return [
            embed
            for embed_batch in tqdm(
                self.batch_embed(
                    iter(texts), model_name, batch_size, texts_per_request
                ),
                total=ceil(len(texts) / (batch_size * texts_per_request)),
            )
            for embed in embed_batch
        ]
