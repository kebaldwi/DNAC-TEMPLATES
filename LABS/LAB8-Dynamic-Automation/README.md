# Dynamic Automation - Under Development
## Overview
This Lab is designed to be used after first completing labs 1 and 2 and has been created to address how to combine and use **IBNS 2.0** using **closed mode** and multiple Regular Templates within DNA Center to onboard network devices at Day 1 through N. This allows Network Administrators the ability to configure network devices in an ongoing and programmatic manner from within DNA Center without using the SD-Access Fabric methodology. It also enables an administrator to drag Regular Templates into and out of the flow as needed for ongoing maintenance.

This section will go through the flow involved in creating a deployable Composite Template from an IOS configuration script for a Catalyst switch linking it to a Switch profile, and deploying it through DNAC using provisioning workflows.

## General Information
As previously discussed, DNA Center can be used for Plug-and-Play and Day N or Ongoing Templates. Customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates and, for more flexibility Composite Templates. They can apply ongoing changes and allow device modifications after initial deployment. This lab section will focus on Day N templates built as regular templates within the DNA Center.

Another important consideration is that part of a typical configuration would include some lines of code, which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used, you should **not** deploy the same feature from cli code in a template to configure the device. It's a decision you have to make upfront, avoids a lot of lines in the templates, and allows for a more UI-centric configuration that is easier to maintain. 

As guidance, try and use **Design Settings** for as many of the configurations as you can, leaving Templates light and nimble for configurations that might change ongoing.

## Autoconf & IBNS 2.0 Secure Access
Previously within the Composite Templating Lab and in the previous section, we introduced a methodology of automatically configuring the interfaces within the switch. This configuration relies on a few variables used to extrapolate the settings that were then configured via the template. This allowed a set of macros to be utilized to build out the various settings for VLANs, Ports, and Uplinks. 

While these were methodologies that dealt programmatically with port configuration, and while you may adapt them for an environment, they are both lacking in the fact that they are not dynamic enough. Again, it's impossible to determine without looking at the configuration where something is plugged in. Secondly, if equipment or users are plugged into the wrong interface, they may get the wrong level of access. 

In previous code revisions, we could deal with some of the problems with Auto Smart Port technology, but that has been deprecated, and its replacement is a lot more dynamic. This section will deal with the first part of the problem concerning assigning ports for hardware like Access Points.

**Autoconf** is a solution that can be used to manage port configurations for data or voice VLAN, quality of service (QoS) parameters, storm control, and MAC-based port security on end devices that are deployed in the access layer of a network. Device classification is enabled when you enable the **Autoconf** feature using the `autoconf enable` command in global configuration mode. The onboard device classifier acts as an event trigger, which applies the appropriate automatic template to the interface. The default Autoconf service policy is applied to all the interfaces when the Autoconf feature is enabled using the `autoconf enable` command. For more information about **[Autoconf](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9400/software/release/16-12/configuration_guide/nmgmt/b_1612_nmgmt_9400_cg/configuring_autoconf.pdf)** or alternatively **[Autoconf Documentation](./configuring_autoconf.pdf)**

While **Autoconf** is a tremendous step forward for **non closed mode** ports, it will not function where **closed mode** has been applied at the moment. We need a way to *bridge* the gap so that we can dynamically assign a **low impact mode** configuration should the need arise. Luckily, we can use **EEM Event Manager** to solve the problem.

Luckily we can create a fully dynamic environment with a gated procedure. We include EEM scripts to give that Dynamic look and feel in this Lab entirely. Typically, the types of devices where we might have issues like this where *MAB* or *EAP* are not going to work fast enough, maybe those which identify themselves in another way. In those instances, we can use **PoE** power events to trigger an EEM. Likewise, on a port down event, we can revert the configuration. Those aspects are built into this Lab.

## Lab Section 1 - DNA Center Design Preparation
While we could deploy more extensive settings for deployment, we will limit the configuration to the minimum necessary to perform this step, building off the completed tasks in labs one, [PnP Preparation](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB1-PNP-PREP/) and two, [Onboarding Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB2-Onboarding-Template/).

Should you desire to deploy rapidly and build the lab faster then use the following approach:

### Step 1 - ***Import Postman Collection with Environment***
Download and import the collection within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB8-Dynamic-Automation/postman/DCLOUD_DNACTemplatesLab_Workflow.postman_collection.json">⬇︎DCLOUD_DNACTemplateLab_Workflow.postman_collection.json⬇︎</a> file.

