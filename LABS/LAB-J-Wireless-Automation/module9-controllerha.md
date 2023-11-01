# Cisco Wireless Controller High Availability

Cisco Wireless Controller High Availability (HA) can be configured through Cisco DNA Center. Currently, both the formation and breaking of wireless controller HA is supported; switchover options are not supported.

While the DCLOUD Lab we have been using does not currently support this configuration, the steps which have been added below detail how to prepare and how to configure Wireless Controller High Availability. 

## Prerequisites
Configuring High Availability (HA) on the Cisco Catalyst 9800 Series Wireless Controller involves the following prerequisites:

* Both the Cisco Catalyst 9800 Series Wireless Controller devices are running the same software version and have the active software image on the primary Catalyst 9800 Series Wireless Controller.

* The service port and management port of Catalyst 9800 Series Wireless Controller 1 and Catalyst 9800 Series Wireless Controller 2 are configured.

* The redundancy port of Catalyst 9800 Series Wireless Controller 1 and Catalyst 9800 Series Wireless Controller 2 are physically connected.

* Preconfigurations such as interface configurations, route addition, ssh line configurations, netconf-yang configurations are completed on the Catalyst 9800 Series Wireless Controller appliance.

* The management interface of Catalyst 9800 Series Wireless Controller 1 and Catalyst 9800 Series Wireless Controller 2 are in the same subnet.

* The discovery and inventory of Catalyst 9800 Series Wireless Controller 1 and Catalyst 9800 Series Wireless Controller 2 devices are successful from Cisco DNA Center.

* The devices are reachable and are in the Managed state.

## Procedure:

1. Click the menu icon (**≡**) and choose **Provision>Network Devices>Inventory**.
   The **Inventory** window is displayed with the discovered devices listed.
2. To view devices available in a particular site, expand the **Global** site in the left pane, and select the site, building, or floor that you are interested in.
   All the devices available in that selected site are displayed in the **Inventory** window.
3. From the **Device Type** list, click the **WLCs** tab, and from the **Reachability** list, click the **Reachable** tab to get the list of wireless controllers that are discovered and reachable.
4. In the **Inventory** window, click the desired Cisco Catalyst 9800 Series Wireless Controller name to configure as a primary controller.
5. Click the **High Availability** tab.
   The selected Catalyst 9800 Series Wireless Controller by default becomes the primary controller and the **Primary C9800** field is grayed out.
6. From the **Select Primary Interface** and **Secondary Interface** drop-down lists, choose the interface that is used for HA connectivity. 
   
   The HA interface serves the following purposes:

   - Enables communication between the controller pair before the IOSd boots up.
   - Provides transport for IPC across the controller pair.
   - Enables redundancy across control messages exchanged between the controller pair. The control messages can be HA role resolution, keepalives, notifications, HA statistics, and so on.

7. From the **Select Secondary C9800** drop-down list, choose the secondary controller to create an HA pair.

   >**Note:** When you choose the secondary controller, based on the wireless management interface IP subnet of the primary controller, the redundancy management IP is auto populated, and an i icon is displayed at the top of the **High Availability** window, along with the following message:
   >
   >Ensure that the Redundancy Management IP and Peer Redundancy Management IP are not assigned to any other network entities. If the IPs are in use, change the IPs accordingly and configure.

8. Enter the **Redundancy Management IP** and **Peer Redundancy Management IP** addresses in the respective fields.
   
   >**Note:** The IP addresses used for the redundancy management IP and peer redundancy management IP should be configured in the same subnet as the management interface of the Cisco Catalyst 9800 Series Wireless Controller. Ensure that these IP addresses are unused IP addresses within the subnet range.
   >
   >Cisco DNA Center only pushes the management IP address of the Cisco Catalyst 9800 Series Wireless Controller to the Cisco ISE network access device list. Whereas the standby controller uses the redundancy management IP address to initiate AAA requests. So, you must add the redundancy management IP addresses to the AAA servers for a seamless client authentication and standby monitoring.

9. In the **Netmask** field, enter the netmask address.

10. Click **Configure HA**.
    
    The HA configuration is initiated at the background using the CLI commands. First, the primary controller is configured. On success, the secondary controller is configured. Both the devices reboot once the HA is enabled. This process may take up to 2.5 minutes to complete.

11. After the HA is initiated, the **Redundancy Summary** under **High Availability** tab displays the **Sync Status** as **HA Pairing is in Progress**. When Cisco DNA Center finds that the HA pairing is successful, the **Sync Status** becomes **Complete**.

    This is triggered by the inventory poller or manual resynchronization. By now, the secondary controller (Catalyst 9800 Series Wireless Controller 2) is deleted from Cisco DNA Center. This flow indicates successful HA configuration in the Catalyst 9800 Series Wireless Controller.

12. To manually resynchronize the controller, on the **Provision>Inventory** window, select the controller that you want to synchronize manually.

13. From the **Actions** drop-down list, choose **Resync**.

14. The following is the list of actions that occur after the process is complete:

    * Catalyst 9800 Series Wireless Controller 1 and Catalyst 9800 Series Wireless Controller 2 are configured with redundancy management, redundancy units, and Single sign-on (SSO). The devices reboot in order to negotiate their role as an active controller or a standby controller. The configuration is synchronized from active to standby.

      >**Note:** If you've configured a AAA server or Cisco ISE server for client and endpoint authentication in Cisco DNA Center then in a HA setup, the CTS credentials for active and standby controllers are synchronized and hence, during a HA switchover, Cisco DNA Center does not update the CTS credentials for the wireless controllers on Cisco ISE.

    * On the **Show Redundancy Summary** window, you can see these configurations:
      - SSO is enabled.
      - The Catalyst 9800 Series Wireless Controller 1 is in the active state.
      - The Catalyst 9800 Series Wireless Controller 2 is in the standby state.

### Demonstration

To watch the steps they are captured in this recording:

<div align="center">
   <a href="https://www.youtube.com/watch?v=yhryDaFBaDk"><img src="https://img.youtube.com/vi/yhryDaFBaDk/0.jpg" style="width=560; height=315;"></a>
</div>

### Documentation:

#### Wireless Design and Configuration Guides

1. [Wireless Design Guide](./guide/cisco-dna-center-sd-access-wl-dg.pdf)
2. [Wireless Controller HA Configuration Guide](./guide/High_Availability_DG.pdf)

#### Catalyst (DNA) Center Guides

1. [User Guide](./guide/cisco_dna_center_ug_2_3_5.pdf)
2. [Wireless Device Provisioning Guide](./guide/provision-wireless-devices.pdf)

## Summary

Congratulations you have reviewed the Wireless Controller HA section. While this could not be performed in the lab it is our hope the documentation, instructions and video demonstration will help cover this section. Please use the navigatation below to continue your learning.

Our thanks to the creator of the video, Jaison Mathew.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Return to Lab Menu**](./README.md)