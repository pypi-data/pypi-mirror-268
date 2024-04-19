from guidance import models
from kbraincortex.common.configuration import OPENAI_API_KEY, OPENAI_BASE_URL

def azure_config(api_key=None, azure_endpoint=None):
    api_key = api_key if api_key is not None else OPENAI_API_KEY
    azure_endpoint = azure_endpoint if azure_endpoint is not None else OPENAI_BASE_URL
    return api_key, azure_endpoint

def initialize_instruct_guidance(
        api_key=None, 
        azure_endpoint=None, 
        model=None,
        deployment_id=None,
        version=None,
    ):
    
    version = version if version is not None else "2023-07-01-preview"
    deployment_id = deployment_id if deployment_id is not None else "instruct"
    api_key, azure_endpoint = azure_config(api_key, azure_endpoint)
    model_url = f"{azure_endpoint}openai/deployments/{deployment_id}/completions?api-version={version}"
    model = model if model is not None else "gpt-35-turbo-instruct"
    
    instruct = models.AzureOpenAIInstruct(
        model=model,
        azure_endpoint=model_url,
        api_key=api_key,
    )
    
    return instruct

def initialize_chat_guidance(api_key=None, azure_endpoint=None, model=None):

    api_key, azure_endpoint = azure_config(api_key, azure_endpoint)
    model = model if model is not None else "chat"

    instruct = models.AzureOpenAIChat(
        model=model,
        azure_endpoint=azure_endpoint,
        api_key=api_key
    )
    
    return instruct
