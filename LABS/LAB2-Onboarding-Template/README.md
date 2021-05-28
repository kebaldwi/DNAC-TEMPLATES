# Onboarding Templates 
## Overview
This Lab is designed to be used after first completing lab 1 and has been created to address how to use Onboarding Templates within DNA Center to onboard network devices at Day Zero which is to say no configuration on the device whatsoever.

In this section will go through the flow involved in creating a deployable Template from an IOS configuration script for a Catalyst switch linking it to a Switch profile and deploy it through DNAC using Plug and Play workflows.

## General Information
As DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates as they can be used to apply ongoing changes and to allow device modifications after initial deployment.

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used you should not deploy the cli code in a template to configure the device. Its a decision you have to make upfront and avoids a lot of lines in the templates and allows for a more UI centric configuration which is easier to maintain. 

As a guidance try and use Design settings for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing.

## Lab Section 1 - DNA Center Design Preparation
While a more extensive set of settings can be built out for a deployment we will limit the configuration to the minimal necessary to perform this step. We will augment the Design Settings during the **DayN Templating Lab** to include others that may be required.

Before DNA Center can automate the deployment we have to do a couple of tasks to prepare. Please log into the DNA Center using a browser within the Windows **Jump host**. Use the credentials of username: ***admin*** password: ***C1sco12345***. Then browse to [DNA Center](https://198.18.129.100). Use the credentials of username: ***admin*** password: ***C1sco12345*** within the DCLOUD environment.

Although you can manually set up the hierarchy we will use automation scripts built to implement the hierarchy via **postman** which will utilize the **DNA Center API's** To do this we will make use of the application `postman` in the Windows workstation and install json files.

1. Download the following two files in zip format to the desktop and expand them:
   <p><a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB2-Onboarding-Template/postman/DNAC_Templates_Lab.postman_collection.json" target="_blank" rel="noopener noreferrer">⬇︎COLLECTIONS⬇︎</a></p>
   <p><a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB2-Onboarding-Template/postman/DNAC_Template_Labs.postman_environment.json" target="_blank" rel="noopener noreferrer">⬇︎ENVIRONMENT⬇︎</a></p>
   [go](http://stackoverflow.com){:target="_blank" rel="noopener"}
2. Open the **postman** application from the desktop. Once the application is open select *Collections* then click the *Import* link and on the window that appears click raw text and copy and paste the 
3. Once the both the environment variables, and the collection are installed we will walk through the sections below.

### Step 1 - ***Hierarchy***
1. The **Hierarchy** within DNA Center will be used to roll out code and configurations ongoing so my guidance around this is to closely align this to the change management system. If you need change management down to floors or even Intermediate/Main Distribution Facilities then its a good idea to build your hierarchy to suit this. This is a **(required)** step and the process below will explain in detail how to set up for our lab.

### Step 2 - ***Network Settings***
1. **Network Settings** can then be added hierarchically being either inherited and or overidden at each level throughout the hierarchy. The following is a description of the Network Settings and configurations that we will push as part of this lab **(required)**:
   1. ***DHCP Servers***
   2. ***DNS Servers***
   3. ***SYSLOG Servers***
   4. ***SNMP Servers***
   5. ***Netflow Collector Servers*** 
   6. ***NTP Servers***
   7. ***Timezone***
2. Paste the lines below and refresh the Network Settings page to watch the changes.

```
# Create Global Settings
dnacentercli --base_url https://198.18.129.100 --verify False -v 2.1.1 -u admin -p C1sco12345 network-settings create-network --site_id "5f012eea-c19f-4130-96e2-ee47c99e7c3b" --settings '{ "dhcpServer":["198.18.133.1"], "syslogServer":{"ipAddresses":["198.18.129.100"],"configureDnacIP": true}, "snmpServer": {"ipAddresses":["198.18.129.100"],"configureDnacIP": true}, "netflowcollector":{"ipAddress":"198.18.129.100","port":6007}, "ntpServer":["198.18.133.100"], "timezone":"EST5EDT" }'  --headers '{"__runsync" : true }'
```
3. At the Global level enter the domain name setting of `dcloud.cisco.com` and the name server ip address of `198.18.133.1`. Ensure that all the settings are inherited all the way to Floor 1.

### Step 3 - ***Device Credentials***
1. **Device Credentials** can then be added hierarchically being either inherited and or overidden at each level throughout the hierarchy. The following is a description of the credentials and configurations that can be pushed **(required)**:
   1. ***CLI Credentials*** 
   2. ***SNMP Read and Write Credentials***
2. Paste the lines below one at a time and refresh the Credentials page to watch the changes.

```
# Create Credentials
dnacentercli --base_url https://198.18.129.100 --verify False -v 2.1.1 -u admin -p C1sco12345 network-settings create-device-credentials --settings '{"cliCredential":[{"description":"netadmin","username":"netadmin","password": "C1sco12345","enablePassword": "C1sco12345"}], "snmpV2cRead":[{"description":"RO","readCommunity":"ro"}],"snmpV2cWrite":[{"description":"RW","writeCommunity":"rw"}] }' --headers '{"__runsync" : true }'

dnacentercli --base_url https://198.18.129.100 --verify False -v 2.1.1 -u admin -p C1sco12345 network-settings assign-credential-to-site --site_id "5f012eea-c19f-4130-96e2-ee47c99e7c3b" '{ "cliId": "netadmin", "snmpV2ReadId": "RO", "snmpV2WriteId": "RW" }' --headers '{"__runsync" : true }'
```
3. Ensure that the Credentials are set for the Global level and that the are inherited all the way to Floor 1. If not select the Credentials and save them.

### Step 4 - ***Image Repository***
The image used in this lab for the 9300 is downloadable from here [Amsterdam-17.03.03 MD](https://software.cisco.com/download/home/286315874/type/282046477/release/Amsterdam-17.3.3)

1. **Image Repository** should be populated with the image of the network device you wish to deploy. You can import the image using the **+Import** link which will open a popup allowing you to choose a file from the local file system, or allow you to reference a URL for either HTTP or FTP transfer. 
2. You then indicate whether the file is Cisco or 3rd Party and click import. 
3. Once the file is imported if there is no instance of the device on the system you can go into the imported images section and assign it to a specific type of device. 
4. Select the image and mark it as golden for PnP to use it. **(required)**

## Lab Section 2 - DNA Center Onboarding Template Preparation
You can create onboarding templates within the ***Templating Tool*** within **DNA Center**. Go to the ***Templating Tool*** to complete the next task.

### Step 1 - ***Create an Onboarding Template***
Download and import an Onboarding Template in the Templating tool using the [JSON](./templates/Platinum_Onboarding_Template.json) file. If using DNAC prior release to 2.1.2.X then build the [Template](./templates/Platinum-Onboarding.txt) located within this lab. 

The Onboarding template has the minimal configuration to bring up device connectivity with DNAC. Below is for explanation purposes only. (Please Import the Template JSON above)

```
##<------Onboarding-Template------->
##To be used for onboarding when using Day N Templates
##Define Variables provision with vlan and port channel
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
##Set Interfaces and Build Port Channel 
interface range gi 1/0/10-11
 shut 
 switchport trunk allowed vlan add ${MgmtVlan}
 channel-protocol lacp
 channel-group 1 mode passive
 no shut
!
interface Port-channel1
 switchport trunk native vlan ${MgmtVlan}
 switchport mode trunk
 no port-channel standalone-disable
!
##Set Up Managment Vlan ${MgmtVlan}
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
interface Vlan 1
 shutdown
!
```

It will set up static addressing and hostname entries along with updating management source interfaces for management connectivity. This file is transfered to the target device in a single file as opposed to linne by line configuration which accomodates the changes in network connectivity which may be lost when iterating line by line.

### Step 2 - ***Create a Network Profile***
Next we need to assign the Onboarding Template to a site using the Network Profile.

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

### Step 1 - ***Claiming the Device***
At this point you can claim the device putting it in a planned state for onboarding onto the system. To do this do the following:

   1. Put a checkmark next to the device to be claimed
   2. Click the **Actions>Claim** link and walk through the workflow
   3. Section 1 select the part of the hierarchy to which the device will be deployed then click **next**
   4. Section 2 you can click the hyperlinks to the right of the workflow page and view or amend the templates and images utilized then click **next**
   5. Section 3 select the device **serial number** on the left and fill in the variables within the template click **next**. Please use the following:
      *   Hostname type `ACCESS-9300-ASW`
      *   Management Vlan enter `5`
      *   IP Address `192.168.5.10`
      *   Subnet Mask `255.255.255.0`
      *   Gateway `192.168.5.1`
      *   VTP Domain `Cisco`   
   6. Section 4 review the elements including configuration to be deployed 
   7. Click **claim** to initiate
   
At this stage the device will be placed in **Planned** state, and will cycle through **Onboarding** and **Provisioned** when complete. After the device is completed it will appear in the device inventory after being sync'd with DNA Center.
   
#### Note:
If you populate the UI with settings those parameters should **not** be in your templates as they will conflict and the deployment through provisioning will fail. While it is easy to populate these settings it is best to test with a switch to see what configuration is pushed.

## Automating Claiming and Provisioning
While it is possible to click through the claiming and process, for bulk deployments its important to be able to address that as well. With DNAC after the templates are built and assigned to the network profile and assigned to a site they may be referenced and used by uploading a csv file to DNA Center via REST API.

## Summary
The next step will be to build DayN Templates for the switches to be pushed out to the various devices in the network infrastructure. 

## Feedback
If you found this set of Labs helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
