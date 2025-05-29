# Catalyst Center Advanced REST API with Postman 

## Overview

This Lab is designed as a standalone lab to help customers with varying challenges in Automating and Orchestrating their network infrastructure. Within the lab, we will use various tools and techniques to Automate various tasks and orchestrate DNA Center. This lab used in DEVWKS-2004 at Cisco Live.

## General Information

Until this point, we have used Rest-API for some basic setup tasks, but there are so many situations that can be solved or at least eased using Rest-API in conjunction with DNA Center. In this lab, we will use a complete set of REST-API collections which will build upon the foundational knowledge acquired in the previous labs. For this lab, we will concentrate on DNA Center configuration and how DNA Center can be automated to perform various functions which we have already covered. 

This page will serve as the landing page for this lab section due to the amount of content it will cover and the need to expand on it over time. 

The lab will utilize a set of collections publically shared on postman workspaces and those collections will also be expanded to keep in line with this lab.

## Lab Modules

The use cases we will cover are the following which you can access via the links below:

1. [**Postman Orientation**](./dnac-0-orientation/01-intro.md)
2. [**Building Hierarchy**](./dnac-1-hierarchy/01-intro.md)
3. [**Assign Settings and Credentials**](./dnac-2-settings/01-intro.md)
4. [**Device Discovery**](./dnac-3-discovery/01-intro.md)
5. [**Template Deployment**](./dnac-4-templates/01-intro.md)
6. [**Configuration Archive**](./dnac-5-archive/01-intro.md)
7. [**Retrieving Network Inventory**](./dnac-6-inventory/01-intro.md)
8. [**Running Show Commands**](./dnac-7-cmd-run/01-intro.md)
9. [**Python REST API Application**](./dnac-8-pythonapp/01-intro.md)
10. [**Ansible Orchestration**](./dnac-9-ansible/01-intro.md)

## Preparation

To complete this module, it's best to connect to the dCloud lab environment using your laptop so that you can get accustomed to and begin using the tools. If you cannot install postman, completing all tasks via the workstation in the dCloud environment is possible.

Our screenshots will all be from the jump host but remember you can use your laptop.

If you would like to connect to the dCloud environment, please ensure you install the following.

### Lab Requirements

This lab is designed to be run in Cisco dClouds - Enterprise Network Sandbox Lab. It was developed in version 4, including DNA Center 2.2.3.5 and equipment running at least 17.x versions of code.

### Tools Required

Please utilize the following tools to run the lab effectively and ensure they are installed on your workstation/laptop before attempting the lab.

1. Cisco AnyConnect VPN Client
2. Postman
3. Google Chrome

### Cisco AnyConnect VPN Client

This software is required to connect your workstation to Cisco dCloud. For an explanation of AnyConnect and how to use it with dCloud, please visit the following URL: 

> **Documentation**: For AnyConnect Documentation visit: <a href="https://dcloud-cms.cisco.com/help/android_anyconnect" target="_blank">dCloud AnyConnect Documentation</a>

> **Download**: Get AnyConnect here: <a href="https://dcloud-rtp-anyconnect.cisco.com" target="_blank">⬇︎ AnyConnect Download Site ⬇︎</a>

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

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Return to LAB Main Menu**](../README.md)
