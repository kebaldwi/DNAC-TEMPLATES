# Dynamic Automation - Under Development
![json](./images/underconstruction.png?raw=true "Import JSON")

## Overview
This Lab is designed to be used as a stand alone lab due. It has been created to address how to combine and use **IBNS 2.0** using **closed mode** and multiple Regular Templates within DNA Center to onboard network devices at Day 1 through N. This allows Network Administrators the ability to configure network devices in an ongoing and programmatic manner from within DNA Center without using the SD-Access Fabric methodology. It also enables an administrator to drag Regular Templates into and out of the flow as needed for ongoing maintenance.

This section will go through the flow involved in creating a deployable Composite Template from an IOS configuration script for a Catalyst switch linking it to a Switch profile, and deploying it through DNAC using provisioning workflows.

## General Information
As previously discussed, DNA Center can be used for Plug-and-Play and Day N or Ongoing Templates. Customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates and, for more flexibility Composite Templates. They can apply ongoing changes and allow device modifications after initial deployment. This lab section will focus on Day N templates built as regular templates within the DNA Center.

Another important consideration is that part of a typical configuration would include some lines of code, which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used, you should **not** deploy the same feature from cli code in a template to configure the device. It's a decision you have to make upfront, avoids a lot of lines in the templates, and allows for a more UI-centric configuration that is easier to maintain. 

As guidance, try and use **Design Settings** for as many of the configurations as you can, leaving Templates light and nimble for configurations that might change ongoing.

## Autoconf & IBNS 2.0 Secure Access
Previously within the Composite Templating Lab and in the previous section, we introduced a methodology of automatically configuring the interfaces within the switch. This configuration relies on a few variables used to extrapolate the settings that were then configured via the template. This allowed a set of macros to be utilized to build out the various settings for VLANs, Ports, and Uplinks. 

While these were methodologies that dealt programmatically with port configuration, and while you may adapt them for an environment, they are both lacking in the fact that they are not dynamic enough. Again, it's impossible to determine without looking at the configuration where something is plugged in. Secondly, if equipment or users are plugged into the wrong interface, they may get the wrong level of access. 

In previous code revisions, we could deal with some of the problems with Auto Smart Port technology, but that has been deprecated, and its replacement is a lot more dynamic. This section will deal with the first part of the problem concerning assigning ports for hardware like Access Points.

**Autoconf** is a solution that can be used to manage port configurations for data or voice VLAN, quality of service (QoS) parameters, storm control, and MAC-based port security on end devices that are deployed in the access layer of a network. Device classification is enabled when you enable the **Autoconf** feature using the `autoconf enable` command in global configuration mode. The onboard device classifier acts as an event trigger, which applies the appropriate automatic template to the interface. The default Autoconf service policy is applied to all the interfaces when the Autoconf feature is enabled using the `autoconf enable` command. For more information about **[Autoconf](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9400/software/release/16-12/configuration_guide/nmgmt/b_1612_nmgmt_9400_cg/configuring_autoconf.pdf)** or alternatively **[Autoconf Documentation](./configuring_autoconf.pdf)**

While **Autoconf** is a tremendous step forward for **non closed mode** ports, it will not function where **closed mode** has been applied at the moment. We need a way to *bridge* the gap so that we can dynamically assign a **low impact mode** configuration should the need arise. Luckily, we can use **EEM Event Manager** to solve the problem.

Luckily we can create a fully dynamic environment with a gated procedure. We include EEM scripts to give that Dynamic look and feel in this Lab entirely. Typically, the types of devices where we might have issues like this where *MAB* or *EAP* are not going to work fast enough, maybe those which identify themselves in another way. In those instances, we can use **PoE** power events to trigger an EEM. Likewise, on a port down event, we can revert the configuration. Those aspects are built into this Lab.

# Lab Preparation
## Lab Section 1 - DNA Center and ISE Integration
In this lab our focus changes slightly as we start to automate for host onboarding. A large component of host onboarding is the authentication of hosts and assignment within the network. In this section and in preparation for the steps which follow we will integrate DNA Center with Identity Services Engine. This integration allows pxGrid communication between the two and allows for automation of configuration within ISE for Network Access Devices, SGT, SGACL, and Policys.

### Step 1 - ***Prepare ISE for DNA Center Integration***
1. Open a web browser on the Windows Workstation Jump host. Open a connection to Identity Services Engine (ISE) and select the hamburger menu icon to open the system menu.

