# Retrieving the Device Inventory

We will now retrieve the device inventory from  Cisco DNA Center.

Follow these steps:

1. Navigate and open the desired collection runner through the following:

   1. Within Postman, click on the collection shortcut in the sidebar
   2. Hover over the collection `DNA Center API LAB 401 - Device Inventory`
   3. Click the `Run Collection` submenu option

      ![json](./images/Postman-Collection-DeviceInventory.png?raw=true "Import JSON")

2. To run the collection, do the following:

   1. Locate the sub-components of the `Runner`
   2. Select the `Save Responses` option as we will need the output
   3. Click  the `DNA Center API LAB 401 - Device Inventory` button

      ![json](./images/Postman-Collection-DeviceInventory-Runner.png?raw=true "Import JSON")

3. The following results will slowly appear as the collection is processed.

   1. Click `View Results` on the Left
   2. Watch the Results slowly appear. The API has been set up to give device info in the test area.

      ![json](./images/Postman-Collection-DeviceInventory-Summary.png?raw=true "Import JSON")

5. To view the results, do the following:

   1. Click the `Console` option at the bottom of postman
   2. Expand the Get request that begins `GET https://198.18.129.100/api/v1/network-device` 
   3. Within the `Response Body` click the `Drop Down` arrow and view the Response

      ![json](./images/Postman-Collection-DeviceInventory-Console.png?raw=true "Import JSON")

> [**Next Section**](03-summary.md)