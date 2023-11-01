# Wireless Controller PnP or Discovery

Within this lab module, we will concentrate our efforts on the discovery or PnP of each of the devices by **Cisco DNA Center**, so that we can onboard and gain management of those devices. 

Within this lab we will concentrate on the following which are typical in most Enterprise Networks today:

1. Controller Discovery
2. Access Point switch port configuration
3. Access Point Onboarding

To begin lets review the wireless within the Cisco DCLOUD environment.

### Required Components 

For these labs we will be focusing on the wireless aspects, and while the switching and routing has been setup ahead of time our focus will be on the following:

Virtual Machines:

    DNA Center 2.2.3.4 or better
    Identity Services Engine (ISE) 3.0 Patch 4 or better (deployed)
    Wireless LAN Controller - C9800 running IOS-XE Bengaluru 17.5.1 code or better
    Windows 10 Jump Host 
    Windows Server 2019 - Can be configured to provide identity, DHCP, DNS, etc.
    Windows 10 Clients

Hardware Devices:

    Catalyst 9300 Switch - 17.06.01 IOS-XE Code with Embedded Wireless Controller (EWC) and ThousandEyes Enterprise Agent
    9130AX Access Points
    Silex Controllers (3 Wired NIC's and 1 Wireless NIC)

### Logical Topology

The lab envionment that is available is depicted here:

For routing in the environment an OSPF IGP process has been created to propogate internal route information. Within the access switches which are connected at Layer 3 to the router, we have estansiated a layer 2 port channel between them and initiated various vlans for Access Point connectivity and for the clients, whose gateway is built on an HSRP instance shared between the two switches.

The 9130AX Access Points are connected to both access switches and the ports are automatically configured via the AUTOCONF feature.

![json](./images/DCLOUD_Topology_Wireless-v1.png?raw=true "Import JSON")

## Lab Section 1 - Controller Discovery

To get started with Wireless configuration and automation we first need to onboard the Wireless Controller into DNA Center. In the preparation lab we discovered the rest of the topology, set up the required services, and so we will now concentrate her on the controller. 

While we have the ability to PnP a Wireless Controller typically these are estantiated initially with IP information on the physical hardware. As a result, and because of the current liimitations within the DCLOUD lab, we will concentrate on Discovery methods here. We will cover Controller PnP separately in another module (TBD).

<details open>
<summary> Click for Details and Sub Tasks</summary>

### Step 1 - ***Setup Discovery Job***

1. Open a web browser on the Windows Workstation Jump host. Open a connection to DNA Center and select the hamburger menu icon to open the menu. Select `Tools>Discovery`.

   ![json](./images/module1-pnpdiscovery/dnac-navigation-discovery.png?raw=true "Import JSON")

2. On the Discovery page click `Add Discovery`.

   ![json](./images/module1-pnpdiscovery/dnac-discovery-dashboard.png?raw=true "Import JSON")

3. On the **New Discovery** Page enter the following:
   1. *Discovery Name* for the discovery `Wireless Controller`
   2. Select *Discovery Type* of `IP Address/Range`
   3. Enter *From - To* fields with `198.18.134.100`

      ![json](./images/module1-pnpdiscovery/dnac-discovery-new.png?raw=true "Import JSON")

4. Scroll down the page to Credentials. The credentials on the controller are different to those of the Global settings shown. DNA Center allows for us to use separate credentials where necesssary. Do the following;
   1. Click **Add Credentials**

      ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-creds.png?raw=true "Import JSON")

   2. Click the *CLI* tab
   3. Enter the following:
      - *Name* as `admin`
      - *Username* as `admin`
      - *Password* as `C1sco12345`
      - *Enable Password* as `C1sco12345`
      - Click *Save* to add the credential 
      - a Warning will appear after the Save. Click `Ok` this is expected.

        ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-cli.png?raw=true "Import JSON")
        ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-cli-warning.png?raw=true "Import JSON")
        ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-cli-results.png?raw=true "Import JSON")

   4. Click the *SNMPv2c* tab
      1. Enter the following on the *READ* sub-tab:
         - *Name* as `public`
         - *Read Community* as `public`
         - Click *Save* to add the credential 

           ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-snmpro.png?raw=true "Import JSON")

           ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-snmpro-results.png?raw=true "Import JSON")

      2. Click and Enter the following on the *WRITE* sub-tab:
         - *Name* as `private`
         - *Write Community* as `private`
         - Click *Save* to add the credential 

           ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-snmprw.png?raw=true "Import JSON")

           ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-snmprw-results.png?raw=true "Import JSON")

   5. If *NETCONF* was not enabled for some reason click the *NETCONF* tab

      ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-netconf-results.png?raw=true "Import JSON")

   6. Enter the following:
      - *Port* as `830`
   7. Click *Save*

      ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-netconf.png?raw=true "Import JSON")
      
      ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-netconf-results.png?raw=true "Import JSON")

   8. Close the **Add Credentials** Slide Out App.
