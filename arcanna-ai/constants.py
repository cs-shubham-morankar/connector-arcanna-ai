"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

LOGGER_NAME = 'arcanna-ai'
EVENTS_ENDPOINT = '/api/v1/events/'
JOBS_ENDPOINT = '/api/v1/jobs/'
EVENT_STATUS_FORMAT = '/api/v1/events/{}/{}'
EVENT_FEEDBACK_FORMAT = '/api/v1/events/{}/{}/feedback'
HEALTH_ENDPOINT = '/api/v1/health/'
TRIGGER_TRAIN_ENDPOINT = '/api/v1/jobs/{}/train?username={}'
START_JOB_ENDPOINT = '/api/v1/jobs/{}/start?username={}'
STOP_JOB_ENDPOINT = '/api/v1/jobs/{}/stop?username={}'
EXPORT_EVENT_ENDPOINT = '/api/v1/events/{}/{}/export'
GET_DECISION_SET_ENDPOINT = '/api/v1/jobs/{}/labels'
GET_JOB_BY_NAME_ENDPOINT = '/api/v1/jobs/get_by_name'

