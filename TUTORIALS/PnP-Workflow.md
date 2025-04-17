# PnP Workflow [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

With the advent of Cisco Catalyst Center, Cisco has taken a leap forward in applying automation when deploying intended configuration to network devices at scale. Through the use of Cisco Catalyst Center PnP (plug and play) we can drastically simplify out-of-box device initialization and Day-0 configuration as the first step towards automation.

For Cisco Catalyst Center to begin the process it must first learn of the device. The device therefore must communicate to Cisco Catalyst Center and this section will explain how this can be achieved.

The first piece to the puzzle is that the device must obtain an IP address to have basic network reachability. It does not have one by default as it has not been primed nor do we want to do that in a fully automated flow.

## Device Connectivity

For PnP processes to work our intention is to have a management interface on the device, such as a Loopback or Vlan interface. As the device is connected to the front facing ports by default there is little configuration required. As a result initially Vlan 1 is all that is available on the target device for the pnp workflow. We can manipulate addresses and even change the source of the management interface to a loopback, vlan, or routed interface through additional configuration steps.

By default the target switch is using vlan 1 as no other vlan exists, and vlan 1 by default accepts DHCP assigned addresses. We could use vlan 1 for provisioning, but more than likely we would need to use some other vlan for our management vlan. 

If management vlan is going to be different from the default vlan 1 assignment, we will use a command on the upstream switch to communicate that to the downstream target device. To that end we must make use of the *pnp startup-vlan* command which allows the device to use any vlan in pnp. This command introduced on the upstream neighbor enables automatic downstream configuration on the target enabling it for DHCP and making it ready for the pnp process. Refer to [Fundamentals of Cisco Catalyst Center Plug and Play](https://blogs.cisco.com/developer/dna-center-pnp-day-0)
 
```vtl
pnp startup-vlan 100
```

The target switch will then set up a separate vlan for management traffic. This command will program the target switch port connected with a trunk and automatically add the vlan and SVI to the target switch making that vlan ready to accept a DHCP address. This is available on switches running IOS-XE 16.6 code or greater as upstream neighbors. Older switches or upstream devices that are not capable of running the command should be onboarded in vlan 1 and the vlan modified as part of the onboarding process.

The Target switch will typically be connected to either a single port or as part of a port channel. The port where the Target switch will be connected is configured as a trunk. 

```vtl
interface Port-channel1
switchport trunk native vlan 5
switchport mode dynamic desirable
no port-channel standalone-disable
!
interface range gi 1/0/10-11
description PnP Test Environment to Cataylist 9300
switchport mode dynamic desirable
switchport trunk allowed vlan 5
channel-protocol lacp
channel-group 1 mode passive
```

If a port channel is used initially, then you want to ensure that the port channel can operate as a single link within the bundle and for that reason use passive methods for building the port channel bundles on both the Target and Upstream Neighbor for maximum flexibility. Additionally add the **no port-channel standalone-disable** command to ensure the switch does not automatically disable the port channel if it does not come up properly.

## DHCP

We require a DHCP scope to supply the IP address within the management network temporarily in order to complete the device configuration and onboarding. The scope should be carved out from an unused range. It also can be a static reservation, as DHCP servers can reserve addresses for specific MAC addresses. 

The DHCP scope would incorporate the following parameters sufficient to issue an IP address:

* **network**
* **default gateway**
* **domain**                
  - *required if option 2 is used below*
* **name-server ip**        
  - *required if option 2 or 3 is used below*
* **option 43**             
  - *required if option 1 is used below*

Obviously a dhcp relay or helper statement is required on the gateway router interface pointing towards the DHCP server.

## Cisco Catalyst Center Discovery

In order to communicate with Cisco Catalyst Center the device going through the PnP process needs additional information while finding it. 

The PnP components are as follows:

![json](../ASSETS/pnp-workflows.png?raw=true "Import JSON")

There are 3 automated methods that can be used to assist with Cisco Catalyst Center discovery process:

1. **DHCP with option 43**
```shell
   PnP string: 5A1D;B2;K4;I172.19.45.222;J80 added to DHCP Server
``` 
2. **DNS lookup**
```shell
   pnpserver.localdomain resolves to Cisco Catalyst Center VIP Address
```
3. **Cloud re-direction https://devicehelper.cisco.com/device-helper**
   **which, re-directs to on-prem Cisco Catalyst Center IP Address**

**Option 1:** requires that along with the IP address and gateway the DHCP server must offer a PnP string via option 43. This option is often used with Cisco wireless so you may want to incorporate option 60 and the use of vendor specific information to ensure the correct controller is referenced for the device in question. 
When the DHCP server receives a DHCP discover message from the device, with Option 60 containing the string “ciscopnp”, it responds to the device by returning a response that contains the Option 43 information. The Cisco Plug and Play IOS Agent in the device extracts the Cisco Catalyst Center controller IP address from the response and uses this address to communicate with the controller.
If DHCP Option 43 is not configured, the device cannot contact the DHCP server, or this method fails for another reason, the network device attempts discovery using DNS

**Option 2:** requires that along with the IP address and gateway the DHCP server offer the domain suffix that the **pnpserver** record will reside in and a name server to resolve the address. Caveats here would be that if not all devices were to be landing on Cisco Catalyst Center then you may need sub domains.

**Option 3:** requires that along with the address and the gateway the DHCP server offer a name server to resolve the address of **device-helper.cisco.com**. Additionally it requires the that Cisco Catalyst Center registers a file with the PnP Connect portal which it will offer via SSL to a device which reaches out. In order to whitelist those devices, the serial number would have to be associated to the Cisco Catalyst Center profile within "Software Central" > [Plug and Play Connect](https://software.cisco.com/software/csws/ws/platform/home?locale=en_US#pnp-devices) portal.

![json](../ASSETS/pnp-connect.png?raw=true "Import JSON")

Once the above has been configured, devices undergoing PnP process will discover Cisco Catalyst Center IP address and be redirected to it via "Plug and Play Connect" cloud proxy discovery process.

## Setup Information:

### Option 43 

Option 43 format follows as documented on the [Cisco Catalyst Center User Guide](https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/dna-center/1-2-8/user_guide/b_dnac_ug_1_2_8/b_dnac_ug_1_2_8_chapter_01100.html#id_90877). It may be offered by any DHCP server including but not limited to IOS, Windows, Infoblox and many more.

Benefits to this method are that you can contain the connectivity in a finite manner and prescriptively by only allowing equipment on specific subnets to find Cisco Catalyst Center.

```shell
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

Ixxx.xxx.xxx.xxx; IP address or hostname of the Cisco Catalyst Center controller (following a 
                  capital letter i). In this example, the IP address is 172.19.45.222.
                  

Jxxxx             Port number to use to connect to the Cisco Catalyst Center controller. 
                  In this example, the port number is 80. The default is port 80 for HTTP 
                  and port 443 for HTTPS.
```

#### IOS Configuration Example

Configured on an IOS device it would look like this example:

```vtl
  ip dhcp pool pnp_device_pool                          <-- Name of DHCP pool
     network 192.168.1.0 255.255.255.0                  <-- Range of IP addresses assigned to clients
     default-router 192.168.1.1                         <-- Gateway address
     option 43 ascii "5A1N;B2;K4;I172.19.45.222;J80"    <-- Option 43 string
```
#### Windows Server Configuration Example

On MS Windows DHCP Server, you have two options to deploy DHCP scopes the UI or PowerShell. We will show you Option 43 set up on a specific scope but it can be quickly replicated to other scopes using the binary entry gathered from a dhcp dump via netshell. That said here is what the option looks like as configured as option 43:

![json](../ASSETS/WindowsDHCP.png?raw=true "Import JSON")

### DNS Setup

DNS may be set up on many types of servers, but for simplification we will speak about the records which can be created. Typically it is a good practice to add DNS entries for all interfaces of Cisco Catalyst Center cluster members, and a DNS entry for the Cisco Catalyst Center **Virtual IP address(VIP)** on the Enterprise Network which may be used for Management and Enterprise Network connectivity.

Benefits to this methodology are that you can cover a large organization rapidly avoiding the need to make changes to multiple DHCP scopes, and can accomplish a regional approach through the use of sub domains within an organization like * *pnpserver.west.us.domain.com* * or * *pnpserver.east.us.domain.com* * which allows for 2 different clusters due to RTT times perhaps.

When using the DNS methodology with the **pnpserver** host entry please be aware that the record should exist in the Subject Alternative Names section within the Certificate on Cisco Catalyst Center.

**Option 1:** An A record would be created pointing to the VIP address. Another A record may also be added for the pnpserver record to resolve to the same address. In this regard the two entries might look like this:

```shell
             A - dnac.domain.com -> 10.10.0.20
             A - pnpserver.domain.com -> 10.10.0.20
             
             where 10.10.0.20 is the VIP address on the Enterprise Network
```
This might show the following when using **nslookup**
```shell
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
**Option 2:** An 'A' record would be created pointing to the VIP address. A CNAME alias record may also be added for the pnpserver record to resolve to the address via its parent record name. In this regard the two entries might look like below. This allows for changes to the A record to automatically be propogated to any child records at the same time.

```shell
             A - dnac.domain.com -> 10.10.0.20
             CNAME - pnpserver.domain.com -> dnac.domain.com
             
             where 10.10.0.20 is the VIP address on the Enterprise Network
```

This might show the following when using **nslookup**
```shell
nslookup dnac.domain.com
Server:		10.10.0.250
Address:	10.10.0.250#53

Name:	dnac.domain.com
Address: 10.10.0.20

nslookup pnpserver.domain.com
Server:		10.10.0.250
Address:	10.10.0.250#53

pnpserver.domain.com	canonical name = dnac.domain.com.
Name:	dnac.domain.com
Address: 10.10.0.20
```

### PnP Connect Portal

The PNP connect portal is where a device would land that had internet connectivity which had not been able to contact Cisco Catalyst Center through either * *option 43* * or * *dns resolution* * and for this method to work, the pnp connect portal must be set up accordingly on the customers virtual account. 

Benefits to this methodology are that devices can be whitelisted on the pnp-connect portal and specifically redirected to one cluster vs another with the profile file configured for the matching device serial number.

The steps to complete in order to use this method are as follows:

#### To Set up PnP Connect

1. Navigate to System Settings>Settings>Cisco Credentials>PnP Connect

   ![json](../ASSETS/dnac-pnp-profile.png?raw=true "Import JSON")

2. Click Add
3. Ensure the Smart Account

   ![json](../ASSETS/dnac-register.png?raw=true "Import JSON")

4. Enter the Virtual Account to be mapped to for the PnP Profile
5. Select if this is to be the Default Profile for the Virtual Account
6. Select whether you want the device to use IP or DNS entry to find Cisco Catalyst Center.

   > **Note:** DNS entry will need Domain Suffix to be provided in DHCP
   
7. Ensure VIP is shown or alternatively enter FQDN for VIP address
8. Enter a name for the profile or accept the default
9. Click Register
10. Ensure Sync Success is reported

Upon completion, Cisco Catalyst Center Controller Profile will be created in PnP Connect portal

#### To Stage Devices in PnP Connect Portal on software.cisco.com

1. Navigate to https://Software.cisco.com and log in.
2. Select PnP Connect

   ![json](../ASSETS/software.png?raw=true "Import JSON")

3. Navigate to the Virtual Account and Select the Device to be modified
4. Click Edit Selected

   ![json](../ASSETS/pnp-connect-device.png?raw=true "Import JSON")

5. From the drop down selections choose Controller Profile

   ![json](../ASSETS/pnp-controller-profile.png?raw=true "Import JSON")

6. Select the Controller Profile from the list

   ![json](../ASSETS/pnp-connect-profile.png?raw=true "Import JSON")

7. Submit the settings

#### For Devices

1. DHCP Setup to include:
   - DNS Server Address for name resolution
2. IP reachability to Internet

> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Return to Main Menu**](../README.md)