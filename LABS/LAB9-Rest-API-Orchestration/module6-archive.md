# Module 6 - Configuration Archive
In this module we will use *Postman* to download an archive of the running and startup configurations of a device in the hierarchy within DNA Center. DNA Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network.

## Configuration Archive Background
DNA Center allows for the Archiving of both the Running and Startup Configurations for devices within the inventory of DNA Center. In the earlier DNA Center GUI's there was no capability to archive the configurations apart for this Rest-API based approach. That has since been remedied, but there still remains good use cases for this capability.

One such use case is configuraiton compliance. If we wanted to create a python based complaince tool, which utilized the Device Inventory as well as the configuration files, we could keep track of devices code and configurations to make sure that the code was of a certain version and perhaps certain lines of code were included in the configuration. 

## Deploying Templates to Devices
### Objectives
- Authenticate and retrieve a token from Cisco DNA Center.
- Build configuration archives based on the devices in DNA Center.
- Download each archive file.

### Prerequisites
The prerequisites steps for preparing for the lab are the following;
1. Complete [Module 5 - Template Deployment](./module5-templates.md)

## Retrieving a Configuration Archive for a Device
We will now use the Rest-API's within the collection `Configuration Archive` to pull the configuration archive for all devices within the inventory. This collection will first get a list of devices, then download the configuration archive for each one. You will need to save the responses to download them.

Follow these steps:

1. Navigate and open the desired collection runner through the following:
   1. Within Postman click on the collection shortcut in the sidebar
   2. Hover over the collection `DNA Center API LAB 304 - Configuration Archive`
   3. Click the `Run Collection` submenu option
      ![json](./images/Postman-Collection-ConfigArchive.png?raw=true "Import JSON")
2. To run the collection do the following:
   1. Locate the sub-components of the `Runner`
   2. Deselect the `Get Results` sub-component as we will run this separately
   2. Optionally select the `Save Responses` option
   3. Click  the `Run DNA Center API LAB 304 - Configuration Archive` button
      ![json](./images/Postman-Collection-ConfigArchive-Runner.png?raw=true "Import JSON")
3. The following summary will slowly appear as the collection is processed
   ![json](./images/Postman-Collection-ConfigArchive-Summary.png?raw=true "Import JSON")
4. Click on the collection `DNA Center API LAB 304 - Configuration Archive` to expand it in the left pane then do the followiing:
   1. Click on the Rest-API `Get Results` sub-component to open it on the right
   2. Click on the little arrow on the right of `Send` to expose a submenu
   3. Click `Send and Download` to send this Rest-API and automatically download what is retrieved
      ![json](./images/Postman-Collection-ConfigArchive-ResultsAPI.png?raw=true "Import JSON")
5. As the Rest-API `Get Results`completes a explorer window will prompt to save the results to the desktop click ok to save the file
   ![json](./images/Postman-Collection-ConfigArchive-ResultsAPI-Send.png?raw=true "Import JSON")
6. Within Postman click on the `Test Results 1/1` tab to display the password we will use to open the zip file downloaded. The password will be `TestT3$t` in the event you need it.
   ![json](./images/Postman-Collection-ConfigArchive-ResultsAPI-TestResults.png?raw=true "Import JSON")
7. Locate the zip file on the desktop, and extract it using whatever extraction tool is available to your system. WinRar is what can be used and is displayed here.
   ![json](./images/Postman-Collection-ConfigArchive-Extract.png?raw=true "Import JSON")
8. During Extraction you will be prompted for the password we stored from step 6 but again it is `TestT3$t` in the event you can't locate it. Enter the password as prompted and complete the extraction.
   ![json](./images/Postman-Collection-ConfigArchive-Pwd.png?raw=true "Import JSON")
9. Locate the Extracted folder and open one of the text based files within to reveal the configuration selected.
   ![json](./images/Postman-Collection-ConfigArchive-Verify.png?raw=true "Import JSON")

## Summary
Congratulations, in this lablet we used *Postman* to download an archive of the running and startup configurations of devices from DNA Center. DNA Center allows for the Archiving of both the Running and Startup Configurations for devices within the inventory of DNA Center. In the earlier DNA Center GUI's there was no capability to archive the configurations apart for this Rest-API based approach. That has since been remedied, but there still remains good use cases for this capability.

Additionally if there is time, look at the pre and post scripts within Postman.
