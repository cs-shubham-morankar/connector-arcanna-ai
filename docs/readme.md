## About the connector
Arcanna.ai is a platform for delivering decision intelligence. It augments Security Operation Center analysts in dealing with incoming threats by increasing analyst efficiency in decision-making. More information is available at https://arcanna.ai
<p>This document provides information about the Arcanna.ai Connector, which facilitates automated interactions, with a Arcanna.ai server using FortiSOAR&trade; playbooks. Add the Arcanna.ai Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Arcanna.ai.</p>

### Version information

Connector Version: 1.1.0


Authored By: Arcanna.ai

Certified: No

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
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Arcanna Response</td><td>Retrieves a event status from Arcanna.ai server based on the job ID and event ID that you have specified.</td><td>get_arcanna_response <br/>Investigation</td></tr>
<tr><td>Trigger AI Job Training</td><td>Trigger AI job training in Arcanna.ai server based on the job ID you have specified.</td><td>trigger_training <br/>Investigation</td></tr>
<tr><td>Get Decision Set</td><td>Retrieve the information of decision set from Arcanna.ai server based on the job ID you have specified.</td><td>get_decision_set <br/>Investigation</td></tr>
<tr><td>Export Event</td><td>Exports an event from Arcanna.ai server based on the job ID and event ID that you have specified.</td><td>export_event <br/>Investigation</td></tr>
<tr><td>Send Feedback</td><td>Send an feedback for a event in Arcanna.ai server.</td><td>send_feedback <br/>Investigation</td></tr>
<tr><td>Get Jobs</td><td>Retrieves a list of all the jobs from Arcanna.ai server.</td><td>get_jobs <br/>Investigation</td></tr>
<tr><td>Send To Arcanna</td><td>Send an event in Arcanna.ai server based on the job ID, title, and other input parameters you have specified.</td><td>send_to_arcanna <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Arcanna Response
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the ID of the job based on which you want to retrieve event status from Arcanna.ai server.
</td></tr><tr><td>Event ID</td><td>Specify the ID of the event based on which you want to retrieve event status from Arcanna.ai server.
</td></tr><tr><td>Retry Count</td><td>
</td></tr><tr><td>Wait Time</td><td>
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Trigger AI Job Training
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the ID of the job based on which you want to trigger AI job training in Arcanna.ai server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Decision Set
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the ID of the job based on which you want to retrieve decision set from Arcanna.ai server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Export Event
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the ID of the job based on which you want to export event from Arcanna.ai server.
</td></tr><tr><td>Event ID</td><td>Specify the ID of the event based on which you want to export event from Arcanna.ai server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Send Feedback
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>User</td><td>Specify the user based on which you want to send feedback of an event in Arcanna.ai server.
</td></tr><tr><td>Job ID</td><td>Specify the ID of the job based on which you want to send feedback of an event in Arcanna.ai server.
</td></tr><tr><td>Event ID</td><td>Specify the ID of the event based on which you want to send feedback of an event in Arcanna.ai server.
</td></tr><tr><td>Closing Status</td><td>Specify the closing status based on which you want to send feedback of an event in Arcanna.ai server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.

### operation: Get Jobs
#### Input parameters
None.

#### Output

 The output contains a non-dictionary value.

### operation: Send To Arcanna
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Job ID</td><td>Specify the ID of the job based on which you want to send event in Arcanna.ai server.
</td></tr><tr><td>Title</td><td>Specify the title based on which you want to send event in Arcanna.ai server.
</td></tr><tr><td>Case ID</td><td>Specify the ID of the case based on which you want to send event in Arcanna.ai server.
</td></tr><tr><td>Body</td><td>Specify the body based on which you want to send event in Arcanna.ai server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - Arcanna.ai - 1.1.0` playbook collection comes bundled with the Arcanna.ai connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Arcanna.ai connector.

- Arcanna.ai UseCase
- Export Event
- Get Arcanna Response
- Get Decision Set
- Get Jobs
- Send Feedback
- Send To Arcanna
- Trigger AI Job Training

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
