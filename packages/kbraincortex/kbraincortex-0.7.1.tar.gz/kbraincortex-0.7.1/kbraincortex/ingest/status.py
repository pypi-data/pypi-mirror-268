from kbraincortex.azure.cosmos import query_cosmos_db 
from kbraincortex.azure.datafactory import get_pipeline_status
def get_status(datasource):

    query = {
        "query": "SELECT * FROM c WHERE c.id = @datasource",
        "parameters": [{"name": "@datasource", "value": datasource}]
    }

    statuses, _ = query_cosmos_db(
        query,
        "status",        
        "ingest"
    )

    if len(statuses) == 0:
        raise ValueError(f"Could not find status for datasource {datasource}")

    status = statuses[0]
    message = status["status"]
    updated = status["_ts"]
    return message, updated

def get_adf_pipeline_status(run_id, environment="production"):
    return get_pipeline_status(run_id, environment)