## DAY N Templates and Flows [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

In this section we will go through the flow involved in creating a Template from an IOS configuration script for a Catalyst switch and various thoughts around how to link it to a Switch profile and deploy it through Cisco Catalyst Center using Plug and Play workflows.

Cisco Catalyst Center can be used for not only Plug and Play but also Day N or Ongoing Templates. Typically customers will start by building out an Onboarding Template which might deploy just enough information to bring the device up initially, or might include the entire configuration for a traditional network. Customers also need to be able to deploy ongoing changes to the network infrastructure.

Please remember that Onboarding templates are deployed one time only when the device is being brought online. For that reason sometimes it is better to keep the configuration limited to general connectivity and leave the complexitities of the rest of the configuration to the Day N template. This will allow you as the administrator the ablity to modify templates and redeploy them or parts of them for ongoing changes and modifications.

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* application within Cisco Catalyst Center. If the Design component is used you cannot deploy that text within a template to the device. Using the settings means that you can avoid CLI entries in the templates, and avoid having to transition from one method to another later.

As a guidance try and use Design settings for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing. Day N templates allows for administrators to build either monolithic or regular templates and add them to workflows, or to build composite templates for use in provisioning. 

### Regular Templates

The use of regular templates allows you to reuse build code in the form of a set of IOS commands listed out very much like a configuration file. Those commands may be nested within logical constructs using either Velocity or Jinja2 scripting language, but the intent is that this regular template is a set of instructions initiated on a target device to create a configuration.

### Composite Templates

The use of composite templates allows you to reuse templates and code that you have previously used on other deployments without duplicating it on Cisco Catalyst Center. This allows you to manage those smaller templates or modules allowing for easier management moving forward.

Composite templates may be created in a similar method to regular templates but a project must be specified for the Day N flow. Once the Composite template is built, saved and committed templates within the project may be dragged into the flow and moved up or down to adjust the order they are deployed.

I have given examples of composite templates within the folder [DayN](./DAYN). The order to be used for those is the following:

1. GlobalSwitchServices
2. SwitchManagement
3. SwitchInterfaces

## Cisco Catalyst Center Design Preparation

Before Cisco Catalyst Center can automate the deployment we have to perform following tasks in preparation:

1. The **Hierarchy** within Cisco Catalyst Center. This will be used to roll out code and configurations ongoing so my guidance around this is to closely align this to the change management system. If you need change management down to floors or even Intermediate/Main Distribution Facilities then its a good idea to build your hierarchy to suit this. There are plenty of blogs and guides about how to do this. **(required)**
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

      ![json](../ASSETS/DesignSettings.png?raw=true "Import JSON")

3. **Device Credentials** can then be added hierarchically being either inherited and or overidden at each level throughout the hierarchy. The following is a description of the credentials and configurations that can be pushed **(required)**:
   1. **CLI Credentials** - *Usernames, Passwords and Enable Passwords*
   2. **SNMP Credentials** - *SNMP v1, v2 for both Read and Write as well as SNMP v3*
   3. **HTTP(S) Credentials** - *HTTP(S) usernames and passwords for both Read and Write Access*
4. **Image Repository** should be populated with the image of the network device you wish to deploy. You can import the image using the **+Import** link which will open a popup allowing you to choose a file from the local file system, or allow you to reference a URL for either HTTP or FTP transfer. You then indicate whether the file is Cisco or 3rd Party and click import. Once the file is imported if there is no instance of the device on the system you can go into the imported images section and assign it to a specific type of device. Select the image and mark it as golden for PnP to use it. **(required)**

## DayN Templates

DayN templates can be regular or composite templates which serve the purpose of providing a method of making ongoing configuration changes to the device as mentioned during provisioning. Typically there are two types of configuration that are used here Layer 3 routed or Layer 2 access. Both have different use cases and while they are typical they are by no means the only types of configuration used. To that end a set of examples has been provided in the [DAYN folder](./DAYN) within this repository. Some of those examples are the ones I most typically use with customers in workshops. Included there are a number of **JSON Import Files** to facilitate import into Cisco Catalyst Center 2.1.X and above.

## DayN Template Deployment

Once you have built your onboarding template you then have to let **Cisco Catalyst Center** know where you want to use the template. We will assume at this point you have already built out the template for use. You would then follow the following steps:
   1. Create network profile Under *Design> Network Profiles* you will select **+Add Profile**

      ![json](../ASSETS/NetworkProfile.png?raw=true "Import JSON")
   
   2. Select the type of device (ie Switching)
   3. Profile name 
   
      ![json](../ASSETS/NetworkProfileTabs.png?raw=true "Import JSON")
   
   4. On the Onboarding Template page select device type **(optional)**
   
      ![json](../ASSETS/OnboardingDevice.png?raw=true "Import JSON")
   
   5. On the Onboarding Template page select the template(s) to be used for onboarding **(optional)**
   
      ![json](../ASSETS/OnboardingTemplate.png?raw=true "Import JSON")
   
   6. On the DayN Template page select device type **(required)**
   
      ![json](../ASSETS/DayNtemplates.png?raw=true "Import JSON")
   
   7. On the DayN Template page select the template(s) to be used for Day N provisioning **(required)**
   8. Save the network profile
   9. Assign the network profile to the hierarchy

If the Network Profile is already deployed it can be edited at a later date to add DayN templates by simply:
   1. Click edit next to the network profile Under *Design> Network Profiles*  
   2. On the DayN Template page select device type **(required)**

      ![json](../ASSETS/DayNtemplates.png?raw=true "Import JSON")
      
   3. On the DayN Template page select the template(s) to be used for Day N provisioning **(required)**
   4. Save the network profile
   5. Assign the network profile to the hierarchy

## Provisioning

At this point Cisco Catalyst Center is set up and ready for DayN templates to be used on the first device. Provided the device has been onboarded or discovered by Cisco Catalyst Center and is present in Cisco Catalyst Center Device Inventory. If not, please discover the device through the tools menu or see the onboarding section [Onboarding Templates](./Onboarding.md)

At this point you can select the device putting on the Device Inventory and provision it by do the following:

   1. Put a checkmark next to the device to be provisioned
   2. Select **Actions> Provision> Provision Device** and walk through the workflow
   3. Section 1 assign the device to part of the hierarchy if not completed then click next
   4. Section 2 select the device and or sections and populate variable information then click next
   5. Section 3 review the elements including configuration to be deployed
   6. Click Deploy to initiate
   
At this stage the device will be placed in **configuring** state, and will cycle to **Managed** when complete. After the device is completed you may need to either wait for the next resync interval or you can resync the device for the changes in the configuration to appear within Cisco Catalyst Center.
   
> **Note:** If you populate the UI with settings those parameters should **not** be in your templates as they will conflict and the deployment through provisioning will fail. While it is easy to populate these settings it is best to test with a switch to see what configuration is pushed.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Return to Main Menu**](./README.md)