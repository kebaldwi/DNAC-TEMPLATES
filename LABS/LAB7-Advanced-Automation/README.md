# Advanced Automation
## Overview
This Lab is designed to be used after first completing labs 1 through 4 and has been created to address how to use some advanced automation concepts not previously touched on in the previous labs. This enablement type lab is designed to help customers reach beyond what they currently understand, try new concepts, and push the boundaries of automation.

We will cover various topics about template logic to solve multiple use cases during this lab. Some of these concepts have been previously covered but perhaps not in-depth.

The examples shown below can be used in building your versions of the templates. The concept of this lab is for you to create regular templates that you can substitute into the composite to test with. Various methods for the varying use cases will explain the pros and cons along the way. Expand your capabilities with this lab and take your abilities to the next level. You're only inhibited by your imagination. 

## General Information
As previously discussed, DNA Center can be used for Plug-and-Play and Day N or Ongoing Templates. Customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates and, for more flexibility Composite Templates. They can apply ongoing changes and allow device modifications after initial deployment. 

Another important consideration is that part of a typical configuration would include some lines of code, which will be automatically built out using the information within the *Design >Network Settings >* application within DNA Center. If the Design component is used, you should **not** deploy the same feature from cli code in a template to configure the device. It's a decision you have to make upfront, avoids a lot of lines in the templates, and allows for a more UI-centric configuration that is easier to maintain. 

As guidance, try and use **Design Settings** for as many of the configurations as you can, leaving Templates light and nimble for configurations that might change ongoing.

We will cover various aspects and use cases that perhaps allow for a more programmatic approach with these things in mind.

## Topics
The various topics covered in the lab will be the following:

1. *Self-deleting EEM scripts*
2. Working with *Arrays and Methods* in *Velocity*
3. Using *Conditional Statements* for Configuration
4. Velocity and *Enable* versus *Interactive* mode
5. Assigning port configuration in a stack
6. Autoconf vs Smartports
7. IBNS 2.0 configuration

## Use Cases
The Topics listed above will be covered in several use cases to show the capability and flexibility of the templating engine within DNA Center. While we will utilize Velocity language, the same can be accomplished in the Jinja2 language.