5. Review and deselect unused credentials as shown for this device.

   ![json](./images/module1-pnpdiscovery/dnac-discovery-new-select-creds.png?raw=true "Import JSON")

6. Ensure *NETCONF* is enabled as shown.

      ![json](./images/module1-pnpdiscovery/dnac-discovery-new-add-netconf-results.png?raw=true "Import JSON")

7. Click **Discover** to start the device discovery.

   ![json](./images/module1-pnpdiscovery/dnac-discovery-begin.png?raw=true "Import JSON")

8. Click Start to begin the discovery process.

   ![json](./images/module1-pnpdiscovery/dnac-discovery-begin-schedule.png?raw=true "Import JSON")

9. When the Discovery is complete the summary should show as the following:

   ![json](./images/module1-pnpdiscovery/dnac-discovery-results.png?raw=true "Import JSON")

### Step 2 - ***Assign Controller to Site***

1. Navigate to the Inventory through the menu. Select `Provision>Network Devices>Inventory`

   ![json](./images/module1-pnpdiscovery/dnac-navigation-inventory.png?raw=true "Import JSON")

2. After some time the Wireless Controller will appear as shown in the inventory.
3. Click the *Assign* link to begin the assignment of the Wireless Controller.

   ![json](./images/module1-pnpdiscovery/dnac-inventory-assign.png?raw=true "Import JSON")

4. Click *Choose a site*.

   ![json](./images/module1-pnpdiscovery/dnac-inventory-choose.png?raw=true "Import JSON")

5. Select *Floor 1* from the hierarchy and click *Save*.

   ![json](./images/module1-pnpdiscovery/dnac-inventory-hierarchy.png?raw=true "Import JSON")

6. Click *Next* to complete the get to the summary.

   ![json](./images/module1-pnpdiscovery/dnac-inventory-hierarchychosen.png?raw=true "Import JSON")

7. Review the *Summary* and click next.

   ![json](./images/module1-pnpdiscovery/dnac-inventory-hierarchysummary.png?raw=true "Import JSON")

8. Click *Assign* to assign the device to the site.

   ![json](./images/module1-pnpdiscovery/dnac-inventory-assignment.png?raw=true "Import JSON")

9. At this point the Wireless Controller will show as assigned to the site `Floor 1`

   ![json](./images/module1-pnpdiscovery/dnac-inventory-assignment-results.png?raw=true "Import JSON")

</details>

## Lab Section 2 - PnP of Wireless Controller 

The lab within DCLOUD does not today have the ability to run PnP of the Controller, but please check out this video which explains the process. 

<div align="center">
   <a href="https://www.youtube.com/watch?v=Vl7AfhNaGuc"><img src="https://img.youtube.com/vi/Vl7AfhNaGuc/0.jpg" style="width=560; height=315;"></a>
</div>

## Summary

Congratulations you have completed the Controller Discovery module of the lab and the Wireless LAN Controller is ready for configuration and provisioning. Please use the navigatation below to continue your learning.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Continue to WLAN Creation Module**](../LAB-J-Wireless-Automation/module2-wlans.md)

> [**Return to Lab Menu**](./README.md)
