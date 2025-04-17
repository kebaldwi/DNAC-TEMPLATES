# CICD Orchestration 

## Overview

This Lab is designed as a standalone lab to help customers with varying challenges in Automating and Orchestrating their network infrastructure. Within the lab, we will use various tools and techniques to Automate various tasks and orchestrate Cisco Catalyst Center.

## General Information

Until this point, we have used Rest-API for some basic setup tasks, but there are so many situations that can be solved or at least eased using Rest-API in conjunction with Cisco Catalyst Center. In this lab, we will use a complete set of REST-API collections which will build upon the foundational knowledge acquired in the previous labs. For this lab, we will concentrate on Cisco Catalyst Center configuration and how Cisco Catalyst Center can be automated to perform various functions which we have already covered utilizing **Python**, inconjunction with **Jenkins CI/CD Pipelines**

![json](./images/cicd-pipeline2.png?raw=true "Import JSON")

This page will serve as the landing page for this lab section due to the amount of content it will cover and the need to expand on it over time. 

The lab will utilize a set of collections publically shared on Postman workspaces, Python and Ansible librarys, and Jenkins.

**IMPORTANT:** Please note that LAB content in this Repository is aligned with specific DCLOUD Demonstrations that have to be set up by either a **Cisco Employee** or a **Cisco Parter**. If you are having trouble accessing the DCLOUD content please get in touch with your **Local Cisco Account Team**.

## Lab Modules

The use cases we will cover are the following which you can access via the links below:

### Overview

1. [**The Journey to Orchestration**](./cicd-0-orientation/01-intro.md)

### Jenkins Pipelines with Python

2. [**Python Building Hierarchy with Settings**](./cicd-1-hierarchy/01-intro.md)
3. [**Python Device Discovery**](./cicd-2-discovery/01-intro.md)
4. [**Python Template Deployment**](./cicd-3-templates/01-intro.md)
5. [**Python Inventory Collection**](./cicd-4-inventory/01-intro.md)

## Preparation

To complete this module, it's best to connect to the dCloud lab environment using your laptop so that you can get accustomed to and begin using the tools. If you cannot install python and jenkins, completing all tasks via the workstation in the dCloud environment is possible via the script server.

Our screenshots will all be from the jump host but remember you can use your laptop.

If you would like to connect to the dCloud environment, please ensure you install the following.

### Lab Requirements

This lab is designed to be run in Cisco dClouds - Enterprise Network Sandbox Lab. It was developed in version 4, including Cisco Catalyst Center 2.2.3.5 and equipment running at least 17.x versions of code.

### Tools Required

Please utilize the following tools to run the lab effectively and ensure they are installed on your workstation/laptop before attempting the lab.

1. Cisco AnyConnect VPN Client
2. Python and Jenkins installation
3. Visual Studio Code
4. Google Chrome

### Cisco AnyConnect VPN Client

This software is required to connect your workstation to Cisco dCloud. For an explanation of AnyConnect and how to use it with dCloud, please visit the following URL: 

> **Documentation**: For AnyConnect Documentation visit: <a href="https://dcloud-cms.cisco.com/help/android_anyconnect" target="_blank">dCloud AnyConnect Documentation</a>

> **Download**: Get AnyConnect here: <a href="https://dcloud-rtp-anyconnect.cisco.com" target="_blank">⬇︎ AnyConnect Download Site ⬇︎</a>

### Google Chrome

Google Chrome is the optimal browser of choice when working in the Cisco Catalyst Center UI. 

> **Download**: Get Google Chrome here: <a href="https://www.google.com/chrome/downloads/" target="_blank">⬇︎ Chrome Download ⬇︎</a>

## Summary

This lab is intended for educational purposes only. Use outside of a lab environment should be done at the operator's risk. Cisco assumes no liability for incorrect usage.

This lab is intended to help drive the adoption of Rest-API and will be added to over time with various use cases. The Public Workspace will also mirror the changes and be kept up to date. We hope this set of labs helps explain how the Rest-API may be used and goes a little further in helping define and document them.

> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Return to LAB Main Menu**](../README.md)
