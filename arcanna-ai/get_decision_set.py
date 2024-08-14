"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from connectors.core.connector import get_logger, ConnectorError
from .constants import *
from .utils import invoke_rest_endpoint
logger = get_logger(LOGGER_NAME)


def get_decision_set(config, params, *args, **kwargs):
    job_id = params.get('jobId')
    endpoint = GET_DECISION_SET_ENDPOINT.format(job_id)
    api_response = invoke_rest_endpoint(config, endpoint, 'GET', {})
    return api_response
