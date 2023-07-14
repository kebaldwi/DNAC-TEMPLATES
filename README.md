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

The goal of this repository is a practical guide to allow engineers to rapidly begin using DNAC automation and begin conversion of IOS CLI Templates. The Templates have been developed over the years and with various use cases in mind, and so the intent of sharing this collection is to reduce the lift to begin automating.

## Intent Based Networking

Either one or multiple Templates may be used to deploy Intent in combination with the Design Settings and Policies deployed within the UI. One or Multiple templates may be used in Onboarding (PnP) or Day N methods. Day N methods are designed for making ongoing changes and may require 'no' statements depending on the configuration construct being modified. 

Additionally:

1.	Intent can be defined as the set of configuration constructs deployed via a template.
2.	Variables can be used to modify or choose between constructs deployed via decision (‘IF’) statements
3.	Repetition of any construct may be introduced through the use of Looping structures on any device.
4.	Variables may be used when the device is being onboarded or provisioned

## Tutorial Sections

Various sections will be covered within this github repository. Please use this menu as the main index for navigating content. 
You will find various examples within the various folders of this repository, with supplied explanation readme files for reference.

### Workflows

* [PnP Workflow](./PnP-Workflow.md#pnp-workflow) - This section explains the overall Plug and Play Methodology
* [Onboarding Templates](./Onboarding.md#onboarding-templates-and-flows) - This section will explain Onboarding Templates in DNAC and their use in bringing various devices under DNA Center management
* [DayN Templates](./DayN.md#day-n-templates-and-flows) - This section will explain how to use templates for ongoing (Day-N) changes to the network
### Templating
* [Building Templates](./Templates.md#building-templates) - This section will explain how to build a template on DNAC from scratch
#### Velocity Language
* [Velocity Variables](./Variables.md#velocity-variables) - This section explains Template Variables in depth, and how and where to use them
* [Velocity Scripting](./Velocity.md#velocity-scripting) - This section will dive into Velocity Language Template Scripting constructs and use cases
* [Advanced Velocity Scripting](./AdvancedVelocity.md#advanced-velocity) - This section will dive into Advanced Velocity Language Template examples
#### Jinja2 Language
* [Jinja2 Variables](./Variables.md#jinja2-variables) - This section explains Template Variables in depth, and how and where to use them
* [Jinja2 Scripting](./Jinja2.md#jinja2-scripting) - This section will dive into Jinja2 Language Template Scripting constructs and use cases
* [Advanced Jinja2 Scripting](./AdvancedJinja2.md#advanced-jinja2) - This section will dive into Advanced Jinja2 Language Template examples
### Advanced Use Cases
* [Embedded Event Manager](./EEM.md#EEM) - This section will dive into EEM (Embedded Event Manager) Scripting and various use cases 
* [System Variables](./SystemVariables.md#dna-center-system-variables) - This section explains DNA Centers System Variables

### Fault-Finding

* [Troubleshooting](./TroubleShoot.md#Troubleshooting) - This section will dive into Troubleshooting Velocity based Template Constructs

## [Practical Template Examples](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/ExamplesAndConcepts.md)

In this section I have compiled a number of template examples built with Jinja2 Language. These samples include a wide ranging set of configurations which may be used in your labs to solve specific configuration requirements. This collection summarizes aspects covered previously in this templating repository, and are aimed at providing quick practical references to help engineers solve automation tasks with the help of DNA Center. Additionally these examples may be used in testing in [dCloud](https://dcloud.cisco.com) with any of the labs on this repository.

* [Practical Template Examples](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/ExamplesAndConcepts.md)

## [DNAC Template LABS](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS#dnac-template-labs-)

This section built out in a lab format to guide you through the typical steps to complete various automation tasks delivered by DNA Center. It allows for customers to practice DNA Center workflows with Onboarding, DayN Templates, and Application Policy automation on both Wired and Wireless Platforms, while reducing the time and effort needed to instantiate the network The lab will also introduce advanced velocity templating topics and troubleshooting tools, which may help determine common failure scenarios in a deployment.

* [PnP Preparation](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-A-PNP-PREP/) - The lab covers setup for Plug and Play **(allow 1.5 hrs)**
* [Onboarding Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-B-Onboarding-Template/) - The lab covers in depth topics in deploying Day 0 templates **(allow 1.5 hrs)**
* [Day N Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-C-DayN-Template/) - The lab covers Day N template constructs and use cases **(allow 0.5 hrs)**
* [Composite Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-D-Composite-Template/) - This lab covers building a composite template on DNA Center **(allow 0.5 hrs)**
* [Application Policys](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-E-Application-Policy/) - This lab covers Application Policy & SDAVC in DNAC **(allow 1.0 hrs)**
* [Telemetry](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-F-Telemetry-Enablement/) - This lab explains how to deploy Streaming Telemetry for DNA Center Assurance **(allow 0.5 hrs)**
* [Advanced Automation](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-G-Advanced-Automation/) - This lab will explore Advanced Automation examples **(allow 1.5 hrs)**
* [Dynamic Automation](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-H-Dynamic-Automation/) - This lab will explore additional Advanced Automation examples **(allow 2.0 hrs)**
* [Rest-API Orchestration](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-I-Rest-API-Orchestration/) - This lab uses [Postman](https://www.postman.com) Collections to automate DNA Center **(allow 2.0 hrs)**

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

As a quick start with DNA Center Automation, you may utilize the above labs in conjuction with DCLOUD's sandbox [Cisco Enterprise Networks Hardware Sandbox](https://dcloud2-sjc.cisco.com/content/catalogue?search=Enterprise%20Networks%20Hardware%20Sandbox&screenCommand=openFilterScreen) Lab. This allows you to run these labs and gives not only an environment to try the various code samples, but also to develop and export your own code for use in your production environment. DCLOUD  provides for rapid and safe POC/POV on-demand environment without impacting production environments. DCLOUD also negates the need for shipping equipment, associated lead times, and licensing issues associated with setting up your own private testing environment. Please do adhere to the best practices for the DCLOUD environment when using it.

DCLOUD allows for use with a web-based browser client for VPN-less connectivity, as well as AnyConnect VPN client connectivity for those who prefer it. The labs are hosted in Cisco San Jose Facility (Select US West Region when scheduling in DCLOUD). Choose the Cisco Enterprise Network Sandbox version you prefer. To access this or any other content, including demonstrations, labs, and training in Cloud please work with your Cisco Account team or Cisco Partner Account Team directly. Your Account teams will make sure the session is scheduled and shared for you to use. Once booked follow the guide within Github to complete the tasks adhering to the best practices of the dCLOUD environment.

## Examples

These examples must be used with two conditions:
* Deployed a PnP Discovery method and DHCP scope - see [PnP Workflow](./PnP-Workflow.md#pnp-workflow)
* Build the template with methods detailed - see [Creating Templates](./Templates.md#template-creation)

Specific examples of Templates are available in the following folders:
* [PnP Onboarding](./ONBOARDING) - Examples of PnP/ZTP Templates explained in [Onboarding Templates](./Onboarding.md#onboarding-templates-and-flows)
* [DayN](./DAYN) - Examples of DayN Templates explained in [DayN Templates](./DayN.md#day-n-templates-and-flows)

If you found this repository please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

