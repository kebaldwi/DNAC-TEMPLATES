# Wireless Templates

While most configurations for wireless can be addressed via the Cisco Catalyst (DNA) Center Graphical User Interface (GUI), there are a few items where configuration is required and neither the GUI nor the Model-Based Configuration can accomodate. In this subsection we will design templates to be used with Wireless Controllers to provision things which are not currently scoped by the Cisco Catalyst (DNA) Center Graphical User Interface (GUI).

Templates may be utilized as Composite or Regular Templates, and in either Jinja2 or Velocity. Additionally System and Bind Variables may be utilized in accordance to the previously mentioned topics earlier in this repository.

To refresh on those topics please refer to the following:

#### Templating

* [Onboarding Templates](../../Onboarding.md#onboarding-templates-and-flows) - This section will explain Onboarding Templates in DNAC and their use in bringing various devices under DNA Center management
* [DayN Templates](../../DayN.md#day-n-templates-and-flows) - This section will explain how to use templates for ongoing (Day-N) changes to the network
* [Building Templates](../../Templates.md#building-templates) - This section will explain how to build a template on DNAC from scratch

#### Velocity Language

* [Velocity Variables](../../Variables.md#velocity-variables) - This section explains Template Variables in depth, and how and where to use them
* [Velocity Scripting](../../Velocity.md#velocity-scripting) - This section will dive into Velocity Language Template Scripting constructs and use cases
* [Advanced Velocity Scripting](../../AdvancedVelocity.md#advanced-velocity) - This section will dive into Advanced Velocity Language Template examples

#### Jinja2 Language

* [Jinja2 Variables](../../Variables.md#jinja2-variables) - This section explains Template Variables in depth, and how and where to use them
* [Jinja2 Scripting](../../Jinja2.md#jinja2-scripting) - This section will dive into Jinja2 Language Template Scripting constructs and use cases
* [Advanced Jinja2 Scripting](../../AdvancedJinja2.md#advanced-jinja2) - This section will dive into Advanced Jinja2 Language Template examples

#### Variables

* [System Variables](../../SystemVariables.md#dna-center-system-variables) - This section explains DNA Centers System Variables

#### Fault-Finding

* [Troubleshooting](../../TroubleShoot.md#Troubleshooting) - This section will dive into Troubleshooting Velocity based Template Constructs

While there may be many use cases for templates in wireless, the use of the GUI negates the complexities involved with maintaining lengthy ones. There are however some examples which have used over the past few years when certain features were not available via the GUI in any form:

1. [⬇︎**SSID with mPSK**⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-J-Wireless-Automation/templates/wireless/Wifi_SSID_mPSK.json) - *(create mPSK keys in SSID)* - *(available in 2.3.5.x)*
2. [⬇︎**CCKM SSID**⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-J-Wireless-Automation/templates/Wifi_CCKM_templates.json) - *(CCKM setting for SSID)* - *(available in 2.3.5.x)*
3. [⬇︎**Anchor Priority**⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-J-Wireless-Automation/templates/Wifi_Anchor_Priority_templates.json) - *(Enabling)* - *(available in 2.3.3.x)*
4. [⬇︎**Open Roaming**⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-J-Wireless-Automation/templates/Wifi_Open_Roaming_project.json) - *(Set up open roaming from a Project)*
5. [⬇︎**RF**⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-J-Wireless-Automation/templates/Wifi_RF_templates.json) - *(Enabling RF Thresholds)*
6. [⬇︎**Radius Probes**⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-J-Wireless-Automation/templates/Wifi_AAA_Probes_templates.json) - *(Enabling Probes for AAA)*
7. [⬇︎**9800 Hardening**⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-J-Wireless-Automation/templates/Wifi_9800_Harden_templates.json) - *(Various Security Settings)*
8. [⬇︎**Onboarding**⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-J-Wireless-Automation/templates/Wifi_PnP_Onboarding_project.json) - *(Composite Example for PnP from a Project)*

9. [⬇︎**ALL Wireless Examples**⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-J-Wireless-Automation/templates/Wifi_Templates_project.json) - *(All Wireless Examples in a Project)*

<details open>
<summary> Click the arrow for details</summary>

## Step 1 - ***Creating Wireless Templates***

1. Open a web browser on the Windows Workstation Jump host. Open a connection to DNA Center and select the hamburger menu icon to open the menu. Select `Tools>Template Editor`.

   ![json](./images/underconstruction.png?raw=true "Import JSON")

   

## Step 2 - ***Assigning Wireless Templates***

1. Select the hamburger menu icon to open the menu. Select `Design>Network Profiles`.

   ![json](./images/underconstruction.png?raw=true "Import JSON")

2. Select the **edit** button beside the Wireless Network Profile

   ![json](./images/underconstruction.png?raw=true "Import JSON")

3. Scroll down to the **Attach Model Configs** and click the **⨁ Add Model Config** button

   ![json](./images/underconstruction.png?raw=true "Import JSON")

4. In the Window that appears:
   
   1. Device Types select Wireless Controller

      ![json](./images/underconstruction.png?raw=true "Import JSON")

   2. Select **> Wireless** to display the list

      ![json](./images/underconstruction.png?raw=true "Import JSON")

   3. Open **AAA Radius Attributes Configuration**

      ![json](./images/underconstruction.png?raw=true "Import JSON")

   4. Select `DNAC-Templates`

      ![json](./images/underconstruction.png?raw=true "Import JSON")

   5. Click **Add**

      ![json](./images/underconstruction.png?raw=true "Import JSON")

5. Click Save to add the changes.

   ![json](./images/underconstruction.png?raw=true "Import JSON")

6. The configuration changes would now need to be provisioned to the Wireless Controller.

</details>

## Summary

Congratulations you have completed the XXX module of the lab and . Please use the navigatation below to continue your learning.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Continue to Wireless Controller High Availability Module**](../LAB-J-Wireless-Automation/module7-controllerha.md)

> [**Return to Lab Menu**](./README.md)