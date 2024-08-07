## About the connector
Arcanna.ai is a platform for delivering decision intelligence. It augments Security Operation Center analysts in dealing with incoming threats by increasing analyst efficiency in decision-making. More information is available at https://arcanna.ai
<p>This document provides information about the Arcanna.ai Connector, which facilitates automated interactions, with a Arcanna.ai server using FortiSOAR&trade; playbooks. Add the Arcanna.ai Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Arcanna.ai.</p>
### Version information

Connector Version: 1.1.0


Authored By: Arcanna.ai

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-arcanna-ai`

## Prerequisites to configuring the connector
- You must have the URL of Arcanna.ai server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Arcanna.ai server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Arcanna.ai</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Protocol<br></td><td>Specify the protocol of the Arcanna.ai server to connect and perform automated operations.<br>
<tr><td>Server Address<br></td><td>Specify the URL of the Arcanna.ai server to connect and perform automated operations.<br>
<tr><td>Server Port<br></td><td>Specify the port of the Arcanna.ai server to connect and perform automated operations.<br>
<tr><td>Api Key<br></td><td>Specify the api key to access the Arcanna.ai server to connect and perform automated operations.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>
## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Event Status<br></td><td>Retrieves a event status from Arcanna.ai server based on the job ID and event ID that you have specified.<br></td><td>get_arcanna_response <br/>Investigation<br></td></tr>
<tr><td>Send Event Feedback<br></td><td>Send an feedback for a event in Arcanna.ai server.<br></td><td>send_feedback <br/>Investigation<br></td></tr>
<tr><td>Get Jobs List<br></td><td>Retrieves a list of all the jobs from Arcanna.ai server.<br></td><td>get_jobs <br/>Investigation<br></td></tr>
<tr><td>Send Event<br></td><td>Send an event in Arcanna.ai server based on the job ID, title, and other input parameters you have specified.<br></td><td>send_to_arcanna <br/>Investigation<br></td></tr>
</tbody></table>
### operation: Get Event Status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Job ID<br></td><td>Specify the ID of the job based on which you want to retrieve event status from Arcanna.ai server.<br>
</td></tr><tr><td>Event ID<br></td><td>Specify the ID of the event based on which you want to retrieve event status from Arcanna.ai server.<br>
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Send Event Feedback
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Username<br></td><td>Specify the username based on which you want to send feedback of an event in Arcanna.ai server.<br>
</td></tr><tr><td>Job ID<br></td><td>Specify the ID of the job based on which you want to send feedback of an event in Arcanna.ai server.<br>
</td></tr><tr><td>Event ID<br></td><td>Specify the ID of the event based on which you want to send feedback of an event in Arcanna.ai server.<br>
</td></tr><tr><td>Closing Status<br></td><td>Specify the closing status based on which you want to send feedback of an event in Arcanna.ai server.<br>
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Get Jobs List
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Send Event
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Job ID<br></td><td>Specify the ID of the job based on which you want to send event in Arcanna.ai server.<br>
</td></tr><tr><td>Title<br></td><td>Specify the title based on which you want to send event in Arcanna.ai server.<br>
</td></tr><tr><td>Body<br></td><td>Specify the body based on which you want to send event in Arcanna.ai server.<br>
</td></tr><tr><td>Case ID<br></td><td>Specify the ID of the case based on which you want to send event in Arcanna.ai server.<br>
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - arcanna-ai - 1.0.0` playbook collection comes bundled with the Arcanna.ai connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Arcanna.ai connector.

- Get Event Status
- Send Event Feedback
- Get Jobs List
- Send Event

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
