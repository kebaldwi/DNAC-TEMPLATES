# Rest-API Orchestration 
## Overview
This Lab is designed as a standalone lab to help customers with varying challenges in Automating and Orchestrating their network infrastructure. Within the lab we will make use of various tools and techniques to Automate various tasks, and orchestrate over DNA Center.

## General Information
Up until this point we have used Rest-API for some basic set up tasks, but their are so many varying situations that can be solved or atleast eased utilizing Rest-API inconjunction with DNA Center.

## Lab Section 1 - DNA Center Design Preparation
While a more extensive set of settings can be built out for deployment, we will limit the configuration to the minimum necessary to perform these steps. 

Should you desire to deploy rapidly and build the lab faster then use the following approach:

### Step 1 - ***Import Postman Collection***
1. Download and import the collection within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB9/postman/DCLOUD_DNACTemplatesLab_Workflow.postman_collection.json">⬇︎DCLOUD_DNACTemplateLab_Workflow.postman_collection.json⬇︎</a> file.
2. Extract the file to the desktop using **Winrar** to expand them
3. Open the **postman** application from the desktop. Once the application is open select *Collections* then click the *Import* link. 
![json](../images/Postman-Pre-Collection-Import.png?raw=true "Import JSON")
4. A window should appear on the file upload page. Click the upload button and select desktop from the windows explorer. Select the file named `DCLOUD_DNACTemplatesLab_Workflow.postman_collection.json` and click open. 
![json](../images/Postman-Collection-Select.png?raw=true "Import JSON")
5. Then click import and the collection should be loaded into the collections as shown.
![json](../images/Postman-Post-Collection-Import.png?raw=true "Import JSON")

### Step 2 - ***Import Postman Environment***
1. Download and import the environment within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB9/postman/DCLOUD_DNACTemplateLabs.postman_environment.json">⬇︎DCLOUD_DNACTemplateLabs.postman_environment.json⬇︎</a> file.
2. Extract the file to the desktop using **Winrar** to expand them
3. If not open, open the **postman** application from the desktop. Once the application is open select *Environments* and then the *Import* link. 
![json](../images/Postman-Pre-Environment-Import.png?raw=true "Import JSON")
4. A window should appear on the file upload page. Click the upload button and select desktop from the windows explorer. Select the file named `DCLOUD_DNACTemplateLabs.postman_environment.json` and click open. 
![json](../images/Postman-Environment-Select.png?raw=true "Import JSON")
5. Then click import and the environment should be loaded into the environments as shown. 
![json](../images/Postman-Post-Environment-Import.png?raw=true "Import JSON")
6. Next we will choose the environment by clicking the checkmark on the right of Environment in postman as shown here. 
![json](../images/Postman-Environment-Selection.png?raw=true "Import JSON")

### Step 3 - ***Turn off SSL validation for LAB purposes within Postman***
1. Turn off SSL verification for lab purposes in the settings of Postman by click the **Gear** icon to select **settings** and **deselect** `SSL certificate verification` and then close the settings window. 
![json](../images/Postman-SSL-Deselect.png?raw=true "Import JSON")
2. With these steps completed we are prepared to start the walk through of the sections below.

### Step 4 - ***Run the Collection within Postman***
This collection is built with a flow and delay timers wait for the collection to finish entirely.
1. If not open, open the **postman** application from the desktop. Once the application is open select *Collections* and then the '...' link and select **run collection**. </br>
![json](../images/Postman-CollectionRunner.png?raw=true "Import JSON")
2. On the right ensure all API are selected and click run collection. 
![json](../images/Postman-CollectionRunner-Run.png?raw=true "Import JSON")
3. After the entire collection has run you will see all of them listed on the left as shown, and two buttons on the top right, one for results and the other to run again.
![json](../images/Postman-CollectionRunner-Results.png?raw=true "Import JSON")

### Step 5 - ***Evaluating the Results***
Time should now be taken to evaluate the result of the previous steps.

1. Within DNA Center you should see 3 devices within the inventory and additionally you should observe a complete hierarchy as well as settings and telemetry configured. The Devices will be discovered in the Building level at this stage. Walk through the various settings noting where AAA settings are inherited and where they are overidden. Look at the telemetry settings, and the credentials. Additionaly go to the Discovery tool and look at hte discovery event that was automated.

![json](../images/Postman-Discovery.png?raw=true "Import JSON")
![json](../images/Postman-Settings.png?raw=true "Import JSON")

## Automating Claiming and Provisioning
While it is possible to click through the claiming and provisioning processes manually, which can be time-consuming, we can handle bulk deployments differently. For Bulk deployments, after the templates are built and assigned to the network profile and a site, we may automate them further by uploading a CSV file to DNA Center via REST API.

## Summary
The next step will be to build Composite Template to include the Day N regular templates created in this lab for the switches to be pushed out to the various devices in the network infrastructure. 

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
