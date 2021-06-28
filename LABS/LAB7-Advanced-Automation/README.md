# Advanced Automation - In Development
## Overview
This Lab is designed to be used after first completing labs 1 through 4 and has been created to address how to use some advanced automation concepts not previously touched on in the previous labs. This is an enablement type lab and is designed to help customers to reach beyond what they currently understand and try new concepts and really push the boundaries of automation.

During this lab we will cover various topics with regard to template logic to solve various use cases. Some of these concepts have been previously covered but perhaps not with as indepth a focus.

The examples of shown below can be used in building your own versions of the templates. The concept of this lab is for you to build regilar templates that you can substitute into the composite to test with. Various methods for the varing use cases will be given explaining pros and cons along the way. Expand your capabilities with this lab and take your abilities toward the next level. Your only inhibited by your own imagination. 

## General Information
As previously discussed, DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates and for more flexibility Composite Templates. as they can be used to apply ongoing changes and to allow device modifications after initial deployment. 

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used you should **not** deploy the same feature from cli code in a template to configure the device. Its a decision you have to make upfront and avoids a lot of lines in the templates and allows for a more UI centric configuration which is easier to maintain. 

As a guidance try and use **Design Settings** for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing.

With these things in mind we will cover various aspects and use cases which perhaps allow for a more programamtic approach.

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
The Topics listed above will be covered in a number of use cases to show the capability and flexibility of the templating engine within DNA Center. While we will utilize Velocity language the same can be accomplished in the Jinja2 language.

