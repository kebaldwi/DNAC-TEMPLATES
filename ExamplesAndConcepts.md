# Practical Template Examples [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
When working with many customers over the past 6 years with automation, I have seen the same questions asked in workshop after workshop. Are there practical examples of templates that we can use as a starting point to begin deploying with automation.

After working with well over 30 customers, I have come up with templates which fit for the majority of typical access switch situations. 

Within this section we will only deal with the non Fabric environment and deployment.

## Plug and Play (PnP) Template
### Why
To help get started with and better understand the PnP process we have provided this material. It is designed to help you understand the Plug and Play process, templates and deployment of these within a lab setting. Once you are comfortable with the concepts you can work on a deployment and implementation plan for your network.

### What
To help get started with the PnP process and to better understand the process, please review the following information:

1. [PnP Workflow](./PnP-Workflow.md) - This section explains the overall Plug and Play Methodology
2. [Onboarding](./Onboarding.md) - This section will explain Onboarding Templates in DNAC and their use
3. [Building Templates](./Templates.md#building-templates) - This section will explain how to build a template on DNAC

### How
To let you practice and get experience with the PnP process to better understand it, please review the following lab information:

1. [PnP Preparation](./LABS/LAB1-PNP-PREP/README.md)
2. [Onboarding Templates](./LABS/LAB2-Onboarding-Template/README.md)

This material is designed to help you understand the Plug and Play process, templates and deployment of these within a lab setting.

### Where 
Within the following location is an example template written in ***Jinja2*** in JSON format which can be imported into the **Onboarding Configuration** section in the Template Editor/Hub:

[⬇︎Full DNA Center PnP Onboarding Template⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/ONBOARDING/DNAC-SAMPLE-TEMPLATES-01302023-PnP-template.json)

### Features
This template includes a number of built in features, which allow for the majority of use cases. We will explore those here in this section.

examples

## DayN Template Project
### Why
To help get started with and better understand the DayN process we have provided this material. It is designed to help you understand regular and composite templates and deployment of these within a lab setting. Once you are comfortable with the concepts you can work on a deployment and implementation plan for your network.

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

### What
To help get started with the PnP process and to better understand the process, please review the following information:

1. [DayN Templates](./DayN.md#day-n-templates-and-flows) - This section will explain how to use templates for ongoing changes to the network
2. [Building Templates](./Templates.md#building-templates) - This section will explain how to build a template on DNAC

#### Jinja2 Language
Here we concentrate on building **Jinja2** templates, and work with logical concepts.

1. [Jinja2 Variables](./Variables.md#jinja2-variables) - This section explains Variables in depth and how and where to use them
2. [Jinja2 Scripting](./Jinja2.md#jinja2-scripting) - This section will dive into Velocity Scripting constructs and use cases
3. [Advanced Jinja2 Scripting](./AdvancedJinja2.md#advanced-jinja2) - This section will dive into Advanced Velocity examples

#### Advanced Use Cases
Here we concentrate on advanced uses of templating, and work system variables.

* [Embedded Event Manager](./EEM.md#EEM) - This section will dive into EEM Scripting and various use cases 
* [System Variables](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/SystemVariables.md#dna-center-system-variables) - This section explains DNA Centers System Variables

#### Fault-Finding
* [Troubleshooting](./TroubleShoot.md#Troubleshooting) - This section will dive into Troubleshooting in general terms 

### How
To let you practice and get experience with the DayN process to better understand it, please review the following lab information:

1. [Day N Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB3-DayN-Template/) - The lab covers Day N template constructs and use cases **(allow 0.5 hrs)**
2. [Composite Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB4-Composite-Template/) - This lab covers building a composite template on DNA Center **(allow 0.5 hrs)**
3. [Advanced Automation](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB7-Advanced-Automation/) - This lab will explore Advanced Automation examples **(allow 1.5 hrs)**
4. [Dynamic Automation](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB8-Dynamic-Automation/) - This lab uses Advanced Automation techniques **(allow 2.0 hrs)**

### Where
This is an example which you may want to test with in the lab in combination with the **PnP Template** offered [here](). Within the following location is an example project written in ***Jinja2*** in JSON format which can be imported into the Template Editor/Hub:

[⬇︎Full DNA Center Sample Project⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/DAYN/DNAC-SAMPLE-TEMPLATES-01302023-project.json)

### Features



## Summary
These examples are ready for testing in your lab. These are aides to help you get up to speed with what is possible when automating with DNA Center. The intent of this part of the repository is to aide in learning and not provide production ready templates. All templates here are for **LAB Purposes ONLY** and by downloading any content you acknowledge that this is not production ready code.

If you found this repository or any section helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

Special mention to: https://jinja.palletsprojects.com/en/3.0.x/templates as examples and extrapolations were made using this documentation.
