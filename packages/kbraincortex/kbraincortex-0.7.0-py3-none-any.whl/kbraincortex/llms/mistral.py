import json
import requests
from kbraincortex.common.configuration import MISTRAL_LARGE_CHAT_API_KEY

BASE_URL_MAP = {
    "chat-mistral-large": "chat-mistral-large-serverless"
}

API_KEY_MAP = {
    "chat-mistral-large": MISTRAL_LARGE_CHAT_API_KEY
}

class Mistral:
    def __init__(self, deployment_id, base_url, api_key):
        self.base_url = f"https://{BASE_URL_MAP[deployment_id]}.{base_url}"
        if api_key is None:
            api_key = API_KEY_MAP[deployment_id]

        self.api_key = api_key

    def chat(self, messages, stream=False, max_tokens=8192, top_p=1.0, temperature=1.0, ignore_eos=False, safe_prompt=False, presence_penalty=None):
        url = f'{self.base_url}/v1/chat/completions'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-type': 'application/json',
        }
        payload = {
            'messages': messages,
            'stream': stream,
            'max_tokens': max_tokens,
            'top_p': top_p,
            'temperature': temperature,
            'ignore_eos': ignore_eos,
            'safe_prompt': safe_prompt,
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json()
        
        raise Exception(f'Failed to get a response from the API, status_code: {response.status_code}')