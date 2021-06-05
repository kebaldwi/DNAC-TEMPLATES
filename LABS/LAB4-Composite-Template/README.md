# Composite Templates - In Development - Check back Monday!
## Overview
This Lab is designed to be used after first completing labs 1 through 3 and has been created to address how to combin and use multiple Regular Templates within DNA Center to onboard network devices at Day 1 through N. This allows Network Administrators the ability to configure network devices in an ongoing and pragmantic manner from within DNA Center without using the SD-Access Fabric methodology. It also allows an Administrator the ability to drag Regular Templates into and out of the flow as needed for ongoing maintenance.

In this section will go through the flow involved in creating a deployable Composite Template from an IOS configuration script for a Catalyst switch linking it to a Switch profile and deploy it through DNAC using provisioning workflows.

## General Information
As previously discussed, DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates and for more flexibility Composite Templates. as they can be used to apply ongoing changes and to allow device modifications after initial deployment. This lab section will focus on Day N templates to be built as regular templates within DNA Center.

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used you should **not** deploy the same feature from cli code in a template to configure the device. Its a decision you have to make upfront and avoids a lot of lines in the templates and allows for a more UI centric configuration which is easier to maintain. 

As a guidance try and use **Design Settings** for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing.

## Lab Section 1 - DNA Center Design Preparation
While we could deploy more extensive settings for deployment, we will limit the configuration to the minimum necessary to perform this step, building off the completed tasks in lab 2.

## Lab Section 2 - DNA Center Day N Composite Template Preparation
You can create Day N Composite Templates within the ***Template Editor*** within **DNA Center**. Go to the ***Template Editor*** to complete the next task. In this lab, we will deploy a Composite Template and additional Regular Templates within a project.  The import and export function within **DNA Center** allows both the import and export of templates and projects, along with the ability to clone them.

### Step 1 - ***Import Project with Templates***
Download and import the project within the ***Template Editor*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB4-Composite-Template/templates/2125templates/DNAC_Template_Lab_DayN_project.json">⬇︎DNAC_Template_Lab_DayN_project.json⬇︎</a> file. If using DNAC prior release to 2.1.2.X then use the previously built project within Lab 3 and build the templates located within the following <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB4-Composite-Template/templates/Platinum_Templates.zip">⬇︎Platinum_Templates.zip⬇︎</a> file located within this lab. 

Previously in Lab 3, we created a project where we assigned a template to the site and provisioned it. We will now expand on that by importing a project with the same name overtop the current project, thereby importing additional regular templates. Take a few moments and examine the construction of these templates, as each has a specific form and function. Their design is modular to allow reuse of them within other composite templates for other switches or routers.

1. Navigate to the **Template Editor** within DNA Center through the menu *Tools>Template Editor*.
   ![json](./images/DNAC-NavigateTemplate.png?raw=true "Import JSON")
2. Within the **template editor**, left-click the ⨁ icon to the right of find template and click **Import Project(s)** within the menu.  
   ![json](./images/DNAC-ProjectImportBegin.png?raw=true "Import JSON")
3. Download the file above *DNAC_Template_Lab_DayN_project.json* to be imported into the DNA Center. Once downloaded, extract the file.
4. From the **Import Project(s)** window, click **Select a file from your computer** from the explorer window, select the extracted JSON file and click open. 
   ![json](./images/DNAC-ProjectSelect.png?raw=true "Import JSON")
5. Click **Import**, and the project and all the templates within it will be imported.   
   ![json](./images/DNAC-ProjectImport.png?raw=true "Import JSON")
6. Once the project is imported, select it to view each of the template files within it.
   ![json](./images/DNAC-ProjectFiles.png?raw=true "Import JSON")
 
The project we imported contains the following templates:
1. **AAA** for local AAA services
   ![json](./images/DNAC-Project-AAA-Template.png?raw=true "Import JSON")
2. **System Management** for global system settings
   ![json](./images/DNAC-Project-SysMgmt-Template.png?raw=true "Import JSON")
3. **VLANs Ports per DF** to add VLAN and port configuration
   ![json](./images/DNAC-Project-PortAssign-Template.png?raw=true "Import JSON")
4. **Local User Management** for additional user accounts
   ![json](./images/DNAC-Project-USR-Template.png?raw=true "Import JSON")
5. **Stacking** to set up powerstack and stack priority
   ![json](./images/DNAC-Project-Stacking-Template.png?raw=true "Import JSON")
6. **Access Lists** to restrict management access
   ![json](./images/DNAC-Project-ACL-Template.png?raw=true "Import JSON")
7. **Automatic Uplink Naming** to automatically name uplinks 
   ![json](./images/DNAC-Project-AUN-Template.png?raw=true "Import JSON")

Additionally, it contains a Composite Template. The composite template will allow us to reuse multiple Regular templates, thereby allowing modularity. Thus we can keep our configuration scripts in smaller files allowing reuse across various platforms. Subsequently helps in troubleshooting as the configurations become smaller and less complex as a result.

### Step 2 - ***Create Composite Template***
Within the project is a Composite Template, but the steps involved to create one are simple. **The next steps are optional**.

1. Within the **template editor**, Hover over the right side of the project, and a small ⚙ gear icon will appear. Select **Add Template(s)** from the menu.     
   ![json](./images/DNAC-CompositeCreate.png?raw=true "Import JSON")
2. On the *Add New Template* sidebar:
   1. Select **Composite Sequence**
   2. Enter a **Name** for the Composite Template
   3. Click **Edit** beside *Device Types* to select the device families to be used.
3. On the *Select Device Types* sidebar type in `9300`to filter for the switch family and select the entire series



## General Information
This lab is under development please come back soon. ETA for delivery June 2021.

