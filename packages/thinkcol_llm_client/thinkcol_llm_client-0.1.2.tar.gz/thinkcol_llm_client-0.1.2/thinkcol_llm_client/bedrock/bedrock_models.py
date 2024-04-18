from abc import ABC, abstractmethod
from typing import Callable
import json

from . import payloads


class BedrockModel(ABC):

    @property
    @abstractmethod
    def payload_cls(self) -> Callable:
        pass

    @abstractmethod
    def parse_output(self, response):
        pass


class Provider(ABC):
    @property
    @abstractmethod
    def models(self) -> dict:
        pass


class Cohere(Provider):

    class CommandText(BedrockModel):
        payload_cls = payloads.CohereCommandText

        def parse_output(self, response):
            return json.loads(response.get("body").read()).get("generations")

    class Embed(BedrockModel):
        payload_cls = payloads.CohereEmbed

        def parse_output(self, response):
            return json.loads(response.get("body").read()).get("embeddings")

    models: dict = {
        "generate": {
            "cohere.command-text-v14": CommandText(),
            "cohere.command-light-text-v14": CommandText(),
        },
        "embed": {
            "cohere.embed-english-v3": Embed(),
            "cohere.embed-multilingual-v3": Embed(),
        },
    }


class Titan(Provider):
    class Embed(BedrockModel):
        payload_cls = payloads.TitanEmbed

        def parse_output(self, response):
            return json.loads(response.get("body").read()).get("embedding")

    models = {"embed": {"amazon.titan-embed-text-v1": Embed()}}


class Mistral(Provider):
    class Instruct(BedrockModel):
        payload_cls = payloads.MistralInstruct

        def parse_output(self, response):
            return json.loads(response["body"].read()).get("outputs")[0].get("text")

    models = {"generate": {"mistral.mixtral-8x7b-instruct-v0:1": Instruct()}}


class Anthropic(Provider):
    class Opus(BedrockModel):
        payload_cls = payloads.ClaudeText

        def parse_output(self, response):
            return json.loads(response.get("body").read()).get("content", [])

    class Sonnet(BedrockModel):
        payload_cls = payloads.ClaudeText

        def parse_output(self, response):
            return (
                json.loads(response.get("body").read())
                .get("content", [])[0]
                .get("text")
            )

    models = {
        "generate": {
            "anthropic.claude-3-opus-20240229-v1:0": Opus(),
            "anthropic.claude-3-sonnet-20240229-v1:0": Sonnet(),
        }
    }
