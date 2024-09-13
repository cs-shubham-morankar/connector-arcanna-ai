## About the connector

Arcanna.ai is a platform for delivering decision intelligence. It augments Security Operation Center analysts in dealing
with incoming threats by increasing analyst efficiency in decision-making. More information is available
at https://arcanna.ai
<p>This document provides information about the Arcanna.ai Connector, which facilitates automated interactions, with a Arcanna.ai server using FortiSOAR&trade; playbooks. Add the Arcanna.ai Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Arcanna.ai.</p>

### Version information

Connector Version: 1.2.0

Authored By: Arcanna.ai

Certified: No

## Release Notes for version 1.2.0

Following enhancements have been made to the Arcanna.ai Connector in version 1.2.0:

- Added the following new operations:
    - Start Job
    - Stop Job
    - Get Job by Name
- Updated logo
- Refactored code for easier maintenance
- Renamed the following operations:
    - `Export Event` to `Get Event`
    - `Trigger AI Job Training` to `Trigger Job Training`
    - `Get Arcanna Response` to `Get Decision on Event`
    - `Send to Arcanna` to `Send Event`
- Fixed bug on `Send Event` operation
- Added relevant descriptions/tooltips to operations and parameters
- Added output schemas on all operations
- Updated the following parameters:
    - In operation `Send Feedback` renamed parameter `Closure status` to `Feedback`
    - In operation `Send Event` removed deprecated `Title` parameter

## Installing the connector

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-arcanna-ai</pre>

## Prerequisites to configuring the connector

- You must have the credentials of Arcanna.ai server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Arcanna.ai server.

## Minimum Permissions Required

- Not applicable

## Configuring the connector

For the procedure to configure a connector,
click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

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

The following automated operations can be included in playbooks and you can also use the annotations to access
operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1>
  <thead>
    <tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr>
  </thead>
  <tbody>
    <tr><td>Get Decision on Event</td><td>Retrieves a decision from Arcanna.ai for a previously ingested event using the specified job ID and event ID.</td><td>get_arcanna_response <br/>Investigation</td></tr>
    <tr><td>Trigger Job Training</td><td>Trigger the training of Arcanna.ai models for the provided job ID.</td><td>trigger_training <br/>Utilities</td></tr>
    <tr><td>Get Job Decision Set</td><td>Retrieve the available decisions of a job in Arcanna.ai, based on the job ID you have specified.</td><td>get_decision_set <br/>Investigation</td></tr>
    <tr><td>Get Event</td><td>Retrieves an event from Arcanna.ai based on the job ID and event ID that you have specified.</td><td>export_event <br/>Investigation</td></tr>
    <tr><td>Send Feedback</td><td>Send feedback for an event in Arcanna.ai.</td><td>send_feedback <br/>Investigation</td></tr>
    <tr><td>Get Jobs</td><td>Retrieves a list of all the jobs from Arcanna.ai.</td><td>get_jobs <br/>Utilities</td></tr>
    <tr><td>Send Event</td><td>Send an event to Arcanna.ai.</td><td>send_to_arcanna <br/>Investigation</td></tr>
    <tr><td>Get Job by Name</td><td>Retrieve details of a job from Arcanna.ai based on the job name.</td><td>get_job_by_name <br/>Utilities</td></tr>
    <tr><td>Start job</td><td>Start job in Arcanna.ai based on the provided job id.</td><td>start_job <br/>Utilities</td></tr>
    <tr><td>Stop job</td><td>Stop job in Arcanna.ai based on the provided job id.</td><td>stop_job <br/>Utilities</td></tr>
  </tbody>
</table>

Here’s the markdown documentation for each operation described in the provided JSON:

---

### operation: Get Decision on Event

#### Input parameters

<table border=1>
<thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Job ID</td><td>Specify the ID of the job to retrieve a decision for a previously ingested event in Arcanna.ai.</td></tr>
<tr><td>Event ID</td><td>Specify the ID of the event for which the decision will be retrieved.</td></tr>
<tr><td>Retry Count</td><td>Number of retries while waiting for the decision to be available. Default value: 10.</td></tr>
<tr><td>Wait Time</td><td>Time in seconds between retries. Default value: 5.</td></tr>
</tbody>
</table>

