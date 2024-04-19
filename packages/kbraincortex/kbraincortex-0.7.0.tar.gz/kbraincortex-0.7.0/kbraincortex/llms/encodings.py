from tiktoken import encoding_for_model

def count_tokens(model_name, text):
    encoding = encoding_for_model(model_name)
    return len(encoding.encode(text))