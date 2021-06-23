# Advanced Automation - In Development
## Overview
This Lab is designed to be used after first completing labs 1 through 4 and has been created to address how to use some advanced automation concepts not previously touched on in the previous labs. This is an enablement type lab and is designed to help customers to reach beyond what they currently understand and try new concepts and really push the boundaries of automation.

During this lab we will cover various topics with regard to template logic to solve various use cases. Some of these concepts have been previously covered but perhaps not with as indepth a focus.

## General Information
As previously discussed, DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates and for more flexibility Composite Templates. as they can be used to apply ongoing changes and to allow device modifications after initial deployment. 

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used you should **not** deploy the same feature from cli code in a template to configure the device. Its a decision you have to make upfront and avoids a lot of lines in the templates and allows for a more UI centric configuration which is easier to maintain. 

As a guidance try and use **Design Settings** for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing.

With these things in mind we will cover various aspects and use cases which perhaps allow for a more programamtic approach.

## Topics
The various topics covered in the lab will be the following:

1. *Self-deleting EEM scripts*
2. Working with *Arrays and Methods* in *Velocity*
3. Velocity and *Enable* versus *Interactive* mode
4. Assigning port configuration in a stack
5. Autoconf vs Smartports
6. IBNS 2.0 configuration

## Use Cases
The Topics listed above will be covered in a number of use cases to show the capability and flexibility of the templating engine within DNA Center. While we will utilize Velocity language the same can be accomplished in the Jinja2 language.

## Renaming Interfaces Use Case
So previously within the Composite Templating Lab we introduced a methodology of automatically naming the interfaces within the switch. When a new device or switch/router/access point connects to a switch we want to name those interfaces. Naming the uplinks specifically, but also the various wireless access points and IP Phones would be a nice addition. 

The script which we used on the Composite Templates uses an EEM Script which runs whenever a CDP event occurs.

```
   event manager applet update-port
    event neighbor-discovery interface regexp GigabitEthernet.* cdp add
    action 101 regexp "(Switch|Router)" "$_nd_cdp_capabilities_string"
    action 102 if $_regexp_result eq "1"
    action 103  cli command "enable"
    action 104  cli command "config t"
    action 105  cli command "interface $_nd_local_intf_name"
    action 106  regexp "^([^\.]+)\." "$_nd_cdp_entry_name" match host
    action 107  regexp "^([^\.]+)" "$_nd_port_id" match connectedport
    action 108  cli command "no description"
    action 109  cli command "description Uplink to $host - $connectedport"
    action 110  cli command "interface port-channel 1"
    action 111  cli command "no description"
    action 112  cli command "description Uplink to $host"
    action 113  cli command "end"
    action 114  cli command "write"
    action 115 end
```

While this script will rename the uplinks connected to a Router or Switch it is limited in terms of the following:
1. Timing, as its not scheduled, and you cannot clear the CDP table from the template
2. Naming Access Points or other devices is also not taken into consideration

So lets modify the EEM script to first solve the naming aspect with regard to connected devices

```
   event manager applet update-port
    event neighbor-discovery interface regexp GigabitEthernet.* cdp add
    action 101 regexp "(Switch|Router)" "$_nd_cdp_capabilities_string"
    action 200 if $_regexp_result eq "1"
    action 201  regexp "(Trans-Bridge)" "$_nd_cdp_capabilities_string"
    action 210  if $_regexp_result eq "1"
    action 211   cli command "enable"
    action 212   cli command "config t"
    action 213   cli command "interface $_nd_local_intf_name"
    action 214   regexp "^([^\.]+)" "$_nd_cdp_entry_name" match host
    action 215   regexp "^([^\.]+)" "$_nd_port_id" match connectedport
    action 216   cli command "no description"
    action 217   cli command "description AP - $host - $connectedport"
    action 220  else
    action 221   cli command "enable"
    action 222   cli command "config t"
    action 223   cli command "interface $_nd_local_intf_name"
    action 224   regexp "^([^\.]+)\." "$_nd_cdp_entry_name" match host
    action 225   regexp "^([^\.]+)" "$_nd_port_id" match connectedport
    action 226   cli command "no description"
    action 227   cli command "description Link - $host - $connectedport"
    action 228   cli command "interface port-channel 1"
    action 229   cli command "no description"
    action 230   cli command "description Link - $host"
    action 240  end
    action 250 else
    action 251  regexp "(Phone)" "$_nd_cdp_capabilities_string"
    action 252  if $_regexp_result eq "1"
    action 253   cli command "enable"
    action 254   cli command "config t"
    action 255   cli command "interface $_nd_local_intf_name"
    action 256   regexp "^([^\.]+)" "$_nd_cdp_entry_name" match host
    action 257   regexp "^([^\.]+)" "$_nd_port_id" match connectedport
    action 258   cli command "no description"
    action 259   cli command "description Phone - $host - $connectedport"
    action 260  end
    action 270 end
    action 280 cli command "write"
```
You will see that lines *250 to 260* were appended to the EEM script. Within that construct we look for the keyword `Phone` within the built in variable to determine if the port is connected to a Phone. If it is then it results in a True or binary 1 state and the included code from lines *253 to 260* run line by line. The configuration adds a description to the interface for the phone of `description Phone - SEPB07D47D34910 - Port 1` for example.

The second part of the problem within this use case is solving for the issue presented by a lack of functionality when the code is configured on the switch. While we can get the configuration in place it will only run when the port is cycled or when the CDP information for the port is cleared. To solve the problem we therefore employ a *Self-Destructing EEM script*

*Self-Destructing EEM scripts* are those that delete themselves on termination. Within the code below you will notice that the line 2.1 removes the EEM applet from the configuration and then line 2.3 ensures the configuration is written to NVRAM prior to terminating.

```
   event manager applet POST_PNP
    event timer countdown time 30
    action 1.0 cli command "enable"
    action 1.1 cli command "clear cdp table"
    action 2.0 cli command "config t"
    action 2.1 cli command "no event manager applet POST_PNP"
    action 2.2 cli command "end"
    action 2.3 cli command "wr
    action 2.4 cli command "exit
```

## Availability Information
This lab is under development please come back soon. ETA for delivery June 30 2021.



