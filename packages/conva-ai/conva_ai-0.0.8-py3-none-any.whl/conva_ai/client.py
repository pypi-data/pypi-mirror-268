import uuid
import json
import requests
import sseclient
from conva_ai.base import BaseClient
from conva_ai.response import ConvaAIResponse
from typing import AsyncGenerator


class AsyncConvaAI(BaseClient):

    async def invoke_capability(
        self,
        query: str,
        stream: bool = False,
        capability_group: str = "",
    ) -> AsyncGenerator[ConvaAIResponse, None]:
        app_context: dict = {}
        request_id = uuid.uuid4().hex
        response = requests.post(
            f"{self.host}/v1/assistants/{self.copilot_id}/text2action",
            json={
                "type": "text2action",
                "request_id": request_id,
                "assistant_id": self.copilot_id,
                "assistant_version": self.copilot_version,
                "device_id": str(uuid.getnode()),
                "input_query": query,
                "domain_name": self.domain,
                "app_context": app_context,
                "conversation_history": "{}" if not self.keep_conversation_history else self.history,
                "capability_group": capability_group,
            },
            headers={"Authorization": self.api_key, "Content-Type": "application/json"},
            stream=stream,
        )
        client = sseclient.SSEClient(response)  # type: ignore
        for event in client.events():
            event_data = event.data
            event_response = json.loads(event_data)
            rt = event_response.get("response_type", "assistant")

            if rt != "status":
                is_final = event_response.get("is_final", False)
                if stream:
                    yield ConvaAIResponse(**event_response)
                if is_final:
                    action_response = ConvaAIResponse(**event_response)
                    self.history = action_response.conversation_history
                    yield action_response
