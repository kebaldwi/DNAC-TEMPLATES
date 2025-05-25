# PnP Claiming - In Development

![json](../../ASSETS/COMMON/BUILD/underconstruction.png?raw=true "Import JSON")

> [!WARNING]
> The contents of this lab are not ready for public use. Do not use this lab or attempt to use it until this header is removed entirely from the lab.

## Overview

This module is designed to be used after first completing the **[Building PnP Templates](../LAB-3-Advanced-Automation/module2-day0-template.md)** and has been created to address how to operationalize **Plug and Play (PnP) Templates** to onboard devices into Cisco Catalyst Center. This module will go through the network profile, and how to claim devices as well as the claim process. 

### Overview Summary

In this section will go through the flows involved with **PnP**.This will allow us to create successful onboarding of network devices into Cisco Catalyst Center for Greenfield situations.

This is the lab we will be utilizing. Notice the **PnP Target Switch**. This is the C9300-1, which is a variant of the 9300 family. We will be building a configuration for this device from a sample configuration.

![json](../../ASSETS/COMMON/DCLOUD/DCLOUD_Topology_PnPLab2.png?raw=true "Import JSON")

## Exercises

### Step 1 - Navigate to Template Hub

Navigate to the CLI Template Hub on Catalyst Center Tools>Template Hub
Within the Projects Section locate the Onboarding Configuration Project and select it as shown.
You will notice there is not much in there. What we will do is now Build our first template.

### Step 2 - PnP Template 

We have previously built a PnP template within the **Template Hub** previously known as **Template Editor** within **Cisco Catalyst Center**. Go to the **Template Hub**  to complete the next task.

The Onboarding template has the minimal configuration and is designed to bring up device connectivity with Cisco Catalyst Center. Below are examples of Velocity and Jinja2 examples for explanation purposes only. 

#### Sample Velocity Template

This is an example of a complete PnP (onboarding) Template to compare with the template that you created in the first section.

<details closed>
<summary> Expand to review the Velocity Example </summary></br>

```vtl
## <------Onboarding-Template------->
## To be used for onboarding when using Day N Templates
## Define Variables provision with vlan and port channel
!
##MTU Adjust (if required)
#if(${SystemMTU} != 1500)
    system mtu ${SystemMTU}
#end
!
##Set hostname
hostname ${Hostname}
!
#set(${VtpDomain} = ${Hostname})
!
##Set VTP and VLAN for onboarding
vtp domain ${VtpDomain}
vtp mode transparent
!
##Set Management VLAN
vlan ${MgmtVlan}
!
#if(${MgmtVlan} > 1)
  name MgmtVlan
  ## Disable Vlan 1 (optional)
  interface Vlan 1
   shutdown
#end

##Set Interfaces and Build Port Channel 
interface range ${Interfaces}
 shut
 switchport mode trunk
 switchport trunk allowed vlan ${MgmtVlan}
 #set($pc = $Interfaces.split(','))
 #if($pc.size() > 1)
   channel-protocol lacp
   channel-group ${PortChannel} mode active
 #end
 no shut
!
#if($pc.size() > 1)
  interface port-channel ${PortChannel}
   switchport trunk native vlan ${MgmtVlan}
   switchport trunk allowed vlan add ${MgmtVlan}
   switchport mode trunk
   no port-channel standalone-disable
#end
!
##Set up managment vlan ${MgmtVlan}
interface Vlan ${MgmtVlan}
 description MgmtVlan
 ip address ${SwitchIP} ${SubnetMask}
 no ip redirects
 no ip proxy-arp
 no shut
!
ip default-gateway ${Gateway}
!
##Set Source of Management Traffic
ip domain lookup source-interface Vlan ${MgmtVlan}
ip http client source-interface Vlan ${MgmtVlan}
ip ftp source-interface Vlan ${MgmtVlan}
ip tftp source-interface Vlan ${MgmtVlan}
ip ssh source-interface Vlan ${MgmtVlan}
ip radius source-interface Vlan ${MgmtVlan}
logging source-interface Vlan ${MgmtVlan}
snmp-server trap-source Vlan ${MgmtVlan}
ntp source Vlan ${MgmtVlan}
!
netconf-yang
!
```

