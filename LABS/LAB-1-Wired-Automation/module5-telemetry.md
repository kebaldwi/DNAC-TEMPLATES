# Telemetry

## Overview

This Lab is designed to be used after first completing labs A through D and has been created to address how to properly deal with enabling Telemetry for Assurance with regard to Cisco Catalyst Center. During the lab we will edit the Telemetry settings within Cisco Catalyst Center. This allows Cisco Catalyst Center the ability to configure network devices for the required Telemetry settings required to get the best results when viewing Assurance within Cisco Catalyst Center.

## General Information

Within this lab we will direct Netflow to Cisco Catalyst Center. It is important to understand that some networking devices have minimal allowed Netflow Collectors which can be configured. SHould it be the case that you need addiitional flows to other servers or management devices, then please incorporate a Netflow Redirector in your design. This will allow the same flow to be replicated by the redirector to other management systems which require the feed.

## Lab Section 1 - Enabling Telemetry

In this lab we will enable the Telemetry Settings and Provision the new settings to a device on Cisco Catalyst Center.

<details open>
<summary> Click for Details and Sub Tasks</summary>

1. Navigate to the **Network Settings** within Cisco Catalyst Center through the menu *Design>Network Settings>*.

   ![json](./images/DNAC-Navigate-Settings.png?raw=true "Import JSON")

2. Navigate to the **Telemetry** tab within the **Network Settings** page within Cisco Catalyst Center through the submenu.

   ![json](./images/DNAC-Telemetry-Navigation-2.png?raw=true "Import JSON")

3. View the **Telemetry** settings within Cisco Catalyst Center. Until this point we have not provisioned Netflow onto the switch.

   ![json](./images/DNAC-Telemetry-Settings.png?raw=true "Import JSON")

4. Select the checkbox next to **Use Cisco Catalyst Center as a Netflow Collector Server**. Then click **Save**.

   ![json](./images/DNAC-Telemetry-Settings-NetFlow.png?raw=true "Import JSON")

5. Click **Okay** in the popup which appears.

   ![json](./images/DNAC-Telemetry-Settings-Save.png?raw=true "Import JSON")

6. Navigate to the **Inventory** within Cisco Catalyst Center through the menu *Provision>Network Devices>Inventory>*.

   ![json](./images/DNAC-NavigateInventory.png?raw=true "Import JSON")

7. From the inventory we will provison the **Telemetry** to the network device.

   ![json](./images/DNAC-Provision-Telemetry-1.png?raw=true "Import JSON")

8. Select the switch checkbox, then click **Actions > Telemetry > Enable Application Telemetry** from the submenu.

   ![json](./images/DNAC-Provision-Telemetry-2.png?raw=true "Import JSON")

9. Navigate to the **Provision** focus on the Inventory Page and notice the configuring message.

   ![json](./images/DNAC-Provision-Telemetry-3.png?raw=true "Import JSON")

10. Eventually **Success** will be displayed.

    ![json](./images/DNAC-Provision-Telemetry-4.png?raw=true "Import JSON")

11. Click the **Success** message for more information.

    ![json](./images/DNAC-Provision-Telemetry-5.png?raw=true "Import JSON")

</details>

## Lab Section 2 - Reviewing Telemetry Configuration

In this section we will review the configuration that has been pushed to the device.

<details open>
<summary> Click for Details and Sub Tasks</summary>

1. Select the **Inventory** focus.

   ![json](./images/DNAC-Provision-Telemetry-1.png?raw=true "Import JSON")

2. Select the switch checkbox, then click **Actions > Inventory > Resync Device** from the submenu.

   ![json](./images/DNAC-Provision-Resync.png?raw=true "Import JSON")

3. After a few moments of **syncing** the device will show in a managed state.

   ![json](./images/DNAC-Provision-Telemetry-1.png?raw=true "Import JSON")

4. Click the actual name **ACCESS-c9300-1-ASW.dcloud.cisco.com** and from the page that appears select **configuration** from the sidebar menu.

   ![json](./images/DNAC-Provision-Config.png?raw=true "Import JSON")

Notice the Netflow configuation that has been pushed and additinally scroll through the fully configured switch to see all the various telemetry settings whcih have been deployed from Syslog to SNMP.

</details>

At this point you have successfully built and deployed Telemety to a switch from Cisco Catalyst Center.

## Automating Telemetry

While it is possible to click through these processes manually, which can be time-consuming, we can handle this differently. We may automate them further via REST API.

## Summary

The next step will be to build Advanced Automation Templates in the network infrastructure. 

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Continue to Advanced Automation Lab**](./module6-advanced.md)

> [**Return to LAB Menu**](./README.md)
