# Creating a Wireless Radio Frequency RF Profile

In this subsection we will build a Wireless Radio Frequency (RF) Profile. This helpful tool, allows the administrator to tune the RF spectrum for the type of environment, and channels which are needed to support clients within their carpeted and non carpeted spaces. 

There are many things that can be accomplished from an RF Profile, to tweek the environment, from channels used, to data rates, to power settings deployed. Access points when deployed will utilize these RF Profiles to deploy the SSID's and the intention is to have the best wireless experience for the clients served in a specific area.

<details open>
<summary> Click the arrow for details</summary>

### Step 1 - ***Create RF Profile***

1. To create an RF Profile, first open a web browser on the Windows Workstation Jump host. Open a connection to DNA Center and select the hamburger menu icon to open the menu. Select `Design>Network Settings`.

   ![json](./images/module2-wlans/dnac-menu-network-settings.png?raw=true "Import JSON")

2. On the Network page click the `Wireless` tab to navigate to the wireless page.

   ![json](./images/module2-wlans/dnac-navigation-wireless-settings.png?raw=true "Import JSON")

3. On the **Wireless** page click `Add` above the *RF Profile* section to create a new Wireless RF Profile

   ![json](./images/module2-wlans/dnac-wireless-rfprofile-begin.png?raw=true "Import JSON")

4. The Create RF Profile page displays with *Wireless > Create RF Profile*. Complete the following steps:
   1. Enter the **Profile Name** as `DNAC-WIRELESS`
   2. Under the 2.4 Ghz Section set the *Supported Data Rates* to start at **12**
   3. Set the *Mandatory Data Rates* to **12** and **24** as shown
   4. Scroll down continue

      ![json](./images/module2-wlans/dnac-wireless-rfprofile-24ghz.png?raw=true "Import JSON")

5. Continue creating the RF Profile by completing the following steps:
   1. Under the 5 Ghz Section set the *Channel Width* to **20 Mhz**
   2. Set the *Mandatory Data Rates* to **12** and **24** as shown
   3. Click **Save** continue

      ![json](./images/module2-wlans/dnac-wireless-rfprofile-5ghz.png?raw=true "Import JSON")

6. The `Wireless` tab will reappear with the new *RF Profile* as displayed.

   ![json](./images/module2-wlans/dnac-wireless-rfprofile-results.png?raw=true "Import JSON")

</details>

## Summary

At this point you will have successfully configured **RF Profiles** on the **Wireless Controller** from **DNA Center**. During this lab we configured have configured SSID's, Wireless Network Profiles, RF Profiles, FlexConnect VLANs. The next step is **WLC** provisioning.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Continue to WLC Provisioning Module**](../LAB-J-Wireless-Automation/module4-wlcprovisioning.md)

> [**Return to Lab Menu**](./README.md)