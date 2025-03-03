# ISE Integration

In this lab, our focus changes slightly as we start to automate host onboarding. A large component of host onboarding is the authentication of hosts and assignments within the network. 

In this section, and in preparation for the steps which follow, we will integrate Cisco Catalyst Center with Identity Services Engine. This integration allows pxGrid communication between the Cisco Catalyst Center and ISE. For this reason, the **PxGrid** **persona** does need to be enabled on at least 1 ISE Node within an ISE Cluster. **This has already been completed in the sandbox.** 

PxGrid integration allows configuration automation by Cisco Catalyst Center within ISE for Network Access Devices, SGT creation, and SGACL builds via Contracts and Policy.

## Step 1: Verify ISE for Cisco Catalyst Center Integration

> **Note:** The following two tasks have been completed for you.

1. Open a web browser connection to Identity Services Engine (ISE) and select the hamburger menu to open the system menu.

   ![json](../assets/ise-dashboard.png?raw=true "Import JSON")

2. From the system menu under Administration, select PxGrid Settings

   ![json](../assets/ise-menu.png?raw=true "Import JSON")

3. On the PxGrid Settings page, you will see both options selected which allow Cisco Catalyst Center integration.

   ![json](../assets/ise-pxgrid-setup.png?raw=true "Import JSON")

## Step 2: Cisco Catalyst Center and ISE Integration

1. Open a web browser connection to Cisco Catalyst Center, select the hamburger menu, and navigate to the System > Settings menu item.

   ![json](../assets/dnac-system-settings.png?raw=true "Import JSON")

2. Within the System Settings page, navigate down the list on the left and select the Authentication and Policy Server section.

   ![json](../assets/dnac-system-settings-aaa.png?raw=true "Import JSON")

3. On the page, you will see and **Active** ISE integration.

   ![json](../assets/dnac-system-settings-aaa-ise-complete.png?raw=true "Import JSON")

> [**Next Section**](./04-scriptserver.md)
