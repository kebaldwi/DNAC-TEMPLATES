# DNS Discovery using IOS DHCP and Windows DNS Services

As you may recall, for a device to discover Cisco Catalyst Center, the device uses a discovery method to help it find Cisco Catalyst Center. 

The PnP components are as follows:

![json](../../ASSETS/pnp-workflows.png?raw=true "Import JSON")

There are three automated methods to make that occur and in this section we will use DNS Discovery. To aide in that we are goiing to utilize a combination of IOS DHCP with DNS services. The Target switch, commonly called Access switch will need to do a DNS lookup in order to find Cisco Catalyst Center.

**DNS lookup** 
    - *requires the DHCP server to offer a domain suffix and a name server to resolve the **pnpserver** address*
    - *requires the **pnpserver** entry to appear in the Subject Alternative Name of the GUI Certificate*

#### Step 3.2a - IOS DHCP and DNS Discovery Configuration

Configured on an IOS device, the DHCP pool elements would be configured either on a router or switch in the network. We will configure the helper address statement on the management VLAN's SVI to point to the router or switch to the DHCP configuration. 

When using the IOS DHCP Server and the DNS Lookup discovery method, we will add the appropriate DNS server IP addresses along with the domain suffix that the switch will use to resolve the **pnpserver** record within DNS.

Connect to switch **c9300-2** and paste the following configuration:

```vtl
!
conf t
!
  ip dhcp excluded-address 192.168.5.1 192.168.5.1
  ip dhcp pool pnp_device_pool                         
     network 192.168.5.0 255.255.255.0                  
     default-router 192.168.5.1 
     dns-server 198.18.133.1                           
     domain-name dcloud.cisco.com                       
!
  interface Vlan 5                         
     ip helper-address 192.168.5.1                  
     end
!
wr
!
```

For a complete configuration example please see [Configuring the Cisco IOS DHCP Server](https://www.cisco.com/en/US/docs/ios/12_4t/ip_addr/configuration/guide/htdhcpsv.html#wp1046301)

Next, we will add the relevant DNS entries into the Windows DNS service to allow for the Cisco Catalyst Center to be discovered. This script will add an A host entry for the VIP address and a CNAME entry as an alias for the pnpserver record required for DNS discovery.

```ps
Add-DnsServerResourceRecordA -Name "dnac-vip" -ZoneName "dcloud.cisco.com" -AllowUpdateAny -IPv4Address "198.18.129.100" -TimeToLive 01:00:00
Add-DnsServerResourceRecordCName -Name "dnac" -HostNameAlias "dnac-vip.dcloud.cisco.com" -ZoneName "dcloud.cisco.com"

Add-DnsServerPrimaryZone -Name "pnp.dcloud.cisco.com" -ReplicationScope "Forest" -PassThru

#Pause required to allow Zone to be created prior to CNAME Entry
Start-Sleep -Seconds 60

Add-DnsServerResourceRecordCName -Name "pnpserver" -HostNameAlias "dnac-vip.dcloud.cisco.com" -ZoneName "pnp.dcloud.cisco.com"
```

The DNS Zone will look like this in Windows DNS Administrative tool: 

![json](./images/DNACenterDNSentries.png?raw=true "Import JSON")

![json](./images/DNACenterDNSentries2.png?raw=true "Import JSON")

> **Note:** To utilize DNS Entry for Discovery purposes Certificates will need to be rebuilt with Subject Alternative Names. Please utilize the process documented in the following [**page**](./Certificates.md) for information on that process.

## Verification and Testing

To test the environment to ensure it's ready, we need to try a few things.

First, from a Windows host, use the *nslookup* command to resolve **pnpserver.dcloud.cisco.com**. Connect to the Windows workstation, and within the search window, search for CMD. Open the application and type the following command:

```bash
nslookup pnpserver.dcloud.cisco.com
```

The following output or something similar shows the resolution of the alias to the A host record entry which identifies the VIP address for the Cisco Catalyst Center Cluster will display.

![json](./images/DNACenterDNStests.png?raw=true "Import JSON")

Second, we need to ensure the Cisco Catalyst Center responds on the VIP, so use the ping command within the CMD application window previously opened as follows:

```bash
ping pnpserver.dcloud.cisco.com
```

The test results should look similar to this:

![json](./images/DNACenterDNStestPing.png?raw=true "Import JSON")

Third, we can ping Cisco Catalyst Center from the Distribution Switch utilizing the following:

```bash
ping 198.18.129.100 source vlan 5 repeat 2
ping pnpserver.dcloud.cisco.com source vlan 5 repeat 2
```
The test results should look similar to this:

![json](./images/blank.png?raw=true "Import JSON")

At this point, the environment should be set up to onboard devices within VLAN 5 using the network address **192.168.5.0/24** utilizing **DNS discovery**

> [**Return to PnP Preparation Lab**](./module1-pnpprep.md#step-6---reset-eem-script-or-pnp-service-reset)
