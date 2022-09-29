# Wireless Automation 
## Overview
This Lab is designed as a set of standalone labs to help customers with varying challenges in Automating and Orchestrating their wireless network infrastructure. Within the lab, we will use various tools and techniques to Automate various tasks and orchestrate DNA Center.

## General Information
Until this point, we have focused our efforts on the wired space and utilized templates, and REST-API to solve some basic to advanced use cases. In this lab, we will change our focus to deal with the wireless environment and utilize methods to deal with common tasks from a wireless automation point of view. This lab will build upon the foundational knowledge acquired in the previous labs. For this lab, we will concentrate on DNA Center configuration specific to Cisco Wireless and how DNA Center can be automated to perform various functions.

This page will serve as the landing page for this lab section due to the amount of content it will cover and the need to expand on it over time. 

## Lab Preparation
Please set up the lab using the following:

1. [**Lab Preparation**](./preparation.md)

## Lab Modules
The lab will be split into modules to concentrate on specific tasks. Eash is designed to build your knowledge in specific areas and they will call out any dependancies on previous modules. We will cover are the following which you can access via the links below:

1. [**Controller PnP or Discovery**](./module1-pnpdiscovery.md)
2. [**Controller HA**](./module2-controllerha.md)
3. [**WLAN Creation**](./module3-wlans.md)
4. [**AP Provisioning**](./module4-approvisioning.md)
5. [**Application QoS**](./module5-applicationqos.md)
6. [**Model Based Config**](./module6-modelbasedconfig.md)
7. [**Wireless Templates**](./module7-wirelesstemplates.md)

## Preparation
To complete this module, it's best to connect to the dCloud lab environment using your laptop so that you can get accustomed to and begin using the tools. If you cannot install postman, completing all tasks via the workstation in the dCloud environment is possible.

Our screenshots will all be from the jump host but remember you can use your laptop.

If you would like to connect to the dCloud environment, please ensure you install the following.

### Lab Requirements
This lab is designed to be run in Cisco dClouds - Enterprise Network Sandbox Lab. It was developed in version 4, including DNA Center 2.2.3.5 and equipment running at least 17.x versions of code.

#### SJC
[Cisco Enterprise Networks Hardware Sandbox](https://dcloud2-sjc.cisco.com/content/catalogue?search=Enterprise%20Networks%20Hardware%20Sandbox&screenCommand=openFilterScreen)

#### Components
The DCLOUD session includes the following equipment:

Virtual Machines:

    DNA Center 2.2.3.4 or better
    Identity Services Engine (ISE) 3.0 Patch 4 or better (deployed)
    Identity Services Engine (ISE) 3.0 (Not deployed)
    Stealthwatch 7.4.0 or better
    FlowCollector 7.4.0 or better
    Cisco Prime Infrastructure 3.10  or better
    Script Server - Ubuntu 20.04  or better
    Wireless LAN Controller - C9800 running IOS-XE Bengaluru 17.5.1 code or better
    Windows 10 Jump Host 
    Windows Server 2019 - Can be configured to provide identity, DHCP, DNS, etc.
    Windows 10 Clients

Hardware Devices:

    ISR 4451 Router - 17.06.01a IOS-XE Code
    Catalyst 9300 Switch - 17.06.01 IOS-XE Code with Embedded Wireless Controller (EWC) and ThousandEyes Enterprise Agent
    9130AX Access Points
    Silex Controllers (3 Wired NIC's and 1 Wireless NIC)

The lab envionment that is available is depicted here:

![json](./LAB1-PNP-PREP/images/DCLOUD_Topology2.png?raw=true "Import JSON")


### Tools Required
Please utilize the following tools to run the lab effectively and ensure they are installed on your workstation/laptop before attempting the lab.

1. Cisco AnyConnect VPN Client
2. Postman
3. Google Chrome

#### Cisco AnyConnect VPN Client
This software is required to connect your workstation to Cisco dCloud. For an explanation of AnyConnect and how to use it with dCloud, please visit the following URL: 

- <a href="https://dcloud-cms.cisco.com/help/android_anyconnect" target="_blank">dCloud AnyConnect Documentation</a>

If you do not have the AnyConnect client, please visit. 

- <a href="https://dcloud-rtp-anyconnect.cisco.com" target="_blank">⬇︎AnyConnect Download Site⬇︎</a>

#### Postman
Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration so you can create better APIs—faster.

Once Postman has been downloaded to your desktop, it is advisable to set up an account and sign in so that all your changes can be used within any system with the client or a web browser, much in the same way as a chrome or firefox profile work. This additional capability I have found instrumental when working in multiple environments. 

- <a href="https://www.postman.com/downloads/" target="_blank">⬇︎Postman Download⬇︎</a>

##### Postman Documentation
For an understanding of postman, please visit this site:

- <a href="https://learning.postman.com/docs/getting-started/introduction/" target="_blank">Postman Documentation</a>

#### Google Chrome
Google Chrome is the optimal browser of choice when working in the DNA Center UI. 

To download Google Chrome, please visit. 

- <a href="https://www.google.com/chrome/downloads/" target="_blank">⬇︎Chrome Download⬇︎</a>

## Summary
This lab is intended for educational purposes only. Use outside of a lab environment should be done at the operator's risk. Cisco assumes no liability for incorrect usage.

This lab is intended to help drive the adoption of Rest-API and will be added to over time with various use cases. The Public Workspace will also mirror the changes and be kept up to date. We hope this set of labs helps explain how the Rest-API may be used and goes a little further in helping define and document them.

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
