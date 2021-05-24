# PnP Preparation 
## Overview
This lab is the first one in a series of labs. You may use the steps in the DCLOUD environment, or equally, you might utilize them as part of a Proof of Concept setup at a customer's lab. These procedures may also help form part of a deployment or implementation. Use them to ensure that all the necessary steps are complete before onboarding any devices within DNA Center.

We will be utilizing the lab in this manner:
![json](./images/DCLOUD_Topology_PnPLab.png?raw=true "Import JSON")

## General Information
As you may recall, in the informational sections of this repository, we set for the various methods of discovery for a device and the preliminary things required for proper zero-touch provisioning. This lab will ensure a successful connection to DNA Center by helping to deploy the initial concepts.

### Lab Preparation
To set up the lab, please log into the console connection to the ***4451X*** and issue the following commands:

```
!
conf t
!
!disable port 0/0/2 for the templating lab
int gi 0/0/2
 shutdown
 end
!
wr
!
```

## Lab Section 1 - Device Connectivity
For PnP processes to work, we intend to have a management interface on the device. In this lab, we will set up a VLAN interface for both management and connectivity. You don't have to do it this way; we are just giving a relatively uncomplicated example, and you can alter this to suit your needs. As the device connects to the front-facing ports, we have to rely on the default configuration. 

As you may recall, a factory default configuration is using VLAN one as no other VLAN exists, and by default, it accepts DHCP addresses. We can use this method in the PnP process. However, the management VLAN may be different, and so may the native VLAN structure of our environment. To that end, we must use the *pnp startup-vlan* command, which allows the device to use varying VLANs in PnP and should be set up and configured on the upstream switch.

### Step 1.1 - ***Upstream Neighbor Setup***
As depicted in the diagram above, the 3850 will serve as the upstream neighbor for this exercise and the environment's distribution switch. The Catalyst 9300 will act as the target switch, which we will deploy via PnP and Day 0 and N templates.

For the lab, we will utilize ***VLAN 5*** as the management VLAN. Connect to switch ***c3850-1*** and paste the following configuration:

```
config t
!
vlan 5
name "managment vlan"
!
int vlan 5 
 ip address 192.168.5.1 255.255.255.0
 ip ospf 1 area 0
 no shutdown
!
pnp startup-vlan 5
end
!
wr
!
```

The ***pnp startup-vlan 5*** command will program the target switches port connected with a trunk and automatically add the vlan and SVI to the target switch making that vlan ready to accept a DHCP address. The feature is available on switches running 16.6 code or greater as upstream neighbors. Older switches or upstream devices that cannot run the command should utilize VLAN 1 and then set up the correct management VLAN modified as part of the onboarding process.

### Step 1.2 - ***DHCP Setup***
We need a DHCP scope to temporarily supply the address within the management network to complete the configuration and onboarding. Configure the scope to offer IP addresses from the part of the address's range, leaving the other part of the scope for static addresses. You could also make use of reservations as DHCP servers can reserve addresses for specific MAC addresses. One benefit of this is that DNS host entries are automatically updated depending on the DHCP Server.

The DHCP scope should therefore incorporate the following minimal configuration:

* network
* default gateway
* domain - ***required if option 2 is used below***
* name-server ip - ***required if option 2 or 3 is used below***
* DHCP relay or helper statement - ***to be added to the gateway interface pointing to the DHCP server***

There are many options for DHCP services. Although you have many options for DHCP, we will cover Windows and IOS configurations in this lab. Configure the DHCP scope to one of the following:

1. Switch or Router
2. Windows DHCP Server
3. InfoBlox or other 3rd party server

During this lab setup, please choose which option you wish to use for DHCP for PnP services and follow those subsections.

#### Step 1.2a - ***IOS DHCP Configuration***
Configured on an IOS device, the DHCP pool elements would be configured either on a router or switch in the network. 

If we want to use the IOS DHCP configuration method, connect to switch ***c3850-1*** and paste the following configuration:

```
!
conf t
!
  ip dhcp pool pnp_device_pool                         
     network 192.168.5.0 255.255.255.0                  
     default-router 192.168.5.1 
     end
!
wr
!
```

Next, we will configure the helper address statement on the management VLAN's SVI to point to the router or switch to the DHCP configuration. Connect to switch ***c3850-1*** and paste the following configuration:

```
!
conf t
!
  interface Vlan 5                         
     ip helper-address 192.168.5.1                  
     end
!
wr
!
```

