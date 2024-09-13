"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from .job_actions import get_jobs, get_job_by_name, trigger_training, get_decision_set, start_job, stop_job
from .event_actions import send_to_arcanna, get_arcanna_response, export_event, send_feedback

supported_operations = {
  'get_arcanna_response': get_arcanna_response,
  'send_feedback': send_feedback,
  'get_jobs': get_jobs,
  'send_to_arcanna': send_to_arcanna,
  'trigger_training': trigger_training,
  'get_decision_set': get_decision_set,
  'export_event': export_event,
  'get_job_by_name': get_job_by_name,
  'start_job': start_job,
  'stop_job': stop_job
  
}
