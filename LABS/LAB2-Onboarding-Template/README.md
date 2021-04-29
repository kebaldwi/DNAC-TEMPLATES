# Onboarding Templates [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
## Overview
This Lab is designed to be a standalone lab to address how to use Onboarding Templates within DNA Center to onboard network devices at Day Zero which is to say no configuration on the device whatsoever.

In this section will go through the flow involved in creating a deployable Template from an IOS configuration script for a Catalyst switch linking it to a Switch profile and deploy it through DNAC using Plug and Play workflows.

## General Information
As DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates as they can be used to apply ongoing changes and to allow device modifications after initial deployment.

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used you should not deploy the cli code in a template to configure the device. Its a decision you have to make upfront and avoids a lot of lines in the templates and allows for a more UI centric configuration which is easier to maintain. 

As a guidance try and use Design settings for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing.

## Lab Section 1 - DNA Center Design Preparation
While a more extensive set of settings can be built out for a deployment we will limit the configuration to the minimal necessary to perform this step. We will augment the Design Settings during the **DayN Templating Lab** to include others that may be required.

Before DNA Center can automate the deployment we have to do a couple of tasks to prepare: 

### Step 1 - Hierarchy
1. The **Hierarchy** within DNA Center will be used to roll out code and configurations ongoing so my guidance around this is to closely align this to the change management system. If you need change management down to floors or even Intermediate/Main Distribution Facilities then its a good idea to build your hierarchy to suit this. This is a **(required)** step.
2. Although you can manually set up the hierarchy we will use an automation script to implement the hierarchy via **dnacentercli** part of the ***DNA Center SDK**

```
# Create Sites
dnacentercli --base_url https://198.18.129.1 --verify False -v 2.1.1 -u admin -p C1sco12345 sites create-site --type "area" --site '{ "area" : { "name":"DNAC Template Lab","parentName":"Global"}}' --headers '{"__runsync" : true }'

dnacentercli --base_url https://198.18.129.1 --verify False -v 2.1.1 -u admin -p C1sco12345 sites create-site --type "building" --site '{ "building" : { "name":"Building","parentName":"Global/DNAC Template Lab","address":"Cisco Building 24, 510 McCarthy Blvd, Milpitas, CA 95035"} }' --headers '{"__runsync" : true }'

dnacentercli --base_url https://198.18.129.1 --verify False -v 2.1.1 -u admin -p C1sco12345 sites create-site --type "floor" --site '{ "floor" : { "name":"Floor1","parentName":"Global/DNAC Template Lab/Building","rfModel":"Cubes And Walled Offices","width":100,"length":100,"height":10} }' --headers '{"__runsync" : true }'

# Create Credentials
dnacentercli --base_url https://198.18.129.1 --verify False -v 2.1.1 -u admin -p C1sco12345 network-settings create-device-credentials --settings '{"cliCredential":[{"description":"netadmin","username":"netadmin","password": "C1sco12345","enablePassword": "C1sco12345"}], "snmpV2cRead":[{"description":"RO","readCommunity":"ro"}],"snmpV2cWrite":[{"description":"RW","writeCommunity":"rw"}] }' --headers '{"__runsync" : true }'

dnacentercli --base_url https://198.18.129.1 --verify False -v 2.1.1 -u admin -p C1sco12345 network-settings assign-credentials-to-site --site-id "5f012eea-c19f-4130-96e2-ee47c99e7c3b" '{ "cliId": "admin", "snmpV2ReadId": "ro", "snmpV2WriteId": "rw" }' --headers '{"__runsync" : true }'

# Create Global Settings
dnacentercli --base_url https://198.18.129.1 --verify False -v 2.1.1 -u admin -p C1sco12345 network-settings create-network --site_id "5f012eea-c19f-4130-96e2-ee47c99e7c3b" --settings '{ "dhcpServer":["198.18.133.1"], "syslogServer":{"ipAddresses":["198.18.129.1"],"configureDnacIP": true}, "snmpServer": {"ipAddresses":["198.18.129.1"],"configureDnacIP": true}, "netflowcollector":{"ipAddress":"198.18.129.1","port":6007}, "ntpServer":["198.18.133.1"], "timezone":"EST5EDT" }'  --headers '{"__runsync" : true }'
```

### Step 2 - Network Settings
1. **Network Settings** can then be added hierarchically being either inherited and or overidden at each level throughout the hierarchy. The following is a description of the Network Settings and configurations that we will push as part of this lab **(required)**:
   1. **AAA Servers** - *both Network Administration and Client/Endpoint Authentication*
   2. **DHCP Servers** - *DHCP Server Addresses for Vlan Interfaces for example*
   3. **DNS Servers** - *both the Domain Suffix and the DNS servers used for lookups*
   4. **SYSLOG Servers** - *the servers to which logging will be sent*
   5. **SNMP Servers** - *the servers to which SNMP traps will be sent and or that will poll the device*
   6. **Netflow Collector Servers** - *the server to which Netflow is sent*
   7. **NTP Servers** - *NTP Server Addresses*
   8. **Timezone** - *Timezone to be used in logging*
   9. **Message of Day** - *Banner displayed when you log into a device*
   ![json](../../images/DesignSettings.png?raw=true "Import JSON")

### Step 3 - Device Credentials
3. **Device Credentials** can then be added hierarchically being either inherited and or overidden at each level throughout the hierarchy. The following is a description of the credentials and configurations that can be pushed **(required)**:
   1. **CLI Credentials** - *Usernames, Passwords and Enable Passwords*
   2. **SNMP Credentials** - *SNMP v1, v2 for both Read and Write as well as SNMP v3*
   3. **HTTP(S) Credentials** - *HTTP(S) usernames and passwords for both Read and Write Access*