For a complete configuration example please see [Configuring the Cisco IOS DHCP Server](https://www.cisco.com/en/US/docs/ios/12_4t/ip_addr/configuration/guide/htdhcpsv.html#wp1046301)

#### Step 1.2b - ***Windows Server Configuration***
If we want to use the Windows DHCP service, connect to the windows ***AD1*** server. On the windows server, you have two options to deploy DHCP scopes the UI or PowerShell. We will deploy the scope via PowerShell. Paste the following into PowerShell to create the required DHCP scope:

```
Add-DhcpServerv4Scope -Name "DNAC-Templates-Lab" -StartRange 192.168.5.1 -EndRange 192.168.5.254 -SubnetMask 255.255.255.0 -LeaseDuration 6.00:00:00 -SuperScope "PnP Onboarding"
Set-DhcpServerv4OptionValue -ScopeId 192.168.5.0 -Router 192.168.5.1 
```

The DHCP scope will look like this in Windows DHCP Administrative tool:

![json](./images/WindowsDHCPscope.png?raw=true "Import JSON")

Next, we will introduce the helper address statement on the management VLAN's SVI to point to the Windows DHCP server. Connect to switch ***c3850-1*** and paste the following configuration:

```
!
conf t
!
  interface Vlan 5                         
     ip helper-address 198.18.133.1                  
     end
!
wr
!
```

## Lab Section 2 - DNA Center Discovery
As you may recall, for a device to discover DNA Center, the device uses a discovery method to help it find DNA Center. 

The PnP components are as follows:

![json](../../images/pnp-workflows.png?raw=true "Import JSON")

There are three automated methods to make that occur:

1. **DHCP with option 43** - ***requires the DHCP server to offer a PnP string via option 43***
2. **DNS lookup** - ***requires the DHCP server to offer a domain suffix and a name server to resolve the **pnpserver** address***
3. **Cloud re-direction via https://devicehelper.cisco.com/device-helper** - ***requires the DHCP server to offer a name server to make DNS resolutions***

### Step 2.1 - ***DNA Center Discovery***
Please choose one of the following subsections as the discovery method.

#### Step 2.1a - ***Option 43 with IOS DHCP Configuration***
If using the IOS DHCP Server and the desire is to use Option 43 discovery method, then paste the following configuration:

```
!
conf t
!
  ip dhcp pool pnp_device_pool                    
     option 43 ascii "5A1N;B2;K4;I198.18.129.100;J80"
     end
!
wr
!
```

#### Step 2.1b - ***Option 43 with Windows DHCP Configuration***
If using the Windows DHCP Server and the desire is to use Option 43 discovery method, then paste the following configuration into PowerShell:

```
Set-DhcpServerv4OptionValue -ScopeId 192.168.5.0 -OptionId 43 -Value ([System.Text.Encoding]::ASCII.GetBytes("5A1N;B2;K4;I198.18.129.100;J80"))
```

The DHCP scope modification will resemble the following image of the Windows DHCP Administrative tool:

![json](./images/DNACDHCPoption43.png?raw=true "Import JSON")

#### Step 2.1c - ***DNS Lookup with IOS DHCP Configuration***
If using the IOS DHCP Server and the desire is to use the DNS Lookup discovery method, then paste the following configuration:

```
!
conf t
!
  ip dhcp pool pnp_device_pool                          
     dns-server 198.18.133.1                           
     domain-name dcloud.cisco.com                       
     end
!
wr
!
```

Next, add the DNS entries to allow for the DNA Center to be discovered. This script will add an A host entry for the VIP address and a CNAME entry as an alias for the pnpserver record required for DNS discovery.

```
Add-DnsServerResourceRecordA -Name "dnac-vip" -ZoneName "dcloud.cisco.com" -AllowUpdateAny -IPv4Address "198.18.129.100" -TimeToLive 01:00:00
Add-DnsServerResourceRecordCName -Name "pnpserver" -HostNameAlias "dnac-vip.dcloud.cisco.com" -ZoneName "dcloud.cisco.com"
```

The DNS Zone will look like this in Windows DNS Administrative tool: 

![json](./images/DNACenterDNSentries.png?raw=true "Import JSON")

#### Step 2.1d - ***DNS Lookup with Windows DHCP Configuration***
If using the Windows DHCP Server and the desire is to use the DNS Lookup discovery method, then paste the following configuration into PowerShell:

```
Set-DhcpServerv4OptionValue -ScopeId 192.168.5.0 -DnsServer 198.18.133.1 -DnsDomain "dcloud.cisco.com"
```

The DHCP scope will resemble the following image of the Windows DHCP Administrative tool:

![json](./images/WindowsDHCPscope.png?raw=true "Import JSON")

Next, add the DNS entries to allow for the DNA Center to be discovered. This script will add an A host entry for the VIP address and a CNAME entry as an alias for the pnpserver record required for DNS discovery.

```
Add-DnsServerResourceRecordA -Name "dnac-vip" -ZoneName "dcloud.cisco.com" -AllowUpdateAny -IPv4Address "198.18.129.100" -TimeToLive 01:00:00
Add-DnsServerResourceRecordCName -Name "pnpserver" -HostNameAlias "dnac-vip.dcloud.cisco.com" -ZoneName "dcloud.cisco.com"
```

The DNS Zone will look like this in Windows DNS Administrative tool: 

![json](./images/DNACenterDNSentries.png?raw=true "Import JSON")

## Lab Section 3 - Target Connectivity
Typically, the Target switch is connected via a trunk to a single port or a bundle of ports as part of a port channel. 

If it is a single port connection to the target switch, then use a simplified configuration; however, we will not be utilizing this method in this lab. An example provided here:

```
!
conf t
!
  interface range gi 1/0/10
     description PnP Test Environment to Cataylist 9300
     switchport mode trunk
     switchport trunk allowed vlan 5
     end
!
wr
!
```

In this exercise, the port where the Target switch connects is a layer two trunk as part of a Port Channel. 

```
!
conf t
!
  interface range gi 1/0/10-11
     description PnP Test Environment to Cataylist 9300
     switchport mode trunk
     switchport trunk allowed vlan 5
     channel-protocol lacp
     channel-group 1 mode passive
!
  interface Port-channel1
     description PnP Test Environment to Cataylist 9300
     switchport trunk native vlan 5
     switchport trunk allowed vlan 5
     switchport mode trunk
     no port-channel standalone-disable
     end
!
wr
!
```

If a port channel is used initially, then you want to ensure that the port channel can operate as a single link within the bundle and for that reason use passive methods for building the port channel bundles on both the Target and Upstream Neighbor for maximum flexibility. Additionally add the **no port-channel standalone-disable** command to ensure the switch does not automatically disable the port channel if it does not come up properly

## Lab Section 4 - Testing
Please use the testing for the DNS Discovery method used above

### Step 4.1a - ***DNS Resolution Tests***
To test the environment to ensure its ready, we need to test a few things.

First from a windows host use the nslookup command to resolve ***pnpserver.dcloud.cisco.com***. Connect to the windows workstation and within the search window search for CMD. Open the application and type the following command:

```
nslookup pnpserver.dcloud.cisco.com
```

They should be presented with the following output or something similar which shows the resolution of the alias to the A host record entry which identifies the VIP address for the DNA Center Cluster.

![json](./images/DNACenterDNStests.png?raw=true "Import JSON")

### Step 4.1b - ***DNS Resolution***
Second we need to ensure the DNA Center responds on the VIP, so use the ping command within the CMD application window previously opened as follows:

```
ping pnpserver.dcloud.cisco.com
```

![json](./images/DNACenterDNStestPing.png?raw=true "Import JSON")

At this point the environment should be set up to onboard devices within Vlan 5 using the network address ***192.168.5.0/24*** utilizing either ***option 43*** or ***DNS Discovery***.

### Step 4.2 - ***Reset EEM Script***
When testing you will frequently need to start again on the switch to test the whole flow. To accomplish this paste this small script into the 9300 target switch which will create a file on flash which you may load into the running-configuration at any time to reset the device to factory settings:

```
tclsh                            
puts [open "flash:prep4dnac" w+] {
!
alias exec prep4dnac event manager run prep4dnac
!
! Remove any confirmation dialogs when accessing flash
file prompt quiet
!
no event manager applet prep4dnac
event manager applet prep4dnac
 event none sync yes
 action a1010 syslog msg "Starting: 'prep4dnac'  EEM applet."
 action a1020 puts "Preparing device to be discovered by device automation - This script will reboot the device."
 action b1010 cli command "enable"
 action b1020 puts "Saving config to update BOOT param."
 action b1030 cli command "write"
 action c1010 puts "Erasing startup-config."
 action c1020 cli command "wr er" pattern "confirm"
 action c1030 cli command "y"
 action d1010 puts "Clearing crypto keys."
 action d1020 cli command "config t"
 action d1030 cli command "crypto key zeroize" pattern "yes/no"
 action d1040 cli command "y"
 action e1010 puts "Clearing crypto PKI stuff."
 action e1020 cli command "no crypto pki cert pool" pattern "yes/no"
 action e1030 cli command "y"
 action e1040 cli command "exit"
 action f1010 puts "Deleting vlan.dat file."
 action f1020 cli command "delete /force vlan.dat"
 action g1010 puts "Deleting certificate files in NVRAM."
 action g1020 cli command "delete /force nvram:*.cer"
 action h0001 puts "Deleting PnP files"
 action h0010 cli command "delete /force flash:pnp*"
 action h0020 cli command "delete /force nvram:pnp*"
 action z1010 puts "Device is prepared for being discovered by device automation.  Rebooting."
 action z1020 syslog msg "Stopping: 'prep4dnac' EEM applet."
 action z1030 reload
!
end
}
tclquit
```

### Step 4.3 - ***Reset Switch and Test Discovery***
At this point we want to test the routing, connectivity, dhcp and dns services as well as discovery mechanism. Paste the following into the 9300 target switch and watch the switch come up but do not intercede or type anything into the console after the reboot has started.

```
copy prep4dnac running-config
!
prep4dnac
```

The Switch should reboot and display this eventually in the console which acknowledges that the 9300 has discovered the DNA Center.

![json](./images/DNAC-IPV4-DISCOVERY.png?raw=true "Import JSON")

Additionally within DNA Center on the Plug and Play window the device should show as unclaimed

![json](./images/DNAC-9300-Discovery.png?raw=true "Import JSON")

## Summary
The next step would be to build the PnP Onboarding settings and template on DNA Center which will be covered in the next lab entitled [Onboarding Templates](../LAB2-Onboarding-Template/README.md#Day0) - This section explains in depth and how to deploy Day 0 templates

## Feedback
If you found this set of Labs helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
