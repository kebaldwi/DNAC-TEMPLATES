# Preparation

We will be using the script server in conjunction with this lab. That together with Catalyst Center, and ISE to configure the various routers and switches in the environment.

## DCLOUD Lab Components

For this Lab, use this environment: [DNAC pods for DevNet Test Drives](https://tbv3-ui.ciscodcloud.com/edit/9uxy98sb1wresh3vrw60lfsa7)

The DCLOUD session includes the following equipment which we will be using:

Virtual Machines:

    Catalyst Center 2.3.5.6 or better
    Identity Services Engine (ISE) 3.0 Patch 4 or better (deployed)
    Script Server - Ubuntu 20.04  or better
    Wireless LAN Controller - C9800 running IOS-XE Bengaluru 17.5.1 code or better
    Windows 10 Jump Host 
    Windows Server 2019 - Can be configured to provide identity, DHCP, DNS, etc.
    Windows 10 Clients

Virtual Networking Devices:

    Catalyst 8000v Router - 17.06.01a IOS-XE Code
    Catalyst 9300v Switch - 17.12.01 IOS-XE Code 

The lab envionment that is available is depicted here:

![DCLOUD LAB TOPOLOGY](../assets/DCLOUD_Topology_A.png?raw=true)

The following diagram shows one of the CML pods topology:

![DCLOUD CML POD TOPOLOGY](../assets/DCLOUD_Topology_B.png?raw=true)

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

### Credentials:

| Platform:       | IP Address:    | Username | Password   | 
|-----------------|----------------|----------|------------|
| Catalyst Center | 198.18.129.100 | admin    | C1sco12345 |
| ISE             | 198.18.133.27  | admin    | C1sco12345 |
| Windows AD      | 198.18.133.1   | admin    | C1sco12345 |
| Script Server   | 198.18.133.28  | root     | C1sco12345 |
| Router          | 198.18.14[X].1 | netadmin | C1sco12345 |
| Switch 1        | 198.18.1[X].2  | netadmin | C1sco12345 |
| Switch 2        | 198.18.2[X].2  | netadmin | C1sco12345 |

Next we will setup the environment to orchestrate Catalyst Center. Please ensure you are connected via VPN to the DCLOUD Lab.

> [**Next Section**](./03-integration.md)