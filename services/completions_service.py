from typing import Any

import requests
import tiktoken

from config import GPT_TOKEN

PROXY_URL = "http://173.212.230.201:8080/chatgpt"

contextName = "exampleDialog"

encoding = tiktoken.encoding_for_model("gpt-4")


class CompletionsService:
    TOKEN = GPT_TOKEN
    TOKEN_LIMIT = 2000

    def query_chatgpt(self, user_id, message) -> Any:
        payload = {
            'token': self.TOKEN,
            'dialogName': user_id,
            'query': message,
            'tokenLimit': self.TOKEN_LIMIT,
            'singleMessage': True,
        }

        response = requests.post(PROXY_URL, json=payload, headers={'Content-Type': 'application/json'})

        if response.status_code == 200:
            return response.json()
        else:
            return {"success": False, "response": f"Ошибка 😔: {response.json().get('message')}"}


completionsService = CompletionsService()
