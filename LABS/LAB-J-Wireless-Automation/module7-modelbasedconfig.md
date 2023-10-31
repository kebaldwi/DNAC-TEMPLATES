# Model-Based Configuration

In this subsection we will design and provision the Wireless Controller with model-based configurations to augment the wireless settings of WLAN's. Whenever a new WLAN or a configuration change is made, the change will need to be provisioned to the controller using this process. The Model-Based Configurations may be added to the wireless profiles to modify settings for the wireless SSID that are provisioned by Cisco DNA Center.

The various use cases for model-based configuration are as follows:

1. **AAA Radius Attributes Configuration** - *(Modify Called Station ID)*
2. **Advanced SSID Configuration** - *(General, Client and SSID Data Rates, 802.AX)*
3. **CleanAir Configuration** - *(Enabling, Interferer Features)*
4. **Dot11ax Configuration** - *(AX BSS Color etc)*
5. **Event Driven RRM Configuration** - *(Enabling EDRRM and Sensitivity Thresholds)* - *(in 2.3.5.x)*
6. **Flex Configuration** - *(IP Overlap)*
7. **Global IPv6 Configuration** - *(Global IPv6)*
8. **Multicast Configuration** - *(Enabling Multicast Globally for Unicast or Multicast)*
9. **RRM FRA Configuration** - *(Enabling Flexible Radio Assignment)* - *(in 2.3.5.x)*
10. **RRM General Configuration** - *(Thresholds, Monitoring and Coverage)* - *(in 2.3.5.x)*

<details open>
<summary> Click the arrow for details</summary>

## Step 1 - ***Creating Model-Based Configuration***

1. Open a web browser on the Windows Workstation Jump host. Open a connection to DNA Center and select the hamburger menu icon to open the menu. Select `Tools>Model Config Editor`.

   ![json](./images/underconstruction.png?raw=true "Import JSON")

2. On the **Model Config Editor** page click the `Design` tab and complete the following:

   ![json](./images/underconstruction.png?raw=true "Import JSON")

   1. Select a model-based config as shown (AAA Radius Attributes Configuration)

      ![json](./images/underconstruction.png?raw=true "Import JSON")

   2. Click the **⨁ Add** button to create custom config.

      ![json](./images/underconstruction.png?raw=true "Import JSON")

   3. Enter a Name for the Design Element, `DNAC-Templates`

      ![json](./images/underconstruction.png?raw=true "Import JSON")

   4. From the dopdown select the value `ap-macaddress-ssid` for the **Called Station Id**

      ![json](./images/underconstruction.png?raw=true "Import JSON")

   5. Click Save

      ![json](./images/underconstruction.png?raw=true "Import JSON")


## Step 2 - ***Assigning Model-Based Configuration***

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

Congratulations you have completed the Model-Based Config module of the lab and added AAA configuration to add `Called Station Id` information for AAA purposes. Additional Model-Based Configuration may also be added in a simlar fashion. Please consult the Cisco Unified Wireless Design Guide for further details. Please use the navigatation below to continue your learning.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Continue to Wireless Templates Module**](../LAB-J-Wireless-Automation/module8-wirelesstemplates.md)

> [**Return to Lab Menu**](./README.md)