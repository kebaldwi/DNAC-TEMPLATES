# PnP Workflow [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
With the advent of Cisco DNA Center, Cisco has taken a leap forward in how to deploy network devices. Through the use of DNA Center it is now possible use PnP to deploy switches and automate the build of branch and device deployments.

For DNA Center to begin the process it must first learn of the device. The device therefore must communicate to DNA Center and this section will explain how this can be achieved.

The first piece to the puzzle is that the device must get an IP address. It does not have one by default as it has not been primed nor do we want to do that in a fully automated flow.

## Device Connectivity
For PnP processes to work our intention is to have a management interface on the device, like a Loopback or Vlan interface. As the device is connected to the front facing ports by default there is little configuration. As a result the Vlan 1 will be used initially on the target device for the pnp workflow, but during provisioning we can manipulate addresses, and change the source of the management interface to a loopback, vlan, or routed interface. 

By default the target switch is using vlan 1 as no other vlan exists, and vlan 1 by default accepts DHCP addresses. This will be used in the pnp process. Our management vlan however, may be a different vlan, and so may the native vlan structure of our environment. To that end we must make use of the *pnp startup-vlan* command which allows the device to use this vlan in pnp and needs to be configured on the upstream switch.

```
pnp startup-vlan 100
```

Alternatively we can tell the target switch to set up a separate vlan for management from the upstream neighbor. The way this is done is to make use of the ***pnp startup-vlan x*** command. This command will program the target switches port connected with a trunk and automatically add the vlan and SVI to the target switch making that vlan ready to accept a DHCP address. This is available on switches running 16.6 code or greater as upstream neighbors. Older switches or upstream devices that are not capable of running the command should be onboarded in vlan 1 and the vlan modified as part of the onboarding process.

## DHCP
So we need a DHCP scope to supply the address within the management network temporarily in order to complete the configuration and onboarding. The scope should be configured so as to offer addresses from part of the range of addresses not used. It also can be a reservation as DHCP servers can reserve addresses for specific MAC addresses. 

The DHCP scope would incorporate therefore the following which would be enough to get an address:
* **network**
* **default gateway**
* **domain**                
  - *required if option 2 is used below*
* **name-server ip**        
  - *required if option 2 or 3 is used below*
* **option 43**             
  - *required if option 1 is used below*

Obviously a dhcp relay or helper statement would need to be added to the gateway interface pointing to the DHCP server.

## DNA Center Discovery
In order to land on DNA Center though the device needs help in finding it. 

The PnP components are as follows:

![json](images/pnp-workflows.png?raw=true "Import JSON")

There are 3 automated methods to make that occur:

1. **DHCP with option 43**
```
   PnP string: 5A1D;B2;K4;I172.19.45.222;J80 added to DHCP Server
``` 
2. **DNS lookup**
``` 
   pnpserver.localdomain resolves to DNA Center VIP Address
```
3. **Cloud re-direction https://devicehelper.cisco.com/device-helper**
   **which, re-directs to on-prem DNA Center IP Address**

**Option 1:** requires that along with the IP address and gateway the DHCP server must offer a PnP string via option 43. This option is used with Cisco wireless so I typically recommend that you go with option 2. 

**Option 2:** requires that along with the IP address and gateway the DHCP server offer the domain suffix that the **pnpserver** record will reside in and a name server to resolve the address.

**Option 3:** requires that along with the address and gateway the DHCP server offer a name server to resolve the address of **device-helper.cisco.com**. Additionally it requires the that DNA Center register a file with the PnP Connect portal which it will offer via SSL to a device which reaches out. In order to whitelist those devices, the serial number would have to be associated to the DNAC profile within software centrals pnp connect portal.

![json](images/pnp-connect.png?raw=true "Import JSON")

Once one of the options has been built devices will get the address and be pointed to and land on DNA Center within the PnP Device list.

## Setup Information:

