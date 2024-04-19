# Python Library for Conva AI

This is the python library for using Conva AI Co-pilots

## Examples

### 1. A simple example for generating response using Conva Co-pilot
```
import asyncio
from conva_ai.client import AsyncConvaAI

async def generate(query: str, stream: bool):
    client = AsyncConvaAI(
        copilot_id="<YOUR_COPILOT_ID>", 
        copilot_version="<YOUR_COPILOT_VERSION>", 
        api_key="<YOUR_API_KEY>"
    )
    response = client.invoke_capability(query, stream=stream)
    out = "" 
    async for res in response:
        out = res.model_dump_json(indent=4)
        print(out)
    return out

final_response = asyncio.run(generate("how are you", True))
print(final_response)
```

### 2. How to clear history

Conva AI client, by default keeps track of your conversation history and uses it as the context for responding intelligently

You can clear conversation history by executing the below code:

```
from conva_ai.client import AsyncConvaAI
client = AsyncConvaAI(
    copilot_id="<YOUR_COPILOT_ID>", 
    copilot_version="<YOUR_COPILOT_VERSION>", 
    api_key="<YOUR_API_KEY>"
)
client.clear_history()
```

In case you are buliding an application where you don't want to track conversation history, you can disable history tracking

```
from conva_ai.client import AsyncConvaAI
client = AsyncConvaAI(
    copilot_id="<YOUR_COPILOT_ID>", 
    copilot_version="<YOUR_COPILOT_VERSION>", 
    api_key="<YOUR_API_KEY>"
)
client.disable_history(False)
```

### 3. Debugging responses

Conva AI uses generative AI to give you the response to your query. In order for you to understand the reasoning behind the response. We also provide you with AI's reasoning

```
import asyncio
from conva_ai.client import AsyncConvaAI

async def generate(query: str, stream: bool):
    client = AsyncConvaAI(
        copilot_id="<YOUR_COPILOT_ID>", 
        copilot_version="<YOUR_COPILOT_VERSION>", 
        api_key="<YOUR_API_KEY>"
    )
    response = client.invoke_capability(query, stream=stream)
    async for res in response:
        out = res.model_dump_json(indent=4)
    return out

final_response = asyncio.run(generate("how are you", True))
print(final_response.reason)
```