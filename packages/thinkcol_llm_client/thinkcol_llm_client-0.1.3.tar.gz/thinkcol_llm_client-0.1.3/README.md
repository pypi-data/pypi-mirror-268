# LLM Client 
Internal package for making multi-threaded calls to LLMs.

# Supported Models
Cohere Command, Cohere Embed, OpenAI Models, Titan Embed, Mixtral

## Install
```
pip install thinkcol_llm_client
```

## Usage: 
### Normal Usage
```
from thinkcol_llm_client import OpenAIClient, BedrockClient
from thinkcol_llm_client import Anthropic

texts = ["Hello", "Text 1", "ThinkCol"]

client = OpenAIClient()
client.embed(texts)

questions = ["How do I implement best practices in data science projects" for _ in range(500)]
client.invoke(questions)

anthropic_client = BedrockClient(provider = Anthropic())
anthropic_client.invoke(questions)
```

## Providers
The list of providers for bedrock models can be found in bedrock/clients. Support for new providers/models can be added in this file.

## Tests



