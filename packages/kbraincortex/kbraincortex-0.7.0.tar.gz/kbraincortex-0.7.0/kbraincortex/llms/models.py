from openai import AzureOpenAI
from kbraincortex.common.configuration import OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_GPT4_BASE_URL, OPENAI_GPT4_API_KEY, AI_STUDIO_BASE_URL
from kbraincortex.llms.meta import Meta
from kbraincortex.llms.mistral import Mistral
import logging 
class LLMModelException(Exception):
    pass

openai_chat_arguments = [
    "messages", "prompt", "model_name", "model_type", 
    "temperature", "max_tokens", "base_url", "deployment_id", "full_response", 
    "max_tokens", "frequency_penalty", "presence_penalty", "stop", "n", 
    "stream", "logit_bias", "response_format", "best_of", 
    "seed", "tools", "tool_choice"
]

def get_model_response(model_type, model_name, mode, prompt, **kwargs):
    if model_type.lower() not in supported_model_types:
        raise LLMModelException(f"Model type {model_type} is not supported.")
    
    client = supported_model_types[model_type.lower()](model_name, **kwargs)
    return response_mode_functions[model_type.lower()][mode](client, prompt, **kwargs)

def initialize_openai(
        model_name,
        base_url=None, 
        api_key=None,
        version="2023-10-01-preview",
        **kwargs
):
    
    if base_url is None:
        base_url = OPENAI_BASE_URL if model_name != 'gpt-4' else OPENAI_GPT4_BASE_URL
    if api_key is None:
        api_key = OPENAI_API_KEY if model_name != 'gpt-4' else OPENAI_GPT4_API_KEY

    assert isinstance(model_name, str) and model_name, "model_name must be a non-empty string"
    assert isinstance(base_url, str) and base_url, "base_url must be a non-empty string"
    assert isinstance(api_key, str) and api_key, "api_key must be a non-empty string"
    assert version is None or isinstance(version, str), "version must be a string or None"
    
    client = AzureOpenAI(
        api_key=api_key,  
        api_version=version,
        azure_endpoint=base_url
    )
    
    return client


def initialize_meta(
        model_name,
        base_url=None, 
        api_key=None,
        **kwargs
):
    
    if base_url is None:
        base_url = AI_STUDIO_BASE_URL

    assert isinstance(model_name, str) and model_name, "model_name must be a non-empty string"
    assert isinstance(base_url, str) and base_url, "base_url must be a non-empty string"
    
    client = Meta(
        api_key=api_key,  
        deployment_id=model_name,
        base_url=base_url
    )
    
    return client

def initialize_mistral(
        model_name,
        base_url=None, 
        api_key=None,
        **kwargs
):
    if base_url is None:
        base_url = AI_STUDIO_BASE_URL

    assert isinstance(model_name, str) and model_name, "model_name must be a non-empty string"
    assert isinstance(base_url, str) and base_url, "base_url must be a non-empty string"
    
    client = Mistral(
        api_key=api_key,  
        deployment_id=model_name,
        base_url=base_url
    )
    
    return client

def get_abstract_response(response, text, prompt_tokens, completion_tokens, total_tokens, full_response=False):
    logging.info(text)
    tokens = {
        "prompt": int(prompt_tokens),
        "completion": int(completion_tokens),
        "total": int(total_tokens)
    }
    result = response if full_response else text
    return result, tokens    


def get_aistudio_chat_response(
    client, 
    messages, 
    full_response=False,
    max_tokens=1000,
    temperature=0,
    frequency_penalty=None,
    presence_penalty=0,
    stream=False,
    **kwargs  
):
    del kwargs["deployment_id"]

    response = client.chat( 
        messages=messages, 
        max_tokens=max_tokens,
        temperature=temperature,
        presence_penalty=presence_penalty,
        stream=stream,
        **kwargs
    )

    text = response["choices"][0]["message"]["content"]
    prompt_tokens = response["usage"]["prompt_tokens"]
    completion_tokens = response["usage"]["completion_tokens"]
    total_tokens = response["usage"]["total_tokens"]

    return get_abstract_response(response, text, prompt_tokens, completion_tokens, total_tokens, full_response)

def get_aistudio_completion_response(
    client, 
    prompt, 
    full_response=False,
    max_tokens=1000,
    temperature=0,
    frequency_penalty=0,
    presence_penalty=0,
    stream=False,
    **kwargs
):
    del kwargs["deployment_id"]

    response = client.completion( 
        prompt=prompt, 
        max_tokens=max_tokens,
        temperature=temperature,
        presence_penalty=presence_penalty,
        stream=stream,
        **kwargs
    )

    text = response["choices"][0]["text"]
    prompt_tokens = response["usage"]["prompt_tokens"]
    completion_tokens = response["usage"]["completion_tokens"]
    total_tokens = response["usage"]["total_tokens"]

    return get_abstract_response(response, text, prompt_tokens, completion_tokens, total_tokens, full_response)

def get_openai_chat_response(
        client, 
        messages, 
        full_response=False,
        max_tokens=1000,
        temperature=0,
        frequency_penalty=0,
        presence_penalty=0,
        stream=False,
        **kwargs
    ):

    model = kwargs["deployment_id"]
    del kwargs["deployment_id"]

    response = client.chat.completions.create( 
        model=model,
        messages=messages, 
        max_tokens=max_tokens,
        temperature=temperature,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stream=stream,
        **kwargs
    )

    text = response.choices[0].message.content
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    total_tokens = response.usage.total_tokens

    return get_abstract_response(response, text, prompt_tokens, completion_tokens, total_tokens, full_response)

def get_openai_completion_response(
        client, 
        prompt, 
        full_response=False,
        max_tokens=1000,
        temperature=0,
        frequency_penalty=0,
        presence_penalty=0,
        stream=False,
        **kwargs
    ):

    model = kwargs["deployment_id"]
    del kwargs["deployment_id"]

    response = client.completions.create( 
        model=model,
        prompt=prompt, 
        max_tokens=max_tokens,
        temperature=temperature,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stream=stream,
        **kwargs
    )

    text = response.choices[0].text
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    total_tokens = response.usage.total_tokens

    return get_abstract_response(response, text, prompt_tokens, completion_tokens, total_tokens, full_response)
  
def get_unsupported_completion_response(
    **kwargs
):
    raise ValueError("Completion mode is not supported for this model type")

supported_model_types = {
    "openai": initialize_openai,
    "meta": initialize_meta,
    "mistral": initialize_mistral
}

response_mode_functions = {
    "openai": {
        "chat": get_openai_chat_response,
        "completion": get_openai_completion_response
    },
    "meta": {
        "chat": get_aistudio_chat_response,
        "completion": get_aistudio_completion_response,
    },
    "mistral": {
        "chat": get_aistudio_chat_response,
        "completion": get_unsupported_completion_response
    }
}