"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from connectors.core.connector import get_logger, ConnectorError
from .constants import *
from .utils import invoke_rest_endpoint
import time

logger = get_logger(LOGGER_NAME)

def send_to_arcanna(config, params, *args, **kwargs):
    logger.info("Start sending.")

    job_id = params.get('jobId')
    body = params.get('body')
    caseId = params.get("caseId", None)

    data = {
        "job_id": int(job_id),
        "raw_body": body
    }

    endpoint = EVENTS_ENDPOINT
    if caseId is not None and caseId != "":
        endpoint = endpoint + str(caseId)

    request_body = data

    api_response = invoke_rest_endpoint(config, endpoint, 'POST', request_body)
    return api_response

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

def export_event(config, params, *args, **kwargs):
    event_id = params.get('eventId')
    job_id = params.get('jobId')
    endpoint = EXPORT_EVENT_ENDPOINT.format(job_id, event_id)
    api_response = invoke_rest_endpoint(config, endpoint, 'GET', {})
    return api_response

def send_feedback(config, params, *args, **kwargs):
    logger.info("Start sending feedback")
    job_id = params.get('jobId')
    user = params.get('user')
    event_id = params.get('eventId')
    feedback = params.get('feedback')

    data = {
        "cortex_user": user,
        "feedback": feedback
    }
    request_body = data
    endpoint = EVENT_FEEDBACK_FORMAT.format(job_id, event_id)
    api_response = invoke_rest_endpoint(config, endpoint, 'PUT', request_body)
    return api_response

