# DNAC-TEMPLATES [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
## Overview
This Repository will give examples of templates used in DNA Center that can be modified. Additional information will be included to hopefully give a well rounded explanation of Automation methods with Templates using DNA Center and flows with both Onboarding and DayN Templates and concepts.

The repository will include scripts and examples with the following:
1. Template Scripting in both
   - Velocity Language
   - Jinja2 Language
2. Variables in both
   - Velocity Language
   - Jinja2 Language
3. Binding Variables
4. System Variables
5. Regular Templates
6. Composite Templates

The goal of this repository is a practical guide to allow engineers to rapidly begin using DNAC automation and begin conversion of IOS CLI Templates. The Templates they may have been using over the years and with various use cases and so the intent is to reduce the lift to begin automating.

## Intent Based Networking
Either one or multiple Templates may be used to deploy Intent in combination with the Design Settings and Policies deployed within the UI. One or Multiple templates may be used in Onboarding (PnP) or Day N methods. Day N methods are designed for making ongoing changes and may require 'no' statements depending on the configuration construct being modified. 

Additionally:
1.	Intent can be defined as the set of configuration constructs deployed via a template.
2.	Variables can be used to modify or choose between constructs deployed via decision (‘IF’) statements
3.	Repetition of any construct may be introduced through the use of Looping structures on any device.
4.	Variables may be used when the device is being onboarded or provisioned

## Tutorial Sections
Various sections will be covered within this github repository please use this menu for navigation. Within the various folders are examples, explanation readme files for reference.

