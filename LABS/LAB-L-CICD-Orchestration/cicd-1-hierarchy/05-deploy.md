# Hierarchy Build Deployment

We will now `build` the Hierarchy using the CSV variables previously discussed.

Follow these steps:

1. Navigate and open the desired collection runner through the following:

   1. Within Postman, click on the collection shortcut in the sidebar
   2. Hover over the collection `DNA Center API LAP 100 - Build Hierarchy`
   3. Click the `Run Collection` submenu option

      ![json](./images/Postman-Collection-Hierarchy.png?raw=true "Import JSON")

2. To run the collection, do the following:

   1. Ensure all the sub-components of the `Runner` are selected
   2. On the right under data, click *select* 
   3. Browse and select the CSV using explorer
   4. Click Open to select the file to be used

      ![json](./images/Postman-Collection-Hierarchy-Run-CSV.png?raw=true "Import JSON")

   5. Click  the `Run DNA Center API LAP 100 - Build Hierarchy` button

      ![json](./images/Postman-Collection-Hierarchy-Runner.png?raw=true "Import JSON")

3. Select `View Results` to view the following summary, which will slowly appear as the collection is processed. Notice APIs are only run when they are required. You may view the pre and post-script logic that causes this behavior. Each iteration is a row of the CSV being processed.

   ![json](./images/Postman-Collection-Hierarchy-Summary.png?raw=true "Import JSON")

> [**Next Section**](06-verify.md)
