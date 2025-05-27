# DayN Templates - In Development

![json](../../ASSETS/COMMON/BUILD/underconstruction.png?raw=true "Import JSON")

> [!WARNING]
> The contents of this lab are not ready for public use. Do not use this lab or attempt to use it until this header is removed entirely from the lab.

## Overview

This Module is designed and built to address how to use DayN templates within Cisco Catalyst Center to configure network devices at Day 1 through N. This Lab is designed to be used after first completing the previous modules. 

The purpose of DayN templates is to allow for **ongoing configuration** of features on devices beyond those deployed on the Claiming process. With Cisco Catalyst Center, if devices are not within a fabric, the host onboarding part of the UI will not be available. To that end, templates are an easy way of deploying those types of configuration and much more. Before starting this Lab, please make sure you have finished all the steps in the previous modules.

## General Information

Cisco Catalyst Center can be used for Plug and Play and Day N or Ongoing Templates; customers will start by building out an Onboarding Template that typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates as they can be used to apply ongoing changes and to allow device modifications after initial deployment. This lab section will focus on Day N templates to be built as regular templates within Cisco Catalyst Center.

Another important consideration is that part of a typical configuration would include some lines of code, which are built by the **Design > Network Settings >** application within Cisco Catalyst Center. 

If the Design component is used, you should **NOT** deploy the same feature from cli code in a template to configure the device. It's a decision you have to make upfront, and the benefit is that it avoids many lines in the templates, and allows for a more UI-centric configuration that is easier to maintain. 

As guidance, try to use **Design Settings** for as many configurations as you can, leaving Templates light and nimble for configurations that might change ongoing.

### Greenfield Devices

When dealing with net new devices using the Provisioning process we utilize it is better to utilize composite templates with multiple regular templates within. This allows greater flexibility and a method to always add to the structure for compliance reasons. Additionally, Jinja2 and Velocity Scripting languages may be intermingled, allowing for the reuse of existing scripts.

### Brownfield Devices

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

## Cisco Catalyst Center DayN Template Provisioning

This section will go through the build and provisioning of a **Regular** template via Cisco Catalyst Center to a Catalyst 9k switch. We will deal with **Brownfield** and **Greenfield** scenarios during this module.

### Section 1 - Preparation

We will download and import a template project to include templates for deployment of the Wired Lab environment. Contained in the download will be **Regular** and **Composite** template examples which we will use against both the **Greenfield** and **Brownfield** devices.

#### Step 1 - Import the Day N Templates

We will use the **Template Hub** previously known as the **Template Editor** to write, maintain and test template projects. A Project is a logical folder or grouping of templates. Templates can be imported or exported individually or as a collection in a project. We will be importing a Project into the template editor which will have a combination of **Regular** and **Composite** templates.

**Download**, **Extract** and **import** a set of Day N Templates into the **Template Hub** using the file: <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/TEMPLATES/JINJA2/DAYN/JSON/Titanium_WiredAutoLab_Jinja2_project.json">**⬇︎Titanium_WiredAutoLab_Jinja2_project.json⬇︎**</a></br></br>

1. Navigate to the **Template Hub**  within Cisco Catalyst Center through the menu **`Tools > Template Hub`**.

   ![json](./images/DNAC-NavigateTemplate.png?raw=true "Import JSON")

2. Within the **Template Hub**, hover over the import link and select **Import Project** within the menu.  

   ![json](./images/DNAC-ProjectImportBegins.png?raw=true "Import JSON")

3. Click **Select a file from your computer**, then in the file explorer search for the file as shown in the image `Titanium_WiredAutoLab_Jinja2_project.json`. This project will be the one that has all our templates. Click **Open** to prepare it for uploading.

   ![json](./images/DNAC-ProjectImportSelect.png?raw=true "Import JSON")

4. Click **Import** 

   ![json](./images/DNAC-ProjectImportDayN.png?raw=true "Import JSON")

5. Within the **Template Hub** you will notice a new Project appear, click on the **Project Name** link to display the Projects. Notice the following:
   1. Project - **DCLOUD CATC Template Labs DayN Jinja2** 
   2. Composite Template - **CATC Template Labs DayN Composite Jinja2** 
   3. Regular Template - **c9300-2-Setup-Configuratioh**

   ![json](./images/DNAC-ProjectImported.png?raw=true "New IMage Required")

6. Select the **AAA-Configuration** template and notice it has configuration within it. Some templates are just that, others make use of logical statements, conditional statements, looping structures and variables. You will see the following commands in the template selected.

```J2
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


## Summary

Congratulations you have completed xxx

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Continue to DayN Provisioning Module**](../LAB-3-Advanced-Automation/module5-dayn.md)

> [**Return to Lab Menu**](./README.md)