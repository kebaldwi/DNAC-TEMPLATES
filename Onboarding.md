# Onboarding Templates and Flows
In this section will go through the flow involved in creating a Template from an IOS configuration script for a Catalyst switch and various thoughts around how to link it to a Switch profile and deploy it through DNAC using Plug and Play workflows.

DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates. Typically customers will start by building out an Onboarding Template which might deploy only enough information to bring the device up initially or might include the entire configuration for a traditional network.

A good thing to note is that Onboarding templates are deployed one time only when the device is being brought online. While there is nothing wrong in doing only this, its important to understand that there is a lot more power gained by being able to modify templates and redeploy them or parts of them for ongoing changes and modifications. For ongoing modifications DayN templates should be considered for those parts of the configuration. Additionally keeping your onboarding configuration light means that you gain the maximum flexibility of being able to make ongoing changes later.

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used you cannot deploy the text code to the device. Its a decision you have to make upfront and avoids a lot of lines in the templates. 

As a guidance try and use Design settings for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing.

## DNA Center Design Preparation
Before DNA Center can automate the deployment we have to do a couple of tasks to prepare:

1. The **Hierarchy** within DNA Center. This will be used to roll out code and configurations ongoing so my guidance around this is to closely align this to the change management system. If you need change management down to floors or even Intermediate/Main Distribution Facilities then its a good idea to build your hierarchy to suit this. There are plenty of blogs and guides about how to do this. **(required)**
2. **Network Settings** can then be added hierarchically being either inherited and or overidden at each level throughout the hierarchy. The following is a description of the Network Settings and configurations that can be pushed **(optional)**:
   1. **AAA Servers** - *both Network Administration and Client/Endpoint Authentication*
   2. **DHCP Servers** - *DHCP Server Addresses for Vlan Interfaces for example*
   3. **DNS Servers** - *both the Domain Suffix and the DNS servers used for lookups*
   4. **SYSLOG Servers** - *the servers to which logging will be sent*
   5. **SNMP Servers** - *the servers to which SNMP traps will be sent and or that will poll the device*
   6. **Netflow Collector Servers** - *the server to which Netflow is sent*
   7. **NTP Servers** - *NTP Server Addresses*
   8. **Timezone** - *Timezone to be used in logging*
   9. **Message of Day** - *Banner displayed when you log into a device*
   ![json](images/DesignSettings.png?raw=true "Import JSON")
3. **Device Credentials** can then be added hierarchically being either inherited and or overidden at each level throughout the hierarchy. The following is a description of the credentials and configurations that can be pushed **(required)**:
   1. **CLI Credentials** - *Usernames, Passwords and Enable Passwords*
   2. **SNMP Credentials** - *SNMP v1, v2 for both Read and Write as well as SNMP v3*
   3. **HTTP(S) Credentials** - *HTTP(S) usernames and passwords for both Read and Write Access*
4. **Image Repository** should be populated with the image of the network device you wish to deploy. You can import the image using the **+Import** link which will open a popup allowing you to choose a file from the local file system, or allow you to reference a URL for either HTTP or FTP transfer. You then indicate whether the file is Cisco or 3rd Party and click import. Once the file is imported if there is no instance of the device on the system you can go into the imported images section and assign it to a specific type of device. Select the image and mark it as golden for PnP to use it. **(required)**

## Onboarding Template Preparation
Once you have built your onboarding template you then have to let **DNA Center** know where you want to use the template. We will assume at this point you have already built out the template for use. You would then follow the following steps:
   1. Create network profile Under *Design> Network Profiles* you will select **+Add Profile** 
   ![json](images/NetworkProfile.png?raw=true "Import JSON")
   2. Select the type of device (ie Switching)
   3. Profile name
   ![json](images/NetworkProfileTabs.png?raw=true "Import JSON")
   4. On the Onboarding Template page select device type **(required)**
   ![json](images/OnboardingDevice.png?raw=true "Import JSON")
   5. On the Onboarding Template page select the template(s) to be used for onboarding **(required)**
   ![json](images/OnboardingTemplate.png?raw=true "Import JSON")
   6. On the DayN Template page select device type **(optional)** (for more info [DayN Templates](./DayN.md))
   ![json](images/DayNtemplates.png?raw=true "Import JSON")
   7. On the DayN Template page select the template(s) to be used for Day N provisioning **(optional)** (for more info [DayN Templates](./DayN.md))
   8. Save the network profile
   9. Assign the network profile to the hierarchy

If the Network Profile is already deployed it can be edited at a later date to add Onboarding templates by simply:
   1. Click edit next to the network profile Under *Design> Network Profiles*  
   2. On the Onboarding Template page select device type **(required)**
   ![json](images/DayNtemplates.png?raw=true "Import JSON")
   3. On the Onboarding Template page select the template(s) to be used for onboarding **(required)**
   4. Save the network profile
   5. Assign the network profile to the hierarchy

## Claiming and Provisioning
At this point DNAC is set up and ready for Plug and Play to onboard the first device. Provided the discovery and dhcp assignment are aligned, the device should when plugged in find DNA Center and land in the plug n play set of the devices section within the provisioning page.

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

This methodology allows for you to specify variables within the csv, serial numbers, and put devices into a planned state waiting for them to land on the Plug and Play page on DNA Center.


