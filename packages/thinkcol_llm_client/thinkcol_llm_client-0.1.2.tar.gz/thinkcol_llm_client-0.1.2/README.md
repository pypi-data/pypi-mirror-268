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
from thinkcol_llm_client import OpenAIClient, AnthropicClient

texts = ["Hello", "Text 1", "ThinkCol"]

client = OpenAIClient()
client.embed(texts)

questions = ["How do I implement best practices in data science projects" for _ in range(500)]
client.invoke(questions)

anthropic_client = AnthropicClient()
anthropic_client.invoke(questions)
```

