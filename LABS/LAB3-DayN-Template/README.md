# DayN Templates [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
## Overview
This Lab is designed to be a part of a series of labs built to address how to use Day N Templates within DNA Center to configure network devices at Day 1 to N. The idea being to allow for ongoing configuraion of feaures on devices beyond those deployed buy the normal provisioning process. Witn DNA Center if devices are not within a fabric the hos onboarding part of the UI will not be applicable. To that end templates are an easy way of deploying those types of configuraion and much more. Before starting this lab please make sure you have finished all the steps in labs 1 and 2.

## General Information
As DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates as they can be used to apply ongoing changes and to allow device modifications after initial deployment. This lab section will focus on Day N templates to be built as regular templates within DNA Center.

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used you should not deploy the cli code in a template to configure the device. Its a decision you have to make upfront and avoids a lot of lines in the templates and allows for a more UI centric configuration which is easier to maintain. 

As a guidance try and use Design settings for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing.

## Lab Section 1 - DNA Center Design Preparation
While a more extensive set of settings can be built out for a deployment we will limit the configuration to the minimal necessary to perform this step building off the completed tasks in lab 2. We will now augment the Design Settings during this **DayN Templating Lab** to include others that may be required.

Before DNA Center can automate the deployment we have to do a couple of tasks to prepare. Please log into the DNA Center using a browser within the Windows Jump host and browse to [DNA Center](https://198.18.129.100). Use the credentials of username: ***admin*** password: ***C1sco12345*** within the DCLOUD environment.

We will need to do a couple of tasks first. 

## Lab Section 2 - DNA Center Day N Template Preparation
You can create Day N Templates within the ***Templating Tool*** within **DNA Center**. Go to the ***Templating Tool*** to complete the next task.

### Step 1 - ***Create an Day N Template***
Import an Onboarding Template in the Templating tool using the [JSON](./templates/Platinum_Onboarding_Template.json) file. If using DNAC prior release to 2.1.2.X then build the [Template](./templates/Platinum-Onboarding.txt) located within this lab. 



### Step 2 - ***Edit the Network Profile***
Next we need to assign the Onboarding Template to a site using the Network Profile.

   1. Edit the network profile Under *Design> Network Profiles* you will select **+Edit** 
   
   ![json](../../images/NetworkProfile.png?raw=true "Import JSON")
   
   2. On the Onboarding Template page select device type **(required)**
   
   ![json](../../images/OnboardingDevice.png?raw=true "Import JSON")
   
   3. On the Onboarding Template page select the template(s) to be used for onboarding **(required)**
   
   ![json](../../images/OnboardingTemplate.png?raw=true "Import JSON")
   
   4. Save the network profile
   5. Assign the network profile to the hierarchy
   
   ![json](./images/NetworkProfile-AssignSite.png?raw=true "Import JSON")
   
   9. Select the sites to apply the profile within the hierarchy and click save
   
   ![json](./images/NetworkProfileSelectSite.png?raw=true "Import JSON")

## Lab Section 3 - Claiming and Onboarding
At this point DNAC is set up and ready for Plug and Play to onboard the first device. Provided the discovery and dhcp assignment are aligned, the device should when plugged in find DNA Center and land in the plug n play set of the devices section within the provisioning page.

### Step 1 - ***Claiming the Device***
At this point you can claim the device putting it in a planned state for onboarding onto the system. To do this do the following:

   1. Put a checkmark next to the device to be claimed
   2. Click the **Actions>Claim** link and walk through the workflow
   3. Section 1 select the part of the hierarchy to which the device will be deployed then click **next**
   4. Section 2 you can click the hyperlinks to the right of the workflow page and view or amend the templates and images utilized then click **next**
   5. Section 3 select the device **serial number** on the left and fill in the variables within the template click **next**. Please use the following:
      *   Hostname type `ACCESS-9300-ASW`
      *   Management Vlan enter `5`
      *   IP Address `192.168.5.10`
      *   Subnet Mask `255.255.255.0`
      *   Gateway `192.168.5.1`
      *   VTP Domain `Cisco`   
   6. Section 4 review the elements including configuration to be deployed 
   7. Click **claim** to initiate
   
At this stage the device will be placed in **Planned** state, and will cycle through **Onboarding** and **Provisioned** when complete. After the device is completed it will appear in the device inventory after being sync'd with DNA Center.
   




#### Note:
If you populate the UI with settings those parameters should **not** be in your templates as they will conflict and the deployment through provisioning will fail. While it is easy to populate these settings it is best to test with a switch to see what configuration is pushed.

## Automating Claiming and Provisioning
While it is possible to click through the claiming and process, for bulk deployments its important to be able to address that as well. With DNAC after the templates are built and assigned to the network profile and assigned to a site they may be referenced and used by uploading a csv file to DNA Center via REST API.

## Summary
The next step will be to build Composite Template to include the Day N regular templates created in this lab for the switches to be pushed out to the various devices in the network infrastructure. 

## Feedback
If you found this set of Labs helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