![json](./images/ise-dashboard.png?raw=true "Import JSON")

2. From the system menu under Administration select PxGrid Settings

![json](./images/ise-menu.png?raw=true "Import JSON")

3. On the PxGrid Settings page select both of the available options and click Save to allow DNA Center to integrate.

![json](./images/ise-pxgrid-settings.png?raw=true "Import JSON")
![json](./images/ise-pxgrid-setup.png?raw=true "Import JSON")

### Step 2 - ***DNA Center and ISE Integration***
1. Open a web browser on the Windows Workstation Jump host. Open a connection to Dna Center and select the hamburger menu icon and navigate to the System > Settings menu item.

![json](./images/dnac-system-settings.png?raw=true "Import JSON")

2. Within the System Settings page navigate down the list on the left and select the Authentication and Policy Server section.

![json](./images/dnac-system-settings-aaa.png?raw=true "Import JSON")

3. On the page select from the dropdown ISE to configure ISE integration.

![json](./images/dnac-system-settings-aaa-ise.png?raw=true "Import JSON")

4. Enter the information as seen on the page and click save.

![json](./images/dnac-system-settings-aaa-ise-config.png?raw=true "Import JSON")

5. A popup will appear as the ISE node is using an untrusted SelfSigned Certificate. For lab purposes Accept the certificate, this may appear a couple of times as shown.

![json](./images/dnac-system-settings-aaa-ise-trust.png?raw=true "Import JSON")

6. You will see the the various stages of integration proceed and finally a success message as shown below.

![json](./images/dnac-system-settings-aaa-ise-done.png?raw=true "Import JSON")
![json](./images/dnac-system-settings-aaa-ise-complete.png?raw=true "Import JSON")

## Lab Section 2 - DNA Center Design Preparation
While we could deploy more extensive settings for deployment, we will limit the configuration to the minimum necessary to perform this step, building off the completed tasks in labs one, [PnP Preparation](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB1-PNP-PREP/) and two, [Onboarding Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB2-Onboarding-Template/).

Should you desire to deploy rapidly and build the lab faster then use the following approach:

### Step 1 - ***Import Postman Collection***
1. Download and import the collection within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB8-Dynamic-Automation/postman/DCLOUD_DNACTemplatesLab_Workflow.postman_collection.json">⬇︎DCLOUD_DNACTemplateLab_Workflow.postman_collection.json⬇︎</a> file.
2. Extract the file to the desktop using **Winrar** to expand them
3. Open the **postman** application from the desktop. Once the application is open select *Collections* then click the *Import* link. 
![json](./images/Postman-Pre-Collection-Import.png?raw=true "Import JSON")
4. A window should appear on the file upload page. Click the upload button and select desktop from the windows explorer. Select the file named `DCLOUD_DNACTemplatesLab_Workflow.postman_collection.json` and click open. 
![json](./images/Postman-Collection-Select.png?raw=true "Import JSON")
5. Then click import and the collection should be loaded into the collections as shown.
![json](./images/Postman-Post-Collection-Import.png?raw=true "Import JSON")

### Step 2 - ***Import Postman Environment***
1. Download and import the environment within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB8-Dynamic-Automation/postman/DCLOUD_DNACTemplateLabs.postman_environment.json">⬇︎DCLOUD_DNACTemplateLabs.postman_environment.json⬇︎</a> file.
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

### Step 4 - ***Run the Collection within Postman***
This collection is built with a flow and delay timers wait for the collection to finish entirely.
1. If not open, open the **postman** application from the desktop. Once the application is open select *Collections* and then the '...' link and select **run collection**. </br>
![json](./images/Postman-CollectionRunner.png?raw=true "Import JSON")
2. On the right ensure all API are selected and click run collection. 
![json](./images/Postman-CollectionRunner-Run.png?raw=true "Import JSON")
3. After the entire collection has run you will see all of them listed on the left as shown, and two buttons on the top right, one for results and the other to run again.
![json](./images/Postman-CollectionRunner-Results.png?raw=true "Import JSON")
4. Within DNA Center you should see 3 devices within the inventory and additionally you should observe a complete hierarchy as well as settings and telemtry configured.
![json](./images/Postman-Discovery.png?raw=true "Import JSON")
![json](./images/Postman-Settings.png?raw=true "Import JSON")

