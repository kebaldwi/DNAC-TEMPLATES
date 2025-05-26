# Building PnP Templates - In Development

![json](../../ASSETS/COMMON/BUILD/underconstruction.png?raw=true "Import JSON")

> [!WARNING]
> The contents of this lab are not ready for public use. Do not use this lab or attempt to use it until this header is removed entirely from the lab.

## Overview

This module is designed to be used after first completing the **[Lab Preparation](../LAB-3-Advanced-Automation/module1-prep.md)** and has been created to address how to build **Plug and Play (PnP)** to onboard devices into Cisco Catalyst Center. 

### Greenfield

When dealing with net **new** devices using the PnP process to onboard devices we utilize **Onboarding templates** within Cisco Catalyst Center to onboard network devices with no configuration on the device. 

**PnP** Onboarding allows for the **claiming** of a device and the ability to automate the deployment of configuration. It is important to note that Onboarding templates are transfered as a **flat file** via HTTP/HTTPS transfer. 

This allows for the manipulation of uplinks and addressing without disconnectivity during reconfiguration from the upstream neighboring device. Additional source commands can be used to allow the device to automatically inform Cisco Catalyst Center of a change in address through the PnP profile applied and the source of the HTTP client information.

### Brownfield (background only)

When dealing with **existing** infrastructure, we want to absorb the device and its configuration into Cisco Catalyst Center to allow for monitoring and a gradual shift to automated management, as the device usually is in a running state supporting the network, and the configuration pre-exists.

Be aware that with Brownfield device configurations, there is no template learning capability for switching. As such configuration on the device may need modification prior to provisioning in some situations. If this is required you may want to Discover and then push a normalization template via REST API to remove settings that would cause ongoing provisioning errors.

### Overview Summary

In this section will go through the flows involved with **PnP** only. **Brownfield** will be **out of scope** for this module. This will allow us to create successful onboarding of network devices into Cisco Catalyst Center for Greenfield situations.

This is the lab we will be utilizing. Notice the **PnP Target Switch**. This is the C9300-1, which is a variant of the 9300 family. We will be building a configuration for this device from a sample configuration.

![json](../../ASSETS/COMMON/DCLOUD/DCLOUD_Topology_PnPLab2.png?raw=true "Import JSON")

## Lab Credentials:

| Platform:       | IP Address:    | Username |  Password  | 
|-----------------|----------------|----------|------------|
| Catalyst Center | 198.18.129.100 | admin    | C1sco12345 |
| ISE             | 198.18.133.27  | admin    | C1sco12345 |
| Windows AD      | 198.18.133.1   | admin    | C1sco12345 |
| Script Server   | 198.18.133.28  | root     | C1sco12345 |
| Router          | 198.18.133.145 | netadmin | C1sco12345 |
| Switch 1        | 198.18.128.22  | netadmin | C1sco12345 |
| Switch 2        | 198.18.128.23  | netadmin | C1sco12345 |

## Considerations about Templates

* PnP vs. DayN Templates: Cisco recommends using DayN Templates for most configurations, reserving PnP templates for establishing a stable network connection.

* Inventory Database Limitations: The inventory database is inaccessible before the claim process, complicating onboarding. This results in a need for manual input in scripts instead of leveraging known device information.

* Ongoing Modifications: DayN operations templates are stored within a project, while onboarding templates are located in the project Onboarding Configuration. Using onboarding templates post-PnP is impractical due to the absence of **system** and **bind** variables, which could simplify code and reduce repetition.

* Automation Potential: DayN templates facilitate ongoing modifications and automate configurations using data from the inventory database, minimizing manual input.

* Configuration Best Practices: Typical configurations should automatically derive from the Network Settings in Cisco Catalyst Center. Avoid deploying CLI code in templates for tasks already defined by design components, promoting a more UI-centric and maintainable configuration approach.

* Guidance: Utilize design settings for as much configuration as possible, keeping templates streamlined for configurations that may change frequently, enhancing maintainability and troubleshooting.

* **Jinja** vs **Velocity**, choose wisely. My recommendation is to use Jinja simply because it is the defactor template rendering language used in multiple platforms. It is modular, and the logic consrtucts are based on **Python**. 

## Developing a PnP Template

So what should be in the PnP Template? Well that depends on the situation, but generally speaking we need to build the foundation of the device, and put that which cannot change without disrupting the communication from Device to Catalyst Center.

### Included items:

* System Configuration
  * Hostname
  * System MTU 
  * VTP 
  * Enable Netconf 
* Management Interface Configuration
  * IP address
  * Subnet Mask
  * Source Management Traffic
