## Catalyst Center and ISE Integration

> [!NOTE]
> If you have already completed the integration between Catalyst Center and ISE as part of the [Module 1 - PnP Prep](../LAB-1-Wired-Automation/module1-pnpprep.md) from Lab 1, you may skip this section and proceed to Module 2.

### Step 1 - Prepare ISE for Catalyst Center Integration

1. Open a web browser on the Windows Workstation Jump host. Open a connection to Identity Services Engine (ISE) and select the hamburger menu icon to open the system menu.

   ![json](../../ASSETS/LABS/ISE/ise-dashboard.png?raw=true "Import JSON")

2. From the system menu under Administration select PxGrid Settings

   ![json](../../ASSETS/LABS/ISE/ise-menu-pxgrid.png?raw=true "Import JSON")

3. On the PxGrid Settings page select both of the available options and click Save to allow Catalyst Center to integrate.

   ![json](../../ASSETS/LABS/ISE/ise-pxgrid-settings.png?raw=true "Import JSON")
   ![json](../../ASSETS/LABS/ISE/ise-pxgrid-setup.png?raw=true "Import JSON")

### Step 2 - Catalyst Center and ISE Integration

1. Open a web browser on the Windows Workstation Jump host. Open a connection to Catalyst Center and select the hamburger menu icon and navigate to the System > Settings menu item.

   ![json](../../ASSETS/LABS/CATC/catc-menu-systemsettings.png?raw=true "Import JSON")

2. Within the System Settings page navigate down the list on the left and select the Authentication and Policy Server section.

   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-aaa.png?raw=true "Import JSON")

3. On the page select from the dropdown ISE to configure ISE integration.

   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-ise.png?raw=true "Import JSON")
   

4. Enter the information as seen on the page and click save.

   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-ise-config.png?raw=true "Import JSON")
   

5. A popup will appear as the ISE node is using an untrusted SelfSigned Certificate. For lab purposes Accept the certificate, this may appear a couple of times as shown.

   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-ise-trust.png?raw=true "Import JSON")

6. You will see the the various stages of integration proceed and finally a success message as shown below.

   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-ise-done.png?raw=true "Import JSON")
   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-ise-complete.png?raw=true "Import JSON")

