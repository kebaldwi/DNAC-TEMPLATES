# REST API Orchestration with Python - IN DEVELOPMENT

![json](../../ASSETS/underconstruction.png?raw=true "Import JSON")

## Overview

This Lab is designed as a standalone lab to help customers with varying challenges in Automating and Orchestrating their network infrastructure using Python. Within the lab, we will use various tools and techniques to Automate various tasks and orchestrate Catalyst Center. 

## General Information

Until this point, we have used Rest-API for some basic setup tasks in labs 1 and 2, but there are so many situations that can be solved or at least eased using Rest-API in conjunction with Catalyst Center. In this lab, we will use a complete set of REST-API collections which will build upon the foundational knowledge acquired in the previous labs. For this lab, we will concentrate on Catalyst Center configuration and how Catalyst Center can be automated to perform various functions which we have already covered. 

Ultimately we are all striving to completely automate the network infrastructure. The closer we get to full service automation the closer we get to business process orchestration. Continual Implementation Continual Deployment is a goal that some companies aspire to and one which the concepts here can stive towards. 

![json](./images/cicd-pipeline2.png?raw=true "Import JSON")

This lab is meant to mirror the concepts of **[LAB 4 REST-API Orchestration with Postman](../LAB-4-Rest-API-Orchestration/README.md)** so as to build on the existing foundation of knowledge. If you have not done so already please do go through lab four to acquaint yourself with the general concepts.

The lab will utilize a set of python programs shared in the code section of the repository. These programs will also be expanded to keep in line with this lab.

## Lab Modules

The use cases we will cover are the following which you can access via the links below:

1. [**Python Orientation**](./python-0-orientation/01-intro.md)
2. [**Building Hierarchy**](./python-1-hierarchy/01-intro.md)
3. [**Assign Settings and Credentials**](./python-2-settings/01-intro.md)
4. [**Device Discovery**](./python-3-discovery/01-intro.md)
5. [**Template Deployment**](./python-4-templates/01-intro.md)
6. [**Configuration Archive**](./python-5-archive/01-intro.md)
7. [**Retrieving Network Inventory**](./python-6-inventory/01-intro.md)
8. [**Running Show Commands**](./python-7-cmd-run/01-intro.md)
9. [**Python REST API Application**]()

## Preparation

To complete this module, it's best to connect to the DCLOUD lab environment using your laptop so that you can get accustomed to and begin using the tools. If you cannot install postman, completing all tasks via the workstation in the DCLOUD environment is possible.

Our screenshots will all be from the jump host but remember you can use your laptop.

If you would like to connect to the DCLOUD environment, please ensure you install the following.

### Lab Requirements

This lab is designed to be run in Cisco DCLOUD - Enterprise Network Sandbox Lab. It was developed in version 4, including DNA Center 2.2.3.5 and equipment running at least 17.x versions of code.

### Tools Required

Please utilize the following tools to run the lab effectively and ensure they are installed on your workstation/laptop before attempting the lab.

1. Cisco AnyConnect VPN Client
2. Postman
3. Google Chrome

### Cisco AnyConnect VPN Client

This software is required to connect your workstation to Cisco DCLOUD. For an explanation of AnyConnect and how to use it with DCLOUD, please visit the following URL: 

> **Documentation**: For AnyConnect Documentation visit: <a href="https://DCLOUD-cms.cisco.com/help/android_anyconnect" target="_blank">DCLOUD AnyConnect Documentation</a>

> **Download**: Get AnyConnect here: <a href="https://DCLOUD-rtp-anyconnect.cisco.com" target="_blank">⬇︎ AnyConnect Download Site ⬇︎</a>

### Postman

Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration so you can create better APIs—faster.

Once Postman has been downloaded to your desktop, it is advisable to set up an account and sign in so that all your changes can be used within any system with the client or a web browser, much in the same way as a chrome or firefox profile work. This additional capability I have found instrumental when working in multiple environments. 

> **Download**: Get Postman here: <a href="https://www.postman.com/downloads/" target="_blank">⬇︎ Postman Download ⬇︎</a>

> **Documentation**: For an understanding of postman, please visit: <a href="https://learning.postman.com/docs/getting-started/introduction/" target="_blank">Postman Documentation</a>

### Google Chrome

Google Chrome is the optimal browser of choice when working in the DNA Center UI. 

> **Download**: Get Google Chrome here: <a href="https://www.google.com/chrome/downloads/" target="_blank">⬇︎ Chrome Download ⬇︎</a>

## Summary

This lab is intended for educational purposes only. Use outside of a lab environment should be done at the operator's risk. Cisco assumes no liability for incorrect usage.

This lab is intended to help drive the adoption of Rest-API and will be added to over time with various use cases. The Public Workspace will also mirror the changes and be kept up to date. We hope this set of labs helps explain how the Rest-API may be used and goes a little further in helping define and document them.

> **Feedback**: If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Return to LAB Main Menu**](../README.md)
