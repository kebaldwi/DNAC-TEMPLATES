# DNAC-TEMPLATES [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
## Overview
This Repository will give examples of templates used in DNA Center that can be modified. Additional information will be included to hopefully give a well rounded explanation of Automation methods with Templates using DNA Center and flows with both Onboarding and DayN Templates and concepts.

The repository will include scripts and examples with the following:
1. Velocity Scripting
2. Variables
3. Binding Variables
4. Composite Templates

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

* [PnP Workflow](./PnP-Workflow.md#pnp-workflow) - This section explains the overall Plug and Play Methodology
* [Variables](./Variables.md#variables) - This section explains Variables in depth and how and where to use them
* [Velocity Scripting](./Velocity.md#velocity-scripting) - This section will dive into Velocity Scripting constructs and use cases
* [Building Templates](./Templates.md#building-templates) - This section will explain how to build a template on DNAC
* [Onboarding Templates](./Onboarding.md#onboarding-templates-and-flows) - This section will explain Onboarding Templates in DNAC and their use
* [DayN Templates](./DayN.md#day-n-templates-and-flows) - This section will explain how to use templates for ongoing changes to the network
* [Advanced Velocity](./AdvancedVelocity.md#advanced-velocity) - This section will dive into Advanced Velocity examples
* [Troubleshooting](./TroubleShoot.md#Troubleshooting) - This section will dive into Troubleshooting Velocity 

## DNAC Template LABS **now available**
This section is built out in LAB form to guide you through the typical steps required to enable the various automation tasks delivered by DNA Center. This lab will give examples of templates used in DNA Center that can be modified for your use and tested on equipment within the LAB environment. Additional information within the lab provides a well-rounded explanation of Automation methods with Templates. Lastly, the lab allows for customers to use DNA Center workflows to practice deploying Onboarding, DayN Templates, and Application Policy automation on both Wired and Wireless Platforms.

The goal of this lab is for it to be a practical guide to aid engineers to rapidly begin using DNA Center automation and help them work towards a template strategy. Additionally, this lab will give customers a permanent place to try out the templates and include configurations for various use cases. This environment will enable engineers to reduce the time and effort needed to instantiate the network.

As a result, customers will gain experience setting up Plug and Play onboarding and templates. Additionally, they will use advanced velocity templating and troubleshooting tools, which may help during faultfinding to determine what is failing in a deployment.

Please use this menu to navigate the various sections of this Github repository. Within the multiple folders are examples, explanation readme files for reference.

* [PnP Preparation](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB1-PNP-PREP/) - This section explains the overall Plug and Play set up steps
* [Onboarding Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB2-Onboarding-Template/) - This section explains in depth and how to deploy Day 0 templates
* [Day N Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB3-DayN-Template/) - This section will dive into Day N template constructs and use cases
* [Composite Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB4-Composite-Template/) - This section will explore how to build a composite template on DNAC
* [Application Policys](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB5-Application-Policy/) - This section will explain Application Policys in DNAC and their use
* [Telemetry](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB6-Telemetry-Enablement/) - This section will explain how to deploy Telemetry for assurance
* [Advanced Automation](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB7-Advanced-Automation/) - This section will explore into Advanced Automation examples

## DCLOUD as a LAB
### Overview
To help aid customers toward success with DNA Center Automation, You may utilize the above labs as they have been designed to work within DCLOUD's  [Cisco Enterprise Networks Hardware Sandbox v2.1](https://dcloud2-rtp.cisco.com/content/demo/759521?returnPathTitleKey=favourites-view) Lab. This allows you to run these labs and gives not only an environment to try the various code, but to develop and export your own code for use in production. This give the customer an environment where they can safely POC/POV methods and steps without harming their own production environments. This also negaes the need for shipping equipment, lead times, and licensing issues needed to get moving rapidly. Please do adhere to the best practices for the DCLOUD environment when using it.

## Examples
These examples must be used with two conditions:
* Deployed a PnP Discovery method and DHCP scope - see [PnP Workflow](./PnP-Workflow.md#pnp-workflow)
* Build the template with methods detailed - see [Creating Templates](./Templates.md#template-creation)

Specific examples of Templates are available in the following folders:
* [PnP Onboarding](./ONBOARDING) - Examples of PnP/ZTP Templates explained in [Onboarding Templates](./Onboarding.md#onboarding-templates-and-flows)
* [DayN](./DAYN) - Examples of DayN Templates explained in [DayN Templates](./DayN.md#day-n-templates-and-flows)

If you found this repository or any section helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

[![Analytics](https://ga-beacon.appspot.com/G-9N2KP80W06/DNAC-TEMPLATES/README.MD)](https://github.com/igrigorik/ga-beacon)