Did you miss any important configurations? Now is the time to fix the issues...

</details>

#### Sample Jinja2 Template

This is an example of a complete PnP (onboarding) Template to compare with the template that you created in the first section.

<details closed>
<summary> Expand to review the Velocity Example </summary></br>

[//]: # ({% raw %})
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
 {% if "," in Interfaces || "-" in Interfaces %}
    channel-protocol lacp
    channel-group {{ Portchannel }} mode active
 {% endif %}
 no shut
!
{% if "," in Interfaces || "-" in Interfaces %}
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
netconf-yang
!
```
[//]: # ({% endraw %})

Did you miss any important configurations? Now is the time to fix the issues...

</details>

Both of these Templates have the settings necessary to bring up a Layer2 access switch with enough configration to be supported by Cisco Catalyst Center for the rest of the provisioning process. As guidance 

it is **highly recommended** that you use **Jinja2** moving forward, due to its modularity and capabilities. You can however achieve the same results with **Velocity**, but the scripting language is not as feature rich.

The onboarding template is designed to set up static addressing and a hostname entry along with updating the management source interfaces for management connectivity. This file is transfered to the target device in a single file as opposed to linne by line configuration which accomodates the changes in network connectivity which may be lost when iterating line by line.

Please note the modifications to the source addressing for all protocols and specifically the **HTTP Client** source interface. This helps Cisco Catalyst Center to know if or when the IP address changes for a device and update it in the inventory automatically.

### Step 3 - Install an Onboarding Template **(OPTIONAL)**

We will now **download** and **import** one of the following PnP Onboarding Templates and install into the **Template Hub** previously known as the **Template Editor**. 

> [!TIP]
> We will attempt to use the template that you built in the previous module, but this will be kept in reserve as a fall back plan.

Please choose and download one from the following:

#### Velocity:

> [!NOTE]
> For older versions of Catalyst Center formerly known as Cisco DNA Center 2.2 and lower use the following for easy import:

&emsp;&emsp;&emsp; <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/TEMPLATES/VELOCITY/ONBOARDING/JSON/Platinum_PnP_Velocity_Template.json">⬇︎Platinum_PnP_Velocity_template.json⬇︎</a></br>

<details closed>
<summary> New Version for NON DCLOUD ONLY </summary></br>
<a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/TEMPLATES/VELOCITY/ONBOARDING/JSON/Titanium_PnP_Velocity_template.json">⬇︎Titanium_PnP_Velocity_template.json⬇︎</a> 
</details>

#### Jinja2:

> [!NOTE]
> For older versions of Catalyst Center formerly known as Cisco DNA Center 2.2 and lower use the following for easy import:

&emsp;&emsp;&emsp; <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/TEMPLATES/JINJA2/ONBOARDING/JSON/Platinum_PnP_Jinja2_Template.json">⬇︎Platinum_PnP_Jinja2_template.json⬇︎</a> 

<details closed>
<summary> New Version for NON DCLOUD ONLY </summary></br>
<a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/TEMPLATES/JINJA2/ONBOARDING/JSON/Titanium_PnP_Jinja2_template.json">⬇︎Titanium_PnP_Jinja2_template.json⬇︎</a>
</details></br>

1. Navigate to the **Template Hub** formerly known as the **Template Editor** within Cisco Catalyst Center through the menu **`Tools > Template Hub`**.

   ![json](./images/DNAC-NavigateTemplate.png?raw=true "Import JSON")

2. Click **Import** then select **Template(s)** from the menu.    

   ![json](./images/DNAC-TemplateImport-1.png?raw=true "Import JSON")

3. Click the link to select files from the local computer. In the Windows explorer window search for the extracted json file, select it and open it into the import window.

   ![json](./images/DNAC-TemplateSelection-1.png?raw=true "Import JSON")

4. Click import to install and import the template.

   ![json](./images/DNAC-TemplatedSelected-1.png?raw=true "Import JSON")

### Step 4 - Create a Network Profile **(REQUIRED)**

Next we need to assign the Onboarding Template to a site using the Network Profile. 

   1. Navigate to Network Profiles by selecting *Design> Network Profiles* 

      ![json](./images/DNAC-NavigateProfile.png?raw=true "Import JSON")

   2. Select *Switching* under **Add Profile**

      ![json](./images/DNAC-SelectProfile.png?raw=true "Import JSON")

   3. Enter the following: 

      1. Enter the **Profile name** 
      2. Select the **Onboarding Template** tab and click **Add Template** to add a template

         ![json](./images/DNAC-Onboard-Add.png?raw=true "Import JSON")

      3. Select the correct PnP Onboarding template that you imported earlier and click **Add**   

         ![json](./images/DNAC-ChoosePnPTemplate.png?raw=true "Import JSON") 

   4. On the Onboarding Template page confirm the template(s) to be used for onboarding then **Save** the profile

      ![json](./images/DNAC-ProfileComplete.png?raw=true "Import JSON")

   5. Assign the network profile to the hierarchy 

      ![json](./images/DNAC-ProfileAssign.png?raw=true "Import JSON")

   6. Select the sites to apply the profile within the hierarchy and click **Save**.

      ![json](./images/DNAC-ProfileAssigned.png?raw=true "Import JSON")

## Step 6 - Claiming the Device **(REQUIRED)**

At this point Cisco Catalyst Center is set up and ready for Plug and Play to onboard the first device. Provided the discovery and dhcp assignment are aligned, the device should when plugged in find Cisco Catalyst Center and land in the plug n play set of the devices section within the provisioning page.

At this point you can claim the device putting it in a planned state for onboarding onto the system. To do this do the following:

   1. Within Cisco Catalyst Center Navigate to **`Provision > Plug and Play`**      

      ![json](./images/DNAC-NavigatePnP.png?raw=true "Import JSON")

   2. Put a checkmark next to the device *Switch* to be claimed
   3. Click the **Actions>Claim** link and walk through the workflow    

      ![json](./images/DNAC-BeginClaim.png?raw=true "Import JSON")

   4. Section 1 click the **Assign** link to select the part of the hierarchy to assign the device

      ![json](./images/DNAC-AssignSite-Start.png?raw=true "Import JSON")

   5. Click the part of the hierarchy to assign the device to and then click **Assign**
   
      ![json](./images/DNAC-AssignSite-Save.png?raw=true "Import JSON")

   6. The assigned site will appear on the section page, click **next** to continue

   7. Section 2 you can click the hyperlinks to the right of the workflow page and view or amend the templates and images utilized. We will make no changes so click **next** to continue   

      ![json](./images/DNAC-SiteClaim.png?raw=true "Import JSON")

   8. Section 3 select the device **serial number** on the left and fill in the variables within the template click **next**. Please use the following:
   
      * Hostname type `c9300-1`
      * Management Vlan enter `5`
      * Interfaces `Gi1/0/10, Gi1/0/11`
      * IP Management Address `192.168.5.3`
      * Subnet Mask `255.255.255.0`
      * Gateway `192.168.5.1`
      * VTP Domain `Cisco` ***(if required)***

      > [!NOTE] 
      > Leave the rest of the settings default 

        ![json](./images/DNAC-TemplateClaim.png?raw=true "Import JSON")

   9. Section 4 review the elements including configuration to be deployed. Click **claim** to initiate

      ![json](./images/DNAC-Claim.png?raw=true "Import JSON")

   10. At this stage the device will be placed in **Planned** state, and will cycle through **Onboarding** and **Provisioned** when complete     

       ![json](./images/DNAC-Claimed.png?raw=true "Import JSON")

   11. After the device is completed it will appear in the device inventory after being sync'd with Cisco Catalyst Center.      

       ![json](./images/DNAC-Inventory.png?raw=true "Import JSON")

## Summary

Congratulations you have completed xxx

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Continue to DayN Templates Module**](../LAB-3-Advanced-Automation/module4-dayn-template.md)

> [**Return to Lab Menu**](./README.md)