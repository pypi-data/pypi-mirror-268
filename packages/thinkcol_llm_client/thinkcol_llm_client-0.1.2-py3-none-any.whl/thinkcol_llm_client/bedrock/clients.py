from dotenv import load_dotenv
import boto3
import os
import asyncio
from math import ceil
from typing import Iterator, Generator, Optional
from tqdm import tqdm
from ..chat_client import ChatClient
from ..constants import TEXTS_PER_REQUEST
from .bedrock_models import Provider, BedrockModel, Cohere, Titan, Mistral, Anthropic
from .payloads import Payload


# vanilla client
class BedrockClient(ChatClient):
    def __init__(
        self,
        *,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        region: str = "us-west-2",
        provider: Optional[Provider] = None,
    ):
        super().__init__()
        load_dotenv()
        # get access keys
        if access_key is None:
            if "BEDROCK_ACCESS_KEY" not in os.environ:
                raise Exception("BEDROCK_ACCESS_KEY not supplied")
            access_key = os.environ["BEDROCK_ACCESS_KEY"]
        if secret_key is None:
            if "BEDROCK_SECRET_KEY" not in os.environ:
                raise Exception("BEDROCK_SECRET_KEY not supplied")
            secret_key = os.environ["BEDROCK_SECRET_KEY"]
        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=region,
            aws_access_key_id=os.environ["BEDROCK_ACCESS_KEY"],
            aws_secret_access_key=os.environ["BEDROCK_SECRET_KEY"],
        )
        self.provider = provider

    # makes batched requests to bedrock
    def batch_request(
        self,
        payloads: Iterator[Payload],
        model_id: str,
        batch_size: int = 20,
        **args,
    ) -> Generator:
        for chunk in self._chunk(payloads, batch_size, lambda x: x.format(), **args):
            aws = [
                asyncio.to_thread(
                    lambda p: self.client.invoke_model(
                        body=p,
                        modelId=model_id,
                        accept="application/json",
                        contentType="application/json",
                    ),
                    payload,
                )
                for payload in chunk
            ]
            yield self.loop.run_until_complete(asyncio.gather(*aws))

    def request(
        self,
        payload_collection: list,
        model_name: str,
        out_parser=lambda x: x,
        batch_size: int = 20,
    ):
        return [
            out_parser(res)
            for batch_res in tqdm(
                self.batch_request(iter(payload_collection), model_name),
                total=ceil(len(payload_collection) / batch_size),
            )
            for res in batch_res
        ]

    def _request_provider(
        self, input_collection: list, model_name: str, type: str, batch_size: int
    ):
        if self.provider is None:
            raise Exception("Provider not provided.")
        if model_name not in self.provider.models[type]:
            raise ValueError(
                f"{model_name} not supported. Supported models: {self.provider.models[type]}"
            )
        model: BedrockModel = self.provider.models[type][model_name]
        payload_collection = [model.payload_cls(input) for input in input_collection]
        return self.request(
            payload_collection, model_name, model.parse_output, batch_size
        )

    def invoke(self, msgs: list, model_name: str, batch_size: int = 20):
        return self._request_provider(msgs, model_name, "generate", batch_size)

    def embed(
        self,
        text_batches: list,
        model_name: str,
        batch_size: int = 20,
    ):
        return self._request_provider(text_batches, model_name, "embed", batch_size)


class CohereClient(BedrockClient):
    def __init__(
        self,
        *,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        region: str = "us-west-2",
    ):
        super().__init__(
            access_key=access_key,
            secret_key=secret_key,
            region=region,
            provider=Cohere(),
        )

    def embed(
        self,
        texts: list,
        model_name: str,
        batch_size: int = 20,
        texts_per_request: int = TEXTS_PER_REQUEST,
    ) -> list:
        text_batches = list(self._chunk(iter(texts), texts_per_request))
        embed_batches = super().embed(text_batches, model_name, batch_size)
        return [embed for batch in embed_batches for embed in batch]


class TitanClient(BedrockClient):
    def __init__(
        self,
        *,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        region: str = "us-west-2",
    ):
        super().__init__(
            access_key=access_key,
            secret_key=secret_key,
            region=region,
            provider=Titan(),
        )


class MistralClient(BedrockClient):
    def __init__(
        self,
        *,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        region: str = "us-west-2",
    ):
        super().__init__(
            access_key=access_key,
            secret_key=secret_key,
            region=region,
            provider=Mistral(),
        )


class AnthropicClient(BedrockClient):
    def __init__(
        self,
        *,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        region: str = "us-west-2",
    ):
        super().__init__(
            access_key=access_key,
            secret_key=secret_key,
            region=region,
            provider=Anthropic(),
        )
