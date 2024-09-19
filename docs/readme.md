## About the connector
Arcanna.ai is a platform for delivering decision intelligence. It augments Security Operation Center analysts in dealing with incoming threats by increasing analyst efficiency in decision-making. More information is available at https://arcanna.ai
<p>This document provides information about the Arcanna.ai Connector, which facilitates automated interactions, with a Arcanna.ai server using FortiSOAR&trade; playbooks. Add the Arcanna.ai Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Arcanna.ai.</p>

### Version information

Connector Version: 1.2.0


Authored By: Arcanna.ai

Certified: No
## Release Notes for version 1.2.0
Following enhancements have been made to the Arcanna.ai Connector in version 1.2.0:
<ul>
<li><p>Added the following new operations:</p>

<ul>
<li>Start Job</li>
<li>Stop Job</li>
<li>Get Job by Name</li>
</ul></li>
<li>Updated logo</li>
<li>Refactored code for easier maintenance</li>
<li><p>Renamed the following operations:</p>

<ul>
<li><code>Export Event</code> to <code>Get Event</code></li>
<li><code>Trigger AI Job Training</code> to <code>Trigger Job Training</code></li>
<li><code>Get Arcanna Response</code> to <code>Get Decision on Event</code></li>
<li><code>Send to Arcanna</code> to <code>Send Event</code></li>
</ul></li>
<li>Fixed bug on <code>Send Event</code> operation</li>
<li>Added output schemas for all operations</li>
<li><p>Updated the following parameters:</p>

<ul>
<li>In operation <code>Send Feedback</code> renamed parameter <code>Closure Status</code> to <code>Feedback</code></li>
<li>In operation <code>Send Event</code> removed deprecated <code>Title</code> parameter</li>
</ul></li>
</ul>

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-arcanna-ai</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Arcanna.ai server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Arcanna.ai server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Arcanna.ai</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Protocol</td><td>Specify the protocol of the Arcanna.ai server to connect and perform automated operations.
</td>
</tr><tr><td>Server Address</td><td>Specify the URL of the Arcanna.ai server to connect and perform automated operations.
</td>
</tr><tr><td>Server Port</td><td>Specify the port of the Arcanna.ai server to connect and perform automated operations.
</td>
</tr><tr><td>Api Key</td><td>Specify the api key to access the Arcanna.ai server to connect and perform automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Decision on Event</td><td>Retrieves a decision from Arcanna.ai for a previously ingested event using the specified job ID and event ID.</td><td>get_arcanna_response <br/>Investigation</td></tr>
<tr><td>Trigger Job Training</td><td>Trigger the training of Arcanna.ai models for the provided job ID.</td><td>trigger_training <br/>Utilities</td></tr>
<tr><td>Get Job Decision Set</td><td>Retrieve the available decisions of a job in Arcanna.ai, based on the job ID you have specified.</td><td>get_decision_set <br/>Investigation</td></tr>
<tr><td>Get Event</td><td>Retrieves an event from Arcanna.ai based on the job ID and event ID that you have specified.</td><td>export_event <br/>Investigation</td></tr>
<tr><td>Send Feedback</td><td>Send feedback for an event in Arcanna.ai.</td><td>send_feedback <br/>Investigation</td></tr>
<tr><td>Get Jobs</td><td>Retrieves a list of all the jobs from Arcanna.ai.</td><td>get_jobs <br/>Utilities</td></tr>
<tr><td>Send Event</td><td>Send an event to Arcanna.ai.</td><td>send_to_arcanna <br/>Investigation</td></tr>
<tr><td>Get Job By Name</td><td>Retrieve details of a job from Arcanna.ai based on the job name.</td><td>get_job_by_name <br/>Utilities</td></tr>
<tr><td>Start Job</td><td>Start job in Arcanna.ai based on the provided job id.</td><td>start_job <br/>Utilities</td></tr>
<tr><td>Stop Job</td><td>Stop job in Arcanna.ai based on the provided job id.</td><td>stop_job <br/>Utilities</td></tr>
</tbody></table>

