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
