"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from .utils import invoke_rest_endpoint
from connectors.core.connector import get_logger, ConnectorError
from .constants import *

logger = get_logger(LOGGER_NAME)


def health_check(config=None, *args, **kwargs):
    auth_endpoint = HEALTH_ENDPOINT
    logger.info("Calling healtcheck")
    # the utility function raises an exception if the response is not one of the success responses
    invoke_rest_endpoint(config, auth_endpoint, 'GET')

    # will reach here only if the previous api_call was a success
    return 'Connector is Available'
