# Device Discovery

In this module, we will use a **CI/CD Pipeline** to **discover** devices within the network and **assign** them to specific sites within the hierarchy within Cisco DNA Center. 

Cisco DNA Center uses hierarchy to logically align intent (code and configuration) against infrastructure. This allows the network administrator to align changes and modifications to the network within maintenance windows.

## Device Discovery Background

Cisco DNA Center has a Discovery Tool, which allows for the discovery of devices across the network through one of the following methods:

1. CDP
2. LLDP
3. IP Range 

This tool also utilizes credentials for SSH/Telnet/SNMP/HTTPS connections.

Once a device has been discovered, the device is synchronized and deposited within the unassigned space in the inventory. The Administrator then must assign the device to a relevant **site** within the hierarchy. 

In this lab, we will **discover** all the devices within the dCloud lab as specified in the given **CSV** file. The devices will then be automatically be added to the sites as defined in the **CSV**. 

The lab envionment that is available is depicted here:

<p align="center"><img src="./images/DCLOUD_Topology_Wireless.png" width="800" height="894.45"></p>

> **Note**: If ISE is integrated with DNA Center and settings are applied, then the device is also added as a Network Access Device within ISE during the assignment task via **PxGrid Integration**

> **Prerequisites**: **Completed** the previous section **Assign Settings and Credentials**

> [**Next Section**](./02-preparation.md)

