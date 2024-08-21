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
import time


def get_arcanna_response(config, params, *args, **kwargs):
    event_id = params.get('eventId')
    job_id = params.get('jobId')
    retry_count = int(params.get('retryCount'))
    wait_time = int(params.get('waitTime'))

    endpoint = EVENT_STATUS_FORMAT.format(job_id, event_id)
    api_response = invoke_rest_endpoint(config, endpoint, 'GET', {})
    while api_response.get('status', "pending_inference") == "pending_inference" and retry_count > 0:
        api_response = invoke_rest_endpoint(config, endpoint, 'GET', {})
        retry_count -= 1
        time.sleep(wait_time)
    return api_response
