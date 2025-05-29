# Preparation

We will be using the script server in conjunction with this lab. That together with Catalyst Center, and ISE to configure the various routers and switches in the environment.

## DCLOUD Lab Components

The DCLOUD session includes the following equipment which we will be using:

Virtual Machines:

    Catalyst Center 2.2.3.4 or better
    Identity Services Engine (ISE) 3.0 Patch 4 or better (deployed)
    Script Server - Ubuntu 20.04  or better
    Wireless LAN Controller - C9800 running IOS-XE Bengaluru 17.5.1 code or better
    Windows 10 Jump Host 
    Windows Server 2019 - Can be configured to provide identity, DHCP, DNS, etc.
    Windows 10 Clients

Hardware Devices:

    ISR 4451 Router - 17.06.01a IOS-XE Code
    Catalyst 9300 Switch - 17.06.01 IOS-XE Code with Embedded Wireless Controller (EWC) and ThousandEyes Enterprise Agent
    9130AX Access Points
    Silex Controllers (3 Wired NIC's and 1 Wireless NIC)

The lab envionment that is available is depicted here:

![json](./images/DCLOUD_Topology_Wireless.png?raw=true "Import JSON")

Next we will setup the environment to orchestrate Catalyst Center. Please ensure you are connected via VPN to the DCLOUD Lab.

> [**Next Section**](./03-scriptserver.md)