### operation: Get Decision on Event
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the ID of the job based on which you want to retrieve event status from Arcanna.ai server.
</td></tr><tr><td>Event ID</td><td>Specify the ID of the event based on which you want to retrieve event status from Arcanna.ai server.
</td></tr><tr><td>Retry Count</td><td>Specify the retry count of the event based on which you want to retrieve event status from Arcanna.ai server.
</td></tr><tr><td>Wait Time</td><td>Specify the wait time of the event based on which you want to retrieve event status from Arcanna.ai server.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "bucket_state": "",
    "confidence_score": "",
    "error_message": "",
    "event_id": "",
    "ingest_timestamp": "",
    "outlier": "",
    "result": "",
    "result_label": "",
    "status": ""
}</pre>

### operation: Trigger Job Training
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the ID of the job based on which you want to trigger AI job training in Arcanna.ai server.
</td></tr><tr><td>Username</td><td>Specify the username that launches the action in Arcanna.ai. If not specified, it will default to the owner of the API key used.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "error_message": "",
    "status": ""
}</pre>

### operation: Get Job Decision Set
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the ID of the job based on which you want to retrieve decision set from Arcanna.ai server.
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Event
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the ID of the job based on which you want to retrieve event from Arcanna.ai server.
</td></tr><tr><td>Event ID</td><td>Specify the ID of the event based on which you want to retrieve event from Arcanna.ai server.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "arcanna_event": {},
    "event_id": "",
    "ingest_timestamp": "",
    "status": ""
}</pre>

### operation: Send Feedback
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the ID of the job based on which you want to send feedback of an event in Arcanna.ai server.
</td></tr><tr><td>Event ID</td><td>Specify the ID of the event based on which you want to send feedback of an event in Arcanna.ai server.
</td></tr><tr><td>Feedback</td><td>Specify the feedback you want to send on to Arcanna.ai for the specified event.
</td></tr><tr><td>Username</td><td>Specify the username that will be attached to the feedback in Arcanna.ai. If no username is provided, the owner of the API key will be used.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Jobs
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "features": [],
        "feedback_documents_count": "",
        "invalid": "",
        "job_id": "",
        "labels": [],
        "last_feedback_timestamp": "",
        "last_processed_timestamp": "",
        "last_train_finished_timestamp": "",
        "last_train_start_timestamp": "",
        "processed_documents_count": "",
        "retrain_msg": "",
        "retrain_state": "",
        "status": "",
        "title": ""
    }
]</pre>

### operation: Send Event
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the Job ID to which the case should be submitted in Arcanna.
</td></tr><tr><td>Body</td><td>Specify the body based on which you want to send event in Arcanna.ai server.
</td></tr><tr><td>Case ID</td><td>Specify the ID of the case based on which you want to send event in Arcanna.ai server.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "error_message": "",
    "event_id": "",
    "ingest_timestamp": "",
    "job_id": "",
    "status": ""
}</pre>

### operation: Get Job By Name
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job Name</td><td>Specify the Job Name to retrieve details from Arcanna.ai
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "features": [],
    "feedback_documents_count": "",
    "invalid": "",
    "job_id": "",
    "labels": [],
    "last_feedback_timestamp": "",
    "last_processed_timestamp": "",
    "last_train_finished_timestamp": "",
    "last_train_start_timestamp": "",
    "processed_documents_count": "",
    "retrain_msg": "",
    "retrain_state": "",
    "status": "",
    "title": ""
}</pre>

### operation: Start Job
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the Job ID to start job in Arcanna.ai
</td></tr><tr><td>Username</td><td>Specify the username to start job in Arcanna.ai
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "error_message": "",
    "status": ""
}</pre>

### operation: Stop Job
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the Job ID to stop job in Arcanna.ai
</td></tr><tr><td>Username</td><td>Specify the username to stop job in Arcanna.ai
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "error_message": "",
    "status": ""
}</pre>
## Included playbooks
The `Sample - Arcanna.ai - 1.2.0` playbook collection comes bundled with the Arcanna.ai connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Arcanna.ai connector.

- Arcanna.ai flow example
- Get Decision on Event
- Get Event
- Get Job Decision Set
- Get Job by Name
- Get Jobs
- Send Event
- Send Feedback
- Start Job
- Stop Job
- Trigger Job Training

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.