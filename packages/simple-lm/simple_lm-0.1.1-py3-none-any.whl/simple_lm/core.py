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

    def get_client(self, client_name):
        if client_name in self.clients:
            return self.clients[client_name]
        else:
            raise ValueError(
                f"Client '{client_name}' not initialized. Please set up the client first."
            )


if __name__ == "__main__":
    from pydantic import BaseModel

    simple_lm = SimpleLM()
    simple_lm.setup_client(
        "together",
        api_key="b09b6bad927f75e1e478123f78a482b8e199f1ef66c5238b442de8b53d77d872",
    )

    together = simple_lm.get_client("together")

    class Person(BaseModel):
        name: str
        role: str

    person = together.create(
        model="microsoft/WizardLM-2-8x22B",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Bob is a software engineer at Google.",
            },
        ],
        response_model=Person,
    )

    print(person)
