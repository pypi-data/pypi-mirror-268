import os
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.search.documents.models import QueryType
from kbraincortex.common.configuration import SEARCH_ENDPOINT, SEARCH_KEY
import logging 

def rag_search(
        query, 
        index_name,
        top="1",
        query_type=QueryType.SEMANTIC,
        semantic_config="kbrain-search-dev",
        query_language="en-us",
        query_caption="extractive",
        query_answer="extractive",
        query_speller="lexicon",
        version="2023-07-01-Preview",
        endpoint=None, 
        key=None,
        files=None
    ):

    endpoint = endpoint if endpoint is not None else SEARCH_ENDPOINT
    key = key if key is not None else SEARCH_KEY

    credential = AzureKeyCredential(key)
     # Create an instance of the SearchClient
    search_client = SearchClient(endpoint=endpoint, 
                                 index_name=index_name, 
                                 credential=credential
                                )

    filter_expression = None
    if files is not None:
        sanitized_files = [f.replace("'", "''") for f in files]
        filter_expression = " or ".join([f"filename eq '{filename}'" for filename in sanitized_files])
        
    # Make a call to azure semantic search to get the documents in the category
    try:
        results = list(search_client.search(
            search_text=query, 
            top=top, 
            query_type=query_type,
            semantic_configuration_name=f"{index_name}-semantic-config",
            query_language=query_language,
            filter=filter_expression
        ))
        return results
    except HttpResponseError as e:
        if "The request is invalid. Details: Requested value" in str(e.message):
            raise ValueError(str(e.message))
        raise e
