# Using Command Runner

We will now initiate a `show cdp neighbor` command against `c9300-2` managed by Cisco DNA Center using the Rest-API within the collection `DNA Center API LAB 402 - Command Runner`

Follow these steps:

1. Navigate and open the desired collection runner through the following:

   1. Within Postman, click on the collection shortcut in the sidebar
   2. Hover over the collection `DNA Center API LAB 402 - Command Runner`
   3. Click the `Run Collection` submenu option

      ![json](./images/Postman-Collection-CmdRun.png?raw=true "Import JSON")

2. To run the collection, do the following:

   1. Ensure all the sub-components of the `Runner` are selected
   2. Select the `Save Responses` option as we will need the output
   3. Click  the `Run DNA Center API LAB 402 - Command Runner` button

      ![json](./images/Postman-Collection-CmdRun-Runner.png?raw=true "Import JSON")

3. The following results will slowly appear as the collection is processed.

   1. Click `View Results` on the Left
   2. Watch the Results slowly appear. The API has been set up to give device info in the test area.

      ![json](./images/Postman-Collection-CmdRun-Summary.png?raw=true "Import JSON")

4. To view the results, do the following:

   1. Click the `Console` option at the bottom of postman
   2. Expand the Get request that begins `GET https://198.18.129.100/dna/intent/api/v1/file/...` 
   3. Within the `Response Body` click the `Drop Down` arrow and view the Response

      ![json](./images/Postman-Collection-CmdRun-Console.png?raw=true "Import JSON")

> [**Next Section**](03-summary.md)