### Step 4 - Image Repository
4. **Image Repository** should be populated with the image of the network device you wish to deploy. You can import the image using the **+Import** link which will open a popup allowing you to choose a file from the local file system, or allow you to reference a URL for either HTTP or FTP transfer. You then indicate whether the file is Cisco or 3rd Party and click import. Once the file is imported if there is no instance of the device on the system you can go into the imported images section and assign it to a specific type of device. Select the image and mark it as golden for PnP to use it. **(required)**

## Lab Section 2 - DNA Center Onboarding Template Preparation
Once you have built your onboarding template you then have to let **DNA Center** know where you want to use the template. We will assume at this point you have already built out the template for use. You would then follow the following steps:

### Step 1 - Create an Onboarding Template
Create an Onboarding Template in the Templating tool using the [Template](./templates/Platinum-Onboarding.txt) located within this lab. If using DNAC 2.1.X and upward importing the Template and settings as already built using the [JSON](./templates/Platinum_Onboarding_Template.json) file.

The Onboarding template has the minimal configuration to bring up device connectivity withe DNAC. 

```
##<------Onboarding-Template------->
##To be used for onboarding when using Day N Templates
##Define Variables provision with vlan1 and 
!
##MTU Adjust (if required)
##system mtu 9100
!
##Set hostname
hostname ${Hostname}
!
##Set VTP and VLAN for onboarding
vtp domain ${VtpDomain}
vtp mode transparent
!
vlan ${MgmtVlan}
!
interface Te1/1/1
shut
switchport trunk allowed vlan add ${MgmtVlan}
no shut
!
##Set up managment vlan ${MgmtVlan}
interface Vlan ${MgmtVlan}
ip address ${SwitchIP} ${SubnetMask}
no ip redirects
no ip proxy-arp
no shut
!
ip default-gateway ${Gateway}
!
##Set Source of Management Traffic
ip domain lookup source-interface Vlan ${MgmtVlan}
ip http client source-interface Vlan ${MgmtVlan}
ip ftp source-interface Vlan ${MgmtVlan}
ip tftp source-interface Vlan ${MgmtVlan}
ip ssh source-interface Vlan ${MgmtVlan}
ip radius source-interface Vlan ${MgmtVlan}
logging source-interface Vlan ${MgmtVlan}
snmp-server trap-source Vlan ${MgmtVlan}
ntp source Vlan ${MgmtVlan}
!
##Disable Vlan 1
interface vlan 1
shutdown
!
```

It will set up static addressing and hostname entries along with updating management source interfaces for management connectivity. This file is transfered to the target device in a single file as opposed to linne by line configuration which accomodates the changes in network connectivity which may be lost when iterating line by line.

### Step 2 - Create a Network Profile
1. Create network profile Under *Design> Network Profiles* you will select **+Add Profile** 
   ![json](../../images/NetworkProfile.png?raw=true "Import JSON")
   2. Select the type of device (ie Switching)
   3. Profile name
   ![json](../../images/NetworkProfileTabs.png?raw=true "Import JSON")
   4. On the Onboarding Template page select device type **(required)**
   ![json](../../images/OnboardingDevice.png?raw=true "Import JSON")
   5. On the Onboarding Template page select the template(s) to be used for onboarding **(required)**
   ![json](../../images/OnboardingTemplate.png?raw=true "Import JSON")
   6. Save the network profile
   7. Assign the network profile to the hierarchy
   ![json](./images/NetworkProfile-AssignSite.png?raw=true "Import JSON")
   9. Select the sites to apply the profile within the hierarchy and click save
   ![json](./images/NetworkProfileSelectSite.png?raw=true "Import JSON")

## Lab Section 3 - Claiming and Onboarding
At this point DNAC is set up and ready for Plug and Play to onboard the first device. Provided the discovery and dhcp assignment are aligned, the device should when plugged in find DNA Center and land in the plug n play set of the devices section within the provisioning page.

### Step 1 - Claiming the device
At this point you can claim the device putting it in a planned state for onboarding onto the system. To do this do the following:

   1. Put a checkmark next to the device to be claimed
   2. Click the Claim link and walk through the workflow
   3. Section 1 select the part of the hierarchy to which the device will be deployed then click next
   4. Section 2 you can click the device hyperlink and view or amend the template and image utilized then click next
   5. Section 3 you can manipulate any of the variables within the template if used then click next
   6. Section 4 review the elements including configuration to be deployed 
   7. Click claim to initiate
   
At this stage the device will be placed in **Planned** state, and will cycle through **Onboarding** and **Provisioned** when complete. After the device is completed it will appear in the device inventory after being sync'd with DNA Center.
   
#### Note:
If you populate the UI with settings those parameters should **not** be in your templates as they will conflict and the deployment through provisioning will fail. While it is easy to populate these settings it is best to test with a switch to see what configuration is pushed.

## Automating Claiming and Provisioning
While it is possible to click through the claiming and process, for bulk deployments its important to be able to address that as well. With DNAC after the templates are built and assigned to the network profile and assigned to a site they may be referenced and used by uploading a csv file to DNA Center via REST API.

## Summary
The next step will be to build DayN Templates for the switches to be pushed out to the various devices in the network infrastructure. 

## Feedback
If you found this set of Labs helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
