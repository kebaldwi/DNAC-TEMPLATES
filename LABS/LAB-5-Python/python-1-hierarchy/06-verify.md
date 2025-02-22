# Hierarchy Build Verification

To verify that the Hierarchy was built successfully, we will inspect the site in Cisco Catalyst Center.

Follow these steps:

1. Open a browser and navigate to `https://198.18.129.100`, where an SSL Error is displayed as depicted. Click the `Proceed to https://192.18.129.100 (unsafe)` link to continue

   ![json](./images/DNAC-SSLERROR.png?raw=true "Import JSON")

2. Log into Cisco Catalyst Center using the username of `admin` and the password `C1sco12345`.

   ![json](./images/DNAC-Login.png?raw=true "Import JSON")

3. When the Cisco Catalyst Center Dashboard is displayed, Click the  icon to display the menu'

   ![json](./images/DNAC-Menu.png?raw=true "Import JSON")

4. Select `Design>Network Hierarchy` from the menu to continue.

   ![json](./images/DNAC-Menu-Hierarchy.png?raw=true "Import JSON")

5. Expand the Hierarchy on the left to show your specific `Area`

   ![json](./images/dnac_cicd_hierarchy.png?raw=true "Import JSON")

6. Go to `Design>Network Settings` from the menu and navigate to `Floor 1`

   ![json](./images/dnac_cicd_settings.png?raw=true "Import JSON")

7. Go to `Credentials` tab on the same page

   ![json](./images/dnac_cicd_creds.png?raw=true "Import JSON")

8. Finally go to the `Telemetry` tab 

   ![json](./images/dnac_cicd_telemetry.png?raw=true "Import JSON")

> [**Next Section**](./07-summary.md)
