from kbraincortex.microsoft.graph import on_behalf_of
from kbraincortex.azure.datafactory import trigger_pipeline
from kbraincortex.azure.cosmos import insert_records_into_container
from kbrainsdk.ingest import Ingest
def trigger_onedrive_ingest(email, assertion_token, environment, client_id, oauth_secret, tenant_id):

    scope = "https://graph.microsoft.com/Files.Read+offline_access"  
    access_token, _ = on_behalf_of(client_id, oauth_secret, tenant_id, assertion_token, scope) 
    
    id = Ingest.convert_email_to_datasource(None, email)
    p_name = "Ingest OneDrive"
    params = {
        "access_token":access_token,
        "email":email,
        "environment": environment
    }

    run_id = trigger_pipeline(p_name, params, environment)

    insert_records_into_container(
        "status", 
        "ingest",
        [{
            "id": id,
            "type": "OneDrive",
            "status": f"Ingest of OneDrive initiated. Waiting for cluster...",
            "run_id": run_id
        }]
    )

    return run_id