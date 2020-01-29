### PnP Workflow
With the advent of Cisco DNA Center, Cisco has taken a leap forward in how to deploy network devices. Through the use of DNA Center it is now possible use PnP to deploy switches and automate the build of branch and device deployments.

For DNA Center to begin the process it must first learn of the device. The device therefore must communicate to DNA Center and this section will explain how this can be achieved.

The first piece to the puzzle is that the device must get an IP address. It does not have one by default as it has not been primed nor do we want to do that in a fully automated flow.

#### DHCP
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

#### DNA Center Discovery
In order to land on DNA Center though the device needs help in finding it. 

The PnP workflow is as follows:

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

![json](images/PnPConnect.png?raw=true "Import JSON")

Once one of the options has been built devices will get the address and be pointed to and land on DNA Center within the PnP Device list.

### Setup Information:

#### Option 43 
Option 43 format follows as documented on https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/dna-center/1-2-8/user_guide/b_dnac_ug_1_2_8/b_dnac_ug_1_2_8_chapter_01100.html#id_90877 It may be offered by any DHCP server including but not limited to IOS, Windows, Infoblox and many more.

```
Option 43 format 
 The option 43 string has the following components, delimited by semicolons:
 
PnP string: 5A1D;B2;K4;I172.19.45.222;J80 
 
Description - dhcpc receiving DHCP Offer with option 43 info, pass the info to PNPA 
 *     5A = PnP DHCP ID
 *     1D = PnP DHCP debug on
 *     1o = PnP DHCP debug off
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

##### IOS Configuration Example
Configured on a IOS device it would look like this example:

```
     ip dhcp pool pnp_device_pool                          <-- Name of DHCP pool
        network 192.168.1.0 255.255.255.0                  <-- Range of IP addresses assigned to clients
        default-router 192.168.1.1                         <-- Gateway address
        option 43 ascii "5A1N;B2;K4;I172.19.45.222;J80"    <-- Option 43 string
```
##### Windows Server Configuration Example

#### DNS Setup

#### PnP COnnect Portal



