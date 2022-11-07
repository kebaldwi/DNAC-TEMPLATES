# Dynamic Automation

## Overview
This Lab is designed to be used as a stand alone lab due. It has been created to address how to combine and use **IBNS 2.0** using **closed mode** and multiple Regular Templates within DNA Center to onboard network devices at Day 1 through N. This allows Network Administrators the ability to configure network devices in an ongoing and programmatic manner from within DNA Center without using the SD-Access Fabric methodology. It also enables an administrator to drag Regular Templates into and out of the flow as needed for ongoing maintenance.

This section will go through the flow involved in creating a deployable Composite Template from an IOS configuration script for a Catalyst switch linking it to a Switch profile, and deploying it through DNAC using provisioning workflows.

## General Information
As previously discussed, DNA Center can be used for Plug-and-Play and Day N or Ongoing Templates. Customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates and, for more flexibility Composite Templates. They can apply ongoing changes and allow device modifications after initial deployment. This lab section will focus on Day N templates built as regular templates within the DNA Center.

Another important consideration is that part of a typical configuration would include some lines of code, which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used, you should **not** deploy the same feature from cli code in a template to configure the device. It's a decision you have to make upfront, avoids a lot of lines in the templates, and allows for a more UI-centric configuration that is easier to maintain. 

As guidance, try and use **Design Settings** for as many of the configurations as you can, leaving Templates light and nimble for configurations that might change ongoing.

## Autoconf & IBNS 2.0 Secure Access
At the outset **IBNS 2.0** using **closed mode** can be modified effectively with the **Authentication Template Timers** deployed correctly on a switch, and while that will address some issues, sometimes a client will behave better with a **low impact mode** type of **access-session**. It is important to understand a few things:

1. You *cannot change* from **closed-mode** to **low-impact mode** *during a 802.1x session* as it will restart
2. That **closed mode** allows *no traffic* on the network from the host and so *DHCP will fail until authorized*
3. **Low impact mode** should be *protected* with a **pre-AUTH ACL** which is *overriden post authorization*
4. *Dynamically* interface templates can be deployed within **CoA**

Previously within the Composite Templating Lab and in the previous section, we introduced a methodology of automatically configuring the interfaces within the switch. This configuration relies on a few variables used to extrapolate the settings that were then configured via the template. This allowed a set of macros to be utilized to build out the various settings for VLANs, Ports, and Uplinks. 

While these were methodologies that dealt programmatically with port configuration, and while you may adapt them for an environment, they are both lacking in the fact that they are not dynamic enough. Again, it's impossible to determine without looking at the configuration where something is plugged in. Secondly, if equipment or users are plugged into the wrong interface, they may get the wrong level of access. 

In previous code revisions, we could deal with some of the problems with Auto Smart Port technology and IBNS 1.0, but that has been deprecated, and its replacement is a lot more dynamic. This section will deal with the first part of the problem concerning assigning ports for hardware like Access Points.

**Autoconf** is a solution that can be used to manage port configurations for data or voice VLAN, quality of service (QoS) parameters, storm control, and MAC-based port security on end devices that are deployed in the access layer of a network. Device classification is enabled when you enable the **Autoconf** feature using the `autoconf enable` command in global configuration mode. The onboard device classifier acts as an event trigger, which applies the appropriate automatic template to the interface. The default Autoconf service policy is applied to all the interfaces when the Autoconf feature is enabled using the `autoconf enable` command. For more information about **[Autoconf](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9400/software/release/16-12/configuration_guide/nmgmt/b_1612_nmgmt_9400_cg/configuring_autoconf.pdf)** or alternatively **[Autoconf Documentation](./configuring_autoconf.pdf)**

It is also essential to understand that with **IBNS2.0** and templates or interfaces running in **closed mode**, the dynamic capability of **Autoconf** is not going to operate because there is a **service-policy** applied to the interface. While the device classifier will operate, for some devices that require an IP address, they may reboot before the classifier has done its job and so inconsistancies can occur. Remember in closed mode no packets are forwarded including DHCP prior to authentication occurring. If the interface is in **low impact mode**, then and only then will **Autoconf** operate properly and as a result of the **pre-AUTH ACL** DHCP may be allowed.

While **Autoconf** is a tremendous step forward for **non closed mode** ports, it will not function where **closed mode** has been applied at the moment. We need a way to *bridge* the gap so that we can dynamically assign a **low impact mode** configuration should the need arise. Luckily, we can use **EEM Event Manager** to solve the problem.

Luckily we can create a fully dynamic environment with a gated procedure. We include EEM scripts to give that Dynamic look and feel in this Lab entirely. Typically, the types of devices where we might have issues like this where *MAB* or *EAP* are not going to work fast enough, maybe those which identify themselves in another way. In those instances, we can use **PoE** power events to trigger an EEM. Likewise, on a port down event, we can revert the configuration. Those aspects are built into this Lab.

