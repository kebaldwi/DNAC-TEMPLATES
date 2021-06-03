# DayN Templates - In Development -
## Overview
This Lab is designed to be a part of a series of labs built to address how to use Day N Templates within DNA Center to configure network devices at Day 1 to N. The idea being to allow for ongoing configuration of feaures on devices beyond those deployed buy the normal provisioning process. Witn DNA Center if devices are not within a fabric the hos onboarding part of the UI will not be applicable. To that end templates are an easy way of deploying those types of configuraion and much more. Before starting this lab please make sure you have finished all the steps in labs 1 and 2.

## General Information
As DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates as they can be used to apply ongoing changes and to allow device modifications after initial deployment. This lab section will focus on Day N templates to be built as regular templates within DNA Center.

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used you should **not** deploy the same feature from cli code in a template to configure the device. Its a decision you have to make upfront and avoids a lot of lines in the templates and allows for a more UI centric configuration which is easier to maintain. 

As a guidance try and use **Design Settings** for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing.

## Lab Section 1 - DNA Center Design Preparation
While a more extensive set of settings can be built out for a deployment at this time we will limit the configuration to the minimal necessary to perform this step building off the completed tasks in lab 2.

## Lab Section 2 - DNA Center Day N Template Preparation
You can create Day N Templates within the ***Templating Tool*** within **DNA Center**. Go to the ***Templating Tool*** to complete the next task. Initially, we will keep things pretty simple and deploy one Day N regular template. Once the process has been discussed in detail we will build on this within the next labs. 

### Step 1 - ***Create a Day N Template***
Download and import a simple Day N Template in the Templating tool using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB3-DayN-Template/templates/2125templates/Platinum_AAA_Template.json">⬇︎Platinum_AAA_Template.json⬇︎</a> file. If using DNAC prior release to 2.1.2.X then build the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB3-DayN-Template/templates/Platinum_AAA_Template.txt">⬇︎Platinum_AAA_Template.txt⬇︎</a> located within this lab. 

1. Navigate to the Template Editing Tool with DNA Center through the menu *Tools>Template Editor*.
   ![json](./images/DNAC-NavigateTemplate.png?raw=true "Import JSON")
2. With the template editor left click the ⨁ icon to the right of onboarding templates and click **Create Project** within the menu.  
   ![json](./images/DNAC-TemplateImport.png?raw=true "Import JSON")
3. Name the new project `DNAC Template Lab DayN`. This will be the project we will use to keep all our templates in.   
   ![json](./images/DNAC-TemplateSelection.png?raw=true "Import JSON")
4. Download the file above *Platinum_AAA_Template.json* to be imported into the DNA Center. Once downloaded Extract the file.
   ![json](./images/DNAC-TemplatedSelected.png?raw=true "Import JSON")
5. Hover over the right side of the new project and a small ⚙ gear icon will appear. Select **Import Template(s)** from the menu.   
   ![json](./images/DNAC-TemplatedSelected.png?raw=true "Import JSON")
6. 

The DayN regular template has the minimal AAA configuration to configure the device for AAA connectivity with DNAC. Below is for explanation purposes only. (Please Import the Template JSON above)




#### Note:
If you populate the UI with settings those parameters should **not** be in your templates as they will conflict and the deployment through provisioning will fail. While it is easy to populate these settings it is best to test with a switch to see what configuration is pushed.

## Automating Claiming and Provisioning
While it is possible to click through the claiming and process, for bulk deployments its important to be able to address that as well. With DNAC after the templates are built and assigned to the network profile and assigned to a site they may be referenced and used by uploading a csv file to DNA Center via REST API.

## Summary
The next step will be to build Composite Template to include the Day N regular templates created in this lab for the switches to be pushed out to the various devices in the network infrastructure. 

## Feedback
If you found this set of Labs helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
