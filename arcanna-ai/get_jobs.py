"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from connectors.core.connector import get_logger, ConnectorError
from .utils import invoke_rest_endpoint
from .constants import *

logger = get_logger(LOGGER_NAME)


def get_jobs(config, params, *args, **kwargs):
    endpoint = JOBS_ENDPOINT
    request_body = {}

    logger.info("Calling get_jobs for {}".format(endpoint))

    api_response = invoke_rest_endpoint(config, endpoint, 'GET', request_body)

    return api_response