# Lab Preparation
## Lab Section 1 - DNA Center and ISE Integration
In this lab our focus changes slightly as we start to automate for host onboarding. A large component of host onboarding is the authentication of hosts and assignment within the network. In this section and in preparation for the steps which follow we will integrate DNA Center with Identity Services Engine. This integration allows pxGrid communication between the two and allows for automation of configuration within ISE for Network Access Devices, SGT, SGACL, and Policys.

<details closed>
<summary> Click for Details and Sub Tasks</summary>

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

</details>

## Lab Section 2 - DNA Center Design Preparation
While we could deploy more extensive settings for deployment, we will limit the configuration to the minimum necessary to perform this step, building off the completed tasks in labs one, [PnP Preparation](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB1-PNP-PREP/) and two, [Onboarding Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB2-Onboarding-Template/).

Should you desire to deploy rapidly and build the lab faster then use the following approach:

<details closed>
<summary> Click for Details and Sub Tasks</summary>

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
4. Within DNA Center you should see 3 devices within the inventory and additionally you should observe a complete hierarchy as well as settings and telemetry configured. The Devices will be discovered in the Building level at this stage.
![json](./images/Postman-Discovery.png?raw=true "Import JSON")
![json](./images/Postman-Settings.png?raw=true "Import JSON")

</details>

## Lab Section 3 - DNA Center Template Preparation
We will now import the various templates for use in this lab. Three will be utilized:

1. Onboarding Template
2. Lab Preparation Project & Templates
3. Dynamic DayN Composite Project & Templates

<details closed>
<summary> Click for Details and Sub Tasks</summary>

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

</details>

## Lab Section 4 - DHCP & DNS Service Preparation
In this section we will prepare Domain Name System (DNS) and Dynamic Host Configuration Protocol (DHCP) on the Windows Server for the lab environment. The reasons for the configurations made here are detailed heavily in Lab 2 titled [Onboarding Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB2-Onboarding-Template/)

<details closed>
<summary> Click for Details and Sub Tasks</summary>

### Step 1 - ***Configuring DHCP and DNS via Powershell***
1. Download the powershell script to the ***windows server*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB8-Dynamic-Automation/scripts/powershell.ps1">⬇︎powershell.ps1⬇︎</a> file.
2. Once downloaded, extract the file.
   ![json](./images/Powershell-Extract.png?raw=true "Import JSON")
   ![json](./images/Powershell-Extract-Location.png?raw=true "Import JSON")
3. Right click on the file and run with powershell.
   ![json](./images/Powershell-Run.png?raw=true "Import JSON")
4. You may see a security warning. If you do accept it by entering **Y**.
   ![json](./images/Powershell-Security.png?raw=true "Import JSON")
At this point all the DNS and DHCP configuration on the ***windows server*** will be generated.
   ![json](./images/DNS-DHCP.png?raw=true "Import JSON")

</details>

## Lab Section 5 - Image Repository
As we have discovered the devices, from the network, DNA Center has the capability to pull those images deployed from the network devices in bundle mode. If the device is in install mode then you would manually have to add the images. We can then mark them as **Golden** for *Plug and Play* and *image upgrade* purposes. 

For our purposes as we will be focusing on only the **9300-2** switch we will complete the following steps.