### Workflows
* [PnP Workflow](./PnP-Workflow.md#pnp-workflow) - This section explains the overall Plug and Play Methodology
* [Onboarding Templates](./Onboarding.md#onboarding-templates-and-flows) - This section will explain Onboarding Templates in DNAC and their use
* [DayN Templates](./DayN.md#day-n-templates-and-flows) - This section will explain how to use templates for ongoing changes to the network
### Templating
* [Building Templates](./Templates.md#building-templates) - This section will explain how to build a template on DNAC
#### Velocity Language
* [Velocity Variables](./Variables.md#velocity-variables) - This section explains Variables in depth and how and where to use them
* [Velocity Scripting](./Velocity.md#velocity-scripting) - This section will dive into Velocity Scripting constructs and use cases
* [Advanced Velocity Scripting](./AdvancedVelocity.md#advanced-velocity) - This section will dive into Advanced Velocity examples
#### Jinja2 Language
* [Jinja2 Variables](./Variables.md#jinja2) - This section explains Variables in depth and how and where to use them
* [Jinja2 Scripting](./jinja2.md#jinja2-scripting) - This section will dive into Velocity Scripting constructs and use cases
* [Advanced Jinja2 Scripting](./AdvancedJinja2.md#advanced-jinja2) - This section will dive into Advanced Velocity examples
### Advanced Use Cases
* [Embedded Event Manager](./EEM.md#EEM) - This section will dive into EEM Scripting and various use cases 
### Fault-Finding
* [Troubleshooting](./TroubleShoot.md#Troubleshooting) - This section will dive into Troubleshooting Velocity 

## [DNAC Template LABS](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS#dnac-template-labs-)
This section is built out in LAB form to guide you through the typical steps required to enable the various automation tasks delivered by DNA Center. This lab will give examples of templates used in DNA Center that can be modified for your use and tested on equipment within the LAB environment. Additional information within the lab provides a well-rounded explanation of Automation methods with Templates. Lastly, the lab allows for customers to use DNA Center workflows to practice deploying Onboarding, DayN Templates, and Application Policy automation on both Wired and Wireless Platforms.

The goal of this lab is for it to be a practical guide to aid engineers to rapidly begin using DNA Center automation and help them work towards a template strategy. Additionally, this lab will give customers a permanent place to try out the templates and include configurations for various use cases. This environment will enable engineers to reduce the time and effort needed to instantiate the network.

As a result, customers will gain experience setting up Plug and Play onboarding and templates. Additionally, they will use advanced velocity templating and troubleshooting tools, which may help during faultfinding to determine what is failing in a deployment.

Please use this menu to navigate the various sections of this Github repository. Within the multiple folders are examples, explanation readme files for reference.

* [PnP Preparation](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB1-PNP-PREP/) - The lab covers setup for Plug and Play **(allow 1.5 hrs)**
* [Onboarding Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB2-Onboarding-Template/) - The lab covers in depth how to deploy Day 0 templates **(allow 1.5 hrs)**
* [Day N Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB3-DayN-Template/) - The lab covers Day N template constructs and use cases **(allow 0.5 hrs)**
* [Composite Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB4-Composite-Template/) - This lab covers building a composite template on DNA Center **(allow 0.5 hrs)**
* [Application Policys](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB5-Application-Policy/) - This lab covers Application Policys & SDAVC in DNAC **(allow 1.0 hrs)**
* [Telemetry](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB6-Telemetry-Enablement/) - This lab explains how to deploy Telemetry for assurance **(allow 0.5 hrs)**
* [Advanced Automation](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB7-Advanced-Automation/) - This lab will explore Advanced Automation examples **(allow 1.5 hrs)**
* [Dynamic Automation](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB8-Dynamic-Automation/) - This lab uses Advanced Automation techniques **(allow 2.0 hrs)**
* [Rest-API Orchestration](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB9-Rest-API-Orchestration/) - This lab uses Postman Collections to automate DNA Center **(allow 2.0 hrs)**

## [DNAC Templates Store](https://github.com/kebaldwi/DNAC-Templates-Store)
This repository is built out to share DNA Center Templates and allow for ongoing submissions from those inclined to share their work with the community. Initially the repository includes all the examples that we have used in this repository in RAW TEXT and JSON format. After your first submission you will be able to continually add your templates as you develop new and interesting approaches to device management. 

Please maintain the directory structure with submissions. If you have a suggestion please reach out and contact me.

Please use this menu to navigate the various sections of this separate [DNAC Templates Store](https://github.com/kebaldwi/DNAC-Templates-Store) Github repository. Within the multiple folders are examples, explanation readme files for reference.

* [RAW TEXT Examples](https://github.com/kebaldwi/DNAC-Templates-Store/tree/main/RAW-TEXT-EXAMPLES) - Templates in raw text for editing
* [DAY ZERO JSON](https://github.com/kebaldwi/DNAC-Templates-Store/tree/main/DAY-ZERO-JSON) - JSON files for easy import to DNA Center for Day Zero
* [DAY N JSON](https://github.com/kebaldwi/DNAC-Templates-Store/tree/main/DAY-N-JSON) - JSON files for easy import to DNA Center for Day N
* [REGULAR JSON](https://github.com/kebaldwi/DNAC-Templates-Store/tree/main/DAY-N-JSON/REGULAR-JSON) - JSON files for easy import to DNA Center for Day N
* [COMPOSITE JSON](https://github.com/kebaldwi/DNAC-Templates-Store/tree/main/DAY-N-JSON/COMPOSITE-JSON) - JSON files for easy import to DNA Center for Day N

## DCLOUD as a LAB
### Overview
To help aid customers toward success with DNA Center Automation, You may utilize the above labs as they have been designed to work within DCLOUD's [Cisco Enterprise Networks Hardware Sandbox](https://dcloud2-sjc.cisco.com/content/catalogue?search=Enterprise%20Networks%20Hardware%20Sandbox&screenCommand=openFilterScreen) Lab. This allows you to run these labs and gives not only an environment to try the various code, but to develop and export your own code for use in production. This give the customer an environment where they can safely POC/POV methods and steps without harming their own production environments. This also negaes the need for shipping equipment, lead times, and licensing issues needed to get moving rapidly. Please do adhere to the best practices for the DCLOUD environment when using it.

The environment allows for use with a web-based browser client for VPN-less connectivity, access as well as AnyConnect VPN client connectivity for those who prefer it. The labs are hosted out of our San Jose Facility and so you would choose sessions from US West. Choose the Cisco Enterprise Network Sandbox version you prefer. To access this or any other content, including demonstrations, labs, and training in Cloud please work with your Cisco Account team or Cisco Partner Account Team directly. Your Account teams will make sure the session is scheduled and shared for you to use. Once booked follow the guide within Github to complete the tasks adhering to the best practices of the dCLOUD environment.

## Examples
These examples must be used with two conditions:
* Deployed a PnP Discovery method and DHCP scope - see [PnP Workflow](./PnP-Workflow.md#pnp-workflow)
* Build the template with methods detailed - see [Creating Templates](./Templates.md#template-creation)

Specific examples of Templates are available in the following folders:
* [PnP Onboarding](./ONBOARDING) - Examples of PnP/ZTP Templates explained in [Onboarding Templates](./Onboarding.md#onboarding-templates-and-flows)
* [DayN](./DAYN) - Examples of DayN Templates explained in [DayN Templates](./DayN.md#day-n-templates-and-flows)

If you found this repository or any section helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

