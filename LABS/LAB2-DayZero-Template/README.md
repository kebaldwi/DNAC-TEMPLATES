# Onboarding Template [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
## Overview
This Lab is designed to be a standalone lab ot be used either in the DCLOUD environment or as part of the setup for a Proof ov Concept at a customers lab. This information may also help from a deployment or implementation point of view to ensure that all the necessary steps are complete prior to onboarding any devices within DNA Center.

## General Information
As you may recall in the informational sections of this repository we set for the various methods of discovery for a device and the preliminary things required for true zero touch provisioning. Those concepts will be set up in this lab so as to ensure a successful connection to DNA Center.

## Lab Section 1 - Device Connectivity
For PnP processes to work our intention is to have a management interface on the device in this lab we will set up a Loopback interface for management and a Vlan interface for connectivity. Obviously, you don't have to do it this way we are just giving a relatively complicated example and you can alter this to suite your needs. As the device is connected to the front facing ports by default there is little configuration. 

By default the target switch is using vlan 1 as no other vlan exists, and vlan 1 by default accepts DHCP addresses. This will be used in the pnp process. Our management vlan however, may be a different vlan, and so may the native vlan structure of our environment. To that end we must make use of the *pnp startup-vlan* command which allows the device to use this vlan in pnp and needs to be configured on the upstream switch.

### Step 1.1 - ***Upstream Neighbor Setup***
For the purposes of the lab we will utilize ***vlan 10*** as the management vlan. Connect to switch ***TBD*** and paste the following configuration:

```
config t
pnp startup-vlan 5
```

This command will program the target switches port connected with a trunk and automatically add the vlan and SVI to the target switch making that vlan ready to accept a DHCP address. This is available on switches running 16.6 code or greater as upstream neighbors. Older switches or upstream devices that are not capable of running the command should be onboarded in vlan 1 and the vlan modified as part of the onboarding process.

### Step 1.2 - ***DHCP Setup***
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

During this lab setup please choose which option you wish to use for DHCP for PnP services and follow that subsection.

#### Step 1.2a - ***IOS DHCP Configuration***
Configured on a IOS device it would look like this example:

```
  ip dhcp pool pnp_device_pool                         
     network 192.168.5.0 255.255.255.0                 
     default-router 192.168.5.1                        
     dns-server 198.18.133.1                           
     domain-name dcloud.cisco.com                      
     option 43 ascii "5A1N;B2;K4;I198.18.129.1;J80"   
```

If we want to use the IOS DHCP Configuration method connect to switch ***TBD*** and paste the following configuration:

```
  ip dhcp pool pnp_device_pool                         
     network 192.168.5.0 255.255.255.0                  
     default-router 192.168.5.1                         
```

Next we will introduce the helper address statement on the management Vlan's SVI. Connect to switch ***TBD*** and paste the following configuration:

```
  interface Vlan 5                         
     ip helper-address 192.168.5.1                  
```