The image used in this lab for the 9300-2 is downloadable from here [⬇︎Bengaluru-17.06.01 MD⬇︎](https://software.cisco.com/download/home/286315874/type/282046477/release/Bengaluru-17.6.1) **(required)** 

<details closed>
<summary> Click for Details and Sub Tasks</summary>

1. Within DNA Center Navigate to *Design>Image Repository*  
   ![json](./images/DNAC-Design-ImageRepo-menu.png?raw=true "Import JSON")
2.  **Image Repository** should be populated with the image of the network device you wish to deploy. You can import the image using the **+ Import** link which will open a popup allowing you to choose a file from the local file system, or allow you to reference a URL for either HTTP or FTP transfer. 
   ![json](./images/DNAC-Design-ImageRepo-import.png?raw=true "Import JSON")
3. We will select the file from our local system.
   ![json](./images/DNAC-Design-ImageRepo-select.png?raw=true "Import JSON")
3. The file will then import into DNA Center.    
   ![json](./images/DNAC-Design-ImageRepo-imageimport.png?raw=true "Import JSON")
4. Once the file is imported and as the devices were previously discovered and assigned to the infrastructure we will navigate to the *Floor 1* in the hierarchy and mark the *17.06.01* as **Golden** as shown for PnP to use it.  
   ![json](./images/DNAC-Design-ImageRepo-golden.png?raw=true "Import JSON")

</details>

## Lab Section 6 - Setup of Discovered Devices
At this point in the lab the setup steps for the lab environment are done, DNS and DHCP are set up, ISE is integrated and DNA Center is ready for deploying configurations. In this section we will deploy the templates to configure the discovered devices. Note we could have automated this process too but wanted to separate this out so you can make modifications as you might need to for testing purposes.

### Lab SubSection 6.1 - 9300 Target Preparation
In this subsection we will prepare the **Target** using the *c9300-2.dcloud.cisco.com*. To begin preparation of this **Target** device we can deploy a template to modify discovered device within the infrastructure to reset it automatically. In order to accomplish this we will need to complete the following stages.

<details closed>
<summary> Click for Details and Sub Tasks</summary>

#### Step 1 - ***Building Switching Network Profiles***
1. Navigate to the **Design** within DNA Center through the menu *Design>Network Profile*.
   ![json](./images/DNAC-NetworkProfile-menu.png?raw=true "Import JSON")
2. Select *Switching* under **Add Profile** .
   ![json](./images/DNAC-NetworkProfile-Switching-Add.png?raw=true "Import JSON")
3. Enter the following: 
      1. Enter the *Profile name* 
      2. Select **DayN Template** tab to add the template for this workflow.
      3. Click the **Table View** 
      4. Click *Add Template* to proceed to the next step. 
         ![json](./images/DNAC-NetworkProfile-Switching-DayN.png?raw=true "Import JSON")
4. Enter the following: 
      1. Leave the **Device Type** as *Switches and Hubs*
      2. Select the dropdown **Template** tand search for *C9300-TARGET-Prep*.
      3. Click the **Tags** 
      4. Enter *RELOAD* as a tag. *(If necessary click the small* ***x** by any other tag visible)*
      5. Click **Add** 
         ![json](./images/DNAC-Profile-Target-add.png?raw=true "Import JSON")
5. Click **View** to ensure the RELOAD tag is the only tag applied and click **Save**.
   ![json](./images/DNAC-Profile-Target-save.png?raw=true "Import JSON")

#### Step 2 - ***Assigning Switching Network Profile to a Site***
1. **Assign** the network profile to the hierarchy 
![json](./images/DNAC-NetworkProfile-Switching-DayN-Assign.png?raw=true "Import JSON")
2. Select the **sites** to apply the profile within the hierarchy and click **Save**
![json](./images/DNAC-NetworkProfile-Switching-DayN-Assign-Site.png?raw=true "Import JSON")

#### Step 3 - ***Provisioning Target 9300 Switch***
We will now provision the **Target** switch using the *C9300-TARGET-Prep* DayN Template. The template uses a *Tag* of **RELOAD** so we need to first set that and then provision the switch. To do this, do the following:

##### Tag Switch
   1. Within DNA Center Navigate to *Provision>Inventory*.      
      ![json](./images/DNAC-InventoryProvision-menu.png?raw=true "Import JSON")
   2. Put a **checkmark** next to the device *c9300-1.dcloud.cisco.com*.
   3. Click the **Tag Device** link 
   4. Search for and place a **checkmark** beside *RELOAD*
   5. Click **Apply**    
      ![json](./images/DNAC-Provision-Target-tag.png?raw=true "Import JSON")

##### Provision Switch
   1. Within DNA Center Navigate to *Provision>Inventory*.      
      ![json](./images/DNAC-InventoryProvision-menu.png?raw=true "Import JSON")
   2. Put a checkmark next to the device *c9300-1.dcloud.cisco.com* to be provisioned.
   3. Click **Actions>Provision>Provision Device** link and walk through the workflow    
      ![json](./images/DNAC-Provision-Target-flow.png?raw=true "Import JSON")
   4. The floor was already selected during the **API Discovery** so click **next**    
      ![json](./images/DNAC-Provision-Target-flow-1.png?raw=true "Import JSON")
   5. Select *c9300-1.dcloud.cisco.com* on the left and the two tick boxes at the top of the page, then click **next**. If the template had inputs, they would be entered.
      ![json](./images/DNAC-Provision-Target-flow-2.png?raw=true "Import JSON")
   6. Check the settings and if you agree accept these settings by clicking  **Deploy**.
      ![json](./images/DNAC-Provision-Target-flow-3.png?raw=true "Import JSON")
   7. Three options are displayed. Choose to deploy **Now** and **Apply**
      ![json](./images/DNAC-Provision-Target-flow-4.png?raw=true "Import JSON")
   8. The task will be submitted, and the deployment will run.
   9. After a small amount of time, you will see a success notification. What is essential to understand is that the configuration, while pushed to the device, will resync in DNA Center after the resync timer has elapsed.        
      ![json](./images/DNAC-Provision-Target-success.png?raw=true "Import JSON")

#### Step 4 - ***Deleting the Target 9300 Switch***
We will now delete the **Target** switch to allow for the switch to be discovered automatically during the **Plug and Play (PnP)** process. In order to accomplish this complete the following tasks:
   1. Within DNA Center Navigate to *Provision>Inventory*.      
      ![json](./images/DNAC-InventoryProvision-menu.png?raw=true "Import JSON")
   2. Put a **checkmark** next to the device *c9300-1.dcloud.cisco.com*.
   3. Click **Actions>Inventory>Delete Device** link 
      ![json](./images/DNAC-Provision-Target-delete-1.png?raw=true "Import JSON")
   4. On the *Popup* that appears click **Ok**
      ![json](./images/DNAC-Provision-Target-delete-2.png?raw=true "Import JSON")
   5. DNA Center will then delete the switch from the Database.  
      ![json](./images/DNAC-Provision-Target-delete-3.png?raw=true "Import JSON")

</details>

### Lab SubSection 6.2 - ISR Preparation
In this subsection we will apply a small template to the ISR 4331. This is to prove out that we can deploy templates to modify discovered devices within the infrastructure no matter what variant they are. You could also use this method to apply configuration to a router to mitigate vulnerabilities discovered as part of a tennable security scan. 

<details closed>
<summary> Click for Details and Sub Tasks</summary>

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

#### Step 2 - ***Assigning Routing Network Profile to a Site***
1. **Assign** the network profile to the hierarchy 
   ![json](./images/DNAC-NetworkProfile-Routing-Assign.png?raw=true "Import JSON")
2. Select the **sites** to apply the profile within the hierarchy and click **Save**
   ![json](./images/DNAC-NetworkProfile-Routing-Assign-Site.png?raw=true "Import JSON")

#### Step 3 - ***Provisioning Router***
   1. Within DNA Center Navigate to *Provision>Inventory*.      
      ![json](./images/DNAC-InventoryProvision-menu.png?raw=true "Import JSON")
   2. Put a checkmark next to the device *isr-4331.dcloud.cisco.com* to be provisioned.
   3. Click the **Actions>Provision>Provision Device** link and walk through the workflow    
      ![json](./images/DNAC-Provision-ISR-flow.png?raw=true "Import JSON")
   4. The floor was already selected during the **API Discovery** so click **next**    
      ![json](./images/DNAC-Provision-ISR-flow-1.png?raw=true "Import JSON")
   5. The ISR 4331 was pre selected in the profile so click **next**
      ![json](./images/DNAC-Provision-ISR-flow-2.png?raw=true "Import JSON")
   6. Do the following:
      1. Select the Day-N Templates Tab
      2. Select the IP of the ISR
      3. Select both **checkmark**
      4. Click **next**
      ![json](./images/DNAC-Provision-ISR-flow-3.png?raw=true "Import JSON")
   7. A summary is displayed. Click **Deploy**.
      ![json](./images/DNAC-Provision-ISR-flow-4.png?raw=true "Import JSON")
   8. Three options are displayed. Choose to deploy **Now** and **Apply**
      ![json](./images/DNAC-Provision-ISR-flow-5.png?raw=true "Import JSON")
   9. The task will be submitted, and the deployment will run.
   10. After a small amount of time, you will see a success notification. What is essential to understand is that the configuration, while pushed to the device, will resync in DNA Center after the resync timer has elapsed.        
      ![json](./images/DNAC-Provision-ISR-success.png?raw=true "Import JSON")

</details>

### Lab SubSection 6.3 - Distribution 9300 Preparation
In this subsection we will apply a small templates to the Cat 9300-2 which is used as a distribution switch. This is to prove out that we can deploy templates to modify discovered devices within the infrastructure no matter what variant they are. You could also use this method to apply configuration to a switch to mitigate vulnerabilities discovered as part of a tennable security scan. 

<details closed>
<summary> Click for Details and Sub Tasks</summary>

#### Step 1 - ***Building Switching Network Profiles***
1. Navigate to the **Design** within DNA Center through the menu *Design>Network Profile*.
   ![json](./images/DNAC-NetworkProfile-menu.png?raw=true "Import JSON")
2. Click the **Edit** beside the *DNAC-Templates-C9300* Profile Name.
   ![json](./images/DNAC-NetworkProfile-Switching-edit.png?raw=true "Import JSON")
3. Enter the following: 
      1. Enter the *Profile name* 
      2. Select **DayN Template** tab to add the template for this workflow.
      3. Click the **Table View** 
      4. Click *Add Template* to proceed to the next step. 
         ![json](./images/DNAC-NetworkProfile-Switching-DayN.png?raw=true "Import JSON")
4. Enter the following: 
      1. Leave the **Device Type** as *Switches and Hubs*
      2. Select the dropdown **Template** tand search for *DISTRO-C9300-2*.
      3. Click the **Tags** 
      4. Enter *INFRA* as a tag. *(If necessary click the small* ***x** by any other tag visible)*
      5. Click **Add** 
         ![json](./images/DNAC-NetworkProfile-Switching-DayN-Template.png?raw=true "Import JSON")
5. Click **View** to ensure the INFRA tag is **the only tag** applied and click **Save**.
   ![json](./images/DNAC-NetworkProfile-Switching-DayN-Template-Save.png?raw=true "Import JSON")

#### Step 2 - ***Assigning Switching Network Profile to a Site***
The network profile is already assigned to the site, so this step is not required but for review purposes only these were the steps we used to accomplish that originally. As this is already completed you can skip to **Step 3**

1. **Assign** the network profile to the hierarchy 
![json](./images/DNAC-NetworkProfile-Switching-DayN-Assign.png?raw=true "Import JSON")
2. Select the **sites** to apply the profile within the hierarchy and click **Save**
![json](./images/DNAC-NetworkProfile-Switching-DayN-Assign-Site.png?raw=true "Import JSON")

#### Step 3 - ***Provisioning Distribution 9300 Switch***
We will now provision the distribution switch using the *DISTRO-C9300-2* DayN Composite Template. The template uses a *Tag* of **INFRA** so we need to first set that and then provision the switch. To do this, do the following:

##### Tag Switch
   1. Within DNA Center Navigate to *Provision>Inventory*.      
   ![json](./images/DNAC-InventoryProvision-menu.png?raw=true "Import JSON")
   2. Put a **checkmark** next to the device *c9300-2.dcloud.cisco.com*.
   3. Click the **Tag Device** link 
   4. Search for and place a **checkmark** beside *INFRA*
   5. Click **Apply**    
   ![json](./images/DNAC-Provision-Distro-tag.png?raw=true "Import JSON")

##### Provision Switch
   1. Within DNA Center Navigate to *Provision>Inventory*.      
      ![json](./images/DNAC-InventoryProvision-menu.png?raw=true "Import JSON")
   2. Put a checkmark next to the device *c9300-2.dcloud.cisco.com* to be provisioned.
   3. Click the **Actions>Provision>Provision Device** link and walk through the workflow    
      ![json](./images/DNAC-Provision-Distro-flow.png?raw=true "Import JSON")
   4. The floor was already selected during the **API Discovery** so click **next**    
      ![json](./images/DNAC-Provision-Distro-flow-1.png?raw=true "Import JSON")
   5. Select *c9300-1.dcloud.cisco.com* on the left and the two tick boxes at the top of the page, then click **next**. If the template had inputs, they would be entered.
      ![json](./images/DNAC-Provision-Distro-flow-2.png?raw=true "Import JSON")
   6. Check the settings and if you agree accept these settings by clicking  **Deploy**.
      ![json](./images/DNAC-Provision-Distro-flow-3.png?raw=true "Import JSON")
   7. Three options are displayed. Choose to deploy **Now** and **Apply**
      ![json](./images/DNAC-Provision-Distro-flow-4.png?raw=true "Import JSON")
   8. The task will be submitted, and the deployment will run.
   9. After a small amount of time, you will see a success notification. What is essential to understand is that the configuration, while pushed to the device, will resync in DNA Center after the resync timer has elapsed.        
      ![json](./images/DNAC-Provision-Distro-flow-success.png?raw=true "Import JSON")

</details>

### Lab SubSection 6.4 - Preparation Confirmation
Once all the steps have been completed, the *c9300-1.dcloud.cisco.com* **Target** will have rebooted in a default state, acquired an IP address, discovered DNA Center and will appear in the **Plug and Play** tab in the **Provisioning** application. Confirm this by 

<details closed>
<summary> Click for Details and Sub Tasks</summary>

   1. Within DNA Center Navigate to *Provision>Inventory*.      
      ![json](./images/DNAC-InventoryProvision-menu.png?raw=true "Import JSON")
   2. Select the *Plug and Play* tab and notice the switch under the *unclaimed* section.
      ![json](./images/DNAC-Provision-Target-delete-4.png?raw=true "Import JSON")

At this point we are ready to set up our **Target** switch.

</details>

## Lab Section 7 - Target Switch Deployment
At this point in the lab the setup steps for the lab environment are done,the switch is in the unclaimed section of the Plug and Play section. In this section we will deploy the templates to configure the Target 9300 device with the dynamic templates discussed in detail in Lab 7. Note we could have automated this process too but wanted to separate this out so you can make modifications as you might need to for testing purposes.

![json](./images/DNAC-Provision-Target-delete-4.png?raw=true "Import JSON")

### Lab SubSection 7.1 - 9300 Templates
In this subsection we will begin preparation of this **Target** device by adding the templates previously uploaded to the network profile associated with the hierarchy. Please note that in DNA Center a single network profile of a given type may be used on a site within the hierarchy. In order to accomplish multiple use cases we use **Tags** and associate them to both the device and the template in question. In order to accomplish this we will need to complete the following stages.

<details closed>
<summary> Click for Details and Sub Tasks</summary>

#### Step 1 - ***Check for Access Tag on Templates***
1. Navigate to the **Template Editor** within DNA Center through the menu *Tools>Template Editor*.
   ![json](./images/DNAC-Template-menu.png?raw=true "Import JSON")
2. Within the **template editor**, select the drop down for the *DCLOUD DNAC Template Lab DayN w Autoconf and IBNS 2.0* Project.  
3. Select the Cog ⚙️ and then Properties from the submenu
   ![json](./images/DNAC-Template-Composite-Menu.png?raw=true "Import JSON")
4. Within the properties under the **Tag** section make sure *Access* appears
   ![json](./images/DNAC-Template-Properties.png?raw=true "Import JSON")

#### Step 2 - ***Modifying the Building Switching Network Profiles***
1. Navigate to the **Design** within DNA Center through the menu *Design>Network Profile*.
   ![json](./images/DNAC-NetworkProfile-menu.png?raw=true "Import JSON")
2. Click the **Edit** beside the *DNAC-Templates-C9300* Profile Name.
   ![json](./images/DNAC-NetworkProfile-Switching-edit.png?raw=true "Import JSON")
##### Onboarding Template
1. Enter the following: 
      1. Select **Onboarding Template** tab to add the template for this workflow.
      2. Click the **Table View** 
      3. Click **Add Template** to proceed to the next step. 
         ![json](./images/DNAC-Profile-Switching-Onboarding-Add.png?raw=true "Import JSON")
2. Enter the following: 
      1. Change the **Device Type** to *9300 Switches* as shown
      2. Select the dropdown **Template** and search for *Platinum Onboarding Template using 2.1.2.5 gen template*.
      3. Click the **Tags** 
      4. Enter *Access* as a tag. *(If necessary click the small* ***x** by any other tag visible)*
      5. Click **Add** 
         ![json](./images/DNAC-NetworkProfile-Switching-Onboarding-Template.png?raw=true "Import JSON")
3. Click **View** to ensure the *Access* tag is **the only tag** then proceed to the **DayN Template Tab** for the next section. 
   ![json](./images/DNAC-NetworkProfile-Switching-Onboarding-Template-Save.png?raw=true "Import JSON")
##### DayN Template
1. Enter the following: 
      1. Select **DayN Template** tab to add the template for this workflow.
      2. Click the **Table View** 
      3. Click **Add Template** to proceed to the next step. 
         ![json](./images/DNAC-NetworkProfile-Switching-DayN-Composite-Template-Add.png?raw=true "Import JSON")
2. Enter the following: 
      1. Change the **Device Type** to *9300 Switches* as shown
      2. Select the dropdown **Template** and search for *DNAC Template Lab DayN Composite Autoconf IBNS*.
      3. Click the **Tags** 
      4. Enter *Access* as a tag. *(If necessary click the small* ***x** by any other tag visible)*
      5. Click **Add** 
         ![json](./images/DNAC-NetworkProfile-Switching-DayN-Composite-Template.png?raw=true "Import JSON")
3. Click **View** to ensure the *Access* tag is **the only tag** then proceed to **Save**. 
   ![json](./images/DNAC-NetworkProfile-Switching-DayN-Composite-Template-Save.png?raw=true "Import JSON")

#### Step 3 - ***Assigning Switching Network Profile to a Site***
The network profile is **already assigned** to the site, so this step is not required but for review purposes only these were the steps we used to accomplish that originally. As this is already completed you can skip to **Step 3**

1. **Assign** the network profile to the hierarchy 
   ![json](./images/DNAC-NetworkProfile-Switching-DayN-Assign.png?raw=true "Import JSON")
2. Select the **sites** to apply the profile within the hierarchy and click **Save**
   ![json](./images/DNAC-NetworkProfile-Switching-DayN-Assign-Site.png?raw=true "Import JSON")

#### Step 4 - ***Claiming and Onboarding*** 
At this point DNAC is set up and ready for the Plug and Play process to onboard the first device. Provided the discovery and dhcp assignment are aligned, the device should when plugged in discover DNA Center and land in the plug n play set of the devices section within the Provisioning Application. 

We will manually do these steps to allow for modifications but again all of these steps could be automated through REST-API. Please claim the device by completing the following:

   1. Within DNA Center Navigate to *Provision>Plug and Play*      
      ![json](./images/DNAC-NavigatePnP.png?raw=true "Import JSON")
   2. Put a checkmark next to the device *Switch* to be claimed
   3. Click the **Actions>Claim** link and walk through the workflow    
      ![json](./images/DNAC-BeginClaim.png?raw=true "Import JSON")
   4. If this is the first time you have worked with images, you may see an EULA window if that has not been accepted under the settings of DNA Center. Simply click the **accept checkbox** and click **save**.
      ![json](./images/DNAC-EULA.png?raw=true "Import JSON")
   5. Section 1 select the **Assign** link to assign the device to the hierarchy *floor1* to where the device will be deployed then click **save** and then click **next**    
      ![json](./images/DNAC-SiteClaim-1.png?raw=true "Import JSON")
      ![json](./images/DNAC-SiteClaim-2.png?raw=true "Import JSON")
      ![json](./images/DNAC-SiteClaim-3.png?raw=true "Import JSON")
   5. Section 2 you can click the hyperlinks to the right of the workflow page and view or amend the templates and images utilized then click **next** 
      ![json](./images/DNAC-AssignConfig-Claim-1.png?raw=true "Import JSON")
      If you open the hyperlinks you can preview the image and template to be deployed, and in stacks select the master.
      ![json](./images/DNAC-AssignConfig-Claim-2.png?raw=true "Import JSON")
   6. Section 3 select the device **serial number** on the left and check the variables within the template click **next**. Please use the following:
      *   Hostname type `ACCESS-c9300-ASW`
      *   Management Vlan enter `5`
      *   IP Address `192.168.5.10`
      *   Subnet Mask `255.255.255.0`
      *   Gateway `192.168.5.1`
      *   VTP Domain `Cisco`   
      ![json](./images/DNAC-TemplateClaim.png?raw=true "Import JSON")
   7. Section 4 review the elements including configuration to be deployed, then click **claim** and the **yes** on the popup to begin the process.
      ![json](./images/DNAC-DeviceClaim-1.png?raw=true "Import JSON")
      ![json](./images/DNAC-DeviceClaim-2.png?raw=true "Import JSON")
      ![json](./images/DNAC-DeviceClaim-3.png?raw=true "Import JSON")
      ![json](./images/DNAC-DeviceClaim-4.png?raw=true "Import JSON")
   8. At this stage the device will be placed in **Planned** state, and will cycle through **Onboarding** and **Provisioned** when complete.       
      ![json](./images/DNAC-Claimed-1.png?raw=true "Import JSON")
      ![json](./images/DNAC-Claimed-2.png?raw=true "Import JSON")
      ![json](./images/DNAC-Claimed-3.png?raw=true "Import JSON")
   11. After the device is completed it will appear in the device inventory after being sync'd with DNA Center.      
      ![json](./images/DNAC-Claimed-to-Inventory.png?raw=true "Import JSON")

#### Step 5 - ***Provisioning Target 9300 Switch***
We will now provision the target *ACCESS-c9300-ASW* access switch using the Composite Template. The template uses a *Tag* of **Access** as previously defined so we need to first set that **Tag** and then **provision** the switch. To do this, do the following:

##### Tag Switch
   1. Within DNA Center Navigate to *Provision>Inventory*.      
      ![json](./images/DNAC-InventoryProvision-menu.png?raw=true "Import JSON")
   2. Put a **checkmark** next to the device *ACCESS-c9300-ASW*.
   3. Click the **Tag Device** link 
   4. Search for and place a **checkmark** beside *ACCESS*
   5. Click **Apply**    
      ![json](./images/DNAC-Provision-Access-tag.png?raw=true "Import JSON")

##### Provision Switch
   1. Within DNA Center Navigate to *Provision>Inventory*.      
      ![json](./images/DNAC-InventoryProvision-menu.png?raw=true "Import JSON")
   2. Put a checkmark next to the device *ACCESS-c9300-ASW* to be provisioned.
   3. Click the **Actions>Provision>Provision Device** link and walk through the workflow    
      ![json](./images/DNAC-Provision-Access-flow.png?raw=true "Import JSON")
   4. The floor was already selected during the **Claim** so click **next**    
      ![json](./images/DNAC-Provision-Access-flow-1.png?raw=true "Import JSON")
   5. Select *ACCESS-c9300-ASW* on the left and the two tick boxes at the top of the page. Then select the *VLANs Ports per DF* use the dropdown and select **C9300-48U** then click **next**.
      ![json](./images/DNAC-Provision-Access-flow-2.png?raw=true "Import JSON")
   6. Check the settings and if you agree accept these settings by clicking  **Deploy**.
      ![json](./images/DNAC-Provision-Access-flow-3.png?raw=true "Import JSON")
   7. Three options are displayed. Choose to deploy **Now** and **Apply**
      ![json](./images/DNAC-Provision-Access-flow-4.png?raw=true "Import JSON")
   8. The task will be submitted, and the deployment will run.
   9. After a small amount of time, you will see a success notification. What is essential to understand is that the configuration, while pushed to the device, will resync in DNA Center after the resync timer has elapsed.        
      ![json](./images/DNAC-Provision-Access-flow-success.png?raw=true "Import JSON")

</details>

## Lab Section 8 - ISE Authorization Policy for FlexConnect
At this point in the lab the setup steps for the lab environment are done,the switch is in the provisioned. In this section we will deploy a policy by configuring ISE to alter the port behaviour on authorization by utilizing a interface template for FlexConnect in a Change of Authorization. 

<details closed>
<summary> Click for Details and Sub Tasks</summary>

### Step 1 - ***Build Logical Profiles for FlexConnect Access Point***
First set up the Logical Profile we will reference for the Access Points. Logical Profile are a method of grouping and referencing multiple device profiles at the same time and may be used policy purposes.
1. Navigate to and click the **Hamburger Button** **☰** on the ISE Dashboard.
   ![json](./images/ISE-Dashboard-Menu.png?raw=true "Import JSON")
2. Navigate to and select *Work Centers>Profiler>Profiling Policies*.
   ![json](./images/ISE-Menu-WorkCenter-ProfilingPolicies.png?raw=true "Import JSON")
3. On the *Profiling Policies* page select *Logical Profiles* on the left and then click **Add**.
   ![json](./images/ISE-Profilng-LogicalProfiles-add.png?raw=true "Import JSON")
4. Do the following to create the profile:
   1. Enter the name *Cisco-AP* 
   2. Under the available profiles select all the *Cisco Access Points* 
   3. Click the arrow to move them to *Assigned*.
      ![json](./images/ISE-Profilng-LogicalProfiles-1.png?raw=true "Import JSON")
5. Then click **Submit** to save the new Logical Profile. (Note on subsequent edits the button will be a **Save**)
   ![json](./images/ISE-Profilng-LogicalProfiles-3.png?raw=true "Import JSON")
6. The new Logical Profile will then be shown in the list of Logical Profiles.
   ![json](./images/ISE-Profilng-LogicalProfiles-Success.png?raw=true "Import JSON")

### Step 2 - ***Build Authorization Profile for FlexConnect Access Point***
Next set up the Authorization Profile which will be the result of a successful authentication and authorization of the Access Points. 
1. Navigate to and click the **Hamburger Button** **☰** on the ISE Dashboard.
   ![json](./images/ISE-Dashboard-Menu.png?raw=true "Import JSON")
2. Navigate to and select *Policy>Policy Elements>Results*.
   ![json](./images/ISE-Menu-Policy-Results.png?raw=true "Import JSON")
3. On the *Results* page select *Authorization>Authorization Profiles* on the left and then click **Add**.
   ![json](./images/ISE-AuthorizationProfile-Add.png?raw=true "Import JSON")
4. Start the Creation of the Authorization Profile by doing the following:
   1. Enter the name *Cisco_FlexAccessPoints* 
   2. Ensure *ACCESS_ACCEPT* is selected for **Access Type** 
   3. Then under *Common Tasks* select the **checkmark** beside *Vlan* and enter *10* for the *ID*
      ![json](./images/ISE-AuthorizationProfile-1.png?raw=true "Import JSON")
5. Continue the creation of the Authorization Profile by doing the following:
   1. Scroll down under *Common Tasks* 
   2. Select the **checkmark** beside *Interface Template* 
   3. Enter *FLEX_ACCESS_POINT*
      ![json](./images/ISE-AuthorizationProfile-2.png?raw=true "Import JSON")
6. Continue the creation of the Authorization Profile by doing the following:
   1. Scroll down again and select the **checkmark** beside *Reauthentication* 
   2. Enter *3600* for the timer which is in milliseconds 
   3. Ensure *RADIUS-Request* is selected
      ![json](./images/ISE-AuthorizationProfile-3.png?raw=true "Import JSON")
7. Ensure the values shown are displayed at the bottom of the page and click **Save**.
   ![json](./images/ISE-AuthorizationProfile-4.png?raw=true "Import JSON")

### Step 3 - ***Build Authorization Policy for FlexConnect Access Point***
Next set up the Authorization Policy which will allow for a successful authentication and authorization of the Access Points. 
1. Navigate to and click the **Hamburger Button** **☰** on the ISE Dashboard.
   ![json](./images/ISE-Dashboard-Menu.png?raw=true "Import JSON")
2. Navigate to and select *Policy>Policy Sets*.
   ![json](./images/ISE-Menu-Policy-PolicySet.png?raw=true "Import JSON")
3. On the *Policy Sets* page select the *>* on the right to enter the **Default Policy**.
   ![json](./images/ISE-PolicySets-Default.png?raw=true "Import JSON")
4. Select and begin the Creation of the Authorization Policy by completing the following:
   1. Click the **Cog** ⚙️ as shown 
   2. Select **Insert new row above**
      ![json](./images/ISE-PolicySets-Authorization-Add.png?raw=true "Import JSON")
5. Continue the creation of the Authorization Policy by doing the following:
   1. Enter a policy name *Cisco FlexConnect AP* 
   2. Click the **+** under *Conditions* 
      ![json](./images/ISE-PolicySets-Authorization-1.png?raw=true "Import JSON")
6. In the conditions studio click **click to add an attribute** 
   ![json](./images/ISE-PolicySets-Authorization-2.png?raw=true "Import JSON")
7. Select **All Dictionaries** a list will appear search and select *Endpoints*
   ![json](./images/ISE-PolicySets-Authorization-3.png?raw=true "Import JSON")
8. Under **Attributes** search and select *LogicalProfile*
   ![json](./images/ISE-PolicySets-Authorization-4.png?raw=true "Import JSON")
9. Ensure the **Equals** operator is selected then select **Choose from the list or type** and select **Cisco-AP** for the Profile
   ![json](./images/ISE-PolicySets-Authorization-5.png?raw=true "Import JSON")
10. Click **Use**
   ![json](./images/ISE-PolicySets-Authorization-6.png?raw=true "Import JSON")
11. Under **Profiles** click *Select from list* and choose the **Cisco_FlexAccessPoints** Profile created earlier
   ![json](./images/ISE-PolicySets-Authorization-7.png?raw=true "Import JSON")
12. Scroll to bottom of the page and click **Save**.
   ![json](./images/ISE-PolicySets-Authorization-8.png?raw=true "Import JSON")

</details>

Congratulations you have set up ISE to perform the required Authentication and Authorization of the Access Point.

## Summary
Congratulations, at this point, you have successfully reviewed and setup the infrastructure equipment. The Composite template used will allow for *Low Impact* mode to be used on ports selectively where PoE devices power up.

During your review of the configurations used in this lab, please review the distribution switch which should have onboarded a Wireless Access Point using **Autoconf**. Then compare that to the switch running 802.1x IBNS 2.0 namely the Access Switch. On the Access Switch we utilize closed mode by default. We automatically modify the config on the port using PoE to put the device into **Low Impact** mode using an **EEM Script** specifically to deal with devices which might need either altered Service Policy for Authentication for instance MAB first vs 802.1x or low impact mode for autoconf. The point is understanding the gated method allows you to modify behaviour no matter what the cause.

### Use cases:
1. Modify policy priority on Auth Failure events Switch side
2. Modify policy to low impact mode
3. Revert the port to Closed Mode

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