#### Output

The output contains the decision result along with additional metadata such as status, confidence score, and any error messages.

---

### operation: Trigger Job Training

#### Input parameters

<table border=1>
<thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Job ID</td><td>Specify the ID of the job to trigger AI job training in Arcanna.ai.</td></tr>
<tr><td>Username</td><td>The username that triggers the action. Defaults to the owner of the API key if not specified.</td></tr>
</tbody>
</table>

#### Output

The output contains a status message and any associated error messages.

---

### operation: Get Job Decision Set

#### Input parameters

<table border=1>
<thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Job ID</td><td>Specify the ID of the job to retrieve its available decisions in Arcanna.ai.</td></tr>
</tbody>
</table>

#### Output

The output contains the set of decisions for the specified job.

---

### operation: Get Event

#### Input parameters

<table border=1>
<thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Job ID</td><td>Specify the job ID to retrieve the event in Arcanna.ai.</td></tr>
<tr><td>Event ID</td><td>Specify the event ID to retrieve.</td></tr>
</tbody>
</table>

#### Output

The output contains the retrieved event data, including the event ID, status, and timestamp.

---

### operation: Send Feedback

#### Input parameters

<table border=1>
<thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Job ID</td><td>Specify the job ID for which the feedback will be provided.</td></tr>
<tr><td>Event ID</td><td>Specify the event ID for which the feedback is provided.</td></tr>
<tr><td>Feedback</td><td>Choose feedback action: Drop or Escalate.</td></tr>
<tr><td>User</td><td>Specify the username that will be associated with the feedback. Defaults to the owner of the API key if not specified.</td></tr>
</tbody>
</table>

#### Output

The output contains a status message confirming the feedback submission.

---

### operation: Get Jobs

#### Input parameters

_None_

#### Output

The output contains a list of all jobs from Arcanna.ai, with detailed job information such as job ID, status, processed documents, and timestamps.

---

### operation: Send Event

#### Input parameters

<table border=1>
<thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Job ID</td><td>Specify the job ID where the event will be submitted.</td></tr>
<tr><td>Body</td><td>Provide the JSON body that contains the event data to be sent to Arcanna.ai.</td></tr>
<tr><td>Case ID</td><td>Optional: Specify the case ID. If not provided, Arcanna will generate one automatically.</td></tr>
</tbody>
</table>

#### Output

The output contains information about the event submission, including the job ID, event ID, status, and timestamp.

---

### operation: Get Job By Name

#### Input parameters

<table border=1>
<thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Job Name</td><td>Specify the name of the job to retrieve its details from Arcanna.ai.</td></tr>
</tbody>
</table>

#### Output

The output contains detailed information about the job, including job ID, status, retraining state, and associated labels and features.

---

### operation: Start Job

#### Input parameters

<table border=1>
<thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Job ID</td><td>Specify the ID of the job to start in Arcanna.ai.</td></tr>
<tr><td>Username</td><td>Optional: Specify the username that triggers the job. Defaults to the owner of the API key if not provided.</td></tr>
</tbody>
</table>

#### Output

The output contains a status message confirming the job start or an error message if applicable.

---

### operation: Stop Job

#### Input parameters

<table border=1>
<thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Job ID</td><td>Specify the ID of the job to stop in Arcanna.ai.</td></tr>
<tr><td>Username</td><td>Optional: Specify the username that triggers the job stop. Defaults to the owner of the API key if not provided.</td></tr>
</tbody>
</table>

#### Output

The output contains a status message confirming the job stop or an error message if applicable.

---

## Included playbooks

The `Sample - Arcanna.ai - 1.2.0` playbook collection comes bundled with the Arcanna.ai connector. These playbooks
contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > *
*Playbooks** section in FortiSOAR&trade; after importing the Arcanna.ai connector.

- Arcanna.ai flow example
- Start job
- Stop Job
- Get Event
- Get Decision on Event
- Get Decision Set
- Get Jobs
- Get Job by Name
- Send Feedback
- Send To Arcanna
- Trigger Job Training

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those
playbooks and move them to a different collection since the sample playbook collection gets deleted during connector
upgrade and delete.
