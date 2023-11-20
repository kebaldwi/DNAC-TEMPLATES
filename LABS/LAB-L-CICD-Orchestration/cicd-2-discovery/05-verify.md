# Device Discovery Verification

We will inspect the Discovery Tool within Cisco DNA Center and the inventory to verify that the devices were discovered successfully.

Follow these steps:

1. If Cisco DNA Center is not already open, use a browser and navigate to `https://198.18.129.100`, where you may see an SSL Error displayed as depicted. Click the `Proceed to https://192.18.129.100 (unsafe)` link to continue if presented

   ![json](./images/DNAC-SSLERROR.png?raw=true "Import JSON")

2. If required, log into Cisco DNA Center using the username of `admin` and the password `C1sco12345`.

   ![json](./images/DNAC-Login.png?raw=true "Import JSON")

3. When the Cisco DNA Center Dashboard is displayed, Click the  icon to display the menu'

   ![json](./images/DNAC-Menu.png?raw=true "Import JSON")

4. Select `Tools>Discovery` from the menu to continue.

5. On the left, you can click on the view all discoveries, then select it and view it on the right. 

   ![json](./images/dnac-discovery-1.png?raw=true "Import JSON")
   ![json](./images/dnac-discovery-2.png?raw=true "Import JSON")

6. Alternatively, you can go `Provision > Inventory` and view the devices in the Global Level.

   ![json](./images/dnac-inventory.png?raw=true "Import JSON")

You will notice the devices have been discovered and assigned to the appropriate level of the Hierarchy as per the CSV.

> [**Next Section**](./06-summary.md)