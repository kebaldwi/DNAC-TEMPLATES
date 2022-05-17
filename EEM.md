# EEM - Embedded Event Manager [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
Embedded Evenet Manager is a tool which allows a switch to automate actions based on triggers. Triggers can come in many forms from Syslog through to Timers as depicted in the following slide. Actions can be then taken by the device utilizing cli commands through to TCL or Python Scripts. This section will start to dive into various capabilities and use cases for EEM scripts which can be deployed on Cisco Catalyst Products.

## Case 1 - ***Renaming Interfaces - Use Case***
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

## Case 2 - ***Sending a IOS-XE command to clear a table - Use Case***
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

## Case 3 - ***Dynamic Port Configuration for Low-Impact Mode - Use Case***
To deal with the chicken and the egg scenario, whereby we can't use **Autoconf** with **Closed Mode** as no packets can pass, which can be used with the parameter map to configure the interface automatically. Additionally, we want to have a **Secure Access** environment with **Zero Trust** using a policy on the interface that initially blocks traffic until authentication occurs. 

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

## Case 4 - ***Dynamic Port Configuration for Closed Mode - Use Case***
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
