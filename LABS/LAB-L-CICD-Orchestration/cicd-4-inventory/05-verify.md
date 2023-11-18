# Device Inventory Verification

To verify that the inventory was successfully retrieved examine the files within the directory `/root/DEVWKS-2176/inventory` and `/root/DEVWKS-2176/reports` Cisco DNA Center.

Follow these steps:

1. If Cisco DNA Center is not already open, use a browser and navigate to `https://198.18.129.100`, where you may see an SSL Error displayed as depicted. Click the `Proceed to https://192.18.129.100 (unsafe)` link to continue if presented

   ![json](./images/DNAC-SSLERROR.png?raw=true "Import JSON")

2. If required, log into Cisco DNA Center using the username of `admin` and the password `C1sco12345`.

   ![json](./images/DNAC-Login.png?raw=true "Import JSON")

3. When the Cisco DNA Center Dashboard is displayed, Click the icon to display the menu'

   ![json](./images/DNAC-Menu.png?raw=true "Import JSON")

4. Select `Network Device>Inventory` from the menu to continue.

   ![json](./images/.png?raw=true "Import JSON")

5. Compare that against the files in the directory `/root/DEVWKS-2176/inventory` by scrolling up and down using the following:

```SHELL
   cat /root/DEVWKS-2176/inventory/*
```

> [**Next Section**](06-summary.md)