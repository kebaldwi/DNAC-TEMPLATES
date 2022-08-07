# Module 5 - Deploying Projects and Templates
In this module we will use *Postman* to build and deploy Projects and a Regular Template for a specific site within the hierarchy within DNA Center. DNA Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network.

## DNA Center Templates Background
DNA Center has a Template Editor which allows for the import and export of custom templates written in Jinja2 or Velocity and encapsulated within JSON inside DNA Center. These templates and associated parameters allow for the configuration of  devices when associated to the hierarchy through a Network Profile. 

Templates both Regular and Composite are grouped logically into Projects.

In this lab we will deploy a template within a project to be ready for deployment at a later date. Included in the repository is a Deployment API which is there for informational purposes and due to the nature of the lab environment should not be invoked.

## Template Deployment to DNA Center 
We will now deploy a template within a Project with your Area Name within DNA Centers template editor.

Follow these steps:

1. Navigate and open the desired collection runner through the following:
   1. Within Postman click on the collection shortcut in the sidebar
   2. Hover over the collection `DNE LAB 1.3 - Template Deployment Student`
   3. Click the `Run Collection` submenu option
      ![json](./images/Postman-Collection-DeployTemplate.png?raw=true "Import JSON")
2. To run the collection do the following:
   1. Locate the sub-components of the `Runner`
   2. Deselect the `POST Deploy Template` sub-component
   3. Optionally select the `Save Responses` option
   4. Click  the `Run DNE LAB 1.3 - Template Deployment Student` button
      ![json](./images/Postman-Collection-DeployTemplate-Runner.png?raw=true "Import JSON")
3. The following summary will slowly appear as the collection is processed
   ![json](./images/Postman-Collection-DeployTemplate-Summary.png?raw=true "Import JSON")

## Verifying Template Deployment 
To verify that the template was deployed successfully we will inspect the template editor within DNA Center.

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
![json](./images/DNAC-TemplateEditor-DeployTemplate-Verify.png?raw=true "Import JSON")

## Summary
We have been able to deploy a template within a project inside DNA Centers template editor. This scenario may be augmented and modified to use of imported files within Postman to allow for a more dynamic approach. The flow allows for us to rapidly stage Projects and Templates perhaps iimporting them from GitHub in CICD pipeline. 

Additionally if there is time, look at the pre and post scripts within Postman and take a look at the additionally included Deploy Template API.
