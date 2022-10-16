# In Development
![json](./images/underconstruction.png?raw=true "Import JSON")

## Wireless LAN Design
Within this lab module, we will concentrate our efforts on the design aspects of creating Wireless LANs (WLANs) via **DNA Center**. Previously we have discovered the Wireless LAN Controller by **Cisco DNA Center**, and assigned it to a site within the hierarchy. At this point we will configure the various settings for the Wireless Design.

Within this lab we will concentrate on the following which are typical in most Enterprise Networks today:
1. Wireless LAN Creation
2. Wireless Profiles
3. RF Profiles
4. FlexConnect 
5. Controller Provisioning

### Logical Topology
To review the lab envionment that is available is depicted here:

For routing in the environment an OSPF IGP process has been created to propogate internal route information. Within the access switches which are connected at Layer 3 to the router, we have estansiated a layer 2 port channel between them and initiated various vlans for Access Point connectivity and for the clients, whose gateway is built on an HSRP instance shared between the two switches.

The 9130AX Access Points are connected to both access switches and the ports are automatically configured via the AUTOCONF feature.

![json](./images/DCLOUD_Topology_Wireless-v1.png?raw=true "Import JSON")

The clients will be connected connected to the network via FlexConnect due to the nature of the DCLOUD labs design. Where applicable we will call out the differences between FlexConnect and Local Mode Design.

The Wireless Clients will associate and connect to the SSID's within the lab and will then be dropped into one of the following VLAN via the trunk from the FlexConnect Access Point.

1. Vlan 20 - datavlan - 192.168.20.0/24
2. Vlan 30 - voicevlan - 192.168.30.0/24
3. Vlan 40 - guestvlan - 192.168.40.0/24

For simplicity we may utilize the Vlan 30 as a second Data network when proving out CoA or AAA Overide features.

## Lab Section 1 - Wireless LAN's
To get started with Wireless Controller configuration and automation we first need to build the settings, Wireless LAN environments and associated profiles for deployment. Each Wireless LAN can be built by DNA Center and all settings may be deployed either through the UI, from Model-Based Config (covered separately), and by Templates (covered separately)for extranious configuration which might be required.

This section will be devoted to building Wireless LAN's. Subsequent sections will cover the profiles and provisioning.

### Building a PreShared Key (PSK) Wireless LAN
In this subsection we will build a Wireless LAN for PSK authentication. 

#### Step 1 - ***Create SSID***
1. Open a web browser on the Windows Workstation Jump host. Open a connection to DNA Center and select the hamburger menu icon to open the menu. Select `Design>Network Settings`.

![json](./images/module2-wlans/dnac-menu-network-settings.png?raw=true "Import JSON")

2. On the Network page click the `Wireless` tab to navigate to the wireless page.

![json](./images/module2-wlans/dnac-navigation-wireless-settings.png?raw=true "Import JSON")

3. On the **Wireless** page click `Add` above the *SSID* section to create a new Wireless LAN

![json](./images/module2-wlans/dnac-wireless-ssid-psk-begin.png?raw=true "Import JSON")

4. A Wireless SSID workflow will begin which will guide you through the build process of the WLAN. Complete the following steps:
   1. Enter the *Wireless Network Name (SSID)* as `CAMPUS-PSK`
   2. **Dual Band Operation (2.4 Ghz and 5 Ghz)** *enables the SSID for dual band operation*
   3. **Voice and Data** *configuring best practices for Both Voice and Data*
   4. **Admin Status** *enables the SSID*
   5. **Broadcast SSID** *enables the SSID to be broadcast allowing clients to see it*

   ![json](./images/module1-pnpdiscovery/dnac-wireless-ssid-psk-name.png?raw=true "Import JSON")



## Lab Modules
The lab will be split into modules to concentrate on specific tasks. Eash is designed to build your knowledge in specific areas and they will call out any dependancies on previous modules. We will cover are the following which you can access via the links below:

1. [**Wireless Controller PnP or Discovery**](./module1-ctrlpnpdiscovery.md)
2. [**WLAN Creation**](./module2-wlans.md)
3. [**Controller HA**](./module3-controllerha.md)
4. [**AP Provisioning**](./module4-approvisioning.md)
5. [**Application QoS**](./module5-applicationqos.md)
6. [**Model Based Config**](./module6-modelbasedconfig.md)
7. [**Wireless Templates**](./module7-wirelesstemplates.md)

## Main Menus
To return to the main menus
1. [Wireless Automation Main Menu](./README.md)
2. [DNAC-TEMPLATES-LABS Main Menu](../README.md)
3. [DNAC-TEMPLATES Repository Main Menu](../../README.md)

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