1. [Renaming interfaces](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB7-Advanced-Automation/README.md#step-1---renaming-interfaces---use-case)
2. [Building Stacks](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB7-Advanced-Automation/README.md#step-2---building-stacks---use-case)
3. [Assigning port configuration](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB7-Advanced-Automation/README.md#step-3---assigning-port-configuration---use-case)
4. [Autoconf port configuration](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB7-Advanced-Automation/README.md#step-4---autoconf-port-configuration---use-case)
5. [Non SDA IBNS 2.0 port configuration](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB7-Advanced-Automation#step-5---non-sda-ibns20-port-configuration---use-case)

## Step 1 - ***Renaming Interfaces - Use Case***
Previously within the Composite Templating Lab, we introduced a methodology of automatically naming the interfaces within the switch. When a new device or switch/router/access point connects to a switch, we want to describe those interfaces. Naming the uplinks specifically and the various wireless access points and IP Phones would be an excellent addition. 

### ***Examine Code***
The script we used on the Composite Templates uses an EEM script that runs whenever a CDP event occurs.

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

While this script will rename the uplinks connected to a Router or Switch, it is limited in terms of the following:
1. Timing, as it's not scheduled, and you cannot clear the CDP table from the template
2. Naming Access Points or other devices is also not taken into consideration

### ***Modify Code***
So let's modify the EEM script first to solve the naming aspect concerning connected devices.

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
First, let's address the primary problem, the naming of interfaces with descriptions.

You will see that lines *201 to 220* were added to the EEM script. We look for the keyword `Trans-Bridge` within the built-in variable to determine if the port is connected to an Access Point within that section. It results in a True or binary 1 state, and the included code from lines *211 to 220* runs line by line. The configuration adds a description to the interface for the phone of `description AP - KO-AP0C75 - GigabitEthernet0`, for example.

You will see that lines *250 to 260* were added to the EEM script. We look for the keyword `Phone` within the built-in variable to determine if the port is connected to a Phone within that section. It results in a True or binary 1 state, and the included code from lines *253 to 260* runs line by line. For example, the configuration adds a description to the interface for the phone of `description Phone - SEPB07D47D34910 - Port 1`.

The second part of the problem within this use case is solving the issue presented by a lack of functionality when the code is configured on the switch. While we can get the configuration in place, it will only run when the port is cycled or when the CDP information for the port is cleared. Therefore, to solve the problem, we employ a *Self-Destructing EEM script*.

*Self-Destructing EEM scripts* are those that delete themselves on termination. Within the code below, you will notice that line 2.1 removes the EEM applet from the configuration, and then line 2.3 ensures the configuration is written to NVRAM before terminating.

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

This code allows us to *clear the CDP table* and delete itself but leave the other EEM script on the switch for any moves, adds, and changes to the devices connected to the switch.

## Step 2 - ***Building Stacks - Use Case***
Previously within the Composite Templating Lab, we introduced a methodology of automatically building a data stack and power stack configuration within the switch. When a new device or switch is built, we may want to control which switch is Active and standby within the stack. 

### ***Examine Code***
To that end, the following configuration has been built previously:

```
   ## 9300 Stack Power and Priority
   ##Variables
   #set( $StackCount = $Serial.split(",") )
   #set( $StackMemberCount = $StackCount.size() )
   !
   ##Stacking Commands
   #if( $StackMemberCount > 1 )
      stack-power stack Powerstack1
      mode redundant strict
      #if( $StackMemberCount > 4 )
         stack-power stack Powerstack2
         mode redundant strict
      #end
      #foreach( $Switch in [1..$StackMemberCount] )
         #if( $Switch < 5 )
            stack-power switch ${Switch}
            stack Powerstack1
         #elseif( $Switch > 4 )
            stack-power switch ${Switch}
            stack Powerstack2
         #end
       #end
       #MODE_ENABLE
       #MODE_END_ENABLE
       #MODE_ENABLE
       #foreach( $Switch in [1..$StackMemberCount] )
          #if($Switch == 1)
             switch $Switch priority 10
          #elseif($Switch == 2)
             switch $Switch priority 9
          #else
             switch $Switch priority 8
          #end 
       #end
       #MODE_END_ENABLE
   #end
```
Within this script, you can see the Arrays `$Stackcount` formed using the `.split(",")` method, which takes the string returned from the database and splits the list into two elements within the Array `$Stackcount`. You could address each element in the Array, remembering that Arrays always start the numbering of elements at position zero (0). You could call the data with these two options; for the first element in the Array `$Stackcount[0]` or the second element in the Array `$Stackcount[1]`.

Within this script, you can see the Conditional Statements `#if #elseif #else #end`. These are used to dynamically build configuration for switch stacks no matter how many switches are within the stack. For example, if the number of switches in the stack exceeds 4, it automatically creates 2 powerstack environments for power redundancy. The script also prioritizes the Active and Standby switch above those of the rest of the switches in the stack.

Within this script, you can see the use of the Enable Statements `#MODE_ENABLE #MODE_END_ENABLE`. These commands allow for enable level configuration commands to be entered. This script needs to configure the enable level command to set switch priority for individual switches `switch $Switch priority #`. Bracketing this configuration command with the velocity statements `#MODE_ENABLE #MODE_END_ENABLE` allows us to change from configuration mode to enable mode and back again.

## Step 3 - ***Assigning Port Configuration - Use Case***
Previously within the Composite Templating Lab, we introduced a methodology of automatically configuring the interfaces within the switch. This configuration relied on a few variables used to extrapolate the settings that were then configured via the template. This allowed a set of macros to be utilized to build out the various settings for VLANs, Ports, and Uplinks. 

### ***Examine Code***
We will analyze the configuration in more detail below and modify it for greater capabilities toward the end of this section.

```
   ##Stack information variables
   #set( $StackPIDs = $ProductID.split(",") )
   #set( $StackMemberCount = $StackPIDs.size() )
   #set( $PortTotal = [] )
   #set( $offset = $StackMemberCount - 1 )
   #foreach( $Switch in [0..$offset] )
     #set( $Model = $StackPIDs[$Switch])
     #set( $PortCount = $Model.replaceAll("C9300L?-([2|4][4|8]).*","$1") )
     #set( $foo = $PortTotal.add($PortCount) )
   #end
```
Within the first block of code, some interesting concepts are dealt with. First, we create an *Array* with the various Product IDs for each switch within the stack using the `.split(",")` *method* as we previously discussed in step 2. The `.size()` *method* is then used to determine how many switches are in the stack. A blank *array* is defined for later use. We then create an offset variable to account that *arrays* start at zero (0) to be used throughout the template.

Within the loop structure, we iterate through using the variable PortCount to load the regex value grep'd from the Product ID accomplished via the `.replaceAll(""C9300L?-([2|4][4|8]).*","$1"")` *method* which in each case is either 24 or 48 to denote a 24 or 48 port switch. The PortCount variable is then appended to the *array* PortTotal using the add *method*.

We now have the data we need to configure the switch's ports, being the number of switches and the number of ports in each switch.
```
   !
   ## VLANs per MDF
   #set( $data_vlan_number = 200 + ${MDF} )
   #set( $voice_vlan_number = 300 + ${MDF} )
   #set( $ap_vlan_number = 400 + ${MDF} )
   #set( $guest_vlan_number = 500 + ${MDF} )
   #set( $bh_vlan_number = 999 )
   !
```
In the configuration above, we use simple addition to determine the VLAN ID for each VLAN built from a set of constants and a numeric variable to denote the MDF.
```
   !
   vlan ${data_vlan_number}
    name data
   vlan ${voice_vlan_number}
    name voice
   vlan ${ap_vlan_number}
    name accesspoint
   vlan ${guest_vlan_number}
    name guest
   vlan ${bh_vlan_number}
    name disabled
   !
   device-tracking upgrade-cli force
   !
   device-tracking policy IPDT_MAX_10
    limit address-count 10
    no protocol udp
    tracking enable
   !
   ##Macros
   ## Use Bind to Source variable to select access interfaces 
   #macro( access_interface )
     description Workstation
     switchport access vlan ${data_vlan_number}
     switchport mode access
     switchport voice vlan ${voice_vlan_number}
     switchport port-security maximum 3
     switchport port-security
     spanning-tree portfast
     spanning-tree bpduguard enable
   #end
```
Here we define a Macro to configure the various ports of the switch with a standard voice and data VLAN.
```
   !
   #macro( uplink_interface )
     switchport trunk allowed vlan add $data_vlan_number,$voice_vlan_number,$ap_vlan_number,$guest_vlan_number,$bh_vlan_number
   #end
```
Within the above code, we define a Macro to add the various VLANs to the trunk interface via the Port-Channel.
```
   !
   ##Access Port Configuration
   #foreach( $Switch in [0..$offset] )
     #set( $SwiNum = $Switch + 1 )
     interface range gi ${SwiNum}/0/1 - 9, gi ${SwiNum}/0/12 - $PortTotal[$Switch]
       #access_interface
   #end
   !
   ##Uplink Port Configuration
   interface portchannel 1
    #uplink_interface
   !
```
We apply the various previously defined Macros in the above code to configure the various access ports via a loop structure. We then apply the VLANs to the port-channel.

### ***Modify Code***
While this is an elegant script, it could be more automated and include ways to deal with Access Points and IoT devices in the same script. Let's look at how we might make these changes in an automated programmatic way.

First, let's deal with VLANs on the Target switch. We use one variable to extrapolate the various VLANs in the example above. Alternatively, that could be accomplished using a built-in variable like the native VLAN and a similar approach.

```
   #set( $Integer = 0 ) ##defines Integer as numeric variable
   #set( $native_bind = $native_vlan) ) ##bind variable to native vlan
   #set( $mgmt_vlan = $Integer.parseInt($native_bind) ) 
   #set( $data_offset = 100 ) ##to set the voice vlan
   #set( $voice_offset = 200 ) ##to set the voice vlan
   #set( $ap_offset = 300 ) ##to set the ap vlan
   #set( $guest_offset = 400 ) ##to set the voice vlan
   #set( $data_vlan_number = $data_offset + $mgmt_vlan )
   #set( $voice_vlan_number = $voice_offset + $mgmt_vlan )
   #set( $ap_vlan_number = $ap_offset + $mgmt_vlan )
   #set( $guest_vlan_number = $guest_offset + $mgmt_vlan )
   #set( $bh_vlan_number = 999 )
```
In this example, we no longer need to input any information, and as the offsets are used if required, we can use excel instead of setting values for defining those in bulk. The example shown illustrates them explicitly, but entry values could replace those lines in a form or excel.

Secondly, we could allow for various device types of Access Point and IoT devices with the introduction of more Macros. As each device type may each require differing VLANs and port settings: *(note: in the guest example below, the assumption is a layer 2 to a firewall providing a local gateway for guest access DIA to the internet)*

```
   ##Macros
   ## Use Bind to Source variable to select access interfaces 
   #macro( access_interface )
     description Workstation
     switchport access vlan ${data_vlan_number}
     switchport mode access
     switchport voice vlan ${voice_vlan_number}
     switchport port-security maximum 3
     switchport port-security
     spanning-tree portfast
     spanning-tree bpduguard enable
   #end
   !
   #macro( access_point )
     description Access Point 
     switchport access vlan ${ap_vlan_number}
     switchport mode access
     switchport port-security maximum 3
     switchport port-security
     spanning-tree portfast
     spanning-tree bpduguard enable
   #end
   !
   #macro( guest_interface )
     description Guest Interface
     switchport access vlan ${guest_vlan_number}
     switchport mode access
     switchport port-security maximum 3
     switchport port-security
     spanning-tree portfast
     spanning-tree bpduguard enable
   #end
   !
```
The last puzzle piece would be to programmatically determine where the ports were configured for the various tasks and devices. To accomplish this, we can again resort to logic. First, we need to account for whether a switch is PoE capable or not, so let's add some magic.

```
   ##Stack information variables
   #set( $StackPIDs = $ProductID.split(",") )
   #set( $StackMemberCount = $StackPIDs.size() )
   #set( $PortTotal = [] )
   #set( $PoECapable = [] )
   #set( $Port = [] )
   #set( $PortsAvailable = [] )
   #set( $offset = $StackMemberCount - 1 )
   #foreach( $Switch in [0..$offset] )
     #set( $Model = $StackPIDs[$Switch])
     #if( $Model.matches(".*([U|P]).*") )
        #set( $foo = $PoECapable.add(1) )
     #else
        #set( $foo = $PoECapable.add(0) )
     #end             	
     #set( $PortCount = $Model.replaceAll("C9300L?-([2|4][4|8]).*","$1") )
     #set( $foo = $PortTotal.add($PortCount) )
     #set( $foo = $Port.add(1) )
     #set( $foo = $PortsAvailable.add($PortCount) )
   #end
```

So six lines of logic added, an *array* is created PoECapable to track switches capable of delivering PoE. Next, a loop with conditional logic sets a true or false flag depending if the switch is PoE Capable again using the `.add` *method*. Lastly, a Port pointer is created and set to the first port in each switch. Lastly, an availability counter for the number of available ports is set up.

The next chunk of code first resolves any accidental division by zero anomalies we might encounter by iterating through the two asked for variables for the number of Access Points, determining if they are even or odd, and making them even in the latter case. Additionally, we need to determine how to distribute the Access Points.

```
   ##Determine how many switches we can support Access Points on
   #foreach( $PoE in $PoECapable)
      #if( $PoECapable[$Switch] == 1 )
         #set( $NoAccessPointCapableSwitch = $NoAccessPointCapableSwitch + 1 )
      #end
   #end
   !
   #set( $ModulusAccessPoints = $NoAccessPoints % $NoAccessPointCapableSwitch )
   #if( $ModulusAccessPoints != 0 )
      #set( $NoAccessPoints = $NoAccessPoints + [$NoAccessPoints % $NoAccessPointCapableSwitch] )
   #end
   !
   #set( $NoAccessPointPerSwitch = $NoAccessPoints / $NoAccessPointCapableSwitch )
   !
```

Next, we need to iterate through the switches logically to set the correct macro to the port. The example might look like the following;

```
   !
   ##Start with AP distribution evenly across the stack
   !
   #foreach( $Switch in [1..$StackMemberCount] )
      #if( $PoECapable[$Switch] == 1 )
         #foreach( $AccessPoint in $NoAccessPointPerSwitch )
            #if( $PortsAvailable[$Switch] != 0 )
            	interface GigabitEthernet${Switch}/0/$Port[$Switch]
                 #access_point
               #set( $PortsAvailable[$Switch] = $PortsAvailable[$Switch] - 1 )
               #set( $Port[$Switch] = $Port[$Switch] + 1 )
            #end
         #end
      #end
   #end
   !
   ##Next with Guest Interface distribution evenly across stack
   #foreach( $GuestInterfaces in $NoGuestInterfaces )
      #foreach( $Switch in [1..${StackMemberCount}] )
         #if( $PortsAvailable[$Switch] != 0 )
   		   interface GigabitEthernet${Switch}/0/$Port[$Switch]
              #guest_interface
            #set( $PortsAvailable[$Switch] = $PortsAvailable[$Switch] - 1)
            #set( $Port[$Switch] = $Port[$Switch] + 1)
   		   #break
   	   #end
      #end
   #end
   !
   ##Add Workstation ports to stack
   #foreach( $Switch in [1..${StackMemberCount}] )
      #if( $PortsAvailable[${Switch}] != 0 )
   	   interface range GigabitEthernet${Switch}/0/$Port[$Switch] - $PortTotal[$Switch]
           #Workstation
         #set( $PortsAvailable[$Switch] = 0 )
   	#end
   #end
   !
```
In the first section, we iterate through the stack, and for switches with PoE Capability, we add an Access Point to each switch until they are evenly distributed. Next, we iterate through each switch evenly distributing guest interfaces. Lastly, we iterate through the ports filling the rest with workstation configured interfaces.

While this methodology deals programmatically with port configuration, and while you may adapt it for an environment, it is again lacking because it's still not dynamic enough. First, it's impossible to determine without looking at the configuration where something is plugged in. Secondly, if equipment or users are plugged into the wrong interface, they may get the wrong level of access. 

To deal with all these outstanding issues, we will look at the next lab section to provide the final solution to the problem.

## Step 4 - ***Autoconf Port Configuration - Use Case***
Previously within the Composite Templating Lab and in the previous section, we introduced a methodology of automatically configuring the interfaces within the switch. This configuration relies on a few variables used to extrapolate the settings that were then configured via the template. This allowed a set of macros to be utilized to build out the various settings for VLANs, Ports, and Uplinks. 

While these were methodologies that dealt programmatically with port configuration, and while you may adapt them for an environment, they are both lacking in the fact that they are not dynamic enough. Again, it's impossible to determine without looking at the configuration where something is plugged in. Secondly, if equipment or users are plugged into the wrong interface, they may get the wrong level of access. 

In previous code revisions, we could deal with some of the problems with Auto Smart Port technology, but that has been deprecated, and its replacement is a lot more dynamic. This section will deal with the first part of the problem concerning assigning ports for hardware like Access Points.

### ***Modify Code***
First, let's deal with VLANs on the Target switch. In the example above, we modified the existing code to extrapolate the various device VLANs using a built-in variable like the native VLAN. This is not a bad idea. Then you could define different native VLANs for downstream switches on a distribution, thereby building out the VLANs dynamically. If you prefer, an excel list of numbers could be an alternative. In that case, you would not need this section and rely on the variables being used after this code block.

```
   #set( $Integer = 0 ) ##defines Integer as numeric variable
   #set( $native_bind = $native_vlan) ) ##bind variable to native vlan
   #set( $mgmt_vlan = $Integer.parseInt($native_bind) ) 
   #set( $data_offset = 100 ) ##to set the voice vlan
   #set( $voice_offset = 200 ) ##to set the voice vlan
   #set( $ap_offset = 300 ) ##to set the ap vlan
   #set( $guest_offset = 400 ) ##to set the voice vlan
   #set( $data_vlan_number = $data_offset + $mgmt_vlan )
   #set( $voice_vlan_number = $voice_offset + $mgmt_vlan )
   #set( $ap_vlan_number = $ap_offset + $mgmt_vlan )
   #set( $guest_vlan_number = $guest_offset + $mgmt_vlan )
   #set( $bh_vlan_number = 999 )
```

The next block of code sets up the VLANs, and should the dynamic creation as mentioned not be desired; an excel list could be used to assign them as the template is run through the UI through importing the variable settings.

```
   !
   vlan ${data_vlan_number}
    name data
   vlan ${voice_vlan_number}
    name voice
   vlan ${ap_vlan_number}
    name accesspoint
   vlan ${guest_vlan_number}
    name guest
   vlan ${bh_vlan_number}
    name disabled
   !
   device-tracking upgrade-cli force
   !
   device-tracking policy IPDT_MAX_10
    limit address-count 10
    no protocol udp
    tracking enable
   !
```
Next, we need to set up the macros, but we will make use of **Autoconf** and **Templates**. **Autoconf** is a solution that can be used to manage port configurations for data or voice VLAN, quality of service (QoS) parameters, storm control, and MAC-based port security on end devices that are deployed in the access layer of a network. Device classification is enabled when you enable the Autoconf feature using the `autoconf enable` command in global configuration mode. The device detection acts as an event trigger, which applies the appropriate automatic template to the interface. When the Autoconf feature is enabled using the autoconf enable command, the default Autoconf service policy is applied to all the interfaces. For more information about **[Autoconf](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9400/software/release/16-12/configuration_guide/nmgmt/b_1612_nmgmt_9400_cg/configuring_autoconf.pdf)** or alternatively [Autoconf](./configuring_autoconf.pdf)

```
   #INTERACTIVE
   autoconf enable<IQ>yes<R>y
   #END_INTERACTIVE
   !
   parameter-map type subscriber attribute-to-service BUILTIN_DEVICE_TO_TEMPLATE
    10 map device-type regex "Cisco-IP-Phone"
     20 interface-template WORKSTATION
    20 map device-type regex "Cisco-IP-Camera"
     20 interface-template WORKSTATION
    30 map device-type regex "Cisco-DMP"
     20 interface-template WORKSTATION
    40 map oui eq "00.0f.44"
     20 interface-template WORKSTATION
    50 map oui eq "00.23.ac"
     20 interface-template WORKSTATION
    60 map device-type regex "Cisco-AIR-AP"
     20 interface-template ACCESS_POINT
    70 map device-type regex "Cisco-AIR-LAP"
     20 interface-template ACCESS_POINT
    80 map device-type regex "Cisco-TelePresence"
     20 interface-template WORKSTATION
    90 map device-type regex "Surveillance-Camera"
     10 interface-template WORKSTATION
    100 map device-type regex "Video-Conference"
     10 interface-template WORKSTATION
    110 map device-type regex "Cisco-CAT-LAP"
     10 interface-template ACCESS_POINT
   !
   template ACCESS_POINT
    description Access Point Interface
    switchport access vlan ${ap_vlan_number}
    switchport mode access
   !
   template WORKSTATION
    description Workstation
    switchport access vlan ${data_vlan_number}
    switchport mode access
    switchport voice vlan ${voice_vlan_number}
   !
   template GUEST
     description Guest Interface
     switchport access vlan ${guest_vlan_number}
     switchport mode access
   !
   ##Macros
   #macro( access_interface )
     description BASE CONFIG
     switchport access vlan ${bh_vlan_number}
     switchport mode access
     switchport port-security maximum 3
     switchport port-security
     snmp trap mac-notification change added
     snmp trap mac-notification change removed
     spanning-tree portfast
     spanning-tree bpduguard enable
     source template WORKSTATION
   #end
```

So the command `autoconf` enables the device classifier, which can then be manipulated to stray from the built-in templates through a *parameter-map*. The parameter map command allows for the mapping of defined interface templates. This is what we need to create our template for the Access Point. The rest of the built-in devices will point to the Workstation template. We define a Guest template as well as the macro for the interfaces. The macro will be used to configure the interfaces delivering the source template of WORKSTATION.

This will configure the interface with the normal VLAN and commands listed, and then when a device is plugged in, the device classifier will run. The interface will by default use the derived configuration of the WORKSTATION interface template, but should an Access Point be plugged in; then the interface would defer to the ACCESS_POINT template. 

Delivering the code to the interfaces becomes simpler now because we utilize a more dynamic device classification approach. 

We can continue to configure the uplink via the following Macro.
```
   !
   #macro( uplink_interface )
     switchport trunk allowed vlan add $data_vlan_number,$voice_vlan_number,$ap_vlan_number,$guest_vlan_number,$bh_vlan_number
   #end
```
Within the above code, we define a Macro to add the various VLANs to the trunk interface via the Port-Channel.

As we configure the interfaces, we can continue to use the previously defined method as the templates will be called and assigned more dynamically.

```
   !
   ##Access Port Configuration
   #foreach( $Switch in [0..$offset] )
     #set( $SwiNum = $Switch + 1 )
     interface range gi ${SwiNum}/0/1 - 9, gi ${SwiNum}/0/12 - $PortTotal[$Switch]
       #access_interface
   #end
   !
   ##Uplink Port Configuration
   interface portchannel 1
    #uplink_interface
   !
```
We apply the various previously defined Macros in the above code to configure the various access ports via a loop structure. We then apply the VLANs to the port-channel.

While we have configured all the various interfaces, this does not consider Authentication and Authorization scenarios. It sets us up nicely to reuse the templates calling them directly from Identity Services Engine in Authorization Policies.

## Step 5 - ***Non SDA IBNS2.0 Port Configuration - Use Case***
The last sections of this lab will walk through the various considerations for **IBNS2.0** and how to deal with host onboarding in a Non **SD-Access** Fabric environment. Once the Identity Services Engine is integrated with DNA Center, then not only do you get the benefit of pxgrid integration allowing for the building of policy, but the AAA Server section within Design will build out the various settings which inturn program the network access devices for AAA Network and Client Dot1x settings.

It is also essential to understand that with **IBNS2.0** and templates or interfaces running in ***closed mode***, the dynamic capability of **Autoconf** is not going to operate because there is a service-policy applied to the interface. While the device classifier will operate, for some devices that require an IP address, they may reboot before the classifier has done its job and so inconsistancies can occur. Remember in closed mode no packets are forwarded including DHCP prior to authentication occurring. If the interface is in ***low impact mode***, then and only then will **Autoconf** operate properly and as a result of the pre-auth acl DHCP may be allowed.

Considering DNA Center will push at that point all the relevant IBNS2.0 settings to the device, this leaves us with the mere setting up of **Host Onboarding**, which we will detail below.

#### **Important Note:** 
*We need to remember that for the use of this section, ISE needs first to have been integrated with DNA Center. Additionally, the Design Settings will need to be modified for the sites to include at the very least* **Client AAA**.

### ***Examine Code***
We will take the script as amended from above, which should look like this now;

```
   #set( ${Integer} = 0 ) 
   #set( ${mgmt_vlan} = $Integer.parseInt($native_bind) ) 
   #set( ${data_offset} = 100 ) 
   #set( ${voice_offset} = 200 ) 
   #set( ${ap_offset} = 300 ) 
   #set( ${guest_offset} = 400 ) 
   #set( $data_vlan_number = $data_offset + $mgmt_vlan )
   #set( $voice_vlan_number = $voice_offset + $mgmt_vlan )
   #set( $ap_vlan_number = $ap_offset + $mgmt_vlan )
   #set( $guest_vlan_number = $guest_offset + $mgmt_vlan )
   #set( $bh_vlan_number = 999 )
   !
   vlan ${data_vlan_number}
    name data
   vlan ${voice_vlan_number}
    name voice
   vlan ${ap_vlan_number}
    name accesspoint
   vlan ${guest_vlan_number}
    name guest
   vlan ${bh_vlan_number}
    name disabled
   !
   device-tracking upgrade-cli force
   !
   device-tracking policy IPDT_MAX_10
    limit address-count 10
    no protocol udp
    tracking enable
   !
   #INTERACTIVE
   autoconf enable<IQ>yes<R>y
   #END_INTERACTIVE
   !
   parameter-map type subscriber attribute-to-service BUILTIN_DEVICE_TO_TEMPLATE
    10 map device-type regex "Cisco-IP-Phone"
     20 interface-template WORKSTATION
    20 map device-type regex "Cisco-IP-Camera"
     20 interface-template WORKSTATION
    30 map device-type regex "Cisco-DMP"
     20 interface-template WORKSTATION
    40 map oui eq "00.0f.44"
     20 interface-template WORKSTATION
    50 map oui eq "00.23.ac"
     20 interface-template WORKSTATION
    60 map device-type regex "Cisco-AIR-AP"
     20 interface-template ACCESS_POINT
    70 map device-type regex "Cisco-AIR-LAP"
     20 interface-template ACCESS_POINT
    80 map device-type regex "Cisco-TelePresence"
     20 interface-template WORKSTATION
    90 map device-type regex "Surveillance-Camera"
     10 interface-template WORKSTATION
    100 map device-type regex "Video-Conference"
     10 interface-template WORKSTATION
    110 map device-type regex "Cisco-CAT-LAP"
     10 interface-template ACCESS_POINT
   !
   template ACCESS_POINT
    description Access Point Interface
    switchport access vlan ${ap_vlan_number}
    switchport mode access
   !
   template WORKSTATION
    description Workstation
    switchport access vlan ${data_vlan_number}
    switchport mode access
    switchport voice vlan ${voice_vlan_number}
   !
   template GUEST
     description Guest Interface
     switchport access vlan ${guest_vlan_number}
     switchport mode access
   !
   ##Macros
   #macro( access_interface )
     description BASE CONFIG
     switchport access vlan ${bh_vlan_number}
     switchport mode access
     switchport port-security maximum 3
     switchport port-security
     snmp trap mac-notification change added
     snmp trap mac-notification change removed
     spanning-tree portfast
     spanning-tree bpduguard enable
     source template WORKSTATION
   #end
   !
   #macro( uplink_physical )
     access-session inherit disable autoconf
   #end
   !
   #macro( uplink_interface )
     switchport trunk allowed vlan add $data_vlan_number,$voice_vlan_number,$ap_vlan_number,$guest_vlan_number,$bh_vlan_number
   #end
   !
   ##Access Port Configuration
   #foreach( $Switch in [0..$offset] )
     #set( $SwiNum = $Switch + 1 )
     interface range gi ${SwiNum}/0/1 - 9, gi ${SwiNum}/0/12 - $PortTotal[$Switch]
       #access_interface
   #end
   !
   ##Uplink Port Configuration
   interface portchannel 1
    #uplink_interface
   !
   ##Uplink Physical Port Configuration
   interface range gi 1/0/10 - 11
    #uplink_physical
```

Lastly, you could modify how you address ports using the built-in variable as it removes tthe need for indexing and additionally can be used with logic to address port types.

```
   ##Access Port Configuration
   #foreach( $interface in $__interface )
     #if( $interface.portMode == "access" && $interface.interfaceType == "Physical")
       interface $interface.portName
        #access_interface
     #end
   #end
```

As it stands, this is not a bad place to start, and only a few additions and modifications are required to allow for IBNS2.0.

### ***Modify Code***
First, we will ensure that the following lines change device tracking to the modern standard.

```
   device-tracking upgrade-cli force
   !
   device-tracking policy IPDT_MAX_10
    limit address-count 10
    no protocol udp
    tracking enable
```
Then we need to define the class maps utilized in the Dot1x policy. The policy and class maps follow the MQC methods previously used for QoS. These have been exploited for other service policies, and now we build IBNS2.0 using the same schema.

```
   !
   class-map type control subscriber match-all DOT1X_FAILED
    match method dot1x
    match result-type method dot1x authoritative
   !
   class-map type control subscriber match-all AAA_SVR_DOWN_UNAUTHD_HOST
    match authorization-status unauthorized
    match result-type aaa-timeout
   !
   class-map type control subscriber match-all AAA_SVR_DOWN_AUTHD_HOST
    match authorization-status authorized
    match result-type aaa-timeout
   !
   class-map type control subscriber match-all DOT1X_NO_RESP
    match method dot1x
    match result-type method dot1x agent-not-found
   !
   class-map type control subscriber match-all MAB_FAILED
    match method mab
    match result-type method mab authoritative
   !
   class-map type control subscriber match-any IN_CRITICAL_AUTH_CLOSED_MODE
    match activated-service-template DefaultCriticalAuthVlan_SRV_TEMPLATE
    match activated-service-template DefaultCriticalVoice_SRV_TEMPLATE
   !
   class-map type control subscriber match-none NOT_IN_CRITICAL_AUTH_CLOSED_MODE
    match activated-service-template DefaultCriticalAuthVlan_SRV_TEMPLATE
    match activated-service-template DefaultCriticalVoice_SRV_TEMPLATE
   !
   class-map type control subscriber match-all AUTHC_SUCCESS-AUTHZ_FAIL
    match authorization-status unauthorized
    match result-type success
   !
```
As we would with MQC, once we have defined the various class maps, we can then call upon them in a policy-map as follows;

```
	policy-map type control subscriber PMAP_DefaultWiredDot1xClosedAuth_1X_MAB
	 event session-started match-all
	  10 class always do-until-failure
	   10 authenticate using dot1x retries 2 retry-time 0 priority 10
	 event authentication-failure match-first
	  5 class DOT1X_FAILED do-until-failure
	   10 terminate dot1x
	   20 authenticate using mab priority 20
	  10 class AAA_SVR_DOWN_UNAUTHD_HOST do-until-failure
	   30 authorize
	   40 pause reauthentication
	  20 class AAA_SVR_DOWN_AUTHD_HOST do-until-failure
	   10 pause reauthentication
	   20 authorize
	  30 class DOT1X_NO_RESP do-until-failure
	   10 terminate dot1x
	   20 authenticate using mab priority 20
	  40 class MAB_FAILED do-until-failure
	   10 terminate mab
	   20 authentication-restart 60
	  50 class DOT1X_TIMEOUT do-until-failure
	   10 terminate dot1x
	   20 authenticate using mab priority 20
	  60 class always do-until-failure
	   10 terminate dot1x
	   20 terminate mab
	   30 authentication-restart 60
	 event aaa-available match-all
	  10 class IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure
	   10 clear-session
	  20 class NOT_IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure
	   10 resume reauthentication
	 event agent-found match-all
	  10 class always do-until-failure
	   10 terminate mab
	   20 authenticate using dot1x retries 2 retry-time 0 priority 10
	 event inactivity-timeout match-all
	  10 class always do-until-failure
	   10 clear-session
	 event authentication-success match-all
	 event violation match-all
	  10 class always do-until-failure
	   10 restrict
	 event authorization-failure match-all
	  10 class AUTHC_SUCCESS-AUTHZ_FAIL do-until-failure
	   10 authentication-restart 60
        !
        policy-map type control subscriber PMAP_DefaultWiredDot1xClosedAuth_MAB_1X
	 event session-started match-all
	  10 class always do-until-failure
	   10 authenticate using mab priority 20
	 event authentication-failure match-first
	  5 class DOT1X_FAILED do-until-failure
	   10 terminate dot1x
	   20 authentication-restart 60
	  10 class AAA_SVR_DOWN_UNAUTHD_HOST do-until-failure
	   30 authorize
	   40 pause reauthentication
	  20 class AAA_SVR_DOWN_AUTHD_HOST do-until-failure
	   10 pause reauthentication
	   20 authorize
	  30 class MAB_FAILED do-until-failure
	   10 terminate mab
	   20 authenticate using dot1x retries 2 retry-time 0 priority 10
	  40 class DOT1X_NO_RESP do-until-failure
	   10 terminate dot1x
	   20 authentication-restart 60
	  50 class DOT1X_TIMEOUT do-until-failure
	   10 terminate dot1x
	   20 authenticate using mab priority 20
	  60 class always do-until-failure
	   10 terminate mab
	   20 terminate dot1x
	   30 authentication-restart 60
	 event aaa-available match-all
	  10 class IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure
	   10 clear-session
	  20 class NOT_IN_CRITICAL_AUTH_CLOSED_MODE do-until-failure
	   10 resume reauthentication
	 event agent-found match-all
	  10 class always do-until-failure
	   10 terminate mab
	   20 authenticate using dot1x retries 2 retry-time 0 priority 10
	 event inactivity-timeout match-all
	  10 class always do-until-failure
	   10 clear-session
	 event authentication-success match-all
	 event violation match-all
	  10 class always do-until-failure
	   10 restrict
	 event authorization-failure match-all
	  10 class AUTHC_SUCCESS-AUTHZ_FAIL do-until-failure
	   10 authentication-restart 60
	   !
```
This policy-map allows for all eventualities and gracefully flows top down in a very simple flow. It deals with all exceptions gracefully and is not as rigid as the interface configuration methodology.

Once the class maps and policies have been defined, we need to utilize them.

```
   template ACCESS_POINT
    description Access Point Interface
    switchport access vlan ${ap_vlan_number}
    switchport mode access
    dot1x pae authenticator
    dot1x timeout supp-timeout 7
    dot1x max-req 3
    mab
    access-session closed
    access-session port-control auto
    authentication periodic
    authentication timer reauthenticate server
    service-policy type control subscriber PMAP_DefaultWiredDot1xClosedAuth_MAB_1X
   !
   template WORKSTATION
    description Workstation
    switchport access vlan ${data_vlan_number}
    switchport mode access
    switchport voice vlan ${voice_vlan_number}
    dot1x pae authenticator
    dot1x timeout supp-timeout 7
    dot1x max-req 3
    mab
    access-session closed
    access-session port-control auto
    authentication periodic
    authentication timer reauthenticate server
    service-policy type control subscriber PMAP_DefaultWiredDot1xClosedAuth_1X_MAB
   !
```
We have defined the various interface templates for use with the MQC DOT1X service policy. You have two options. Some prefer to call out a separate Guest interface template; however, because Dot1x technology automatically deals with that, we will remove that template.

Next, we can then modify the parameter map to suit the policy. Remember that with **IBNS2.0** and templates or interfaces running in ***closed mode***, the dynamic capability of **Autoconf** is not going to operate because only EAP packets are allowed by **Secure Access** on the interface initially until authentication occurs. Alternatively, if the interface is in ***low impact mode***, then and only then will **Autoconf** operate properly. I always leave the config on the switch in case of that eventuality.


```
   #INTERACTIVE
   autoconf enable<IQ>yes<R>y
   #END_INTERACTIVE
   !
   parameter-map type subscriber attribute-to-service BUILTIN_DEVICE_TO_TEMPLATE
    10 map device-type regex "Cisco-IP-Phone"
     20 interface-template WORKSTATION
    20 map device-type regex "Cisco-IP-Camera"
     20 interface-template WORKSTATION
    30 map device-type regex "Cisco-DMP"
     20 interface-template WORKSTATION
    40 map oui eq "00.0f.44"
     20 interface-template WORKSTATION
    50 map oui eq "00.23.ac"
     20 interface-template WORKSTATION
    60 map device-type regex "Cisco-AIR-AP"
     20 interface-template ACCESS_POINT
    70 map device-type regex "Cisco-AIR-LAP"
     20 interface-template ACCESS_POINT
    80 map device-type regex "Cisco-TelePresence"
     20 interface-template WORKSTATION
    90 map device-type regex "Surveillance-Camera"
     10 interface-template WORKSTATION
    100 map device-type regex "Video-Conference"
     10 interface-template WORKSTATION
    110 map device-type regex "Cisco-CAT-LAP"
     10 interface-template ACCESS_POINT
   !
```
Lastly, we need to build the macros for interface configuration, 
```
   ##Macros
   #macro( access_interface )
     description BASE CONFIG
     switchport access vlan ${bh_vlan_number}
     switchport mode access
     spanning-tree portfast
     spanning-tree bpduguard enable
     device-tracking attach-policy IPDT_MAX_10
     dot1x timeout tx-period 7
     dot1x max-reauth-req 3
     source template WORKSTATION
   #end
   !
   #macro( uplink_interface )
     switchport trunk allowed vlan add $data_vlan_number,$voice_vlan_number,$ap_vlan_number,$guest_vlan_number,$bh_vlan_number
   #end
   !
   #macro( #uplink_physical )
     access-session inherit disable autoconf
     cts manual
      policy static sgt 2 trusted     
   #end
   !
```
Then we need to configure the various interfaces with the new interface templates via macro and modify the uplink port-channel. Additionally, we need to add two CTS commands to the physical interfaces within the port-channel bundle that are not available at the logical level and only available at the physical layer.

```
   !Add SGACL enforcement
   cts role-based enforcement
   cts role-based enforcement vlan-list $data_vlan_number,$voice_vlan_number,$ap_vlan_number,$guest_vlan_number,$bh_vlan_number
   !
   ##Access Port Configuration
   #foreach( $Switch in [0..$offset] )
     #set( $SwiNum = $Switch + 1 )
     interface range gi ${SwiNum}/0/1 - 9, gi ${SwiNum}/0/12 - $PortTotal[$Switch]
       #access_interface
   #end
   !
   ##Uplink Port Configuration
   interface portchannel 1
    #uplink_interface
   !
   ##Uplink Physical Port Configuration
   interface range gi 1/0/10 - 11
    #uplink_physical
   !
```
Now that we have defined all the various IBNS2.0 configurations on the switch, as a device comes up on an interface, the device classifier will automatically run logically, attaching the interface template configuration of WORKSTATION onto an access port. If an Access Point is classified as being attached to the interface, it will instead logically attach the interface template configuration of ACCESS_POINT. The DOT1X service policy will run within both those interface templates, and the device will be authenticated. Identity Services Engine may, at that point, send a Change of Authorization and put the device in a differing VLAN or more.

Lastly, to create a fully dynamic environment, you might build out the following EEM scripts to entirely give that Dynamic look and feel. Because of the **Autoconf** vs **Closed Mode** limitation, we do not have a **Fully Dynamic environment**. Luckily, we have a way to resolve that issue. 

## Step 6 - ***Non SDA IBNS2.0 Fully Dynamic Port Configuration - Use Case***
So as explained, we have a chicken and the egg scenario, whereby we can't use **Autoconf** with **Closed Mode** as no packets can pass, which can be used with the parameter map to configure the interface automatically. Additionally, we want to have a **Secure Access** environment with **Zero Trust** using a policy on the interface that initially blocks traffic until authentication occurs. 

So how do we have our cake and eat it too...

Luckily we can create a fully dynamic environment with a gated procedure. You might build out the following EEM scripts to give that Dynamic look and feel entirely. Typically, the types of devices where we might have issues like this where *MAB* or *EAP* are not going to work maybe those which identify themselves in another way. In the following instance, we can use **PoE** power events to trigger an EEM. See the following code:

```
event manager applet DETECT_SW_IEEE_POE_UP
 event syslog pattern "%.*POWER.*GRANTED.* Interface.*"
 action 10    regexp "Interface ([^ ]+):" "$_syslog_msg" match intf
 action 20    cli command "enable"
 action 30    cli command "show run interface $intf | inc channel-group mode"
 action 40    regexp "(^channel-group)" "$_cli_result"
 action 50    if $_regexp_result ne "1"
 action 50.10  puts "POE Device Detected. INSTALL LOWIMPACT on Interface $intf"
 action 50.11  cli command "enable"
 action 50.12  cli command "conf t"
 action 50.13  cli command "default interface $intf"
 action 50.14  cli command "interface $intf"
 action 50.15  cli command " description AP CONFIG"
 action 50.16  cli command " switchport access vlan 10"
 action 50.17  cli command " switchport mode access"
 action 50.18  cli command " switchport port-security maximum 3"
 action 50.19  cli command " switchport port-security"
 action 50.20  cli command " device-tracking attach-policy IPDT_POLICY"
 action 50.21  cli command " snmp trap mac-notification change added"
 action 50.22  cli command " snmp trap mac-notification change removed"
 action 50.23  cli command " source template ACCESS_POINT"
 action 50.24  cli command " spanning-tree portfast"
 action 50.25  cli command " spanning-tree bpduguard enable"
 action 80    end
 action 90    cli command "write"
 action 99    cli command "exit"
``` 

In this section, we bind a new interface template for **ACCESS-POINTS** if a device powers up. This is an example only, and this would also catch IP Phones, so be aware you might deal with that as I will outline later, but let's deal with this use-case from a knowledge point of view.

The template could be designed for either **low-impact mode** or a differing **service policy** allowing *MAB* before *DOT1x*.

Two examples you might use for a differing **ACCESS-POINT** template. The first with *MAB* before *DOT1x*:

```
template ACCESS_POINT
 dot1x pae authenticator
 dot1x timeout supp-timeout 7
 dot1x max-req 3
 switchport access vlan 10
 mab
 access-session closed
 access-session port-control auto
 authentication periodic
 authentication timer reauthenticate server
 service-policy type control subscriber PMAP_DefaultWiredDot1xClosedAuth_MAB_1X
 ip access-group ACL-DEFAULT in
 description Access Point Interface
```

The second example is low impact mode, and session-access closed is removed:

```
template ACCESS_POINT
 dot1x pae authenticator
 dot1x timeout supp-timeout 7
 dot1x max-req 3
 switchport access vlan 10
 mab
 access-session port-control auto
 authentication periodic
 authentication timer reauthenticate server
 service-policy type control subscriber PMAP_DefaultWiredDot1xClosedAuth_MAB_1X
 ip access-group ACL-DEFAULT in
 description Access Point Interface
```

If you need a trunk interface for this scenario, you might add a **FLEXCONNECT** specific configuration like so:

```
template FLEX_ACCESS_POINT
 dot1x pae authenticator
 dot1x timeout supp-timeout 7
 dot1x max-req 3
 switchport trunk native vlan 10
 switchport trunk allowed vlan 10,20,30,40,999
 switchport mode trunk
 mab
 access-session port-control auto
 access-session interface-template sticky timer 30
 authentication periodic
 authentication timer reauthenticate server
 service-policy type control subscriber PMAP_DefaultWiredDot1xClosedAuth_MAB_1X
 ip access-group ACL-DEFAULT in
 description Flex Access Point Interface
```
Alternatively, you might send this as an **AV-PAIR** within the **AUTHZ Profile** as part of the results of an **Authorization Policy**. The `access-session interface-template sticky timer 30` command is required for this type of modification where **AV-PAIR** are sent from **ISE** or other **AAA**. ***Please Note:*** *do not forget the timer option as it's required for dynamic modifications.* If the device was discovered to be an IP Phone, you could also choose to send the workstation template as part of the **AUTHZ Profile**.

But you may say, we have modified the physical interface configuration, well we can reset that too to the **BASE CONFIG** through another EEM script as follows:

```
event manager applet DETECT_SW_INT_DOWN
 event syslog pattern "%LINK.* Interface.* changed state to .* down"
 action 10    regexp "Interface ([^ ]+)," "$_syslog_msg" match intf
 action 20    cli command "enable"
 action 30    cli command "show run interface $intf | inc channel-group mode"
 action 40    regexp "(^channel-group)" "$_cli_result"
 action 50    if $_regexp_result ne "1"
 action 50.10  puts "AP Trunk Interface DOWN. INSTALL BASECONFIG on Interface $intf"
 action 50.11  cli command "enable"
 action 50.12  cli command "conf t"
 action 50.13  cli command "default interface $intf"
 action 50.14  cli command "interface $intf"
 action 50.15  cli command "access-session inherit disable interface-template-sticky"
 action 50.16  cli command "default interface $intf"
 action 50.17  cli command "interface $intf"
 action 50.18  cli command " description BASE CONFIG"
 action 50.20  cli command " switchport mode access"
 action 50.21  cli command " switchport port-security maximum 3"
 action 50.22  cli command " switchport port-security"
 action 50.23  cli command " device-tracking attach-policy IPDT_POLICY"
 action 50.24  cli command " snmp trap mac-notification change added"
 action 50.25  cli command " snmp trap mac-notification change removed"
 action 50.26  cli command " source template WORKSTATION"
 action 50.27  cli command " spanning-tree portfast"
 action 50.28  cli command " spanning-tree bpduguard enable"
 action 60    else
 action 70     puts "Non-EMM port Interface $intf went down."
 action 80    end
 action 90    cli command "write"
 action 99    cli command "exit"
```

This EEM script makes sure the interface is not a portchannel member and then reverts the interface to the **BASE CONFIG** automatically.

## Summary
Congratulations, at this point, you have successfully reviewed and may have adopted the various use cases or parts of them.

The next set of labs will be to build on these concepts utilizing REST-API to push changes to DNA Center Templates and further automate the configuration in the network infrastructure. 

The following **LAB** will tie all this together.

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.



