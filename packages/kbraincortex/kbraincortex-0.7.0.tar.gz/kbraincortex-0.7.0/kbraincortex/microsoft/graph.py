import requests
import json
from kbrainsdk.security.bearer import extract_claims 
import logging
GRAPH_URL = "https://graph.microsoft.com/v1.0/"

def on_behalf_of(client_id, client_secret, tenant_id, assertion_token, scope):
    AUTH_URL = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
    grant_type = "urn:ietf:params:oauth:grant-type:jwt-bearer"
    query_params = f"grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}&assertion={assertion_token}&scope={scope}&requested_token_use=on_behalf_of"
    logging.info(client_id)
    logging.info(scope)
    claims = extract_claims(f"Bearer {assertion_token}")
    logging.info(claims)
    response = requests.post(AUTH_URL, data=f"{query_params}", headers={"Content-Type": "application/x-www-form-urlencoded"})
    token_data = response.json()
    if 'access_token' not in token_data:
        raise ValueError(f"On Behalf of request failed: {token_data}")
    access_token = token_data["access_token"]
    refresh_token = token_data["refresh_token"]
    
    return access_token, refresh_token

def list_site_contents(access_token, site, host):
    HEADERS = {'Authorization': f"Bearer {access_token}" }        
    response = requests.get(f"{GRAPH_URL}sites/{host}:/sites/{site}:/drives", headers=HEADERS) 
    return json.loads(response.text)

def get_entra_groups(client_id, oauth_secret, tenant_id, token, next_link=None):
    
    claims = extract_claims(f"Bearer {token}")
    oid = claims["oid"]
        
    scope = "https://graph.microsoft.com/GroupMember.Read.All"
    access_token, _ = on_behalf_of(client_id, oauth_secret, tenant_id, token, scope)

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    groups = []
    
    try:
        link = next_link if next_link else f"https://graph.microsoft.com/v1.0/users/{oid}/memberOf"
        response = requests.get(link, headers=headers)
        response.raise_for_status()
        logging.info("Graph response:")
        logging.info(response.json())
        #Get next page if there is one
        response_json = response.json()
        group_objects = response_json.get("value", [])
        for group in group_objects:
            groups.append(group["id"])
        if "@odata.nextLink" in response_json:
            next_link = response_json["@odata.nextLink"]
            logging.info(f"Next link: {next_link}")
            groups += get_entra_groups(client_id, oauth_secret, tenant_id, token, next_link = next_link)
        else:
            logging.info("No more pages.")
    except Exception as ex:
        logging.error(f"Error getting groups: {ex}")
        groups += claims["groups"]
    logging.info(groups)
    return groups