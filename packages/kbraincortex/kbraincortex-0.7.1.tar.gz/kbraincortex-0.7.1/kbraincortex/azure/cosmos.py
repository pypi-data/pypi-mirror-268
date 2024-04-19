from azure.cosmos import CosmosClient, PartitionKey
from kbraincortex.common.configuration import COSMOS_CONNECTION_STRING
def query_cosmos_db(query, database_name, container_name, connection_string=COSMOS_CONNECTION_STRING, continuation_token=None, max_item_count=1000, enable_cross_partition_query=True):
    # Create a new Cosmos client
    client = CosmosClient.from_connection_string(connection_string)

    # Get a Cosmos database
    database = client.get_database_client(database_name)

    # Get a Cosmos container
    container = database.get_container_client(container_name)

    # Query the container
    result_iterable = container.query_items(
        query=query,
        enable_cross_partition_query=enable_cross_partition_query,
        max_item_count=max_item_count
    )

    # Use the provided continuation token to get a specific page, or the first page by default
    pages = result_iterable.by_page(continuation_token)

    page = next(pages, [])
    results = list(page)  # Process the page of results

    # Get the continuation token for the next page
    new_continuation_token = pages.continuation_token

    return results, new_continuation_token

def insert_records_into_container(database_name, container_name, items_to_add, connection_string=COSMOS_CONNECTION_STRING):
    client = create_cosmos_client(connection_string)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    for item in items_to_add:
        container.upsert_item(body=item)

def create_cosmos_client(connection_string=COSMOS_CONNECTION_STRING):
    client = CosmosClient.from_connection_string(connection_string)
    return client

def create_container(client, database_name, container_name, partition_key="/account_id"):
    database = client.create_database_if_not_exists(id=database_name)
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path=partition_key),
    )
    return container

def create_cosmos_container(connection_string, database_name, container_name, partition_key):
    client = create_cosmos_client(connection_string)
    container = create_container(client, database_name, container_name, partition_key)
    return container
