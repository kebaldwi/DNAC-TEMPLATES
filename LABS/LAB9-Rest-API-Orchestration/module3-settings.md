# Module3 - Assign Settings and Credentials
In this module we will use *Postman* to deploy settings and credentials to a hierarchy within DNA Center. DNA Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network.

## Settings and Credentials Background
The Design area is where you create the structure and framework of your network, including the logical topology, network settings, and device type profiles that you can apply to devices throughout your network.

The settings and credentials which we assign to the hierarchy allow us to be deterministic in where we inherit settings from parent objects and where we overide settings in the child objects.

This allows for us to deploy not only changes to the network, with localized maintenance windows but also to slowly role out changes through multiple sites without impact to the entire network. 

As with all the Design, Policy & Provisioning elements they are all tied to the hierarchial nature of DNA Center. 

## Student Environment
To ensure you are working on all your changes and not interfering with others, we will modify the settings and Hierarchy to personalize it for your use within the lab. We did this step in the previous lablet, but for confirmation please ensure it is complete.

Follow these steps:

1. Navigate and open the desired environment and modify the variables indicated in the following steps:
   1. Within Postman click on the environment shortcut in the sidebar
   2. Clicking the environment `DNAC Template Labs Student`
      ![json](./images/Postman-Environment.png?raw=true "Import JSON")
2. Scroll down in the Environment variables shown:
   1. Find the variable `HierarchyArea`
   2. Edit the data in the forth column with your student info `Student-12` 
   3. Click the `Save` button to commit the changes
      ![json](./images/Postman-Environment-Area-Modify.png?raw=true "Import JSON")

Within the environment please review the DNS, DHCP, TimeZone, and other components which are utilized within the settings of the environment. Please feel free to modify the DNS, or DHCP settings with your own values.

## Summary
At this point we have reviewed the settings within the environment and ensured we will be targeting the correct hierarchy and we are ready to continue pushing the settings and credentials to our newly created hierarchy.

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
