# DayN Provisioning

## Overview

This Module is designed to be a part of a series of labs built to address how to use DayN templates within Cisco Catalyst Center to configure network devices at Day 1 through N. This Lab is designed to be used after first completing the previous modules. The purpose of DayN templates is to allow for ongoing configuration of features on devices beyond those deployed on the Claiming process. With Cisco Catalyst Center, if devices are not within a fabric, the host onboarding part of the UI will not be available. To that end, templates are an easy way of deploying those types of configuration and much more. Before starting this Lab, please make sure you have finished all the steps in the previous modules.

## General Information

Cisco Catalyst Center can be used for Plug and Play and Day N or Ongoing Templates; customers will start by building out an Onboarding Template that typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates as they can be used to apply ongoing changes and to allow device modifications after initial deployment. This lab section will focus on Day N templates to be built as regular templates within Cisco Catalyst Center.

Another important consideration is that part of a typical configuration would include some lines of code, which are built by the *Design >Network Settings >* application within Cisco Catalyst Center. If the Design component is used, you should **not** deploy the same feature from cli code in a template to configure the device. It's a decision you have to make upfront, avoids many lines in the templates, and allows for a more UI-centric configuration that is easier to maintain. 

As guidance, try and use **Design Settings** for as many configurations as you can, leaving Templates light and nimble for configurations that might change ongoing.

### Greenfield

When dealing with net new devices using the Provisioning process we utilize it is better to utilize composite templates with multiple regular templates within. This allows greater flexibility and a method to always add to the structure for compliance reasons. Additionally, Jinja2 and Velocity Scripting languages may be intermingled, allowing for the reuse of existing scripts.

### Brownfield

When dealing with existing infrastructure, initially we want to absorb the device and its configuration into Cisco Catalyst Center to allow for monitoring and a gradual shift to automated management, as the device usually is in a running state supporting the network, and the configuration pre-exists.

As time progresses though, we may want to introduce slowly automation from Catalyst Center utilizing DayN Templates. Be aware that with Brownfield device configurations, there is no template learning capability for switching. As such configuration on the device may need modification prior to provisioning in some situations. Should it be a newer device, you may want to Discover and then push a normalization template via REST API to remove settings that would cause ongoing provisioning errors. Should this be a device already in Catalyst Center, then a normalization strategy may need to be adopted, backing out certain configuration, prior to provisioning. This script will involve perhaps the removal of AAA commands and others which cause issues with provisioning.

## Cisco Catalyst Center DayN Template Overview

While a more extensive set of settings can be built out for deployment, we will limit the configuration to the minimum necessary to perform this step, building off the completed tasks in module 2.

You can create Regular Day N Templates using Jinja2 and Velocity scripting languages within the **Template Hub** previously known as **Template Editor** within **Cisco Catalyst Center**. Go to the **Template Hub**  to complete the next task. Initially, we will keep things pretty simple and deploy one Day N regular template. Once the process has been discussed in detail, we will build on this within the following labs.

There are two basic types of templates we can utilize. **Regular** templates, as well as **Composite** templates. 

### Regular Templates

**Regular** templates are templates which are typically designed to address a specific use case. Regular templates are written in either Jinja2 or Velocity scripting languages. Each Language has features which may be leveraged to make the script more reusable, allowing the user to not have to repeat themselves. This modular capability allows us to keep a script written to address a specific need small. At the same time each form of scripting language allows for features like variables, conditional logic, and looping constructs. This allows for a small powerful script to be written making it more light weight and easier to fault find and maintain.

### Composite Templates

**Composite** templates are logical templates used for grouping together multiple **Regular** templates. They allow you to use Jinja2 and Velocity **Regular** templates within the same logical template. This allows us to make templates in mutliple languages and to be able to reuse long standing Velocity scripts with newer Jinja2 templates within the same **Composite** Template. This allows for people to code in the language they are more accustomed too, and to continue to support existing scripts.

### Scripting Languages

**Jinja2** and **Velocity** both have similar capabilities. For additional information please see these tutorials. You may want to open these in another tab to read the content and to allow you to continue the lab:

* [Velocity Scripting](../../TUTORIALS/Velocity.md)
* [Jinja2 Scripting](../../TUTORIALSJinja2.md)

Within these logical constructs you have many tools and these are an example but not all of them, please review each section as needed:

#### Velocity Scripting Logic

Velocity's deployment in Cisco Catalyst Center is utilizing 1.75 version, and as such has the typical logical capabilities available within that release. Please see the following:

