# Module 7 - Retrieving Network Inventory
In this module we will use *Postman* to retrieve the device inventory of the hierarchy within DNA Center. DNA Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network.

## DNA Center Inventory Background
DNA Center has keeps a detailed inventory of the devices that are discovered or onboarded from the network. The inventory is used to reference devices, in the DNA Center UI, but also offers a place to see detailed information about the Product ID, Hostname, Software Image, and much more.

The inventory could be used in reports to determine compliance or to reference the devices within the system for either deploying templates, or issuing show commands with the command runner used earlier.

## Deploying Templates to Devices
### Objectives
- Authenticate and retrieve a token from Cisco DNA Center.
- Retrieve the inventory of devices in DNA Center.

### Prerequisites
The prerequisites steps for preparing for the lab are the following;
1. Complete [Module 6 - Configuration Archive](./module6-archive.md)

## Retrieving the Device Inventory from DNA Center 
We will now retrive the device inventory from DNA Center.

Follow these steps:

1. Navigate and open the desired collection runner through the following:
   1. Within Postman click on the collection shortcut in the sidebar
   2. Hover over the collection `DNA Center API LAB 401 - Device Inventory`
   3. Click the `Run Collection` submenu option
      ![json](./images/Postman-Collection-DeviceInventory.png?raw=true "Import JSON")
2. To run the collection do the following:
   1. Locate the sub-components of the `Runner`
   2. Select the `Save Responses` option as we will need the output
   3. Click  the `DNA Center API LAB 401 - Device Inventory` button
      ![json](./images/Postman-Collection-DeviceInventory-Runner.png?raw=true "Import JSON")
3. The following results will slowly appear as the collection is processed.
   1. Click `View Results` on the Left
   2. Watch the Results slowly appear. The API has been set up to give device info in the test area.
   ![json](./images/Postman-Collection-DeviceInventory-Summary.png?raw=true "Import JSON")
5. To view the results do the following:
   1. Click the `Console` option at the bottom of postman
   2. Expand the Get request that begins `GET https://198.18.129.100/api/v1/network-device` 
   3. Within the `Response Body` click the `Drop Down` arrow and view the Response
      ![json](./images/Postman-Collection-DeviceInventory-Console.png?raw=true "Import JSON")

## Summary
We have run a collection against DNA Center, to retrieve the device inventory and can export that to a file within our host. There are plenty of uses that this information might be used for, which include making decisions on template deployment SWIM upgrades and so forth. The limits of what can be done from here on are only those of your imagination.

Additionally if there is time, look at the pre and post scripts within Postman.

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.