from applicationinsights import TelemetryClient
from kbraincortex.common.configuration import TELEMETRY_KEY
import logging 

def get_telemetry_client(operation_id=None, telemetry_key=TELEMETRY_KEY):
    # Create a TelemetryClient
    tc = TelemetryClient(telemetry_key)
    if operation_id is not None:    
        tc.context.operation.id = str(operation_id)
    return tc

def log_request(event_label, custom_metadata, operation_id=None, telemetry_key=TELEMETRY_KEY):
    # Create a TelemetryClient
    tc = get_telemetry_client(operation_id, telemetry_key)

    # Initialize properties as an empty dictionary
    properties = {}

    # Use the function to flatten custom_metadata and add it to properties
    properties = flatten_dict(custom_metadata, properties=properties)
    # Log a custom event with the API key as a property
    tc.track_event(event_label, properties)

    # Flush the telemetry to send it to Application Insights
    tc.flush()

def flatten_dict(d, prefix='', properties={}):
    for key, value in d.items():
        if isinstance(value, dict):
            flatten_dict(value, f'{prefix}{key}_', properties)
        elif isinstance(value, list):
            for i, v in enumerate(value):
                if isinstance(v, dict):
                    flatten_dict(v, f'{prefix}{key}_{i}_', properties)
                else:
                    properties[f'{prefix}{key}_{i}'] = str(v)
        else:
            properties[f'{prefix}{key}'] = str(value)
    return properties