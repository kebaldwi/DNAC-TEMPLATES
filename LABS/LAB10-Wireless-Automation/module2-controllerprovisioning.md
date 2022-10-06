# In Development
![json](./images/underconstruction.png?raw=true "Import JSON")

## Wireless PnP or Discovery
Within this lab module, we will concentrate our efforts on the discovery or PnP of each of the devices by **Cisco DNA Center**, so that we can onboard and gain management of those devices. The lab within DCLOUD does not today have the ability to run PnP of the Controller, but that is possible and we will have a separate section to talk about those aspects. 

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

At this point the Wireless Controller is onboarded and ready for configuration and provisioning. We will start that process in the following lab called [**WLAN Creation**](./module3-wlans.md).

## Lab Section 2 - Access Point PnP
In the preparation lab we discovered the rest of the topology, set up the required services, and part of those services were DHCP addresses which are help within scopes on the Windows AD Server. 

There are a few options for discovery using PnP. These were thoroughly discussed in the switching section and in a tutorial in the main menu. 

#### Background 
In order to land on DNA Center though the device needs help in finding it. 

The PnP components are as follows:

![json](images/pnp-workflows.png?raw=true "Import JSON")

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

### Step 1 - ***DHCP as a Discovery Method***
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

### Step 3 - ***Access Point Claim***
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

1. [**Wireless Controller PnP or Discovery**](./module1-pnpdiscovery.md)

2. [**Controller HA**](./module2-controllerha.md)
3. [**WLAN Creation**](./module3-wlans.md)
4. [**AP Provisioning**](./module4-approvisioning.md)
5. [**Application QoS**](./module5-applicationqos.md)
6. [**Model Based Config**](./module6-modelbasedconfig.md)
7. [**Wireless Templates**](./module7-wirelesstemplates.md)

## Main Menus
To return to the main menus
1. [Wireless Automation Main Menu](./README.md)
2. [DNAC-TEMPLATES-LABS Main Menu](../README.md)
3. [DNAC-TEMPLATES Repository Main Menu](.../README.md)

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
