# Practical Template Examples [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

When working with many customers over the past 6 years with automation, I have seen the same questions asked in workshop after workshop. Are there practical examples of templates that we can use as a starting point to begin deploying with automation.

After working with well over 30 customers, I have come up with templates which fit for the majority of typical access switch situations. 

Within this section we will only deal with the non Fabric environment and deployment.

## Intent Based Networking

Either one or multiple Templates may be used to deploy Intent in combination with the Design Settings and Policies deployed within the UI. One or Multiple templates may be used in Onboarding (PnP) or Day N methods. Day N methods are designed for making ongoing changes and may require 'no' statements depending on the configuration construct being modified. 

Additionally:
1.	Intent can be defined as the set of configuration constructs deployed via a template.
2.	Variables can be used to modify or choose between constructs deployed via decision (‘IF’) statements
3.	Repetition of any construct may be introduced through the use of Looping structures on any device.
4.	Variables may be used when the device is being onboarded or provisioned

## Plug and Play (PnP) Template

### Why

To help get started with and better understand the PnP process we have provided this material. It is designed to help you understand the Plug and Play process, templates and deployment of these within a lab setting. Once you are comfortable with the concepts you can work on a deployment and implementation plan for your network.

### What

To help get started with the PnP process and to better understand the process, please review the following information:

<details open>
<summary> Click for Details and Sub Tasks</summary>

