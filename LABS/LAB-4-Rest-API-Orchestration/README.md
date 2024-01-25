# Catalyst Center REST API with Postman 

This set of Cisco Learning Labs is developed around a set of simple use cases to show both the power of Catalyst Center, the REST APIs, and easy methodologies for execution through Postman.

The Story we will use will be the following, after orientation, we will first integrate ISE with Catalyst Center, and then construct our design. The design comprises of a hierarchy, settings and credentials. With the hierarchy set, we sill discover our pod devices assigned by the instructor and then deploy templates to the pod. After some time we will archive the configurations of the pod, amd then collect the updated inventory. Finally we will send a show CDP neighbor command to the equipment we have been assigned.

## Modules and Content

| Module ID | PubHub Link |
|-----------|-------------|
| catc-catcenter-postman-lab | https://pubhub.cisco.com/detail/#### |

| Lab ID | PubHub link |
|--------|-------------|
| catc-catcenter-0-orientation | https://pubhub.cisco.com/detail/#### |
| catc-catcenter-1-hierarchy | https://pubhub.cisco.com/detail/#### |
| catc-catcenter-2-settings | https://pubhub.cisco.com/detail/#### |
| catc-catcenter-3-discovery | https://pubhub.cisco.com/detail/#### |
| catc-catcenter-4-templates | https://pubhub.cisco.com/detail/#### |
| catc-catcenter-5-archive | https://pubhub.cisco.com/detail/#### |
| catc-catcenter-6-inventory | https://pubhub.cisco.com/detail/#### |
| catc-catcenter-7-cmd-run | https://pubhub.cisco.com/detail/#### |
| catc-catcenter-8-inventory | https://pubhub.cisco.com/detail/#### |
| catc-catcenter-9-cmd-run | https://pubhub.cisco.com/detail/#### |

## Preparation notes

The following section of the README contains information for DevNet Test Drive instructors.

### The DCLOUD environment

For DevNet Test Drive events, use this environment: [DNAC pods for DevNet Test Drives](https://tbv3-ui.ciscodcloud.com/edit/9uxy98sb1wresh3vrw60lfsa7)

The DCLOUD session includes the following equipment.

* Virtual Machines:
  * Cisco Catalyst Center 2.3.5.4 or better
  * Identity Services Engine (ISE) 3.0 Patch 4 or better (deployed)
  * Script Server - Ubuntu 20.04  or better
  * Windows 10 Jump Host 
  * Windows Server 2019 - Can be configured to provide identity, DHCP, DNS, etc.

* Virtual Networking Devices:
  * Catalyst 8000v Router - 17.06.01a IOS-XE Code
  * Catalyst 9300v Switch - 17.12.01 IOS-XE Code 

The following diagram shows the DCLOUD topology.

![DCLOUD LAB TOPOLOGY](./assets/DCLOUD_Topology_A.png?raw=true)

The following diagram shows one of the CML pods topology.

![DCLOUD CML POD TOPOLOGY](./assets/DCLOUD_Topology_B.png?raw=true)

### Management IPs:

This is the pod IP addressing schema that will be used to discover devices within the lab.
Your instructor will assign you a pod number:

| Pod: | Router:     | gi 1         | Switch 1:   | gi 0/0      | Switch2:    | gi 0/0      |
|------|-------------|--------------|-------------|-------------|-------------|-------------|
| 0    | c8000v-p0-1 | 198.18.140.1 | c9000v-p0-1 | 198.18.10.2 | c9000v-p0-2 | 198.18.20.2 |
| 1    | c8000v-p1-1 | 198.18.141.1 | c9000v-p1-1 | 198.18.11.2 | c9000v-p1-2 | 198.18.21.2 |
| 2    | c8000v-p2-1 | 198.18.142.1 | c9000v-p2-1 | 198.18.12.2 | c9000v-p2-2 | 198.18.22.2 |
| 3    | c8000v-p3-1 | 198.18.143.1 | c9000v-p3-1 | 198.18.13.2 | c9000v-p3-2 | 198.18.23.2 |
| 4    | c8000v-p4-1 | 198.18.144.1 | c9000v-p4-1 | 198.18.14.2 | c9000v-p4-2 | 198.18.24.2 |
| 5    | c8000v-p5-1 | 198.18.145.1 | c9000v-p5-1 | 198.18.15.2 | c9000v-p5-2 | 198.18.25.2 |
| 6    | c8000v-p6-1 | 198.18.146.1 | c9000v-p6-1 | 198.18.16.2 | c9000v-p6-2 | 198.18.26.2 |
| 7    | c8000v-p7-1 | 198.18.147.1 | c9000v-p7-1 | 198.18.17.2 | c9000v-p7-2 | 198.18.27.2 |
| 8    | c8000v-p8-1 | 198.18.148.1 | c9000v-p8-1 | 198.18.18.2 | c9000v-p8-2 | 198.18.28.2 |
| 9    | c8000v-p9-1 | 198.18.149.1 | c9000v-p9-1 | 198.18.19.2 | c9000v-p9-2 | 198.18.29.2 |

## Credentials:

| Platform:       | IP Address:    | Username | Password   | 
|-----------------|----------------|----------|------------|
| Catalyst Center | 198.18.129.100 | admin    | C1sco12345 |
| ISE             | 198.18.133.27  | admin    | C1sco12345 |
| Windows AD      | 198.18.133.1   | admin    | C1sco12345 |
| Script Server   | 198.18.133.28  | root     | C1sco12345 |
| Router          | 198.18.14[X].1 | netadmin | C1sco12345 |
| Switch 1        | 198.18.1[X].2  | netadmin | C1sco12345 |
| Switch 2        | 198.18.2[X].2  | netadmin | C1sco12345 |

### DCLOUD VPN Connection

Use AnyConnect VPN to connect to DCLOUD. When connecting, look at the session details and copy the credentials from the session booked into the client to connect.

![DCLOUD VPN CONNECTION](./labs/dntd-catcenter-0-orientation/assets/VPN-to-DCLOUD.png)

## Summary
Cisco Catalyst Center should be set up and ready for the attendees.

## Disclaimer
Various labs are designed for use in the **DCLOUD** environment but can be used elsewhere. The environment allows for use with a web-based browser client for VPN-less connectivity, access as well as AnyConnect VPN client connectivity for those who prefer it. The labs are hosted Globally out of **DCLOUD** Facilities so that you can choose the facility closest to your event. Choose the **DNAC pods for DevNet Test Drives** to access this or any other content, including demonstrations, labs, and training in DCLOUD, please work with your Cisco Account team or Cisco Partner Account Team directly. Your Account teams will make sure the session is scheduled and shared for you to use. Once booked, follow the guide within Github to complete the tasks adhering to the best practices of the DCLOUD environment.
