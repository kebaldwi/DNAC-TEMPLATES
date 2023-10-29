# Settings and Credentials Deployment

At this point, we have reviewed the settings within the environment and ensured we will be targeting the correct hierarchy. We are ready to continue pushing the settings and credentials to our newly created hierarchy.

We will now `assign` the settings, credentials, and telemetry settings using the CSV variables provided in the previous step.

Follow these steps:

1. Navigate and open the desired collection runner through the following:

   1. Within Postman, click on the collection shortcut in the sidebar
   2. Hover over the collection `DNA Center API LAB 101 - Assign Settings Creds`
   3. Click the `Run Collection` submenu option

      ![json](./images/Postman-Collection-Settings.png?raw=true "Import JSON")

2. To run the collection, do the following:

   1. Ensure all the sub-components of the `Runner` are selected
   2. On the right under data, click *select* 
   3. Browse and select the CSV using explorer
   4. Click Open to select the file to be used

      ![json](./images/Postman-Collection-Settings-Run-CSV.png?raw=true "Import JSON")

   5. Click  the `Run DNA Center API LAB 101 - Assign Settings Creds` button

      ![json](./images/Postman-Collection-Settings-Runner.png?raw=true "Import JSON")

3. The following summary will slowly appear as the collection is processed

   ![json](./images/Postman-Collection-Settings-Summary.png?raw=true "Import JSON")

> [**Next Section**](04-verify.md)
