# DNE DNA Center Rest-API with Postman Preparation 
## Overview
This section of the repository is built out in LAB form to guide you through the typical steps required to enable the various automation tasks delivered by DNA Center. This lab will give a postman collection and environment required to prepare the lab for the DNE event.

## DCLOUD as a LAB
### Overview
This section will explain which lab to utilize within the **DCLOUD** environment to run these labs. It will also discuss a customer POC environment and the steps necessary to successfully run these sections within a customer environment for localized testing.

#### SJC
Please use the following lab environment for the event.

[Cisco Enterprise Networks Hardware Sandbox](https://dcloud2-sjc.cisco.com/content/catalogue?search=Enterprise%20Networks%20Hardware%20Sandbox&screenCommand=openFilterScreen)

#### Components
The DCLOUD session includes the following equipment:

Virtual Machines:

    DNA Center 2.2.3.4 or better
    Identity Services Engine (ISE) 3.0 Patch 4 or better (deployed)
    Identity Services Engine (ISE) 3.0 (Not deployed)
    Stealthwatch 7.4.0 or better
    FlowCollector 7.4.0 or better
    Cisco Prime Infrastructure 3.10  or better
    Script Server - Ubuntu 20.04  or better
    Wireless LAN Controller - C9800 running IOS-XE Bengaluru 17.5.1 code or better
    Windows 10 Jump Host 
    Windows Server 2019 - Can be configured to provide identity, DHCP, DNS, etc.
    Windows 10 Clients

Hardware Devices:

    ISR 4451 Router - 17.06.01a IOS-XE Code
    Catalyst 9300 Switch - 17.06.01 IOS-XE Code with Embedded Wireless Controller (EWC) and ThousandEyes Enterprise Agent
    9130AX Access Points
    Silex Controllers (3 Wired NIC's and 1 Wireless NIC)

The lab envionment that is available is depicted here:

![json](./assets/DCLOUD_Topology2.png?raw=true "Import JSON")

## DCLOUD LAB Preparation
### dCLOUD VPN Connection
Use AnyConnect VPN to connect to dCLOUD. When connecting, look at the session details and copy the credentials from the session booked into the client to connect.

![json](./assets/VPN-to-dCLOUD.png?raw=true "Import JSON")

### dCLOUD Service Optimization
The dCLOUD environment used in the lab need to be optimized prior to the session, and to do this we need to disable the following:

![json](./assets/ShutdownUnused.png?raw=true "Import JSON")

In order to accomplish this, use the drop down menu item by each that is shutdown in the image and click the shutdown link.

### SSL Settings and disabling Validation
For lab purposes DNA Center utilizes a self signed certificate which would fail any validation precheck. In order to test in the lab we will therefore disable this setting.

Follow these steps:

1. Click the settings gear icon on the top right of postman to select settings.
![json](./assets/Postman-Settings-Menu.png?raw=true "Import JSON")
2. Deselect the `SSL certificate verification`
![json](./assets/Postman-Settings-SSL-Validation-On.png?raw=true "Import JSON")
3. It should look as shown and then close the settings window.
![json](./assets/Postman-Settings-SSL-Validation-Off.png?raw=true "Import JSON")

### Postman Collection and Environment Import
To prepare Postman for the lab please download the following collection and environment zip file and upload them into Postman. Download the following Student Collection which includes 6 collections and one environment. To do this right click and open this link in a new tab to download them:
   
1. Please download the following Instructors bundle. [⬇︎Instructor-Collection⬇︎](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-DNE-LAB/blob/main/labs/assets/Student-Collection.zip)

Once the file has been downloaded uncompress/unzip it and import all the files into Postman.

Follow these steps:

1. Within postman click the import button and an import window will appear
2. Click the upload file button to begin the files select process
![json](./assets/Postman-Import.png?raw=true "Import JSON")
3. Select the Instructors files and click open and import
![json](./assets/Postman-Instructor-Import.png?raw=true "Import JSON")
4. Confirm the environment is present and set it active
![json](./assets/Postman-Environment-Instructor.png?raw=true "Import JSON")
![json](./assets/Postman-Environment-Instructor-Active.png?raw=true "Import JSON")
5. Confirm the Collection is present and then start the collection runner
![json](./assets/Postman-Collection-Instructor-Runner.png?raw=true "Import JSON")
6. Verify all of the Collection ran successfully
![json](./assets/Postman-Collection-Instructor-Verify.png?raw=true "Import JSON")
7. Check the following on DNA Center:
   1. Hierarchy
   2. Settings
   3. Credentials
   4. Telemetry
   5. Discoveries
   6. Inventory

## Summary
At this point DNA Center should be set up and ready for the attendees.

## Disclaimer
Various labs are designed for use in the **DCLOUD** environment but can but are for use elsewhere. The environment allows for use with a web-based browser client for VPN-less connectivity, access as well as AnyConnect VPN client connectivity for those who prefer it. The labs are hosted out of our San Jose and RTP Facilities and so you would choose sessions from either US East or US West. Choose the Cisco Enterprise Network Sandbox v4 or greater To access this or any other content, including demonstrations, labs, and training in Cloud please work with your Cisco Account team or Cisco Partner Account Team directly. Your Account teams will make sure the session is scheduled and shared for you to use. Once booked follow the guide within Github to complete the tasks adhering to the best practices of the dCLOUD environment.


