"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def invoke_rest_endpoint(config, endpoint, method='GET', data=None, headers=None):
    # utility function for a sample rest based integration using basic authentication
    # change as required for the specific integration being built

    server_address = config.get('server_address')
    port = config.get('port', '443')
    apikey = config.get('apiKey')
    protocol = config.get('protocol', 'https')
    verify_ssl = config.get('verify_ssl', True)
    if not server_address or not apikey:
        raise ConnectorError('Missing required parameters')

    if headers is None:
        headers = {
            'Content-Type': 'application/json',
            'x-arcanna-api-key': apikey

        }

    url = f"{protocol.lower()}://{server_address}:{port}{endpoint}"
    logger.info(f"url={url}")
    try:
        response = requests.request(method, url, verify=verify_ssl,
                                    json=data, headers=headers)
    except Exception as e:
        logger.exception('Error invoking endpoint: {0}'.format(endpoint))
        raise ConnectorError('Error: {0}'.format(str(e)))
    if response.ok:
        logger.info(f"url={url} response {response.status_code}")
        return response.json()
    else:
        logger.error(response.content)
        logger.error(url)

        raise ConnectorError(response.content)
