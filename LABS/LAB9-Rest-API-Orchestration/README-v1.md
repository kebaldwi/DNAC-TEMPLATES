# Rest-API Orchestration 
## Overview
This Lab is designed as a standalone lab to help customers with varying challenges in Automating and Orchestrating their network infrastructure. Within the lab we will make use of various tools and techniques to Automate various tasks, and orchestrate over DNA Center.

## General Information
Up until this point we have used Rest-API for some basic set up tasks, but their are so many varying situations that can be solved or at least eased utilizing Rest-API inconjunction with DNA Center. In this lab we will use a complete set of REST-API collections which will build upon the foundational knowledge acquired in the previous labs. For this lab we will concentrate on DNA Center configuration, and how DNA Center can be automated to perform various functions which we have already covered. 

This page will serve as the landing page for this lab section due to the amount of content it will cover and the need to expand on it over time. 

The lab will utilize a set of collections publically shared on postmans workspaces and those collections will also be expanded to keep in line with this lab.

## Lab Modules
The use cases we will cover are the following which you can access via links below:

1. [**Postman Orientation**](./postman.md)
2. [**Building Hierarchy**](./labs/dnac-101-1-hierarchy/1.md)
3. [**Assign Settings and Credentials**](./labs/dnac-101-2-settings/1.md)
4. [**Device Discovery**]
5. [**Template Deployment**](./labs/dnac-101-4-templates/1.md)
6. [**Configuration Archive**](./labs/dnac-101-6-archive/1.md)
3. [Running Show Commands](./labs/dnac-101-3-cmd-run/1.md)
5. [Retrieving Network Inventory](./labs/dnac-101-5-inventory/1.md)

## Preparation
In order to compete this module, its best to connect to the dCloud lab environment using your own laptop so that you can get accustomed to and begin using the tools. In the event that you cannot install postman though it is possible to complete all tasks via the workstation in the dCloud environment.

Our screen shots will alll be from the jump host, but remember you can use your own laptop.

If you would like to connect to the dCloud environment please ensure you install the following

### Lab Requirements
This lab is designed to be run in Cisco dClouds - Enterprise Network Sandbox Lab. It was developed in version 4 which includes DNA Center 2.2.3.5 and equipment running at least 17.x versions of code.

### Tools Required
Please utilize the following tools to effectively run the lab, and ensure they are installed on your workstation/laptop prior to the class.

1. Cisco AnyConnect VPN Client
2. Postman
3. Google Chrome

#### Cisco AnyConnect VPN Client
This software is required to connect your workstation to Cisco dCloud. For an explanation into AnyConnect and how to use it with dCloud please visit the following URL: 

- <a href="https://dcloud-cms.cisco.com/help/android_anyconnect" target="_blank">dCloud AnyConnect Documentation</a>

If you do not have the anyconnect client please visit 

- <a href="https://dcloud-rtp-anyconnect.cisco.com" target="_blank">⬇︎AnyConnect Download Site⬇︎</a>

#### Postman
Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration so you can create better APIs—faster.

- <a href="https://www.postman.com/downloads/" target="_blank">⬇︎Postman Download⬇︎</a>

##### Postman Documentation
For an understanding of postman please visit this site:

- <a href="https://learning.postman.com/docs/getting-started/introduction/" target="_blank">Postman Documentation</a>

#### Google Chrome
Google Chrome is the optimal browser of choice when working in the DNA Center UI. 

To download Google Chrome please visit 

- <a href="https://www.google.com/chrome/downloads/" target="_blank">⬇︎Chrome Download⬇︎</a>

## Summary
This lab is intended for educational purposes only. Use outside of a lab environment should be done at the operators risk. Cisco assumes no liability for incorrect usage.


## Lab Section 1 - Postman Preparation
While a more extensive set of settings can be built out for deployment, we will limit the configuration to the minimum necessary to perform these steps. 

Should you desire to deploy rapidly and build the lab faster then use the following approach:

### Step 1 - ***Import Postman Collection***
1. Download and import the collection within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB9/postman/DCLOUD_DNACTemplatesLab_Workflow.postman_collection.json">⬇︎DCLOUD_DNACTemplateLab_Workflow.postman_collection.json⬇︎</a> file.
2. Extract the file to the desktop using **Winrar** to expand them
3. Open the **postman** application from the desktop. Once the application is open select *Collections* then click the *Import* link. 
![json](./images/Postman-Pre-Collection-Import.png?raw=true "Import JSON")
4. A window should appear on the file upload page. Click the upload button and select desktop from the windows explorer. Select the file named `DCLOUD_DNACTemplatesLab_Workflow.postman_collection.json` and click open. 
![json](./images/Postman-Collection-Select.png?raw=true "Import JSON")
5. Then click import and the collection should be loaded into the collections as shown.
![json](./images/Postman-Post-Collection-Import.png?raw=true "Import JSON")

### Step 2 - ***Import Postman Environment***
1. Download and import the environment within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB9/postman/DCLOUD_DNACTemplateLabs.postman_environment.json">⬇︎DCLOUD_DNACTemplateLabs.postman_environment.json⬇︎</a> file.
2. Extract the file to the desktop using **Winrar** to expand them
3. If not open, open the **postman** application from the desktop. Once the application is open select *Environments* and then the *Import* link. 
![json](./images/Postman-Pre-Environment-Import.png?raw=true "Import JSON")
4. A window should appear on the file upload page. Click the upload button and select desktop from the windows explorer. Select the file named `DCLOUD_DNACTemplateLabs.postman_environment.json` and click open. 
![json](./images/Postman-Environment-Select.png?raw=true "Import JSON")
5. Then click import and the environment should be loaded into the environments as shown. 
![json](./images/Postman-Post-Environment-Import.png?raw=true "Import JSON")
6. Next we will choose the environment by clicking the checkmark on the right of Environment in postman as shown here. 
![json](./images/Postman-Environment-Selection.png?raw=true "Import JSON")

### Step 3 - ***Turn off SSL validation for LAB purposes within Postman***
1. Turn off SSL verification for lab purposes in the settings of Postman by click the **Gear** icon to select **settings** and **deselect** `SSL certificate verification` and then close the settings window. 
![json](./images/Postman-SSL-Deselect.png?raw=true "Import JSON")
2. With these steps completed we are prepared to start the walk through of the sections below.

## Section Summary
The next step will be to continue the lab and work through the various use cases within the collections. 

