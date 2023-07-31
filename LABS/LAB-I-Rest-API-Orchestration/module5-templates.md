# Module 5 - Template Deployment

In this module, we will use *Postman* to build and deploy Projects and a Regular Template for a specific site within the hierarchy within DNA Center. DNA Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network.

## Template Background

DNA Center has a Template Editor, which allows for the import and export of custom templates written in Jinja2 or Velocity and encapsulated within JSON inside DNA Center. These templates and associated parameters allow for the configuration of devices when associated with the hierarchy through a Network Profile. 

Templates, both Regular and Composite, are grouped logically into Projects.

In this lab, we will deploy a template within a project to be ready for deployment later. Included in the repository is a Deployment API, which is there for informational purposes and should not be invoked due to the nature of the lab environment.

## Deploying Templates to Devices

### Objectives

- Authenticate and retrieve a token from Cisco DNA Center.
- Build a Project and add a Regular Template.
- Deploy a Template to a Device.

### Prerequisites

The prerequisite steps for preparing for the lab are the following;
1. Complete [Module 4 - Device Discovery](./module4-discovery.md)

### CSV Data Source

Within Postman, we will utilize the collection `Template Deployment` to build projects within the Template Editor and add Regular Templates to them in order to configure devices. This Collection may be run whenever you wish to configure or modify the configuration of a device within DNA Center. 

Accompanying the Collection is a required Comma Separated Value (CSV) file, which is essentially an answer file for the values used to build the design. The CSV may be found here. 

<a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-I-Rest-API-Orchestration/csv/DNAC-Design-Settings.csv" target="_blank">⬇︎DNA Center Design Settings CSV⬇︎</a>

We will **open** but **not save** the CSV file to view the hierarchy that will be built during the lab. You will see each row has hierarchal information, settings, credentials, and other information. **Be Careful NOT to modify the file**; if you feel you have modified the file, please download it again.

<p align="center"><img src="./images/csv.png" width="800" height="385"></p>

Within the CSV, scroll to the right for the columns pertaining to this collection.

## Template Deployment to DNA Center 

We will now deploy a template within a Project with your Area Name within DNA Centers template editor.

Follow these steps:

1. Navigate and open the desired collection runner through the following:
   1. Within Postman, click on the collection shortcut in the sidebar
   2. Hover over the collection `DNA Center API LAB 302 - Template Deployment`
   3. Click the `Run Collection` submenu option

      ![json](./images/Postman-Collection-DeployTemplate.png?raw=true "Import JSON")

2. To run the collection, do the following:
   1. Locate the sub-components of the `Runner`
   2. On the right under data, click *select* 
   3. Browse and select the CSV using explorer
   4. Click Open to select the file to be used
   5. Optionally select the `Save Responses` option

      ![json](./images/Postman-Collection-DeployTemplate-Run-CSV.png?raw=true "Import JSON")

   6. Click  the `Run DNA Center API LAB 302 - Template Deployment` button

      ![json](./images/Postman-Collection-DeployTemplate-Runner.png?raw=true "Import JSON")

3. The following summary will slowly appear as the collection is processed

   ![json](./images/Postman-Collection-DeployTemplate-Summary.png?raw=true "Import JSON")

## Verifying Template Deployment 

To verify that the template was deployed successfully, we will inspect the template editor within DNA Center.

Follow these steps:

1. If DNA Center is not already open, use a browser and navigate to `https://198.18.129.100`, where you may see an SSL Error displayed as depicted. Click the `Proceed to https://192.18.129.100 (unsafe)` link to continue if presented

   ![json](./images/DNAC-SSLERROR.png?raw=true "Import JSON")

2. If required, log into DNA Center using the username of `admin` and the password `C1sco12345`.

   ![json](./images/DNAC-Login.png?raw=true "Import JSON")

3. When the DNA Center Dashboard is displayed, Click the  icon to display the menu'

   ![json](./images/DNAC-Menu.png?raw=true "Import JSON")

4. Select `Tools>Template Editor` from the menu to continue.

   ![json](./images/DNAC-Menu-TemplateEditor.png?raw=true "Import JSON")

5. Expand the Project with your Area Name on the left to show your specific Project with the template, then select it and view it on the right.

   ![json](./images/DNAC-TemplateEditor-DeployTemplate-Verify.gif?raw=true "Import JSON")

## Summary

We have been able to deploy a template within a project inside DNA Centers template editor. This scenario may be augmented and modified to use imported files within Postman to allow for a more dynamic approach. The flow allows us to rapidly stage Projects and Templates, perhaps importing them from GitHub in the CICD pipeline. 

If there is time, look at the pre and post-scripts within Postman and look at the additionally included Deploy Template API.

To continue your learning experience, continue on to the next module in the series, module 6, below.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Continue to Configuration Archive Module**](../LAB-I-Rest-API-Orchestration/module6-archive.md)

> [**Return to Lab Menu**](./README.md)