## Python Library for Conva AI

This is the python library for using Conva AI Co-pilots

### Example

```
import asyncio
from conva_ai.client import AsyncConvaAI

async def generate(query: str, stream: bool):
    omni_client = AsyncConvaAI(
        assistant_id="<YOUR_COPILOT_ID>", 
        assistant_version="<YOUR_COPILOT_VERSION>", 
        api_key="<YOUR_API_KEY>"
    )
    response = omni_client.invoke_capability(query, stream=stream)
    async for res in response:
        print(res.model_dump_json(indent=4))

asyncio.run(generate("how are you", True))
```