## Lab Section 3 - DNA Center Template Preparation
We will now import the various templates for use in this lab. Three will be utilized:

1. Onboarding Template
2. Lab Preparation Project & Templates
3. Dynamic DayN Composite Project & Templates

### Step 1 - ***Import Onboarding Template***
The Onboarding Template previously discussed in Lab 2 will be used to Plug and Play a switch within the environment. for more information on this please see [Onboarding Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB2-Onboarding-Template/)

Download and import the Onboarding Template within the ***Template Editor*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB8-Dynamic-Automation/templates/DCLOUD-DNACTemplates-OnboardingTemplate.json">⬇︎DCLOUD-DNACTemplates-OnboardingTemplate.json⬇︎</a> file.

Import the environment into DNA Centers ***Template Editor*** by un-zip the file and import the *json* file which will automatically create a template within the onboarding template project. 

Use the following steps to import the project.

1. Navigate to the **Template Editor** within DNA Center through the menu *Tools>Template Editor* 
   ![json](./images/DNAC-Template-menu.png?raw=true "Import JSON")
2. Hover over the right side of the **onboarding templates**, and a small ⚙ gear icon will appear. Select **Import Template(s)** from the menu.    
   ![json](./images/DNAC-Template-Onboard-menu.png?raw=true "Import JSON")
3. From the **Import Templates(s)** window, click **Select a file from your computer** from the explorer window, select the extracted JSON file and click open.    
   ![json](./images/DNAC-Template-Onboard-select.png?raw=true "Import JSON")
4. Click **Import**, and the template will be imported.
   ![json](./images/DNAC-Template-import.png?raw=true "Import JSON")

### Step 2 - ***Import Lab Preparation Project***
The Lab Preparation Project and Templates will be used to prepare the environment.

Download and import the Onboarding Template within the ***Template Editor*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB8-Dynamic-Automation/templates/DCLOUD-PrepEnvironment-project.json">⬇︎DCLOUD-PrepEnvironment-Project.json⬇︎</a> file.

Please un-zip the file and import the *json* file which will automatically create a project and included templates within. Use the following steps to import the project.

1. Navigate to the **Template Editor** within DNA Center through the menu *Tools>Template Editor*.
   ![json](./images/DNAC-Template-menu.png?raw=true "Import JSON")
2. Within the **template editor**, left-click the ⨁ icon to the right of find template and click **Import Project(s)** within the menu.  
   ![json](./images/DNAC-Template-menu-import.png?raw=true "Import JSON")
3. Download the file above *DNAC_Template_Lab_DayN_project.json* to be imported into the DNA Center. Once downloaded, extract the file.
4. From the **Import Project(s)** window, click **Select a file from your computer** from the explorer window, select the extracted JSON file and click open. 
   ![json](./images/DNAC-Template-Prep-select.png?raw=true "Import JSON")
5. Click **Import**, and the project and all the templates within it will be imported.   
   ![json](./images/DNAC-Template-import.png?raw=true "Import JSON")
6. Once the project is imported, select it to view each of the template files within it.

### Step 3 - ***Import Dynamic DayN Project with Templates***
The Dynamic DayN Project contains a composite template and various regular templates used in a workflow to build out the use cases studied in Lab 7. For more information on Lab 7 please see [Advanced Automation](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB7-Advanced-Automation/)

Download and import the Dynamic DayN Project within the ***Template Editor*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB8-Dynamic-Automation/templates/DCLOUD-DNACTemplates-Dynamic-IBN-Autoconf-Project.json">⬇︎DCLOUD-DNACTemplates-Dynamic-IBN-Autoconf-Project.json⬇︎</a> file.

Please un-zip the file and import the *json* file which will automatically create a project and included templates within. Use the following steps to import the project.

1. Navigate to the **Template Editor** within DNA Center through the menu *Tools>Template Editor*.
   ![json](./images/DNAC-Template-menu.png?raw=true "Import JSON")
2. Within the **template editor**, left-click the ⨁ icon to the right of find template and click **Import Project(s)** within the menu.  
   ![json](./images/DNAC-Template-menu-import.png?raw=true "Import JSON")
