from instructor import from_openai, from_anthropic, Mode
from anthropic import Anthropic
from openai import OpenAI


class SimpleLM:
    def __init__(self):
        self.clients = {}
        self.models = {}

    def setup_client(
        self,
        client_name,
        api_key=None,
    ):
        client_creator = {
            "openai": lambda: from_openai(
                OpenAI(api_key=api_key),
            ),
            "anthropic": lambda: from_anthropic(Anthropic(api_key=api_key)),
            "together": lambda: from_openai(
                OpenAI(api_key=api_key, base_url="https://api.together.xyz/v1"),
                mode=Mode.MD_JSON,
            ),
            "ollama": lambda: from_openai(
                OpenAI(api_key=api_key, base_url="http://localhost:11434/v1"),
                mode=Mode.TOOLS,
            ),
        }

        if client_name in client_creator:
            client = client_creator[client_name]()
        else:
            raise ValueError(f"Unsupported client type: {client_name}")

        self.clients[client_name] = client
        
        return client

    def get_client(self, client_name):
        if client_name in self.clients:
            return self.clients[client_name]
        else:
            raise ValueError(
                f"Client '{client_name}' not initialized. Please set up the client first."
            )
