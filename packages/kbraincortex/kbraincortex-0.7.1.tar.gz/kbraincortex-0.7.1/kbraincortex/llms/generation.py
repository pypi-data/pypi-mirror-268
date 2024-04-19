from kbraincortex.llms.models import get_model_response
def chat(
        messages = [], 
        model_name = "gpt-35-turbo",     
        model_type = 'openai',
        **kwargs
    ):

    validate_input(model_name, str, "Model Name")
    validate_input(model_type, str, "Model Type")
    validate_input(messages, list, "Messages")
    process_messages(messages)

    return get_model_response(model_type, model_name, 'chat', messages, **kwargs)

def completion(
        prompt = "", 
        model_name = "gpt-3.5-turbo",     
        model_type = 'openai',
        **kwargs
    ):

    validate_input(model_name, str, "Model Name")
    validate_input(model_type, str, "Model Type")

    return get_model_response(model_type, model_name, 'completion', prompt, **kwargs)

def validate_input(input, type, name):
    assert isinstance(input, type), f"{name} must be of {type.__name__}"

def validate_message(message):
    assert isinstance(message, dict), "Each message must be a dictionary"
    assert "role" in message, "Each message must have a 'role' key"
    assert "content" in message, "Each message must have a 'content' key"

def process_messages(messages):
    assert len(messages) > 0, "messages must be a non-empty list"
    for message in messages:
        validate_message(message)