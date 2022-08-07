## Use Case 1.2 - Running Show Commands
In this lablet we will use *Postman* to run some show commands on network devices within the infrastructure that are managed by DNA Center. This allows a method of getting troubleshooting information in the event we need to populate 3rd party management systems.

## Command Runner Background
The Command Runner tool allows you to run cli commands from the Inventory window on platforms. 

The platform commands that you can run are those such as ping, traceroute, and snmpget to troubleshoot device reachability issues. Additionally show commands may also be used to help or aid in troubleshooting.

## Using Command Runner
We will now initiate a `show cdp neighbor` command against `c9300-2` managed by DNA Center using the Rest-API within the collection `DNE LAB 1.2 - Command Runner Student`

Follow these steps:

1. Navigate and open the desired collection runner through the following:
   1. Within Postman click on the collection shortcut in the sidebar
   2. Hover over the collection `DNE LAB 1.2 - Command Runner Student`
   3. Click the `Run Collection` submenu option
      ![json](./images/Postman-Collection-CmdRun.png?raw=true "Import JSON")
2. To run the collection do the following:
   1. Ensure all the sub-components of the `Runner` are selected
   2. Select the `Save Responses` option as we will need the output
   3. Click  the `Run DNE LAB 1.2 - Command Runner Student` button
      ![json](./images/Postman-Collection-CmdRun-Runner.png?raw=true "Import JSON")
3. The following summary will slowly appear as the collection is processed
   ![json](./images/Postman-Collection-CmdRun-Summary.png?raw=true "Import JSON")
4. To view the results do the following:
   1. Click the `Console` option at the bottom of postman
   2. Select the `Popout Window` option as we will need the output
   3. Expand the Get request that begins `GET https://198.18.129.100/dna/intent/api/v1/file/...` 
   4. Within the `Response Body` click the `Popout Window` option
      ![json](./images/Postman-Collection-CmdRun-Console.png?raw=true "Import JSON")
5. The following results will appear in a text window allowing for copy to export or to use the file save options
   ![json](./images/Postman-Collection-CmdRun-Export.png?raw=true "Import JSON")

## Summary
We have been able to run diagnostic commands via Rest-API, which is useful if we want to get any show command or output from any diagnostic command to a third party system. This allows us to augment DNA Center and create whatever we like in regards to troubleshooting support for other platforms like ServiceNow or other 3rd party Rest-API based ITSM tools. 

Additionally if there is time, look at the pre and post scripts within Postman.