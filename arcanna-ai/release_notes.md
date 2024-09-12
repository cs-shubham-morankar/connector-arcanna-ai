#### Following enhancements have been made to the Arcanna.ai Connector in version 1.2.0:

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