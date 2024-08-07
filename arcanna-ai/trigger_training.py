from connectors.core.connector import get_logger, ConnectorError
from .constants import *
from .utils import invoke_rest_endpoint
logger = get_logger(LOGGER_NAME)


def trigger_training(config, params, *args, **kwargs):
    username = params.get('username')
    job_id = params.get('jobId')
    endpoint = TRIGGER_TRAIN_ENDPOINT.format(job_id, username)
    api_response = invoke_rest_endpoint(config, endpoint, 'POST', {})
    return api_response
