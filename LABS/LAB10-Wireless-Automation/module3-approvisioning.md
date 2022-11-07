# Wireless Access Point Provisioning
Within this lab module, we will concentrate our efforts on the PnP of each of the access points by **Cisco DNA Center**, so that we can onboard and gain management of those devices. 

Within this lab we will concentrate on the following which are typical in most Enterprise Networks today:

1. DHCP Address Scope
2. DNA Center Discovery
3. Access Point switch port configuration
4. Access Point Onboarding

To begin lets review the wireless within the Cisco DCLOUD environment.

## Required Components 
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

## Logical Topology
The lab envionment that is available is depicted here:

For routing in the environment an OSPF IGP process has been created to propogate internal route information. Within the access switches which are connected at Layer 3 to the router, we have estansiated a layer 2 port channel between them and initiated various vlans for Access Point connectivity and for the clients, whose gateway is built on an HSRP instance shared between the two switches.

The 9130AX Access Points are connected to both access switches and the ports are automatically configured via the AUTOCONF feature.

![json](./images/DCLOUD_Topology_Wireless-v1.png?raw=true "Import JSON")

# Lab Section 1 - Access Point PnP
In the preparation lab we discovered the rest of the topology, set up the required services, and part of those services were DHCP addresses which are help within scopes on the Windows AD Server. 

There are a few options for discovery using PnP. These were thoroughly discussed in the switching section and in a tutorial in the main menu. 

## Background 
In order to land on DNA Center though the device needs help in finding it. 

The PnP components are as follows:

![json](./images/approvisioning/pnp-workflows.png?raw=true "Import JSON")

There are 3 automated methods to make that occur:

1. **DHCP with option 43**
```
   PnP string: 5A1D;B2;K4;I198.18.129.100;J80 added to DHCP Server
``` 
2. **DNS lookup**
``` 
   pnpserver.dcloud.cisco.com resolves to DNA Center VIP Address
```
3. **Cloud re-direction https://devicehelper.cisco.com/device-helper**
   **which, re-directs to on-prem DNA Center IP Address**

**Option 1:** requires that along with the IP address and gateway the DHCP server must offer a PnP string via option 43. This option is often used with Cisco wireless so you may want to incorporate option 60 and the use of vendor specific information to ensure the correct controller is referenced for the device in question. 

**Option 2:** requires that along with the IP address and gateway the DHCP server offer the domain suffix that the **pnpserver** record will reside in and a name server to resolve the address. Caveats here would be that if not all devices were to be landing on DNA Center then you may need sub domains.

**Option 3:** requires that along with the address and gateway the DHCP server offer a name server to resolve the address of **device-helper.cisco.com**. Additionally it requires the that DNA Center register a file with the PnP Connect portal which it will offer via SSL to a device which reaches out. In order to whitelist those devices, the serial number would have to be associated to the DNAC profile within software centrals pnp connect portal.

![json](images/pnp-connect.png?raw=true "Import JSON")

Once one of the options has been built devices will get the address and be pointed to and land on DNA Center within the PnP Device list.

## Step 1 - ***DHCP as a Discovery Method***
DHCP services are important to understand primarily because along with the address and the gateway for connectivity is assigned option 43 which primes or directs the Cisco Access Point towards **DNA Center** or typically a **Wireless Controller**.

![json](./images/module1-pnpdiscovery/dhcp-lab-scope.png?raw=true "Import JSON")

Within the Scopes is a scope for the Access Point Vlan, aptly named *APVLAN* and within that you will see option 43 defined which is given to all clients within the scope.

![json](./images/module1-pnpdiscovery/dhcp-apvlan-option43.png?raw=true "Import JSON")

### Step 2 - ***Access Point Port Configuration***
The second part of the PnP equation is setting the environment up to allow for the device to get the address in question. This was previously accomplished in the setup procedure of the lab utilizing a template which was auto provisioned to the switch after discovery.

The Switch was configured to automatically configure switch ports with connected Access Points with the following configuration. This was accomplished through *AUTOCONF* as explained in previous labs 7 and 8.

This is only one way of accomplishing this task, many others can be used, as was proven out in lab 8, with zero trust environment, and change of authorization being the catalyst for deploying an `interface template`.

In this lab as we are focusing on Wireless, the port configuration was automatically assigned via *AUTOCONF* for simplicity.

The switch port configuration used in this lab is:

```
				c9300-1#sh der int gi 1/0/2
                Building configuration...
                
                Derived configuration : 261 bytes
                !
                interface GigabitEthernet1/0/2
                 description Access Point Interface
                 switchport access vlan 999
                 switchport trunk native vlan 10
                 switchport trunk allowed vlan 10,20,30,40,999
                 switchport mode trunk
                 spanning-tree portfast
                 spanning-tree bpduguard enable
                end
```

### Step 3 - ***Access Point Claim*** TBC
The Access Points are typically in varied state, use the DCLOUD UI to console into each one then complete the following steps to clear them of any configuration:

1. Login to the Access Point with the following credentials: 
   - Username: Cisco
   - Password: Cisco
2. Enter privileged mode by issuing the command `enable`
3. when prompted for the enable password use the following credential:
   - Enable Password: Cisco
4. At the command prompt issue the following command, `capwap ap erase all`
5. When prompted enter at the `[confirm]` prompt.
6. The AP will clear its config and reboot.
7. After a few moments have passed check the PnP Claim page and the AP should be in the list.


1. Open a web browser on the Windows Workstation Jump host. Open a connection to DNA Center and select the 

## Summary
Congratulations you have completed the XXX module of the lab and . Please use the navigatation below to continue your learning.

## Lab Modules
The lab will be split into modules to concentrate on specific tasks. Eash is designed to build your knowledge in specific areas and they will call out any dependancies on previous modules. We will cover are the following which you can access via the links below:

1. [**Wireless Controller PnP or Discovery**](./module1-ctrlpnpdiscovery.md)
2. [**WLAN Creation**](./module2-wlans.md)
3. [**AP Provisioning**](./module3-approvisioning.md)
4. [**Application QoS**](./module4-applicationqos.md)
5. [**Model Based Config**](./module5-modelbasedconfig.md)
6. [**Wireless Templates**](./module6-wirelesstemplates.md)
7. [**Controller HA**](./module3-controllerha.md)

## Main Menus
To return to the main menus
1. [Wireless Automation Main Menu](./README.md)
2. [DNAC-TEMPLATES-LABS Main Menu](../README.md)
3. [DNAC-TEMPLATES Repository Main Menu](../../README.md)

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