* Next Hop Configuration
  * Gateway or Routing Protocol

## Exercises

### Step 1 - Navigate to Template Hub

Navigate to the CLI Template Hub on Catalyst Center **`Tools > Template Hub`**

![json](../../ASSETS/LABS/CATC/MENU/catc-menu-5.png?raw=true "Import JSON")

### Step 2 - Create a Regular Template

Within the **Project Name** Section on the left locate the **Onboarding Configuration** Project and select it as shown

![json](../../ASSETS/LABS/TEMPLATEEDITOR/PNPTEMPLATE/project-onboarding-default.png?raw=true "Import JSON")

You will notice there is not much in there. What we will do is now Build our first template. To do this use the **&#8853; Add** action menu shown and select **New Template**

![json](../../ASSETS/LABS/TEMPLATEEDITOR/PNPTEMPLATE/add-pnp-template-start.png?raw=true "Import JSON")

In the **Add New Template** wizard fill in the following details as shown below:

|Section          |Details                                |
|-----------------|---------------------------------------|
|Template Name    |**PnP-Template-J2**                    |
|Project Name     |**Onboarding Configuration**           |
|Template Type    |**Regular Template**                   |
|Template Language|**JINJA**                              |
|Software Type    |**IOS-XE**                             |
|Device Family    |**Switches and Hubs**                  |
|Devices          |**Cisco Catalyst 9300 Series Switches**|

1. First enter the Template Name **PnP-Template-J2** from above then select the Onboarding Configuration project. This must be selected for this template to be offered within the PnP Onboarding Tab of the Network Profile.

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PNPTEMPLATE/add-pnp-template-1.png?raw=true "Import JSON")

2. Ensure that for Template Type you have selected **Regular Template** and under Template Language that **JINJA** is selected as recommended earlier. For Software Type select **IOS-XE** as shown.

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PNPTEMPLATE/add-pnp-template-2.png?raw=true "Import JSON")

3. Click the **Add Device Details** link to select the type of device to which to associate the template

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PNPTEMPLATE/add-pnp-template-3.png?raw=true "Import JSON")

4. In the **Add Device Details** page select for Device Family **Switches and Hubs**

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PNPTEMPLATE/add-pnp-template-4.png?raw=true "Import JSON")

5. Enter **9300** in the search filter to find the 9300 switches

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PNPTEMPLATE/add-pnp-template-5.png?raw=true "Import JSON")

6. Then select for Devices **Cisco Catalyst 9300 Series Switches** and click **Add**.

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PNPTEMPLATE/add-pnp-template-6.png?raw=true "Import JSON")

7. You should now see the following **configured properties** for the template, click **Continue**

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PNPTEMPLATE/add-pnp-template-7.png?raw=true "Import JSON")

8. The **PnP-Template-J2** will now open in the Editor allowing the configuration to be added.

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PNPTEMPLATE/add-pnp-template-8.png?raw=true "Import JSON")

### Step 3 - Build the Template Logic

As previously stated the PnP Template should use the minimum configuration to adhere to the **Don't Repeat yourself (DRY)** philosophy. Remember No System Variables and limited bind functionality are available. This inhibits the ability to use logic without filling in all the details. Additionally we really want to track these things which is what DayN affords us. 

> [!TIP]
> Keep it **SIMPLE**

In this lab we are connecting a Layer 2 switch and utilizing the typical management VLAN. So at a minimum we need to get this configuration onto that device:

|Detail            |Configuration       |
|------------------|--------------------|
|Hostname          |`c9300-1`           |
|Management Vlan   |`5`                 |
|Uplink Interfaces |`Gi1/0/10, Gi1/0/11`|
|Management Address|`192.168.5.3`       |
|Subnet Mask       |`255.255.255.0`     |
|Gateway           |`192.168.5.1`       |
|VTP Domain        |`Cisco`             |

So in order to get this configuration on the switch we would typically configure something like this:

```j2
hostname c9300-1

vlan 5
 name mgmtvlan

interface vlan 5
 ip address 192.168.5.3 255.255.255.0
 no shutdown
 exit

interface vlan 1
 shutdown

ip default-gateway 192.168.5.1
```

So lets copy and paste that confiiguration into the **PnP-Template-J2**


### Step 4 - Use Variables

### Step 5 - Build Form

### Step 6 - Simulation

## Summary

Congratulations you have completed xxx

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Continue to PnP Claiming Module**](../LAB-3-Advanced-Automation/module3-pnp.md)

> [**Return to Lab Menu**](./README.md)