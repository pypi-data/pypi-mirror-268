import numpy as np
import logging

from kbraincortex.azure.cosmos import query_cosmos_db
from kbraincortex.ai.reasoning import decide
from kbrainsdk.azure_models.model import AzureDeployedModel
from kbraincortex.common.configuration import CATEGORIZE_QUERY_MODEL_API_KEY


class_mapping = [
    "other",
    "Modeling Simulation Training",
    "Engineering",
    "Revamps Conversions",
    "Consulting",
    "Technologies",
    "Cybersecurity",
]

class_threshold = {
    "other": 0.9,
    "Modeling Simulation Training": 0.9,
    "Engineering": 0.9,
    "Revamps Conversions": 0.97,
    "Consulting": 0.97,
    "Technologies": 0.97,
    "Cybersecurity": 0.97,
}

url = "https://kbrain-ml-workspace-qykqu.southcentralus.inference.ml.azure.com/score"
api_key = CATEGORIZE_QUERY_MODEL_API_KEY
if not api_key:
    raise Exception("Please provide an api_key")


def prepare_category_tree():
    query = {
        "query": "SELECT TOP 1 * from c ORDER BY c.id DESC",
    }

    category_list, _ = query_cosmos_db(query, "taxonomy", "categories")

    categories = category_list[0]["categories"]

    high_level_categories = list(
        set([category.split("_")[0] for category in categories])
    )
    tree = {}
    for category in high_level_categories:
        for low_level_category in categories:
            if low_level_category[: len(category)] == category:
                if category not in tree:
                    tree[category] = []
                tree[category].append(low_level_category[len(category) + 1 :])

    return tree, high_level_categories


def get_threshold_prediction(input_array):
    # print(input_array)
    sorted_array = input_array[input_array[:, 1].astype(float).argsort()[::-1]]

    sorted_bool = [
        (key, float(val) > class_threshold[key]) for key, val in sorted_array
    ]

    for item in sorted_bool:
        if item[1]:
            return item[0]
    return "unknown"


def get_model_prediction(query):
    data = {"input_data": {"columns": ["question"], "index": [0], "data": [[query]]}}

    model = AzureDeployedModel(endpoint_url=url, api_key=api_key)

    prediction = model.predict(data)

    prediction_classes = list(zip(class_mapping, prediction))
    logging.info(f"prediction classes: {prediction_classes}")
    return get_threshold_prediction(np.array(prediction_classes))


def categorize_query(query, topic = None):
    if topic is None:
        topic = query
    logging.info(f"Query: {query}")
    high_level_category = get_model_prediction(query)
    logging.info(f"high_level_category: {high_level_category}")
    tree, high_level_categories = prepare_category_tree()

    choices = [
        {
            "label": category,
            "description": f"The {category} is the most semantically relevant",
        }
        for category in high_level_categories
    ]
    examples = [
        {
            "query": "What are KBR's cybersecurity policies?",
            "argument": f"Cybersecurity is the best choice that fits the query semantically since it is mentioned directly in the query.",
            "decision": f"Cybersecurity",
        },
        {
            "query": "What engineering projects has KBR worked on?",
            "argument": f"Engineering is the best choice that fits the query semantically since it is mentioned directly in the query.",
            "decision": f"Engineering",
        },
        {
            "query": "How has KBR helped other companies?",
            "argument": f"Consulting makes the most sense here since it involves how KBR has interacted with other companies in a helpful way.",
            "decision": f"Consulting",
        },
    ]
    logging.info(choices)

    if high_level_category not in ["other", "unknown"]:
        reasoning = "This was predicted by the azure ml model"
        completion_tokens = 0
        prompt_tokens = 0
    else:
        reasoning, high_level_category, completion_tokens, prompt_tokens = decide(
            topic, choices, examples
        )

    logging.info(reasoning)
    logging.info(high_level_category)
    tokens = {
        "tokens_completion": completion_tokens,
        "tokens_prompt": prompt_tokens,
        "tokens_total": completion_tokens + prompt_tokens,
    }

    categories = tree[high_level_category]

    choices = [
        {
            "label": category,
            "description": f"The {category} is the most semantically relevant",
        }
        for category in categories
    ]
    logging.info(choices)
    examples = []
    reasoning, choice, completion_tokens, prompt_tokens = decide(
        topic, choices, examples
    )
    tokens["tokens_completion"] += completion_tokens
    tokens["tokens_prompt"] += prompt_tokens
    tokens["tokens_total"] += completion_tokens + prompt_tokens

    logging.info(reasoning)
    logging.info(choice)
    logging.info(tokens)
    chosen_category = f"{high_level_category}_{choice}"

    return chosen_category, tokens
