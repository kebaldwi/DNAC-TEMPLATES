### PnP Workflow
With the advent of Cisco DNA Center, Cisco has taken a leap forward in how to deploy network devices. Through the use of DNA Center it is now possible use PnP to deploy switches and automate the build of branch and device deployments.

For DNA Center to begin the process it must first learn of the device. The device therefore must communicate to DNA Center and this section will explain how this can be achieved.

The first piece to the puzzle is that the device must get an IP address. It does not have one by default as it has not been primed nor do we want to do that in a fully automated flow.

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

In order to land on DNA Center though the device needs help in finding it. There are 3 automated methods to make that occur.

1. DHCP with option 43
```
   PnP string: 5A1D;B2;K4;I172.19.45.222;J80 added to DHCP Server
``` 
2. DNS lookup
``` 
   pnpserver.localdomain resolves to DNA Center VIP Address
```
3. Cloud re-direction https://devicehelper.cisco.com/device-helper 
   Cisco hosted cloud, re-directs to on-prem DNA Center IP Address

Option 3 requires the that DNA Center register a file with the PnP Connect portal which it will offer via SSL to a device which reaches out. In order to whitelist those devices, the serial number would have to be associated to the DNAC profile within software centrals pnp connect portal.

![json](images/PnPConnect.png?raw=true "Import JSON")

The PnP workflow is as follows:




![json](images/pnp-workflow.png?raw=true "Import JSON")



