import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import *
from .utils import invoke_rest_endpoint

logger = get_logger(LOGGER_NAME)


def send_to_arcanna(config, params, *args, **kwargs):
    logger.info("Start sending.")

    job_id = params.get('jobId')
    title = params.get("title")
    body = params.get('body')
    caseId = params.get("caseId", None)
    if "id" in body:
        body["id"] = str(id)
    data = {
        "job_id": int(job_id),
        "title": title,
        "raw_body": body
    }
    # if not endpoint or not data:
    #    raise ConnectorError('Missing required input')
    endpoint = EVENTS_ENDPOINT
    if caseId:
        endpoint = endpoint + str(caseId)

    # next call the rest endpoint on the target server with the required inputs
    # sample code below. to be replaced for the integration
    request_body = data

    api_response = invoke_rest_endpoint(config, endpoint, 'POST', request_body)
    # data transformation here to add/remove/modify some part of the api response
    # sample code below to add a custom key
    api_response.update({'status': 'ok', "value": endpoint})
    return api_response