* [If Statements](../../TUTORIALSVelocity.md#if-statements)
* [Macros](../../TUTORIALSVelocity.md#macros)
* [Loops](../../TUTORIALSVelocity.md#foreach-loops)
* [Multiline commands](../../TUTORIALSVelocity.md#multi-line-commands)

#### Jinja2 Scripting Logic

Jinja2 as deployed in Cisco Catalyst Center allows for the following capabilities as well as include and extend capabilities. Please see the following:

* [If Statements](../../TUTORIALSJinja2.md#conditional-statements)
* [Macros](../../TUTORIALSJinja2.md#macros)
* [Loops](../../TUTORIALSJinja2.md#for-loops)
* [Multiline commands](../../TUTORIALSJinja2.md#multi-line-commands)

## Cisco Catalyst Center DayN Template Provisioning

This section will go through the build and provisioning of a **Regular** template via Cisco Catalyst Center to a Catalyst 9k switch. We will deal with **Brownfield** and **Greenfield** scenarios during this module.

### Preparation

We will download and import a template project to include templates for deployment.



#### Step 1 - Create a Regular Day N Template

Download and import a simple Day N Template in the **Template Hub**  using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-1-Wired-Automation/templates/2125templates/Platinum_AAA_Template.json">⬇︎Platinum_AAA_Template.json⬇︎</a> file. If using Cisco Catalyst Center prior release to 2.1.2.X then build the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-1-Wired-Automation/templates/Platinum_AAA_Template.txt">⬇︎Platinum_AAA_Template.txt⬇︎</a> located within this lab. 

1. Navigate to the **Template Hub**  within Cisco Catalyst Center through the menu *Tools>Template Hub*.

   ![json](./images/DNAC-NavigateTemplate.png?raw=true "Import JSON")

2. Within the **Template Hub** , left-click the ⨁ icon to the right of onboarding templates and click **Create Project** within the menu.  

   ![json](./images/DNAC-ProjectCreate.png?raw=true "Import JSON")

3. Name the new project `DNAC Template Lab DayN`. This project will be the one we will use to keep all our templates.   

   ![json](./images/DNAC-ProjectAdd.png?raw=true "Import JSON")

4. Download the file above *Platinum_AAA_Template.json* to be imported into the Cisco Catalyst Center. Once downloaded, extract the file.
5. Hover over the right side of the new project, and a small ⚙ gear icon will appear. Select **Import Template(s)** from the menu.   

   ![json](./images/DNAC-TemplateImportBegin.png?raw=true "Import JSON")

6. From the **Import Templates** window, click **Select a file from your computer** from the explorer window, select the extracted JSON file and click open.   

   ![json](./images/DNAC-TemplateSelect.png?raw=true "Import JSON")

7. Click **Import**, and the template will be placed in the project.   

   ![json](./images/DNAC-TemplateImport.png?raw=true "Import JSON")

8. Once the template is in the project, select it to view the configuration.

   ![json](./images/DNAC-TemplateAAA.png?raw=true "Import JSON")

The DayN regular template has the minimal AAA configuration to configure the device for local AAA connectivity independent of ISE to work with Cisco Catalyst Center. Below is for explanation purposes only. (Please Import the Template JSON above)

```vtl
aaa new-model
!
aaa authentication username-prompt "Authorized Username:"
aaa authentication login admin local
aaa authorization console
aaa authorization exec admin local
aaa authentication login admin local-case
aaa authorization exec admin local 
!
mac address-table notification mac-move
mac address-table notification threshold
mac-address-table notification change
!
```

#### Step 2 - Modify Network Profile

Next, we need to assign the DayN Template to a site using the Network Profile. As there is an existing network profile for the site, we must reuse that one for the same device family.**(required)** 

   1. Navigate to Network Profiles by selecting *Design> Network Profiles*.

      ![json](./images/DNAC-NavigateProfile.png?raw=true "Import JSON")

   2. Click the **Edit** link next to the **DNAC Template Lab** switching profile created earlier.  

      ![json](./images/DNAC-ProfileEdit.png?raw=true "Import JSON")

   3. Within the Profile Editor, select the **Day-N Template(s)** tab: 
      1. Click **⨁Add** 
      2. Select the device type by typing *9300* in the search window and select it.    

         ![json](./images/DNAC-ProfileDayN9300.png?raw=true "Import JSON")   

      3. Select the Template by either searching or choosing *AAA* from the dropdown as shown.

         ![json](./images/DNAC-ProfileDayNAAA.png?raw=true "Import JSON")   

      4. Click **Save** to save the modifications to the Network Profile.

         ![json](./images/DNAC-ProfileSuccess.png?raw=true "Import JSON")   

#### Step 3 - Provisioning the Device

At this point, Cisco Catalyst Center is set up and ready to provision the new regular template AAA to the device. This next set of sequences will push the various Network Settings, Services, and DayN Templates to the device.

We will now provision the switch using DayN Templates. To do this, do the following:

   1. Within Cisco Catalyst Center Navigate to *Provision>Inventory*.      

      ![json](./images/DNAC-NavigateInventory.png?raw=true "Import JSON")

   2. Put a checkmark next to the device *ACCESS-c9300-1-ASW* to be provisioned.
   3. Click the **Actions>Provision>Provision Device** link and walk through the workflow    

      ![json](./images/DNAC-ProvisionBegin.png?raw=true "Import JSON")

      1. The floor was already selected as part of the claim so click **next**    

         ![json](./images/DNAC-ProvisionSite.png?raw=true "Import JSON")

      2. Select *ACCESS-c9300-1-ASW* on the left and the two tick boxes at the top of the page, then click **next**. If the template had inputs, they would be entered.  

         ![json](./images/DNAC-ProvisionAdvConfig.png?raw=true "Import JSON")

      3. Review the information to be deployed and click **Deploy**.

         ![json](./images/DNAC-ProvisionDeploy.png?raw=true "Import JSON")

      4. Click **Apply** on the Provision Device pop-up screen. You can schedule deployments though.

         ![json](./images/DNAC-ProvisionApply.png?raw=true "Import JSON")

   4. The task will be submitted, and the deployment will run.

      ![json](./images/DNAC-ProvisionTasking.png?raw=true "Import JSON")

   5. After a small amount of time, you will see a success notification. What is essential to understand is that the configuration, while pushed to the device, will resync in Cisco Catalyst Center after the resync timer has elapsed.        
   6. To resync the configuration so that it may be viewed before the normal 25 mins, then perform the following task:
      1. Change the focus to **Inventory**
      2. Select the *ACCESS-c9300-1-ASW* switch and select **Actions>Inventory>Resync Device**

         ![json](./images/DNAC-InventoryResync.png?raw=true "Import JSON")

      3. After the resync has occurred, you may click the device name and then view the configuration by selecting that from the left pane to view the configuration pushed.

         ![json](./images/DNAC-DeviceConfig.png?raw=true "Import JSON")

At this point, we have onboarded a device and successfully pushed configuration via Onboarding and DayN Templates. 

> **Note:** If you populate the UI with settings, those parameters should **not** be in your templates as they will conflict, and the deployment through provisioning will fail. While it is easy to populate these settings, it is best to test with a switch to see what configuration is pushed.

### Composite Day N Templates

This section will go through the build and provisioning of a **Composite** template via Cisco Catalyst Center to a Catalyst 9k switch. You can create Day N Composite Templates within the **Template Hub** previously known as **Template Editor** within **Cisco Catalyst Center**. Go to the **Template Hub**  to complete the next task. In this lab, we will deploy a Composite Template and additional **Regular** Templates within a project.  The import and export function within **Cisco Catalyst Center** allows both the import and export of templates and projects, along with the ability to clone them.

#### Step 1 - Import Project with Templates

Download and import the project within the **Template Hub**  using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-1-Wired-Automation/templates/2125templates/DNAC_Template_Lab_DayN_project.json">⬇︎DNAC_Template_Lab_DayN_project.json⬇︎</a> file. If using Cisco Catalyst Center prior release to 2.1.2.X then use the previously built project within Lab 3 and build the templates located within the following <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-1-Wired-Automation/templates/Platinum_Templates.zip">⬇︎Platinum_Templates.zip⬇︎</a> file located within this lab. 

For Jinja2, download and import the project within the **Template Hub**  using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-1-Wired-Automation/templates/Jinja2/DNAC_Template_Lab_DayN_Jinja2_project.json">⬇︎DNAC_Template_Lab_DayN_Jinja2_project.json⬇︎</a> file. 

Previously in Lab 3, we created a project where we assigned a template to the site and provisioned it. We will now expand on that by importing a project with the same name overtop the current project, thereby importing additional regular templates. Take a few moments and examine the construction of these templates, as each has a specific form and function. Their design is modular to allow reuse of them within other composite templates for other switches or routers.

1. Navigate to the **Template Hub**  within Cisco Catalyst Center through the menu *Tools>Template Hub*.

   ![json](./images/DNAC-NavigateTemplate.png?raw=true "Import JSON")

2. Within the **Template Hub** , left-click the ⨁ icon to the right of find template and click **Import Project(s)** within the menu.  

   ![json](./images/DNAC-ProjectImportBegin.png?raw=true "Import JSON")

3. Download the file above *DNAC_Template_Lab_DayN_project.json* to be imported into the Cisco Catalyst Center. Once downloaded, extract the file.
4. From the **Import Project(s)** window, click **Select a file from your computer** from the explorer window, select the extracted JSON file and click open. 

   ![json](./images/DNAC-ProjectSelect.png?raw=true "Import JSON")

5. Click **Import**, and the project and all the templates within it will be imported.   

   ![json](./images/DNAC-ProjectImport.png?raw=true "Import JSON")

6. Once the project is imported, select it to view each of the template files within it.

   ![json](./images/DNAC-ProjectFiles.png?raw=true "Import JSON")
 
#### Step 2 - Review the Composite Template Project

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

### Step 3 - Review how to Create Composite Template

Within the project is a Composite Template, but the steps involved to create one are simple. **The next steps are optional**.

1. Within the **Template Hub** , Hover over the right side of the project, and a small ⚙ gear icon will appear. Select **Add Template(s)** from the menu.     

   ![json](./images/DNAC-CompositeCreate.png?raw=true "Import JSON")

2. Notice you have the options on the *Add New Template* sidebar to do the following:
   1. Select **Composite Sequence**
   2. Enter a **Name** for the Composite Template
   3. Click **Edit** beside *Device Types* to select the device families to be used.   

      ![json](./images/DNAC-CompositeDefine.png?raw=true "Import JSON")

3. On the *Select Device Types* sidebar type in `9300`to filter for the switch family and select the entire series then click **Back to Add New Template**.         

   ![json](./images/DNAC-CompositeDevices.png?raw=true "Import JSON")

4. Next Select the **Software Type** *IOS-XE* from the dropdown.    

   ![json](./images/DNAC-CompositeOS.png?raw=true "Import JSON")

5. Lastly to complete the Add New Template sequence you would click **Add**. As one already exists we can close without saving.    

   ![json](./images/DNAC-CompositeAdd.png?raw=true "Import JSON")

### Step 4 - Sequencing the Composite Template

Within the project is a Composite Template **DNAC Template Lab DayN Composite**. This is the template in which we will create a composite sequence or workflow to call modularized regular templates in order to configure the 9300 switch.

Please note the sequence that we want our templates in will be the following:    

![json](./images/DNAC-CompositeSequence.png?raw=true "Import JSON")

1. Within the **Template Hub** , select the template **DNAC Template Lab DayN Composite** from the right pane and it will open.       

   ![json](./images/DNAC-Composite-Begin.png?raw=true "Import JSON")

2. You will notice that beside all the templates which are able to be used within the composite template a small arrow icon is showing. This denotes that those templates are of the same device type and OS and are available to be dragged into the template.   

   ![json](./images/DNAC-Composite-Symbol.png?raw=true "Import JSON")

3. First Drag the **Access Lists** template from the left into the right pane and release it. It should appear in position 1.   

   ![json](./images/DNAC-Composite-ACL-Add.png?raw=true "Import JSON")

4. Next Drag the following into the right pane in this order:
   1. **AAA**
   2. **System Management**
   3. **Local User Management**
   4. **Stacking**
   5. **VLANs Ports per DF**
   6. **Automatic Uplink Naming**    

      ![json](./images/DNAC-Composite-Remain-Add.png?raw=true "Import JSON")

5. Finally we will reorder the sequence by moving the **AAA** template to position one in the sequence. To do this: 

   1. Hover over the left side of the **AAA** template and you will see a green bar. By clicking and grasping this tool you can drag the template to the appropriate spot in the sequence.   

      ![json](./images/DNAC-Composite-MoveBar.png?raw=true "Import JSON")

   2. With this method please move the **AAA** template to position one as shown.    

      ![json](./images/DNAC-Composite-DragAAA.png?raw=true "Import JSON")

   3. After moving the **AAA** template the sequence will look like this. 

      ![json](./images/DNAC-Composite-Sequence-Finish.png?raw=true "Import JSON")

6. Once the Template is properly sequenced save the template.    

   ![json](./images/DNAC-Composite-Save.png?raw=true "Import JSON")

7. Then commit the template for use.   

   ![json](./images/DNAC-Composite-Commit.png?raw=true "Import JSON")   

   ![json](./images/DNAC-Composite-Apply.png?raw=true "Import JSON")

### Step 5 - Modify Network Profile

Next, we need to assign the DayN Composite Template to a site using the Network Profile. As there is an existing network profile for the site, we must reuse that one for the same device family. **(required)** 

   1. Navigate to Network Profiles by selecting *Design> Network Profiles*.

      ![json](./images/DNAC-NavigateProfile.png?raw=true "Import JSON")

   2. Click the **Edit** link next to the **DNAC Template Lab** switching profile created earlier.  

      ![json](./images/DNAC-ProfileEdit.png?raw=true "Import JSON")
   
   3. Within the Profile Editor, select the **Day-N Template(s)** tab:

      ![json](./images/DNAC-ProfileDayN.png?raw=true "Import JSON")

      1. Select the Composite Template by either searching or choosing **DNAC Template Lab DayN Composite** from the dropdown as shown.

         ![json](./images/DNAC-ProfileSelectComposite.png?raw=true "Import JSON")   

      4. Click **Save** to save the modifications to the Network Profile.

         ![json](./images/DNAC-ProfileSave.png?raw=true "Import JSON")   

Now the Composite Template has been applied to the Network Profile, any changes made to the template would immediately be ready for provisioning to the sites aligned to the profile where the template is deployed. This allows for ongoing changes and modifications to the network infrastructure.

### Step 6 - Provisioning the Device

At this point, Cisco Catalyst Center is set up and ready to provision the new composite template to the device. This next set of sequences will push the various Network Settings, Services, and DayN Templates as part of the composite sequence to the device.

We will now provision the switch using DayN Composite Templates. To do this, do the following:

   1. Within Cisco Catalyst Center Navigate to *Provision>Inventory*.      

      ![json](./images/DNAC-NavigateInventory.png?raw=true "Import JSON")

   2. Put a checkmark next to the device *ACCESS-c9300-1-ASW* to be provisioned.
   3. Click the **Actions>Provision>Provision Device** link and walk through the workflow    

      ![json](./images/DNAC-ProvisionBegin.png?raw=true "Import JSON")

      1. The floor was already selected as part of the claim so click **next**    

         ![json](./images/DNAC-ProvisionSite.png?raw=true "Import JSON")

      2. Select *ACCESS-c9300-1-ASW* on the left and the two tick boxes at the top of the page, then click **next**. If the template had inputs, they would be entered.  

         ![json](./images/DNAC-ProvisionAdvConfig.png?raw=true "Import JSON")

      3. Select the auto populated Serial Number using the dropdown under *Stacking*..

         ![json](./images/DNAC-ProvisionConfigSerial.png?raw=true "Import JSON")

      4. Select the auto populated Product ID from the dropdown under *VLANs Ports Per DF*.

         ![json](./images/DNAC-ProvisionConfigPID.png?raw=true "Import JSON")

      5. Ensure the MDF number *01* is entered under *VLANs Ports Per DF*.

         ![json](./images/DNAC-ProvisionConfigMDF.png?raw=true "Import JSON")

      6. Click anywhere in the white space of the page to accept these settings so a green tick appears and then click **Next**.

         ![json](./images/DNAC-ProvisionConfigReady.png?raw=true "Import JSON")

      7. Check the settings and if you agree accept these settings by clicking  **Deploy**.

         ![json](./images/DNAC-ProvisionDeploy.png?raw=true "Import JSON")

   4. The task will be submitted, and the deployment will run.
   5. After a small amount of time, you will see a success notification. What is essential to understand is that the configuration, while pushed to the device, will resync in Cisco Catalyst Center after the resync timer has elapsed.        
   6. To resync the configuration so that it may be viewed before the normal 25 mins, then perform the following task:
      1. Change the focus to **Inventory**
      2. Select the *ACCESS-c9300-1-ASW* switch and select **Actions>Inventory>Resync Device**

         ![json](./images/DNAC-InventoryResync.png?raw=true "Import JSON")

      3. After the resync has occurred, you may click the device name and then view the configuration by selecting that from the left pane to view the configuration pushed.

         ![json](./images/DNAC-DeviceConfig.png?raw=true "Import JSON")

At this point, we have onboarded a device and successfully pushed configuration via Onboarding and DayN Templates as well as Composite Templates. 

### Step 7 - Provision Discovered Devices

We will now utilize some DayN templates written specifically for the disovered devices, to mimic DayN templating being utilized for brownfield or devices with pre-existing configurations.

...

## Automating Provisioning

While it is possible to click through the claiming and provisioning processes manually, which can be time-consuming, we can handle bulk deployments differently. For Bulk deployments, after the templates are built and assigned to the network profile and a site, we may automate them further by uploading a CSV file to Cisco Catalyst Center via REST API.

# Summary

The next step will be to build Composite Template to include the Day N regular templates created in this lab for the switches to be pushed out to the various devices in the network infrastructure. 

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Continue to Application QoS Lab**](./module4-applicationqos.md)

> [**Return to LAB Menu**](./README.md)
