from abc import ABC, abstractmethod
from typing import Iterable
import asyncio


class ChatClient(ABC):

    def __init__(self) -> None:
        super().__init__()
        # set event loop
        try:
            self.loop = asyncio.get_running_loop()
        except Exception:
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)

    @abstractmethod
    def invoke(self, msgs: list, model_name: str, batch_size: int):
        pass

    @abstractmethod
    def embed(self, texts: list, model_name: str, batch_size: int):
        pass

    # helper generator for chunking iterables into {chunk_size}-sized chunks
    def _chunk(
        self, iter: Iterable, chunk_size: int = 50, transform_fn=lambda x: x, **args
    ):
        chunk: list = []
        while True:
            el = next(iter, None)  # type: ignore
            # check if iterator is empty
            if el is None:
                if chunk:
                    yield chunk
                break
            chunk.append(transform_fn(el, **args))
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
