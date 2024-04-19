from pydantic.dataclasses import dataclass
import json


class Payload:
    def format(self):
        return json.dumps(self.__dict__)


@dataclass
class CohereCommandText(Payload):
    prompt: str
    max_tokens: int = 1024
    temperature: int = 0


@dataclass
class CohereEmbed(Payload):
    texts: list[str]
    input_type: str = "search_document"


@dataclass
class TitanEmbed(Payload):
    inputText: str


@dataclass
class MistralInstruct(Payload):
    prompt: str
    max_tokens: int = 1024
    temperature: int = 0


@dataclass
class ClaudeText(Payload):
    messages: list[dict]
    anthropic_version: str = "bedrock-2023-05-31"
    max_tokens: int = 1024
