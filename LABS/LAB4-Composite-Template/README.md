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

### Step 1 - ***Create a Day N Template***
Download and import the project within the ***Template Editor*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB4-Composite-Template/templates/2125templates/DNAC_Template_Lab_DayN_project.json">⬇︎DNAC_Template_Lab_DayN_project.json⬇︎</a> file. If using DNAC prior release to 2.1.2.X then use the previously built project within Lab 3 and build the templates located within the following <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB4-Composite-Template/templates/Platinum_Templates.zip">⬇︎Platinum_Templates.zip⬇︎</a> file located within this lab. 

## General Information
This lab is under development please come back soon. ETA for delivery June 2021.