For a full configuration example please see [Configuring the Cisco IOS DHCP Server](https://www.cisco.com/en/US/docs/ios/12_4t/ip_addr/configuration/guide/htdhcpsv.html#wp1046301)

#### Step 1.2b - ***Windows Server Configuration***
If we want to use the Windows DHCP method connect to the windows server. On windows you have two options to deploy DHCP scopes the UI or PowerShell. We will deploy the scope via PowerShell. Paste the following into powershell to create the required DHCP scope:

```
Add-DhcpServerv4Scope -Name "DNAC-Templates-Lab" -StartRange 192.168.5.1 -EndRange 192.168.5.254 -SubnetMask 255.255.255.0 -LeaseDuration 6.00:00:00 -SuperScope "PnP Onboarding"
Set-DhcpServerv4OptionValue -ScopeId 192.168.5.0 -Router 192.168.5.1 
```

The DHCP scope will look like this in Windows DHCP Administrative tool:

![json](./images/WindowsDHCPscope.png?raw=true "Import JSON")

Next we will introduce the helper address statement on the management Vlan's SVI. Connect to switch ***TBD*** and paste the following configuration:

```
  interface Vlan 5                         
     ip helper-address 192.168.5.1                  
```

## Lab Section 2 - DNA Center Discovery
As you may recall in order to land on DNA Center though the device needs help in finding it. 

The PnP components are as follows:

![json](../../images/pnp-workflows.png?raw=true "Import JSON")

There are 3 automated methods to make that occur:

1. **DHCP with option 43** - ***requires the DHCP server offer a PnP string via option 43***
2. **DNS lookup** - ***requires the DHCP server offer a domain suffix and a name server to resolve the **pnpserver** address***
3. **Cloud re-direction via https://devicehelper.cisco.com/device-helper** - ***requires the DHCP server offer a name server to make DNS resolutions***

### Step 2.1 - ***DNA Center Discovery***
Please choose one of the following subsections as the discovery method.

#### Step 2.1a - ***Option 43 with IOS DHCP Configuration***
If using the IOS DHCP Server and the Option 43 discovery method is desired then paste the following configuration:

```
  ip dhcp pool pnp_device_pool                    
     option 43 ascii "5A1N;B2;K4;I198.18.129.1;J80"
```

#### Step 2.1b - ***Option 43 with Windows DHCP Configuration***
If using the Windows DHCP Server and the Option 43 discovery method is desired then paste the following configuration into PowerShell:

```
Set-DhcpServerv4OptionValue -ScopeId 192.168.5.0 -OptionId 43 -Value ([System.Text.Encoding]::ASCII.GetBytes("5A1N;B2;K4;I198.18.129.1;J80"))
```

The DHCP scope will be modified to look like this in Windows DHCP Administrative tool:

![json](./images/DNACDHCPoption43.png?raw=true "Import JSON")

#### Step 2.1c - ***DNS Lookup with IOS DHCP Configuration***
If using the IOS DHCP Server and the DNS Lookup discovery method is desired then paste the following configuration:

```
  ip dhcp pool pnp_device_pool                          
     dns-server 198.18.133.1                           
     domain-name dcloud.cisco.com                       
```

Next add the DNS entries to allow for the DNA Center to be discovered. This script will add an A host entry for the VIP address, and then a CNAME as an alias for the pnpserver entry required for DNS discovery.

```
Add-DnsServerResourceRecordA -Name "dnac-vip" -ZoneName "dcloud.cisco.com" -AllowUpdateAny -IPv4Address "198.18.129.1" -TimeToLive 01:00:00
Add-DnsServerResourceRecordCName -Name "pnpserver" -HostNameAlias "dnac-vip.dcloud.cisco.com" -ZoneName "dcloud.cisco.com"
```

The DNS Zone will look like this in Windows DNS Administrative tool:

![json](./images/DNACenterDNSentries.png?raw=true "Import JSON")

#### Step 2.1d - ***DNS Lookup with Windows DHCP Configuration***
If using the Windows DHCP Server and the DNS Lookup discovery method is desired then paste the following configuration into PowerShell:

```
Set-DhcpServerv4OptionValue -ScopeId 192.168.5.0 -DnsServer 198.18.133.1 -DnsDomain "dcloud.cisco.com"
```

The DHCP scope will be modified to look like this in Windows DHCP Administrative tool:

![json](./images/WindowsDHCPscope.png?raw=true "Import JSON")

Next add the DNS entries to allow for the DNA Center to be discovered. This script will add an A host entry for the VIP address, and then a CNAME as an alias for the pnpserver entry required for DNS discovery.

```
Add-DnsServerResourceRecordA -Name "dnac-vip" -ZoneName "dcloud.cisco.com" -AllowUpdateAny -IPv4Address "198.18.129.1" -TimeToLive 01:00:00
Add-DnsServerResourceRecordCName -Name "pnpserver" -HostNameAlias "dnac-vip.dcloud.cisco.com" -ZoneName "dcloud.cisco.com"
```

The DNS Zone will look like this in Windows DNS Administrative tool:

![json](./images/DNACenterDNSentries.png?raw=true "Import JSON")

## Lab Section 3 - Target Connectivity
The Target switch will typically be connected to either a single port or as part of a port channel. The port where the Target switch will be connected needs for this lab to be connected as a trunk. 

```
interface gi 1/0/48
description PnP Test Environment
switchport mode trunk
switchport trunk allowed vlan 5
```

If a port channel is used initially, then you want to ensure that the port channel can operate as a single link within the bundle and for that reason use passive methods for building the port channel bundles on both the Target and Upstream Neighbor for maximum flexibility.

## Lab Section 4 - Testing
Please use the testing for the DNS Discovery method used above

### Step 4.1a - DNS Resolution Tests
To test the environment to ensure its ready, we need to test a few things.

First from a windows host use the nslookup command to resolve ***pnpserver.dcloud.cisco.com***. Connect to the windows workstation and within the search window search for CMD. Open the application and type the following command:

```
nslookup pnpserver.dcloud.cisco.com
```

They should be presented with the following output or something similar which shows the resolution of the alias to the A host record entry which identifies the VIP address for the DNA Center Cluster.

### Step 4.1b - DNS Resolution
Second we need to ensure the DNA Center responds on the VIP, so use the ping command within the CMD application window previously opened as follows:

```
ping pnpserver.dcloud.cisco.com
```

The following is the output expected from 3.1a and 3.1b

![json](./images/DNACenterDNStests.png?raw=true "Import JSON")

At this point the environment should be set up to onboard devices within Vlan 5 using the network address ***192.168.5.0/24*** utilizing either ***option 43*** or ***DNS Discovery***.

## Summary
The next step would be to build the PnP Onboarding settings and template on DNA Center which will be covered in the next lab entitled [Onboarding Templates](../LAB2-DayZero-Template/README.md#Day0) - This section explains in depth and how to deploy Day 0 templates

## Feedback
If you found this set of Labs helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
