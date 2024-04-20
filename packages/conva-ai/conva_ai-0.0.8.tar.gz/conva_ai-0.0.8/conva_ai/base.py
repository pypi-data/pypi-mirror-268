import uuid
import requests


class BaseClient:

    def __init__(self, copilot_id: str, copilot_version: str, api_key: str, host: str = "https://infer.conva.ai"):
        self.copilot_id: str = copilot_id
        self.api_key: str = api_key
        self.copilot_version: str = copilot_version
        self.host: str = host
        self.keep_conversation_history: bool = True
        self.domain: str = ""
        self.history: str = ""

    def clear_history(self):
        """
        Clears the history tracked by the client
        """
        self.history: str = ""

    def use_history(self, use_history):
        self.history = use_history

