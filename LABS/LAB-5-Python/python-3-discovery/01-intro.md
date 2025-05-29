# Device Discovery

In this module, we will use **Python** to discover devices within the network and **assign** them to specific sites within the hierarchy within Catalyst Center.  

Catalyst Center uses hierarchy to logically align intent (code and configuration) against infrastructure. This allows the network administrator to align changes and modifications to the network within maintenance windows.

## Device Discovery Background

Catalyst Center has a Discovery Tool, which allows for the discovery of devices across the network through one of the following methods:

1. CDP
2. LLDP
3. IP Range 

This tool also utilizes credentials for SSH/Telnet/SNMP/HTTPS connections.

Once a device has been discovered, the device is synchronized and deposited within the unassigned space in the inventory. The Administrator then must assign the device to a relevant **site** within the hierarchy. 

In this lab, we will **discover** all the devices within the DCLOUD lab as specified in the given **CSV** file. The devices will then be automatically be added to the sites as defined in the **CSV**. 

The lab envionment that is available is depicted here:

<p align="center"><img src="../assets/DCLOUD_Topology_B.png" width="800" height="686.75"></p>

> **Note**: If ISE is integrated with Catalyst Center and settings are applied, then the device is also added as a Network Access Device within ISE during the assignment task via **PxGrid Integration**

> **Prerequisites**: **Completed** the previous section [**Deploy Settings and Credentials**](../python-2-settings/01-intro.md)

> [**Next Section**](./02-examine.md)

