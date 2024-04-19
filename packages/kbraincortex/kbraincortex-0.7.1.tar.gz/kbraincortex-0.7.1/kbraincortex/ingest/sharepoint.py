from kbraincortex.microsoft.graph import on_behalf_of
from kbraincortex.azure.datafactory import trigger_pipeline
from kbraincortex.azure.cosmos import insert_records_into_container

def trigger_sharepoint_ingest(host, site, assertion_token, environment, client_id, oauth_secret, tenant_id):
    
    scope = "https://graph.microsoft.com/AllSites.Read+offline_access"
    access_token, _ = on_behalf_of(client_id, oauth_secret, tenant_id, assertion_token, scope)
    
    p_name = "Ingest SharePoint"
    params = {
        "access_token":access_token,
        "host": host,
        "site": site,
        "environment": environment
    }

    run_id = trigger_pipeline(p_name, params, environment)

    insert_records_into_container(
        "status", 
        "ingest",
        [{
            "id": f"{host}:{site}",
            "type": "SharePoint",
            "status": f"Ingest of {host}:{site} initiated. Waiting for cluster...",
            "run_id": run_id
        }]
    )

    return run_id