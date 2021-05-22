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






#### Note:
If you populate the UI with settings those parameters should **not** be in your templates as they will conflict and the deployment through provisioning will fail. While it is easy to populate these settings it is best to test with a switch to see what configuration is pushed.

## Automating Claiming and Provisioning
While it is possible to click through the claiming and process, for bulk deployments its important to be able to address that as well. With DNAC after the templates are built and assigned to the network profile and assigned to a site they may be referenced and used by uploading a csv file to DNA Center via REST API.

## Summary
The next step will be to build Composite Template to include the Day N regular templates created in this lab for the switches to be pushed out to the various devices in the network infrastructure. 

## Feedback
If you found this set of Labs helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
