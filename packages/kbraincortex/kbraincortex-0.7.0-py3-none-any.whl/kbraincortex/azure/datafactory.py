
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.identity import ClientSecretCredential
from kbraincortex.common.configuration import ADF_SP_SECRET, ADF_SP_CLIENT_ID, ADF_SP_TENANT_ID, ADF_SP_SUBSCRIPTION_ID

adf_configs = {
    "dev": {
        "rg_name": "rg-prd-kbrain",
        "df_name": "kbrain-ingest-factory"
    },
    "production": {
        "rg_name": "rg-prd-kbrain",
        "df_name": "kbrain-ingest-factory"
    }
}

def trigger_pipeline(p_name, params, environment="production"):
    credentials = ClientSecretCredential(
        client_id=ADF_SP_CLIENT_ID, 
        client_secret=ADF_SP_SECRET, 
        tenant_id=ADF_SP_TENANT_ID
    )
    adf_client = DataFactoryManagementClient(credentials, ADF_SP_SUBSCRIPTION_ID)
    config = adf_configs[environment]
    rg_name = config["rg_name"]
    df_name = config["df_name"]
    run_response = adf_client.pipelines.create_run(rg_name, df_name, p_name, parameters=params)
    run_id = run_response.run_id
    return run_id

def get_pipeline_status(run_id, environment="production"):
    credentials = ClientSecretCredential(
        client_id=ADF_SP_CLIENT_ID, 
        client_secret=ADF_SP_SECRET, 
        tenant_id=ADF_SP_TENANT_ID
    )
    config = adf_configs[environment]
    rg_name = config["rg_name"]
    df_name = config["df_name"]
    adf_client = DataFactoryManagementClient(credentials, ADF_SP_SUBSCRIPTION_ID)
    pipeline_run = adf_client.pipeline_runs.get(rg_name, df_name, run_id)
    return pipeline_run.status