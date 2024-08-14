"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from connectors.core.connector import get_logger, ConnectorError
from .constants import *

logger = get_logger(LOGGER_NAME)
from .utils import invoke_rest_endpoint


def send_feedback(config, params, *args, **kwargs):
    CLOSING_STATUS = {'DROP ALERT': 'drop_alert', 'ESCALATE ALERT': 'escalate_alert', 'NOT SURE': 'not_sure'}
    logger.info("Start sending feedback")
    job_id = params.get('jobId')
    user = params.get('user')
    event_id = params.get('eventId')
    closing_status = CLOSING_STATUS.get(params.get('closingStatus'))

    data = {
        "cortex_user": user,
        "feedback": closing_status
    }
    request_body = data
    endpoint = EVENT_FEEDBACK_FORMAT.format(job_id, event_id)
    api_response = invoke_rest_endpoint(config, endpoint, 'PUT', request_body)

    api_response.update({'status': 'ok', "value": endpoint})
    return api_response
