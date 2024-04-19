from datetime import datetime, timedelta
import time
import uuid
import bcrypt
from kbrainsdk.validation.common import validate_email
from kbraincortex.azure.cosmos import insert_records_into_container, query_cosmos_db
from kbraincortex.common.configuration import DEFAULT_ACCOUNT_CONTAINER_NAME, DEFAULT_KEY_CONTAINER_NAME, DEFAULT_KEY_DATABASE_NAME

class APIKeyException(Exception):
    pass

def process_api_key(api_key, account_id):

    # Define the query
    query = {
        'query': 'SELECT * FROM c WHERE c.account_id = @account_id and c.active = true',
        'parameters': [
            {'name': '@account_id', 'value': account_id}
        ]
    }

    # Call the query function
    results, _ = query_cosmos_db(query, DEFAULT_KEY_DATABASE_NAME, DEFAULT_KEY_CONTAINER_NAME)

    # If no results are returned, raise an exception
    if not results:
        raise APIKeyException('No match found for the provided API key')

    # Iterate over the results
    for result in results:
        # Fetch the stored hashed api_key
        stored_hashed_api_key = result['api_key']

        # Compare the provided api_key with the stored hashed api_key
        if bcrypt.checkpw(api_key.encode('utf-8'), stored_hashed_api_key.encode('utf-8')):
            # If a match is found, check if it has the expiration property and it's not None
            if 'expiration' in result and result['expiration'] is not None:
                # If the expiration unix timestamp has passed, raise APIKeyException
                if time.time() > result['expiration']:
                    raise APIKeyException('API key has expired')
            # If the expiration property doesn't exist or is None, or the expiration timestamp hasn't passed, return the result
            return result

    # If no match is found after iterating over all results, raise an exception
    raise APIKeyException('Invalid API key')

def insert_account_record(account_name, account_email, notes):
    # Validate the email
    if not validate_email(account_email):
        raise ValueError("Invalid email address")

    # Generate a short UUID for the account_id
    account_id = str(uuid.uuid4())[:8]

    # Get the current time as a Unix timestamp
    creation_date = int(time.time())

    # Define the account record
    account_record = {
        'id': account_id,
        'account_id': account_id,
        'account_name': account_name,
        'account_email': account_email,
        'creation_date': creation_date,
        'notes': notes
    }

    # Insert the account record into the container
    insert_records_into_container(DEFAULT_KEY_DATABASE_NAME, DEFAULT_ACCOUNT_CONTAINER_NAME, [account_record])
    return account_id

def insert_api_key_record(account_id, scopes):

    # Validate the scopes
    if not isinstance(scopes, list) or not all(isinstance(scope, str) for scope in scopes):
        raise ValueError("Scopes must be a list of strings")

    # Generate a short UUID for the account_id
    id = str(uuid.uuid4())[:8]
    
    # Generate a unique ID for the API key
    api_key_id = str(uuid.uuid4())

    # Get the current time as a Unix timestamp
    creation_date = int(time.time())

    # Set the active property to True
    active = True

    # Set the expiration date to one year in the future
    expiration_date = int((datetime.now() + timedelta(days=365)).timestamp())

    # Hash the password

    api_key_hash = bcrypt.hashpw(api_key_id.encode(), bcrypt.gensalt())
    
    # Define the API key record
    api_key_record = {
        'id': id,
        'api_key': api_key_hash.decode(),
        'account_id': account_id,
        'scopes': scopes,
        'creation_date': creation_date,
        'active': active,
        'expiration_date': expiration_date,
    }

    # Insert the API key record into the container
    insert_records_into_container(DEFAULT_KEY_DATABASE_NAME, DEFAULT_KEY_CONTAINER_NAME, [api_key_record])
    return id, api_key_id

