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


def get_jobs(config, params, *args, **kwargs):
    endpoint = JOBS_ENDPOINT
    request_body = {}
    logger.info("Calling get_jobs for {}".format(endpoint))
    api_response = invoke_rest_endpoint(config, endpoint, 'GET', request_body)
    return api_response


def get_job_by_name(config, params, *args, **kwargs):
    job_name = params.get('jobName')

    endpoint = GET_JOB_BY_NAME_ENDPOINT
    data = {
        "job_name": job_name
    }

    request_body = data
    api_response = invoke_rest_endpoint(config, endpoint, 'POST', request_body)
    return api_response


def start_job(config, params, *args, **kwargs):
    username = params.get('username')
    job_id = params.get('jobId')
    endpoint = START_JOB_ENDPOINT.format(int(job_id), username)
    api_response = invoke_rest_endpoint(config, endpoint, 'POST', {})
    return api_response


def stop_job(config, params, *args, **kwargs):
    username = params.get('username')
    job_id = params.get('jobId')
    endpoint = STOP_JOB_ENDPOINT.format(int(job_id), username)
    api_response = invoke_rest_endpoint(config, endpoint, 'POST', {})
    return api_response


def trigger_training(config, params, *args, **kwargs):
    username = params.get('username')
    job_id = params.get('jobId')
    endpoint = TRIGGER_TRAIN_ENDPOINT.format(job_id, username)
    api_response = invoke_rest_endpoint(config, endpoint, 'POST', {})
    return api_response


def get_decision_set(config, params, *args, **kwargs):
    job_id = params.get('jobId')
    endpoint = GET_DECISION_SET_ENDPOINT.format(job_id)
    api_response = invoke_rest_endpoint(config, endpoint, 'GET', {})
    return api_response
