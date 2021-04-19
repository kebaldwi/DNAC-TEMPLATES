# PnP Preparation [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
## Overview
This Lab is designed to be a standalone lab ot be used either in the DCLOUD environment or as part of the setup for a Proof ov Concept at a customers lab. This information may also help from a deployment or implementation point of view to ensure that all the necessary steps are complete prior to onboarding any devices within DNA Center.

## General Information
As you may recall in the informational sections of this repository we set for the various methods of discovery for a device and the preliminary things required for true zero touch provisioning. Those concepts will be set up in this lab so as to ensure a successful connection to DNA Center.

## Lab Section 1 - Device Connectivity
For PnP processes to work our intention is to have a management interface on the device in this lab we will set up a Loopback interface for management and a Vlan interface for connectivity. Obviously, you don't have to do it this way we are just giving a relatively complicated example and you can alter this to suite your needs. As the device is connected to the front facing ports by default there is little configuration. 

By default the target switch is using vlan 1 as no other vlan exists, and vlan 1 by default accepts DHCP addresses. This will be used in the pnp process. Our management vlan however, may be a different vlan, and so may the native vlan structure of our environment. To that end we must make use of the *pnp startup-vlan* command which allows the device to use this vlan in pnp and needs to be configured on the upstream switch.

### Step 1 - ***Upstream Neighbor Setup***
Connect to the upstream switch and configure the following:
```
config t
pnp startup-vlan 100
```

This command will program the target switches port connected with a trunk and automatically add the vlan and SVI to the target switch making that vlan ready to accept a DHCP address. This is available on switches running 16.6 code or greater as upstream neighbors. Older switches or upstream devices that are not capable of running the command should be onboarded in vlan 1 and the vlan modified as part of the onboarding process.

### Step 2 - ***DHCP Setup***
We need a DHCP scope to supply the address within the management network temporarily in order to complete the configuration and onboarding. The scope should be configured to offer addresses from part of the range of addresses leaving the other part of the scope for the static addresses. It also can be a reservation as DHCP servers can reserve addresses for specific MAC addresses, one benefit of this is DNS host entries are automatically updated sometimes depending on the DHCP Server.

The DHCP scope would incorporate therefore the following which would be enough to get an address:

* network
* default gateway
* domain - ***required if option 2 is used below***
* name-server ip - ***required if option 2 or 3 is used below***
* DHCP relay or helper statement - ***to be added to the gateway interface pointing to the DHCP server***

The DHCP Scope should be added to one of the following, the first two of these will be covered in this lab.

1. Switch or Router
2. Windows DHCP Server
3. InfoBlox or other 3rd party server

#### IOS DHCP Configuration Example
Configured on a IOS device it would look like this example:

```
  ip dhcp pool pnp_device_pool                          <-- Name of DHCP pool
     network 192.168.1.0 255.255.255.0                  <-- Range of IP addresses assigned to clients
     default-router 192.168.1.1                         <-- Gateway address
     dns-server 192.168.1.254                           <-- DNS server option
     domain-name dcloud.cisco.com                       <-- Domain name suffix option
     option 43 ascii "5A1N;B2;K4;I172.19.45.222;J80".   <-- Option 43 string option
```

For a full configuration example please see [Configuring the Cisco IOS DHCP Server](https://www.cisco.com/en/US/docs/ios/12_4t/ip_addr/configuration/guide/htdhcpsv.html#wp1046301)

#### Windows Server Configuration Example
On windows you have two options to deploy DHCP scopes the UI or PowerShell. We will show you Option 43 set up on a specific scope but it can be quickly replicated to other scopes using the binary entry gathered from a dhcp dump via netshell. That said here is what the option looks like as configured as option 43:

![json](../../images/WindowsDHCP.png?raw=true "Import JSON")



