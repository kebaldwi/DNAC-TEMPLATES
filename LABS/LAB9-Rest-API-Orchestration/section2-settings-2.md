# Use Case 1.2 - Defining Settings and Credentials

## Student Settings and Credentials Assignment
We will now assign the settings credentials and telemetry settings using the environment variables which can be modified in the previous step.

Follow these steps:

1. Navigate and open the desired collection runner through the following:
   1. Within Postman click on the collection shortcut in the sidebar
   2. Hover over the collection `DNE LAB 1.1 - Settings Student`
   3. Click the `Run Collection` submenu option
      ![json](./images/Postman-Collection-Settings.png?raw=true "Import JSON")
2. To run the collection do the following:
   1. Ensure all the sub-components of the `Runner` are selected
   2. Click  the `Run DNE LAB 1.1 - Settings Student` button
      ![json](./images/Postman-Collection-Settings-Runner.png?raw=true "Import JSON")
3. The following summary will slowly appear as the collection is processed
   ![json](./images/Postman-Collection-Settings-Summary.png?raw=true "Import JSON")

## Verifying Student Settings Assignment
To verify that the settings were assigned successfully we will inspect the site in DNA Center.

Follow these steps:

1. If DNA Center is not already open, use a browser and navigate to `https;//198.18.129.100` where you may see an SSL Error displayed as depicted. Click the `Proceed to https://192.18.129.100 (unsafe)` link to continue if presented
![json](./images/DNAC-SSLERROR.png?raw=true "Import JSON")
2. If required, log into DNA Center using the username of `admin` and the password `C1sco12345`.
![json](./images/DNAC-Login.png?raw=true "Import JSON")
3. When the DNA Center Dashboard is displayed, Click the  icon to display the menu'
![json](./images/DNAC-Menu.png?raw=true "Import JSON")
4. Select `Design>Network Settings` from the menu to continue.
![json](./images/DNAC-Menu-Settings.png?raw=true "Import JSON")
5. Expand the Hierarchy on the left to show your specific `Area` select it and scroll through the settings.
![json](./images/DNAC-Settings-Student-Verify.png?raw=true "Import JSON")

## Summary
At this point we have assigned settings, credentials, and telemetry settings to the Hierarchy utilizing environment variables and REST-API's within the collection runner. 

Additionally if there is time, look at the results of the Credentials and Telemetry tabs with DNA Center and the various pre and post scripts within Postman.

