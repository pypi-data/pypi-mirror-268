import json
import requests
from kbraincortex.common.configuration import META_LLAMA2_CHAT_API_KEY

BASE_URL_MAP = {
    "chat-llama-2-7b": "chat-llama-2-7b-serverless"
}

API_KEY_MAP = {
    "chat-llama-2-7b": META_LLAMA2_CHAT_API_KEY
}

class Meta:
    def __init__(self, deployment_id, base_url, api_key):
        self.base_url = f"https://{BASE_URL_MAP[deployment_id]}.{base_url}"
        if api_key is None:
            api_key = API_KEY_MAP[deployment_id]

        self.api_key = api_key

    def completion(
            self, 
            prompt, 
            stream=False, 
            max_tokens=16, 
            top_p=1.0, 
            temperature=1.0, 
            n=1, 
            stop=None, 
            best_of=1, 
            logprobs=None, 
            presence_penalty=None, 
            ignore_eos=True, 
            use_beam_search=False, 
            stop_token_ids=None, 
            skip_special_tokens=None
        ):
        url = f'{self.base_url}/v1/completions'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-type': 'application/json',
        }
        payload = {
            'prompt': prompt,
            'stream': stream,
            'max_tokens': max_tokens,
            'top_p': top_p,
            'temperature': temperature,
            'n': n,
            'stop': stop,
            'best_of': best_of,
            'logprobs': logprobs,
            'presence_penalty': presence_penalty,
            'ignore_eos': ignore_eos,
            'use_beam_search': use_beam_search,
            'stop_token_ids': stop_token_ids,
            'skip_special_tokens': skip_special_tokens,
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json()
        
        raise Exception(f'Failed to get a response from the API, status_code: {response.status_code}')

    def chat(
            self, 
            messages, 
            stream=False, 
            max_tokens=16, 
            top_p=1.0, 
            temperature=1.0, 
            n=1, 
            stop=None, 
            best_of=1, 
            logprobs=None, 
            presence_penalty=None, 
            ignore_eos=True, 
            use_beam_search=False, 
            stop_token_ids=None, 
            skip_special_tokens=None
        ):
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
            'n': n,
            'stop': stop,
            'best_of': best_of,
            'logprobs': logprobs,
            'presence_penalty': presence_penalty,
            'ignore_eos': ignore_eos,
            'use_beam_search': use_beam_search,
            'stop_token_ids': stop_token_ids,
            'skip_special_tokens': skip_special_tokens,
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json()
        
        raise Exception(f'Failed to get a response from the API, status_code: {response.status_code}')
