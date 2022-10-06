# In Development
![json](./images/underconstruction.png?raw=true "Import JSON")

## Controller PnP or Discovery
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

### Physical Topology
The lab envionment that is available is depicted here:

![json](../LAB1-PNP-PREP/images/DCLOUD_Topology2.png?raw=true "Import JSON")

### Logical Topology
The lab envionment that is available is depicted here:

![json](./images/DCLOUD_Topology_Wireless-v1.png?raw=true "Import JSON")







## Lab Section 1 - DNA Center and ISE Integration
In this lab our focus changes slightly as we start to automate for host onboarding. A large component of host onboarding is the authentication of hosts and assignment within the network. In this section and in preparation for the steps which follow we will integrate DNA Center with Identity Services Engine. This integration allows pxGrid communication between the two and allows for automation of configuration within ISE for Network Access Devices, SGT, SGACL, and Policys.

### Step 1 - ***Prepare ISE for DNA Center Integration***
1. Open a web browser on the Windows Workstation Jump host. Open a connection to Identity Services Engine (ISE) and select the hamburger menu icon to open the system menu.

## Summary
Congratulations you have completed the XXX module of the lab and . Please use the navigatation below to continue your learning.

## Lab Modules
The lab will be split into modules to concentrate on specific tasks. Eash is designed to build your knowledge in specific areas and they will call out any dependancies on previous modules. We will cover are the following which you can access via the links below:

1. [**Controller PnP or Discovery**](./module1-pnpdiscovery.md)
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