### Option 43 
Option 43 format follows as documented on the [DNA Center User Guide](https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/dna-center/1-2-8/user_guide/b_dnac_ug_1_2_8/b_dnac_ug_1_2_8_chapter_01100.html#id_90877) It may be offered by any DHCP server including but not limited to IOS, Windows, Infoblox and many more.

Benefits to this method are that you can contain the connectivity in a finite manner and perscriptively by only allowing equipment on specific subnets to find DNA Center.

```
Option 43 format 
 The option 43 string has the following components, delimited by semicolons:
 
PnP string: 5A1D;B2;K4;I172.19.45.222;J80 
 
Description - dhcpc receiving DHCP Offer with option 43 info, pass the info to PNPA 
 *     5A = PnP DHCP ID
 *     1D = PnP DHCP debug on
 *     1N = PnP DHCP debug off
 *     token.B = <address type> 1:Host; 2:IPv4; 3:IPv6
 *     token.K = <protocol> 1: XMPP-starttls; 2: XMPP-socket; 3:: XMPP-tls; 4: HTTP; 5: HTTPS
 *     token.I = <remote server ip add / hostname>
 *     token.J = <remote server port> valid ports are 80 or 443
 
Further explanation of PnP string and how to read:

5A1N;             Specifies the DHCP suboption for Plug and Play, active operation, version 1, 
                  no debug information. It is not necessary to change this part of the string.
                  

B2;               IP address type: in this case IPv4 format
                  Alternates would be: 
                            B1 = hostname
                            B2 = IPv4 (default)

K4;               Transport protocol to be used between the device and the controller: In 
                  this example HTTP transport
                  K4 = HTTP (default)
                  K5 = HTTPS

Ixxx.xxx.xxx.xxx; IP address or hostname of the Cisco DNA Center controller (following a 
                  capital letter i). In this example, the IP address is 172.19.45.222.
                  

Jxxxx             Port number to use to connect to the Cisco DNA Center controller. 
                  In this example, the port number is 80. The default is port 80 for HTTP 
                  and port 443 for HTTPS.
```

#### IOS Configuration Example
Configured on a IOS device it would look like this example:

```
  ip dhcp pool pnp_device_pool                          <-- Name of DHCP pool
     network 192.168.1.0 255.255.255.0                  <-- Range of IP addresses assigned to clients
     default-router 192.168.1.1                         <-- Gateway address
     option 43 ascii "5A1N;B2;K4;I172.19.45.222;J80"    <-- Option 43 string
```
#### Windows Server Configuration Example
On windows you have two options to deploy DHCP scopes the UI or PowerShell. We will show you Option 43 set up on a specific scope but it can be quickly replicated to other scopes using the binary entry gathered from a dhcp dump via netshell. That said here is what the option looks like as configured as option 43:

![json](images/WindowsDHCP.png?raw=true "Import JSON")

### DNS Setup
DNS may be set up on many types of servers, but for simplification we will speak about the records which can be created. Typically it is good to remember to add DNS entries for all interface server nodes within the cluster and a DNS entry for the **Virtual IP address(VIP)** on the Enterprise Network which may be used for Management and Enterprise Network connectivity.

Benefits to this methodology are that you can cover a large organization rapidly avoiding the need to make changes to multiple DHCP scopes, and can accomplish a regional approach through the use of sub domains within an organization like * *pnpserver.west.us.domain.com* * or * *pnpserver.east.us.domain.com* * which allows for 2 different clusters due to RTT times perhaps.

**Option 1:** An A record would be created pointing to the VIP address. Another A record may also be added for the pnpserver record to resolve to the same address. In this regard the two entries might look like this:

```
             A - dnac.domain.com -> 10.10.0.20
             A - pnpserver.domain.com -> 10.10.0.20
             
             where 10.10.0.20 is the VIP address on the Enterprise Network
```
This might show the following when using **nslookup**
```
nslookup dnac.domain.com
Server:		10.10.0.250
Address:	10.10.0.250#53

Name:	dnac.domain.com
Address: 10.10.0.20

nslookup pnpserver.domain.com
Server:		10.10.0.250
Address:	10.10.0.250#53

Name:	pnpserver.domain.com
Address: 10.10.0.20
```
**Option 2:** An A record would be created pointing to the VIP address. A CNAME alias record may also be added for the pnpserver record to resolve to the address via . In this regard the two entries might look like this: This allows for changes to the A record to automatically be propogated to any child records easily and at the same time.

```
             A - dnac.domain.com -> 10.10.0.20
             CNAME - pnpserver.domain.com -> dnac.domain.com
             
             where 10.10.0.20 is the VIP address on the Enterprise Network
```

This might show the following when using **nslookup**
```
nslookup dnac.domain.com
Server:		10.10.0.250
Address:	10.10.0.250#53

Name:	dnac.domain.com
Address: 10.10.0.20

nslookup pnpserver.base2hq.com
Server:		10.10.0.250
Address:	10.10.0.250#53

pnpserver.base2hq.com	canonical name = dnac.base2hq.com.
Name:	dnac.base2hq.com
Address: 10.10.0.20
```

### PnP Connect Portal
The PNP connect portal is where a device would land that had internet connectivity which had not been able to contact DNA Center through either * *option 43* * or * *dns resolution* * and for this method to work, the pnp connect portal must be set up accordingly on the customers virtual account. 

Benefits to this methodology are that devices can be whitelisted on the pnp-connect portal and specifically pointed to one cluster or another with the profile file configured.

The steps to complete in order to use this method are as follows:

#### To Set up PnP Connect
1. Navigate to System Settings>Settings>Cisco Credentials>PnP Connect
![json](images/dnac-pnp-profile.png?raw=true "Import JSON")
2. Click Add
3. Ensure the Smart Account
![json](images/dnac-register.png?raw=true "Import JSON")
4. Enter the Virtual Account to be mapped to for the PnP Profile
5. Select if this is to be the Default Profile for the Virtual Account
6. Select whether you want the device to use IP or DNS entry to find DNAC.
   - note DNS entry will need Domain Suffix to be provided in DHCP
7. Ensure VIP is shown or alternatively enter FQDN for VIP address
8. Enter a name for the profile or accept the default
9. Click Register
10. Ensure Sync Success is reported

#### To Stage Devices in PnP Connect Portal on software.cisco.com
1. Navigate to https://Software.cisco.com and log in.
2. Select PnP Connect
![json](images/software.png?raw=true "Import JSON")
3. Navigate to the Virtual Account and Select the Device to be modified
4. Click Edit Selected
![json](images/pnp-connect-device.png?raw=true "Import JSON")
5. From the drop down selections choose Controller Profile
![json](images/pnp-controller-profile.png?raw=true "Import JSON")
6. Select the Controller Profile from the list
![json](images/pnp-connect-profile.png?raw=true "Import JSON")
7. Submit the settings

#### For Devices
1. DHCP Setup to include:
   - DNS Server Address for name resolution
2. IP reachability to Internet

If you found this repository or any section helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
