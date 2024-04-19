from kbraincortex.azure.cosmos import query_cosmos_db
from kbraincortex.common.configuration import DEFAULT_ACCOUNT_CONTAINER_NAME, DEFAULT_KEY_DATABASE_NAME

def get_account_data(account_id):
    query = {
        'query': 'SELECT * FROM c WHERE c.account_id = @account_id',
        'parameters': [
            {'name': '@account_id', 'value': account_id}
        ]
    }

    results, _ = query_cosmos_db(query, DEFAULT_KEY_DATABASE_NAME, DEFAULT_ACCOUNT_CONTAINER_NAME)
    return results[0]