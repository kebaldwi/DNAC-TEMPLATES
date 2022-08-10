# Module 8 - Running Show Commands
In this module we will use *Postman* to run some show commands on network devices within the infrastructure that are managed by DNA Center. This allows a method of getting troubleshooting information in the event we need to populate 3rd party management systems.

## Command Runner Background
The Command Runner tool allows you to run cli commands from the Inventory window on platforms. 

The platform commands that you can run are those such as ping, traceroute, and snmpget to troubleshoot device reachability issues. Additionally show commands may also be used to help or aid in troubleshooting.

## Deploying Templates to Devices
### Objectives
- Authenticate and retrieve a token from Cisco DNA Center.
- Execute a show command against a device in the inventory.
- Retrieve the results of the show command from DNA Center.

### Prerequisites
The prerequisites steps for preparing for the lab are the following;
1. Complete [Module 7 - Retrieving Network Inventory](./module7-inventory.md)

## Using Command Runner
We will now initiate a `show cdp neighbor` command against `c9300-2` managed by DNA Center using the Rest-API within the collection `DNA Center API LAB 402 - Command Runner`

Follow these steps:

1. Navigate and open the desired collection runner through the following:
   1. Within Postman click on the collection shortcut in the sidebar
   2. Hover over the collection `DNA Center API LAB 402 - Command Runner`
   3. Click the `Run Collection` submenu option
      ![json](./images/Postman-Collection-CmdRun.png?raw=true "Import JSON")
2. To run the collection do the following:
   1. Ensure all the sub-components of the `Runner` are selected
   2. Select the `Save Responses` option as we will need the output
   3. Click  the `Run DNA Center API LAB 402 - Command Runner` button
      ![json](./images/Postman-Collection-CmdRun-Runner.png?raw=true "Import JSON")
3. The following results will slowly appear as the collection is processed.
   1. Click `View Results` on the Left
   2. Watch the Results slowly appear. The API has been set up to give device info in the test area.
   ![json](./images/Postman-Collection-CmdRun-Summary.png?raw=true "Import JSON")
4. To view the results do the following:
   1. Click the `Console` option at the bottom of postman
   2. Expand the Get request that begins `GET https://198.18.129.100/dna/intent/api/v1/file/...` 
   3. Within the `Response Body` click the `Drop Down` arrow and view the Response
      ![json](./images/Postman-Collection-CmdRun-Console.png?raw=true "Import JSON")

## Summary
We have been able to run diagnostic commands via Rest-API, which is useful if we want to get any show command or output from any diagnostic command to a third party system. This allows us to augment DNA Center and create whatever we like in regards to troubleshooting support for other platforms like ServiceNow or other 3rd party Rest-API based ITSM tools. 

Additionally if there is time, look at the pre and post scripts within Postman.
