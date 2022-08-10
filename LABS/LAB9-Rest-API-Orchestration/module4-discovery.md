# Module 4 - Device Discovery
In this module we will use *Postman* to discover devices within the network and to assign them to specific sites within the hierarchy within DNA Center. DNA Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network infrastructure and thereby facilitate change to the devices themselves.

## Device Discovery Background
DNA Center has a Discovery Tool which allows for the discovery of devices across the network through one of the following methods CDP/LLDP/IP Range utilizing credentials for SSH/Telnet/SNMP/HTTPS. Once a device has been discovered the device is synchronized to the inventory and left in the unassigned space within the inventory. The Administrator would then assign the device to the relevant site within the hierarchy. 

In this lab we will discover all the devices within the dCloud lab as specified in the given CSV file. The devices will then be automatically added to the sites as specified in the CSV.

## Deploying Templates to Devices
### Objectives
- Authenticate and retrieve a token from Cisco DNA Center.
- Retrieve Credentials for Discovery Creation
- Create a Discovery for each part of the hierarchy.
- Determine which devices were discovered
- Add the discovered devices to the sites within the hierarchy.

### Prerequisites
The prerequisites steps for preparing for the lab are the following;
1. Complete [Module 3 - Assign Settings and Credentials](./module3-settings.md)

### CSV Data Source
Within Postman we will utilize the collection `Device Discovery` to build a projects within the Template Editor, and add Regular Templates to them in order to configure devices. This Collection may be run whenever you wish to configure or modify the configuration of a device within DNA Center. 

Accompanying the Collection is a required Comma Separated Value (CSV) file which is essentially an answer file for the values used to build the design. The CSV may be found here. 

<a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB9-Rest-API-Orchestration/csv/DNAC-Design-Settings.csv" target="_blank">⬇︎DNA Center Design Settings CSV⬇︎</a>

We will **open** but **not save** the CSV file to view the hierarchy that will be built during the lab. You will see each row has hierarchal information as well as settings and credentials and other information. **Be Careful NOT to modify the file**, If you feel you have modified the file please download it again.

<p align="center"><img src="./images/csv.png" width="800" height="385"></p>

Within the CSV look all the way to the right for the columns pertaining to this collection.

## Device Discovery on DNA Center 
We will now discover multiple devices as listed within the CSV, and assign them to the sites as per the hierarchy within the CSV.

Follow these steps:

1. Navigate and open the desired collection runner through the following:
   1. Within Postman click on the collection shortcut in the sidebar
   2. Hover over the collection `DNA Center API LAB 201 - Device Discovery`
   3. Click the `Run Collection` submenu option
      ![json](./images/Postman-Collection-Discovery.png?raw=true "Import JSON")
2. To run the collection do the following:
   1. Locate the sub-components of the `Runner`
   2. On the right under data, click *select* 
   3. Browse and select the CSV using explorer
   4. Click Open to select the file to be used
   5. Optionally select the `Save Responses` option
      ![json](./images/Postman-Collection-Discovery-Run-CSV.png?raw=true "Import JSON")
   6. Click  the `Run DNA Center API LAB 201 - Device Discovery` button
      ![json](./images/Postman-Collection-Discovery-Runner.png?raw=true "Import JSON")
3. The following summary will slowly appear as the collection is processed
   ![json](./images/Postman-Collection-Discovery-Summary.png?raw=true "Import JSON")

## Verifying Device Discovery 
To verify that the devices were discovered successfully we will inspect the Discovery Tool within DNA Center as well as the inventory.

Follow these steps:

1. If DNA Center is not already open, use a browser and navigate to `https;//198.18.129.100` where you may see an SSL Error displayed as depicted. Click the `Proceed to https://192.18.129.100 (unsafe)` link to continue if presented
![json](./images/DNAC-SSLERROR.png?raw=true "Import JSON")
2. If required, log into DNA Center using the username of `admin` and the password `C1sco12345`.
![json](./images/DNAC-Login.png?raw=true "Import JSON")
3. When the DNA Center Dashboard is displayed, Click the  icon to display the menu'
![json](./images/DNAC-Menu.png?raw=true "Import JSON")
4. Select `Tools>Template Editor` from the menu to continue.
![json](./images/DNAC-Menu-TemplateEditor.png?raw=true "Import JSON")
5. Expand the Project with your Area Name on the left to show your specific Project with the template, then select it and view it on the right.
![json](./images/DNAC-TemplateEditor-Discovery-Verify.gif?raw=true "Import JSON")

## Summary
We have been able to discover devices within the network and import them into DNA Center. This scenario may be augmented and modified to create a brownfield learn which would allow for the provisioning of a template to nullify AAA settings and then assign the device to a site for provisioning.

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.