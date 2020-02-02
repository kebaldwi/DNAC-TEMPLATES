# Onboarding Templates and Flows
In this section will go through the flow involved in creating a Template from an IOS configuration script for a Catalyst switch and various thoughts around how to link it to a Switch profile and deploy it through DNAC using Plug and Play workflows.

DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates. Typically customers will start by building out an Onboarding Template which might deploy only enough information to bring the device up initially or might include the entire configuration for a traditional network.

A good thing to note is that the idea behind Onboarding templates is that they are deployed one time only when the device is being brought online. While there is nothing wrong in doing only this, its important to understand that there is a lot more power gained by being able to modify templates and redeploy them or parts of them for ongoing changes and modifications.

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* applications within DNA Center. If the Design component is used you cannot deploy the text code to the device. Its a decision you have to make upfront and avoids a lot of lines in the templates. 

As a guidance try and use Design settings for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing.

## DNA Center Design Preparation
Before DNA Center can automate the deployment we have to do a couple of tasks to prepare:

1. The **Hierarchy** within DNA Center. This will be used to roll out code and configurations ongoing so my guidance around this is to closely align this to the change management system. If you need change management down to floors or even Intermediate/Main Distribution Facilities then its a good idea to build your hierarchy to suit this. There are plenty of blogs and guides about how to do this.
2. The **Network Settings** can then be added hierarchically being either inherited and or overidden at each level throughout the hierarchy. The following is a description of the Network Settings and configurations that can be pushed:
   1. **AAA Servers** - *both Network Administration and Client/Endpoint Authentication*
   2. **DHCP Servers** - *DHCP Server Addresses for Vlan Interfaces for example*
   3. **DNS Servers** - *both the Domain Suffix and the DNS servers used for lookups*
   4. **SYSLOG Servers** - *the servers to which logging will be sent*
   5. **SNMP Servers** - *the servers to which SNMP traps will be sent and or that will poll the device*
   6. **Netflow Collector Servers** - *the server to which Netflow is sent*
   7. **NTP Servers** - *NTP Server Addresses*
   8. **Timezone** - *Timezone to be used in logging*
   9. **Message of Day** - *Banner displayed when you log into a device*
3. The **Device Credentials** can then be added hierarchically being either inherited and or overidden at each level throughout the hierarchy. The following is a description of the credentials and configurations that can be pushed:
   1. **CLI Credentials** - *Usernames, Passwords and Enable Passwords*
   2. **SNMP Credentials** - *SNMP v1, v2 for both Read and Write as well as SNMP v3*
   3. **HTTP(S) Credentials** - *HTTP(S) usernames and passwords for both Read and Write Access*

To Be Continued....
