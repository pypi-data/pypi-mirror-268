from wkregister.models import Records
from typing import Callable, Any


def kafkaParams(result: Any):

    # Retrieve 'record' or 'log', defaulting to None if neither is found
    log: Records = result.get("record") or result.get("log")
    # Check if 'log' was not retrieved and inform the user
    if not log:
        print("No record/log was set")

    # Extract 'org' and 'key' from the log, defaulting to None if not found
    org = log.org
    key = log.key

    # Check if 'org' or 'key' was not set and inform the user
    if not org:
        print("Org was not set")
    if not key:
        print("Key was not set")

    # Return the extracted values
    return org, key, log