Import the collection into postman.
![json](./images/underconstruction.png?raw=true "Import JSON")

Download and import the environment within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB8-Dynamic-Automation/postman/DCLOUD_DNACTemplateLabs.postman_environment.json">⬇︎DCLOUD_DNACTemplateLabs.postman_environment.json⬇︎</a> file.

Import the environment into postman
![json](./images/underconstruction.png?raw=true "Import JSON")

Turn off SSL in the settings of Postman
![json](./images/underconstruction.png?raw=true "Import JSON")

This collection is built with a flow and delay timers wait for the collection to finish entirely.
![json](./images/underconstruction.png?raw=true "Import JSON")

### Step 2 - ***Import Project with Templates***
Download and import the project within the ***Template Editor*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB8-Dynamic-Automation/templates/DCLOUD-DNACTemplates-Dynamic-IBN-Autoconf-Project.json">⬇︎DCLOUD_DNACTemplate_Dynamic_project.json⬇︎</a> file.


## Lab Section 2 - DNA Center Dynamic Composite Template Preparation
We will load a specific project now which encompasses the elements discussed in lab seven. The project will include many regular templates which are deployed as part of a Day N Composite Template. Go to the ***Template Editor*** to complete the next set of tasks. As we discussed in lab four the ***Template Editor*** allows for the import and export of templates and projects within **DNA Center** along with the ability to clone them.

### Step 1 - ***Import Project with Templates***
Download and import the project within the ***Template Editor*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB8-Dynamic-Automation/templates/DCLOUD-DNACTemplates-Dynamic-IBN-Autoconf-Project.json">⬇︎DCLOUD_DNACTemplate_Dynamic_project.json⬇︎</a> file.

Please un-zip the file and import the *json* file which will automatically create a project and included templates within. Use the following steps to import the project.

1. Navigate to the **Template Editor** within DNA Center through the menu *Tools>Template Editor*.
   ![json](./images/DNAC-NavigateTemplate.png?raw=true "Import JSON")
2. Within the **template editor**, left-click the ⨁ icon to the right of find template and click **Import Project(s)** within the menu.  
   ![json](./images/DNAC-ProjectImportBegin.png?raw=true "Import JSON")
3. Download the file above *DNAC_Template_Lab_DayN_project.json* to be imported into the DNA Center. Once downloaded, extract the file.
4. From the **Import Project(s)** window, click **Select a file from your computer** from the explorer window, select the extracted JSON file and click open. 
   ![json](./images/DNAC-ProjectSelect.png?raw=true "Import JSON")
5. Click **Import**, and the project and all the templates within it will be imported.   
   ![json](./images/DNAC-ProjectImport.png?raw=true "Import JSON")
6. Once the project is imported, select it to view each of the template files within it.
   ![json](./images/DNAC-ProjectFiles.png?raw=true "Import JSON")

Take a few moments and examine the construction of these templates, as each has a specific form and function. Their design is modular to allow reuse of them within other composite templates for other switches or routers. 

The project we imported contains the following templates:
1. **AAA** for local AAA services
   ![json](./images/DNAC-Project-AAA-Template.png?raw=true "Import JSON")
2. **System Management** for global system settings
   ![json](./images/DNAC-Project-SysMgmt-Template.png?raw=true "Import JSON")
3. **VLANs Ports per DF** to add VLAN and port configuration
   ![json](./images/DNAC-Project-PortAssign-Template.png?raw=true "Import JSON")
4. **Local User Management** for additional user accounts
   ![json](./images/DNAC-Project-USR-Template.png?raw=true "Import JSON")
5. **Stacking** to set up powerstack and stack priority
   ![json](./images/DNAC-Project-Stacking-Template.png?raw=true "Import JSON")
6. **Access Lists** to restrict management access
   ![json](./images/DNAC-Project-ACL-Template.png?raw=true "Import JSON")
7. **Automatic Uplink Naming** to automatically name uplinks 
   ![json](./images/DNAC-Project-AUN-Template.png?raw=true "Import JSON")

Additionally, it contains a Composite Template. The composite template will allow us to reuse multiple Regular templates, thereby allowing modularity. Thus we can keep our configuration scripts in smaller files allowing reuse across various platforms. Subsequently helps in troubleshooting as the configurations become smaller and less complex as a result.
