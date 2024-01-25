# DNS Discovery using IOS DHCP and Windows DNS Services

As you may recall, for a device to discover Cisco Catalyst Center, the device uses a discovery method to help it find Cisco Catalyst Center. 

The PnP components are as follows:

![json](../../ASSETS/pnp-workflows.png?raw=true "Import JSON")

There are three automated methods to make that occur:

1. **DHCP with option 43** - ***requires the DHCP server to offer a PnP string via option 43***
2. **DNS lookup** 
    - *requires the DHCP server to offer a domain suffix and a name server to resolve the **pnpserver** address*
    - *requires the **pnpserver** entry to appear in the Subject Alternative Name of the GUI Certificate*
3. **Cloud re-direction** via *https://devicehelper.cisco.com/device-helper* - *requires the DHCP server to offer a name server to make DNS resolutions*

#### Step 1.2a - ***IOS DHCP Configuration***

Configured on an IOS device, the DHCP pool elements would be configured either on a router or switch in the network. 

If we want to use the IOS DHCP configuration method, connect to switch ***c9300-2*** and paste the following configuration:

```vtl
!
conf t
!
  ip dhcp excluded-address 192.168.5.1 192.168.5.1
  ip dhcp pool pnp_device_pool                         
     network 192.168.5.0 255.255.255.0                  
     default-router 192.168.5.1 
     end
!
wr
!
```

Next, we will configure the helper address statement on the management VLAN's SVI to point to the router or switch to the DHCP configuration. Connect to switch ***c9300-2*** and paste the following configuration:

```vtl
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

#### Step 2.1c - ***DNS Lookup with IOS DHCP Configuration***

If using the IOS DHCP Server and the desire is to use the DNS Lookup discovery method, then paste the following configuration:

```vtl
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

Next, add the DNS entries to allow for the Cisco Catalyst Center to be discovered. This script will add an A host entry for the VIP address and a CNAME entry as an alias for the pnpserver record required for DNS discovery.

```ps
Add-DnsServerResourceRecordA -Name "dnac-vip" -ZoneName "dcloud.cisco.com" -AllowUpdateAny -IPv4Address "198.18.129.100" -TimeToLive 01:00:00
Add-DnsServerResourceRecordCName -Name "pnpserver" -HostNameAlias "dnac-vip.dcloud.cisco.com" -ZoneName "dcloud.cisco.com"
```

The DNS Zone will look like this in Windows DNS Administrative tool: 

![json](./images/DNACenterDNSentries.png?raw=true "Import JSON")

## Verification and Testing

To test the environment to ensure it's ready, we need to try a few things.

First, from a Windows host, use the *nslookup* command to resolve ***pnpserver.dcloud.cisco.com***. Connect to the Windows workstation, and within the search window, search for CMD. Open the application and type the following command:

```bash
nslookup pnpserver.dcloud.cisco.com
```

The following output or something similar shows the resolution of the alias to the A host record entry which identifies the VIP address for the Cisco Catalyst Center Cluster will display.

![json](./images/DNACenterDNStests.png?raw=true "Import JSON")

Second, we need to ensure the Cisco Catalyst Center responds on the VIP, so use the ping command within the CMD application window previously opened as follows:

```bash
ping pnpserver.dcloud.cisco.com
```

![json](./images/DNACenterDNStestPing.png?raw=true "Import JSON")

Third, we can ping Cisco Catalyst Center from the Distribution Switch utilizing the following:

```bash
ping 198.18.129.100 source vlan 5 repeat 2
ping pnpserver.dcloud.cisco.com source vlan 5 repeat 2
```

At this point, the environment should be set up to onboard devices within VLAN 5 using the network address ***192.168.5.0/24*** utilizing ***DNS discovery ***

> [**Return to PnP Preparation Lab**](./module1-pnpprep.md#step-6---reset-eem-script-or-pnp-service-reset)