1. [Renaming interfaces](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB7-Advanced-Automation/README.md#step-1---renaming-interfaces---use-case)
2. [Building Stacks](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB7-Advanced-Automation/README.md#step-2---building-stacks---use-case)
3. [Assigning port configuration](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB7-Advanced-Automation/README.md#step-3---assigning-port-configuration---use-case)
4. [Autoconf port configuration](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB7-Advanced-Automation/README.md#step-4---autoconf-port-configuration---use-case)
5. [Non SDA IBNS 2.0 port configuration](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB7-Advanced-Automation/README.md#step-5---non-sda-ibns2.0-port-configuration---use-case)

## Step 1 - ***Renaming Interfaces - Use Case***
Previously within the Composite Templating Lab we introduced a methodology of automatically naming the interfaces within the switch. When a new device or switch/router/access point connects to a switch we want to name those interfaces. Naming the uplinks specifically, but also the various wireless access points and IP Phones would be a nice addition. 

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
First lets address the primary problem, the naming of interfaces with descriptions.

You will see that lines *201 to 220* were added to the EEM script. Within that construct we look for the keyword `Trans-Bridge` within the built in variable to determine if the port is connected to an Access Point. If it is then it results in a True or binary 1 state and the included code from lines *211 to 220* run line by line. The configuration adds a description to the interface for the phone of `description AP - KO-AP0C75 - GigabitEthernet0` for example.

You will see that lines *250 to 260* were added to the EEM script. Within that construct we look for the keyword `Phone` within the built in variable to determine if the port is connected to a Phone. If it is then it results in a True or binary 1 state and the included code from lines *253 to 260* run line by line. The configuration adds a description to the interface for the phone of `description Phone - SEPB07D47D34910 - Port 1` for example.

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

## Step 2 - ***Building Stacks - Use Case***
Previously within the Composite Templating Lab we introduced a methodology of automatically build a data stack and power stack configuration within the switch. When a new device or switch is built we may want to control which switch is Active and which switch is standby within the stack. To that end the following configuration has been built previously:

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
Within this script you can see the use of the Arrays `$Stackcount` which is formed through the use of the `.split(",")` method which takes the string returned from the database and splits the list into two elements within the Array `$Stackcount`. You could address each element in the Array remembering that Arrays always start the numbering of elements at position zero (0). In a two element Array you could call the data with these two options; for the first element in the Array `$Stackcount[0]` or for the second element in the Array `$Stackcount[1]`.

Within this script you can see the use of the Conditional Statements `#if #elseif #else #end` these are used to dynamically build configuration for switch stacks no matter how many switches are within the stack. For example if the number of switches in the stack is above 4 then it creates automatically 2 powerstack environments for power redundancy. The script also sets the priority of the Active and Standby switch above those of the rest of the switches in the stack.

Within this script you can see the use of the Enable Statements `#MODE_ENABLE #MODE_END_ENABLE` these commands allow for privileged level non configuration commands to be entered. In this script we need to configure the privileged level command to set switch priority for individual switches `switch $Switch priority #`. Bracketing this configuration command with the velocity statements `#MODE_ENABLE #MODE_END_ENABLE` allows for us to change from configuration mode to enable mode and back again.

## Step 3 - ***Assigning Port Configuration - Use Case***
Previously within the Composite Templating Lab we introduced a methodology of automatically configuring the interfaces within the switch. This configuration relied on a few variables which were use to extrapolate the settings which were then configured via the template. This allowed for a set of macros to be utilized to build out the various settings for VLANs, Ports and Uplinks. We will analyze the configuration in more detail below and modify it for greater capabilities toward the end of this section.

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
Within the first block of code some interesting concepts are dealt with. First we create an *Array* with the various Product ID's for each switch within the stack using the `.split(",")` *method* as we previously discussed in step 2. The `.size()` *method* is then used to determine how many switches are in the stack. A blank *array* is defined for later use. We then create an offset variable to account for the fact that *arrays* start at zero (0) to be used throughout the template.

Within the loop structure, we iterate through using the variable PortCount to load the regex value grep'd from the Product ID accomplished via the `.replaceAll(""C9300L?-([2|4][4|8]).*","$1"")` *method* which in each case is either 24 or 48 to denote a 24 or 48 port switch. The PortCount variable is then appended to the *array* PortTotal using the add *method*.

We now have the data we need to configure the ports of the switch, being the number of switches, and the number of ports in each switch.
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
In the configuration above we use simple addition to determine the VLAN ID for each vlan built from a set of constants and a numeric variable to denote the MDF.
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
Within the above code we define a Macro to add the various VLANs to the trunk interface via the Port-Channel.
```
   !
   ##Access Port Configuration
   #foreach( $Switch in [0..$offset] )
     #set( $SwiNum = $Switch + 1 )
     interface range gi ${SwiNum}/0/1 - 9, gi ${SwiNum}/0/12 $PortTotal[$Switch]
       #access_interface
   #end
   !
   ##Uplink Port Configuration
   interface portchannel 1
    #uplink_interface
   !
```
In the above code we apply the various previously defined Macros to configure the various access ports via a loop structure. We then apply the VLANs to the port-channel.

Now while this is an eligant script it could be more automated and include ways to deal with both Access Points, and IOT devices in the same script. Lets look at how we might make these kind of changes in an automated programatic way.

First lests deal with vlans on the Target switch. In the example above we use one variable to extrapolate the various device VLANs. Alternatively, that could be accomplished using a built in variable like the native VLAN and a similar approach.

```
   #set(${Integer} = 0) ##defines Integer as numeric variable
   #set(${mgmt_vlan} = $Integer.parseInt(${native_bind})) ##bind variable to native vlan
   #set(${data_offset} = 100) ##to set the voice vlan
   #set(${voice_offset} = 200) ##to set the voice vlan
   #set(${ap_offset} = 300) ##to set the ap vlan
   #set(${guest_offset} = 400) ##to set the voice vlan
   #set( $data_vlan_number = $data_offset + $mgmt_vlan )
   #set( $voice_vlan_number = $voice_offset + $mgmt_vlan )
   #set( $ap_vlan_number = $ap_offset + $mgmt_vlan )
   #set( $guest_vlan_number = $guest_offset + $mgmt_vlan )
   #set( $bh_vlan_number = 999 )
```
In this example we now no longer need to input any information and as the offsets are used if needs be we can use excel instead of set values for defining those in bulk. In the example shown we are defining them explicitly, but those lines could be replaced by entry values in a form or excel.

Secondly we could allow for various device types of Access Point and IOT device with the introduction of more Macros. As each device type may each require differing VLANs and port settings: *(note: in the guest example below the assumption is a layer 2 to a firewall providing local gateway for guest access DIA to the internet)*

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
The last piece of the puzzle would be to programatically determine where the ports were configured for the various tasks and devices. To accomplish this we can again resort to logic. Now to start with we need to account for whether a switch is PoE capable or not so lets add some magic.

```
   ##Stack information variables
   #set( $StackPIDs = $ProductID.split(",") )
   #set( $StackMemberCount = $StackPIDs.size() )
   #set( $PortTotal = [] )
   #set( $PoECapable = [] )
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
     #set( $foo = $PortsAvailable.add($PortsCount) )
   #end
```

So six lines of logic added, an *array* is created PoECapable to track switches capable of delivering PoE. Next a loop with conditional logic to set a true of false flag depending if the switch is PoE Capable again using the `.add` *method*. Lastly a Port pointer is created and set to the first port in each switch. Lastly an availability counter for the number of ports still available is set up.

```
   #if( [$NoAccessPoints % 2] != 0 )
      #set( $NoAccessPoints = $NoAccessPoints + 1 )
   #end
   #if( [$NoGuestInterfaces % 2] != 0 )
      #set( $NoGuestInterfaces = $NoGuestInterfaces + 1 )
   #end
```

Next, we need to iterate through the switches in a logical predetermined way to set the correct macro to the port. The example might look like the following;

```
   !
   ##Distribute required devices evenly over stack for power where posible
   ##Start with AP distribution evenly across stack
   #foreach( $AccessPoint in $NoAccessPoints )
      #foreach( $Switch in [1..$StackMemberCount] )
         #if( [$PortsAvailable[$Switch] != 0] && [$PoECapable[$Switch] == 1] && [$NoAccessPoints != 0] )
   		   interface GigabitEthernet${Switch}/0/$Port[$Switch]
              #access_point
              #set( $NoAccessPoints = $NoAccessPoints - 1)
              #set( $PortsAvailable[$Switch] = $PortsAvailable[$Switch] - 1)
              #set( $Port[$Switch] = $Port[$Switch] + 1)
   		#else
   		   #break
   	   #end
      #end
   #end
   !
   ##Next with Guest Interface distribution evenly across stack
   #foreach( $GuestInterfaces in $NoGuestInterfaces )
      #foreach( $Switch in [1..${StackMemberCount}])
         #if( [$PortsAvailable[$Switch] != 0] && [$NoGuestInterfaces != 0] )
   		   interface GigabitEthernet${Switch}/0/$Port[${Switch}]
              #guest_interface
              #set( $NoGuestInterfaces = $NoGuestInterfaces - 1 )
              #set( $PortsAvailable[$Switch] = $PortsAvailable[$Switch] - 1)
              #set( $Port[$Switch] = $Port[$Switch] + 1)
   		#else
   		   #break
   	   #end
      #end
   #end
   !
   ##Add Workstation ports to stack
   #foreach( $Switch in [1..${StackMemberCount}])
      #if($PortsAvailable[${Switch}] != 0)
   	   interface range GigabitEthernet${Switch}/0/$Port[${Switch}]-$PortsCount[${Switch}]
           #Workstation
           #set($PortsAvailable[${Switch}] = 0)
   	#end
   #end
   !
```

## Step 4 - ***Autoconf Port Configuration - Use Case***

## Step 5 - ***Non SDA IBNS2.0 Port Configuration - Use Case***

## Availability Information
This lab is under development please come back soon. ETA for delivery June 30 2021.



