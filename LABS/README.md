# DNAC-TEMPLATE LABS 
## Overview
This section of the repository is built out in LAB form to guide you through the typical steps required to enable the various automation tasks delivered by DNA Center. This lab will give examples of templates used in DNA Center that can be modified for your use and tested on equipment within the LAB environment. Additional information within the lab provides a well-rounded explanation of Automation methods with Templates. Lastly, the lab allows for customers to use DNA Center workflows to practice deploying Onboarding, DayN Templates, and Application Policy automation on both Wired and Wireless Platforms.

The goal of this lab is for it to be a practical guide to aid engineers to rapidly begin using DNA Center automation and help them work towards a template strategy. Additionally, this lab will give customers a permanent place to try out the templates and include configurations for various use cases. This environment will enable engineers to reduce the time and effort needed to instantiate the network.

As a result, customers will gain experience setting up Plug and Play onboarding and templates. Additionally, they will use advanced velocity templating and troubleshooting tools, which may help during faultfinding to determine what is failing in a deployment.

## Sections
Please use this menu to navigate the various sections of this Github repository. Within the multiple folders are examples, explanation readme files for reference.

* [PnP Preparation](./LAB1-PNP-PREP/README.md#PnP) - This section explains the overall Plug and Play set up steps
* [Onboarding Templates](./LAB2-Onboarding-Template/README.md#Day0) - This section explains in depth and how to deploy Day 0 templates
* [Day N Templates](./LAB3-DayN-Template/README.md#DayN) - This section will dive into Day N template constructs and use cases
* [Composite Templates](./LAB4-Composite-Template/README.md#Composite) - This section will explore how to build a composite template on DNAC
* [Application Policys](./LAB5-Application-Policy/README.md#Application) - This section will explain Application Policys in DNAC and their use
* [Telemetry](./LAB6-Telemetry-Enablement/README.md#Telemetry) - This section will explain how to deploy Telemetry for assurance
* [Advanced Automation](./LAB7-Advanced-Automation/README.md#Advanced) - This section will explore into Advanced Automation examples

## DCLOUD as a LAB
### Overview
This section will explain which lab to utilize within the **DCLOUD** environment to run these labs. It will also discuss a customer POC environment and the steps necessary to successfully run these sections within a customer environment for localized testing.

### DCLOUD Labs
This lab environment has been tested on the following DCLOUD session: [Cisco Enterprise Networks Hardware Sandbox v2.1](https://dcloud2-rtp.cisco.com/content/demo/759521?returnPathTitleKey=favourites-view)

The DCLOUD session includes the following equipment:

Virtual Machines:

    DNA Center 2.1.2.5
    Identity Services Engine (ISE) 3.0 (Not Configured)
    Stealthwatch 7.1
    FlowCollector 7.1
    Cisco Prime Infrastructure 3.9
    Wireless LAN Controller - C9800 running IOS-XE Amsterdam 17.3.3 code.
    Windows 10 Jump Host 
    Windows Server 2019 - Can be configured to provide identity, DHCP, DNS, etc.
    Windows 10 Clients 

Hardware Devices:

    ISR 4451 Router - 17.3.3 IOS-XE Code
    Catalyst 9300 Switch - 17.3.3 IOS-XE Code with Embedded Wireless Controller (EWC) and ThousandEyes Enterprise Agent
    Catalyst 3850 Switch - 16.12.5 IOS-XE Code
    4800 Access Points
    Silex Controller (2 NIC's)

The lab envionment that is available is depicted here:
![json](./LAB1-PNP-PREP/images/DCLOUD_Topology.png?raw=true "Import JSON")

## Disclaimer
Various labs are designed for use in the **DCLOUD** environment but can but are for use elsewhere. What is important to realize is the impact of each type of test. For instance, in the ***PnP Preparation*** lab, we go through discovery methods such as ***option 43*** and ***DNS Discovery***. If we were to use the DHCP option 43 and place that in the server options on the DHCP server, it would affect multiple scopes. **Care** is required, therefore, to ensure you do not get unexpected results. Similarly with ***DNS Discovery***, if the sub domain used was available to all devices, more than one device would discover DNA Center. Changes like this may be suitable for production in the future but detrimental during testing.

If you found this set of Labs helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how we can improve.

