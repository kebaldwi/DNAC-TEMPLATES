# Module 3 - Assign Settings and Credentials
In this module we will use *Postman* to deploy settings and credentials to a hierarchy within DNA Center. DNA Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network.

## Settings and Credentials Background
The Design area is where you create the structure and framework of your network, including the logical topology, network settings, and device type profiles that you can apply to devices throughout your network.

The settings and credentials which we assign to the hierarchy allow us to be deterministic in where we inherit settings from parent objects and where we overide settings in the child objects.

This allows for us to deploy not only changes to the network, with localized maintenance windows but also to slowly roll out changes through multiple sites without impact to the entire network. 

As with all the Design, Policy & Provisioning elements they are all tied to the hierarchial nature of DNA Center. 

## Assigning Settings and Credentials to Hierarchy
### Objectives
- Authenticate and retrieve a token from Cisco DNA Center.
- Assign the Hierarchy Settings and Credentials

### Prerequisites
The prerequisites steps for preparing for the lab are the following;
1. Complete [Module 2 Build Hierarchy](./module2-hierarchy.md)

### CSV Data Source
Within Postman we will utilize the collection `Assign Settings Creds` to assign settings and credentials to the Hierarchy of DNA Center in order to associate settings to devices. This Collection may be run whenever you wish to assign or modify the settings and credentials of the Hierarchy to either add additional settings or modify credentials. 

Accompanying the Collection is a required Comma Separated Value (CSV) file which is essentially an answer file for the values used to build the design. The CSV may be found here. 

<a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB9-Rest-API-Orchestration/csv/DNAC-Design-Settings.csv" target="_blank">⬇︎DNA Center Design Settings CSV⬇︎</a>

We will **open** but **not save** the CSV file to view the hierarchy that will be built during the lab. You will see each row has hierarchal information as well as settings and credentials and other information. **Be Careful NOT to modify the file**, If you feel you have modified the file please download it again.

<p align="center"><img src="./images/csv.png" width="800" height="385"></p>

You can see the settings begin to the right of the hierarchy.

## Settings and Credentials Assignment
At this point we have reviewed the settings within the environment and ensured we will be targeting the correct hierarchy and we are ready to continue pushing the settings and credentials to our newly created hierarchy.

We will now assign the settings credentials and telemetry settings using the CSV variables which were provided in the previous step.

Follow these steps:

1. Navigate and open the desired collection runner through the following:
   1. Within Postman click on the collection shortcut in the sidebar
   2. Hover over the collection `DNA Center API LAB 101 - Assign Settings Creds`
   3. Click the `Run Collection` submenu option
      ![json](./images/Postman-Collection-Settings.png?raw=true "Import JSON")
2. To run the collection do the following:
   1. Ensure all the sub-components of the `Runner` are selected
   2. On the right under data, click *select* 
   3. Browse and select the CSV using explorer
   4. Click Open to select the file to be used
      ![json](./images/Postman-Collection-Settings-Run-CSV.png?raw=true "Import JSON")
   5. Click  the `Run DNA Center API LAB 101 - Assign Settings Creds` button
      ![json](./images/Postman-Collection-Settings-Runner.png?raw=true "Import JSON")
3. The following summary will slowly appear as the collection is processed
   ![json](./images/Postman-Collection-Settings-Summary.png?raw=true "Import JSON")

## Verifying Settings Assignment
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
5. Expand the Hierarchy on the left to show all specific `Area` select it and scroll through the settings.
![json](./images/DNAC-Settings-Verify1.gif?raw=true "Import JSON")
5. Expand the Hierarchy on the left to show all specific `Area` select it and scroll through the credentials.
![json](./images/DNAC-Settings-Verify2.gif?raw=true "Import JSON")
5. Expand the Hierarchy on the left to show all specific `Area` select it and scroll through the telemetry settings.
![json](./images/DNAC-Settings-Verify3.png?raw=true "Import JSON")

## Summary
At this point we have assigned settings, credentials, and telemetry settings to the Hierarchy utilizing environment variables and REST-API's within the collection runner. 

Additionally if there is time, look at the results of the Credentials and Telemetry tabs with DNA Center and the various pre and post scripts within Postman.

To continue your learning experience continue on to the next module in the series which is module 4 below.

## Lab Modules
The use cases we will cover are the following which you can access via links below:

1. [**Postman Orientation**](./module1-postman.md)
2. [**Building Hierarchy**](./module2-hierarchy.md)
3. [**Assign Settings and Credentials**](./module3-settings.md)
4. [**Device Discovery**](./module4-discovery.md)
5. [**Template Deployment**](./module5-templates.md)
6. [**Configuration Archive**](./module6-archive.md)
7. [**Retrieving Network Inventory**](./module7-inventory.md)
8. [**Running Show Commands**](./module8-commands.md)

## Main Menus
To return to the main menus
1. [Rest-API Orchestration Main Menu](./README.md)
2. [DNAC-TEMPLATES-LABS Main Menu](../README.md)
3. [DNAC-TEMPLATES Repository Main Menu](.../README.md)

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.