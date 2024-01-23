# DayN Templates

## Overview

This Lab is designed to be a part of a series of labs built to address how to use Day N Templates within DNA Center to configure network devices at Day 1 to N. This Lab is designed to be used after first completing labs A through B. The idea being to allow for ongoing configuration of features on devices beyond those deployed by the normal provisioning process. With DNA Center, if devices are not within a fabric, the host onboarding part of the UI will not be available. To that end, templates are an easy way of deploying those types of configuration and much more. Before starting this Lab, please make sure you have finished all the steps in labs 1 and 2.

## General Information

DNA Center can be used for Plug and Play and Day N or Ongoing Templates; customers will start by building out an Onboarding Template that typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates as they can be used to apply ongoing changes and to allow device modifications after initial deployment. This lab section will focus on Day N templates to be built as regular templates within DNA Center.

Another important consideration is that part of a typical configuration would include some lines of code, which are built by the *Design >Network Settings >* application within DNA Center. If the Design component is used, you should **not** deploy the same feature from cli code in a template to configure the device. It's a decision you have to make upfront, avoids many lines in the templates, and allows for a more UI-centric configuration that is easier to maintain. 

As guidance, try and use **Design Settings** for as many configurations as you can, leaving Templates light and nimble for configurations that might change ongoing.

## Lab Section 1 - DNA Center Design Preparation

While a more extensive set of settings can be built out for deployment, we will limit the configuration to the minimum necessary to perform this step, building off the completed tasks in lab 2.

## Lab Section 2 - DNA Center Day N Template Preparation

You can create Day N Templates within the ***Template Editor*** within **DNA Center**. Go to the ***Template Editor*** to complete the next task. Initially, we will keep things pretty simple and deploy one Day N regular template. Once the process has been discussed in detail, we will build on this within the following labs. 

<details open>
<summary> Click for Details and Sub Tasks</summary>

### Step 1 - ***Create a Day N Template***

Download and import a simple Day N Template in the **Template Editor** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-C-DayN-Template/templates/2125templates/Platinum_AAA_Template.json">⬇︎Platinum_AAA_Template.json⬇︎</a> file. If using DNAC prior release to 2.1.2.X then build the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-C-DayN-Template/templates/Platinum_AAA_Template.txt">⬇︎Platinum_AAA_Template.txt⬇︎</a> located within this lab. 

1. Navigate to the **Template Editor** within DNA Center through the menu *Tools>Template Editor*.

   ![json](./images/DNAC-NavigateTemplate.png?raw=true "Import JSON")

2. Within the **template editor**, left-click the ⨁ icon to the right of onboarding templates and click **Create Project** within the menu.  

   ![json](./images/DNAC-ProjectCreate.png?raw=true "Import JSON")

3. Name the new project `DNAC Template Lab DayN`. This project will be the one we will use to keep all our templates.   

   ![json](./images/DNAC-ProjectAdd.png?raw=true "Import JSON")

4. Download the file above *Platinum_AAA_Template.json* to be imported into the DNA Center. Once downloaded, extract the file.
5. Hover over the right side of the new project, and a small ⚙ gear icon will appear. Select **Import Template(s)** from the menu.   

   ![json](./images/DNAC-TemplateImportBegin.png?raw=true "Import JSON")

6. From the **Import Templates** window, click **Select a file from your computer** from the explorer window, select the extracted JSON file and click open.   

   ![json](./images/DNAC-TemplateSelect.png?raw=true "Import JSON")

7. Click **Import**, and the template will be placed in the project.   

   ![json](./images/DNAC-TemplateImport.png?raw=true "Import JSON")

8. Once the template is in the project, select it to view the configuration.

   ![json](./images/DNAC-TemplateAAA.png?raw=true "Import JSON")

The DayN regular template has the minimal AAA configuration to configure the device for local AAA connectivity independent of ISE to work with DNAC. Below is for explanation purposes only. (Please Import the Template JSON above)

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

### Step 2 - ***Modify Network Profile***

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

</details>

## Lab Section 3 - Provisioning

At this point, DNAC is set up and ready to provision the new regular template AAA to the device. This next set of sequences will push the various Network Settings, Services, and DayN Templates to the device.

<details open>
<summary> Click for Details and Sub Tasks</summary>

### Step 1 - ***Provisioning the Device***

We will now provision the switch using DayN Templates. To do this, do the following:

   1. Within DNA Center Navigate to *Provision>Inventory*.      

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

   5. After a small amount of time, you will see a success notification. What is essential to understand is that the configuration, while pushed to the device, will resync in DNA Center after the resync timer has elapsed.        
   6. To resync the configuration so that it may be viewed before the normal 25 mins, then perform the following task:
      1. Change the focus to **Inventory**
      2. Select the *ACCESS-c9300-1-ASW* switch and select **Actions>Inventory>Resync Device**

         ![json](./images/DNAC-InventoryResync.png?raw=true "Import JSON")

      3. After the resync has occurred, you may click the device name and then view the configuration by selecting that from the left pane to view the configuration pushed.

         ![json](./images/DNAC-DeviceConfig.png?raw=true "Import JSON")

At this point, we have onboarded a device and successfully pushed configuration via Onboarding and DayN Templates. 

> **Note:** If you populate the UI with settings, those parameters should **not** be in your templates as they will conflict, and the deployment through provisioning will fail. While it is easy to populate these settings, it is best to test with a switch to see what configuration is pushed.

</details>

## Automating Claiming and Provisioning

While it is possible to click through the claiming and provisioning processes manually, which can be time-consuming, we can handle bulk deployments differently. For Bulk deployments, after the templates are built and assigned to the network profile and a site, we may automate them further by uploading a CSV file to DNA Center via REST API.

## Summary

The next step will be to build Composite Template to include the Day N regular templates created in this lab for the switches to be pushed out to the various devices in the network infrastructure. 

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Continue to Composite Template Lab**](../LAB-D-Composite-Template/README.md)

> [**Return to LAB Main Menu**](../README.md)