3. Download the file above *DNAC_Template_Lab_DayN_project.json* to be imported into the DNA Center. Once downloaded, extract the file.
4. From the **Import Project(s)** window, click **Select a file from your computer** from the explorer window, select the extracted JSON file and click open. 
   ![json](./images/DNAC-Template-Dynamic-select.png?raw=true "Import JSON")
5. Click **Import**, and the project and all the templates within it will be imported.   
   ![json](./images/DNAC-Template-import.png?raw=true "Import JSON")
6. Once the project is imported, select it to view each of the template files within it.
   ![json](./images/DNAC-Template-Dynamic-files.png?raw=true "Import JSON")

Take a few moments and examine the construction of these projects and templates, as each has a specific function. Their design is modular to allow reuse of them within other composite templates for other switches or routers. 

## Lab Section 4 - DHCP & DNS Service Preparation
In this section we will prepare Domain Name System (DNS) and Dynamic Host Configuration Protocol (DHCP) on the Windows Server for the lab environment. The reasons for the configurations made here are detailed heavily in Lab 2 titled [Onboarding Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB2-Onboarding-Template/)

### Step 1 - ***Configuring DHCP and DNS via Powershell***
1. Download the powershell script to the ***windows server*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB8-Dynamic-Automation/scripts/powershell.ps1">⬇︎powershell.ps1⬇︎</a> file.
2. Once downloaded, extract the file.
   ![json](./images/Powershell-Extract.png?raw=true "Import JSON")
   ![json](./images/Powershell-Extract-Location.png?raw=true "Import JSON")
3. Right click on the file and run with powershell.
   ![json](./images/Powershell-Run.png?raw=true "Import JSON")

At this point all the DNS and DHCP configuration on the ***windows server*** will be generated.
   ![json](./images/DNS-DHCP.png?raw=true "Import JSON")

## Lab Section 5 - Setup of Discovered Devices
At this point in the lab the setup steps for the lab environment are done, DNS and DHCP are set up, ISE is integrated and DNA Center is ready for deploying configurations. In this section we will deploy the templates to configure the discovered devices. Note we could have automated this process too but wanted to separate this out so you can make modifications as you might need to for testing purposes.

### Lab SubSection 5.1 - ISR Preparation
In this subsection we will apply a small template to the ISR 4331. This is to prove out that we can deploy templates to modify discovered devices within the infrastructure no matter what variant they are. You could use this method to apply configuration to a router to mitigate vulnerabilities discovered as part of a tennable security scan. 

#### Step 1 - ***Building Routing Network Profiles***
1. Navigate to the **Design** within DNA Center through the menu *Design>Network Profile*.
   ![json](./images/DNAC-NetworkProfile-menu.png?raw=true "Import JSON")
2. Select *Routing* under **Add Profile** .
   ![json](./images/DNAC-NetworkProfile-Routing-Add.png?raw=true "Import JSON")
3. Enter the following: 
      1. Enter the *Profile name* 
      2. Select *Zero* for **Service Providers**
      3. Click the **Device Type** dropdown and select *Cisco 4331 Integrated Services Router* 
      4. Click *Next* to proceed to the next step. 
      ![json](./images/DNAC-NetworkProfile-Routing-1.png?raw=true "Import JSON")
4. We are not utilizing **Step 2** so click *Next* to proceed to the next step.
   ![json](./images/DNAC-NetworkProfile-Routing-2.png?raw=true "Import JSON")
5. We are not utilizing **Step 3** so click *Next* to proceed to the next step.
   ![json](./images/DNAC-NetworkProfile-Routing-3.png?raw=true "Import JSON")
6. On **Step 4** complete the following: 
      1. Select the *Day-N Template(s)* tab 
      2. Click the **Template** dropdown and select *ISR-Prep* 
      3. Click *Next* to proceed to the next step. 
      ![json](./images/DNAC-NetworkProfile-Routing-4.png?raw=true "Import JSON")
7. To complete the Network Profile in **Step 5** click *Save*.
   ![json](./images/DNAC-NetworkProfile-Routing-5.png?raw=true "Import JSON")


#### Step 1 - ***Assigning Routing Network Profile to a Site***
   1. **Assign** the network profile to the hierarchy 
   ![json](./images/DNAC-NetworkProfile-Routing-Assign.png?raw=true "Import JSON")
   2. Select the **sites** to apply the profile within the hierarchy and click *Save*
   ![json](./images/DNAC-NetworkProfile-Routing-Assign-Site.png?raw=true "Import JSON")