1. [PnP Workflow](./PnP-Workflow.md) - This section explains the overall Plug and Play Methodology
2. [Onboarding](./Onboarding.md) - This section will explain Onboarding Templates in Cisco Catalyst Center and their use
3. [Building Templates](./Templates.md#building-templates) - This section will explain how to build a template on DNAC

</details>

### How

To let you practice and get experience with the PnP process to better understand it. The labs referenced here use templates and projects within those labs, but you may substitute the example below. Please review the following lab information:

<details open>
<summary> Click for Details and Sub Tasks</summary>

1. [PnP Preparation](./LABS/LAB1-PNP-PREP/README.md)
2. [Onboarding Templates](./LABS/LAB2-Onboarding-Template/README.md)

This material is designed to help you understand the Plug and Play process, templates and deployment of these within a lab setting.

</details>

### Where

Within the following location is an example template written in ***Jinja2*** in JSON format which can be imported into the **Onboarding Configuration** section in the Template Editor/Hub:

[⬇︎Full Cisco Catalyst Center PnP Onboarding Template⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/ONBOARDING/DNAC-SAMPLE-TEMPLATES-01302023-PnP-template.json)

### Features

This template includes a number of built in features, which allow for the majority of use cases. We will explore those here in this section.

<details closed>
<summary> Click for Details and Sub Tasks</summary>

Within the form you can see many fields which can be populated with a csv file. These are the typical responses necessary that are different from switch to switch which allow us to template the configuration for repeated use. 

1. The hostname.
2. System MTU is a default setting which if entered changes the configuration. You can have the switch reload to set that setting if you want using an additional EEM script.
3. The typical management VLAN and IP address information for management purposes.
4. The interfaces can be entered comma delimited which allows us to create or not create Etherchannels as necessary. 

![json](../ASSETS/DNAC-SAMPLE-TEMPLATE-PnP-Form.png?raw=true "Import JSON")

Once you have imported the template you can look at the logic.

#### Key Features

1. System MTU set by default, but modifiable via the form
2. VTP Domain set to Hostname, you can change to variable by removing `{% set VtpDomain = Hostname %}`
3. Shuts downn Vlan 1 if not in use
4. Automatically builds Etherchannel if required

```J2
{# <------Onboarding-Template-------> #}
{# To be used for onboarding when using Day N Templates #}
{# Define Variables provision with vlan and port channel #}
!
{# Set MTU if required #}
{% if SystemMTU != 1500 %}
    system mtu {{ SystemMTU }}
{% endif %}
!
{# Set hostname #}
hostname {{ Hostname }}
!
{% set VtpDomain = Hostname %}
!
{# Set VTP and VLAN for onboarding #}
vtp domain {{ VtpDomain }}
vtp mode transparent
!
{# Set Management VLAN #}
vlan {{ MgmtVlan }}
!
{% if MgmtVlan > 1 %}
  name MgmtVlan
  {# Disable Vlan 1 (optional) #}
  interface Vlan 1
   shutdown
{% endif %}
!
{# Set Interfaces and Build Port Channel #}
!{{ Portchannel }}
interface range {{ Interfaces }}
 shut
 switchport mode trunk
 switchport trunk allowed vlan {{ MgmtVlan }}
 {% if "," in Interfaces %}
    channel-protocol lacp
    channel-group {{ Portchannel }} mode active
 {% endif %}
 no shut
!
{% if "," in Interfaces %}
  interface Port-channel {{ Portchannel }}
   switchport trunk native vlan {{ MgmtVlan }}
   switchport trunk allowed vlan {{ MgmtVlan }}
   switchport mode trunk
   no port-channel standalone-disable
{% endif %}
!
{# Set Up Managment Vlan {{ MgmtVlan }} #}
interface Vlan {{ MgmtVlan }}
 description MgmtVlan
 ip address {{ SwitchIP }} {{ SubnetMask }}
 no ip redirects
 no ip proxy-arp
 no shut
!
ip default-gateway {{ Gateway }}
!
{# Set Source of Management Traffic #}
ip domain lookup source-interface Vlan {{ MgmtVlan }}
ip http client source-interface Vlan {{ MgmtVlan }}
ip ftp source-interface Vlan {{ MgmtVlan }}
ip tftp source-interface Vlan {{ MgmtVlan }}
ip ssh source-interface Vlan {{ MgmtVlan }}
ip radius source-interface Vlan {{ MgmtVlan }}
logging source-interface Vlan {{ MgmtVlan }}
snmp-server trap-source Vlan {{ MgmtVlan }}
ntp source Vlan {{ MgmtVlan }}
!
```

</details>

## DayN Template Project

### Why

To help get started with and better understand the DayN process we have provided this material. It is designed to help you understand regular and composite templates and deployment of these within a lab setting. Once you are comfortable with the concepts you can work on a deployment and implementation plan for your network.

### What

To help get started with the PnP process and to better understand the process, please review the following information:

<details open>
<summary> Click for Details and Sub Tasks</summary>

1. [DayN Templates](./DayN.md#day-n-templates-and-flows) - This section will explain how to use templates for ongoing changes to the network
2. [Building Templates](./Templates.md#building-templates) - This section will explain how to build a template on DNAC

</details>

#### Jinja2 Language

Here we concentrate on building **Jinja2** templates, and work with logical concepts.

<details closed>
<summary> Click for Details and Sub Tasks</summary>

##### Jinja2 Templating

1. [Jinja2 Variables](./Variables.md#jinja2-variables) - This section explains Variables in depth and how and where to use them
2. [Jinja2 Scripting](./Jinja2.md#jinja2-scripting) - This section will dive into Velocity Scripting constructs and use cases
3. [Advanced Jinja2 Scripting](./AdvancedJinja2.md#advanced-jinja2) - This section will dive into Advanced Velocity examples

##### Advanced Use Cases

Here we concentrate on advanced uses of templating, and work system variables.

1. [Embedded Event Manager](./EEM.md#EEM) - This section will dive into EEM Scripting and various use cases 
2. [System Variables](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/SystemVariables.md#dna-center-system-variables) - This section explains Cisco Catalyst Centers System Variables

##### Fault-Finding

1. [Troubleshooting](./TroubleShoot.md#Troubleshooting) - This section will dive into Troubleshooting in general terms 

</details>

### How

To let you practice and get experience with the DayN process to better understand it. The labs referenced here use templates and projects within those labs, but you may substitute the example below. Please review the following lab information:

<details open>
<summary> Click for Details and Sub Tasks</summary>

1. [Day N Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-C-DayN-Template/) - The lab covers Day N template constructs and use cases **(allow 0.5 hrs)**
2. [Composite Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-D-Composite-Template/) - This lab covers building a composite template on Cisco Catalyst Center **(allow 0.5 hrs)**
3. [Advanced Automation](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-G-Advanced-Automation/) - This lab will explore Advanced Automation examples **(allow 1.5 hrs)**
4. [Dynamic Automation](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-H-Dynamic-Automation/) - This lab uses Advanced Automation techniques **(allow 2.0 hrs)**

</details>

### Where

This is an example which you may want to test with in the lab in combination with the **PnP Template** offered [here](./ExamplesAndConcepts.md#plug-and-play-pnp-template). Within the following location is an example project written in ***Jinja2*** in JSON format which can be imported into the Template Editor/Hub:

[⬇︎Full Cisco Catalyst Center Sample Project⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/DAYN/DNAC-SAMPLE-TEMPLATES-05312023-project.json)

### Features

This project includes templates with a number of built in features, which allow for the majority of use cases. We will explore those here in this section.

<details closed>
<summary> Click for Details and Sub Tasks</summary>

The package or project includes Jinja2 templates which are rolled into Composite templates to allow for quick deployment of:

1. Simple Access Point and Workstation Deployments.
2. The use or incorporation of AutoConf to Autoconfigure ports based off Device Classification
3. The use of IBNS 2.0 policy to enforce and deploy configuration.

The last of the two above, allow for Dynamic Configuration of networks to allow for networks where devices consistently move but where user and application experience needs to be consistent.

Once you have imported the template you can look at the logic within each modularized regular template. Each of these templates is part of the composites above, and some are referenced using includes where necessary to avoid repeating code.

#### Key Features

1. AAA Configuration for nonPxGrid - *Deployments*
2. ACLs 
3. Autoconf Configuration Options
4. AutoNaming EEM Scripting - *for Interfaces* 
5. DynamicPort EEM Scripting - *for use in changing Auth profiles*
6. IBNS2.0 Configuration
7. Interface Assign Configuration - *for standard interface configurations*
8. Interface Autoconf Configuration - *for dynamic configuration through device classification*
9. Interface IBNS2.0 Configuration - *for policy based interface configuration*
10. Interface Macros - *set of multi-purpose interface macros*
11. Security AAA Modifications - *various security configurations*
12. Sensitive Info - *for securing sensitive information from general configs*
13. Stacking Configuration - *for powerstack and stackwise configuration*
14. System Management - *for global configurations*
15. Vlans Info - *includes examples of how to deploy Vlans using objects*

I hope you find these samples highly useful, and please provide feedback.

</details>

## Summary

These examples are ready for testing in your lab. These are aides to help you get up to speed with what is possible when automating with Cisco Catalyst Center. The intent of this part of the repository is to aide in learning and not provide production ready templates. All templates here are for **LAB Purposes ONLY** and by downloading any content you acknowledge that this is not production ready code.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

Special mention to: https://jinja.palletsprojects.com/en/3.0.x/templates as examples and extrapolations were made using this documentation.

> [**Return to Main Menu**](./README.md)