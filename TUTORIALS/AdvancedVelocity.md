# Advanced Velocity [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

This section will describe the various advanced templating techniques used to make a powerful script out of normal CLI command scripts which are used by organizations on IOS devices around the world. This section builds on the previous sections and is an attempt to demystify the hows and to bring clarity on what is truely possible. While it is possible to take a CLI script for one device and create a template for one device at a time, that would leave us with a lot of templates and make it harder to make changes on an ongoing basis. Using the techniques below will allow us to deploy equipment with scripts which can be reused, allowing us to keep configurations similar for conformity reasons but also to reduce the number of places where changes would have to be made. 

Below will be examples of various use cases that could be implemented.

### Parsing Integers from String Variables

In the following example a variable is bind to Catalyst Centers database and a value is called for the Native Vlan. As all data within the database is essentially in string format, if we wish to use it with some mathematics to calculate other values, we would first need to change it from a string to a integer.

In order to acomplish this we need to use this example. First we need to create an integer variable to be used to parse the bind variable too. Then set the result of that equation into a variable called native_vlan. We can then perform mathematical equations to extrapolate other values.

```vtl
   #set( $integer = 0 )
   #set( $native_vlan = $integer.parseInt($native_vlan_bind) )
   #set( $data_vlan = $native_vlan + 10 )
```

### Working with Arrays or Lists

To create an array we have to perform the following. First we need to concatenate the values into a variable with some kind of delimiter. Then using the delimiter we can split the values into separate elements within the array and call them separately.

```vtl
   #set( $Switches = 8 )
   #foreach( $Switch in [1..${Switches}] )
       #if( $Switch == 1 )
           #set( $PortArray = $PortsCount )
       #else
           #set( $PortArray = $PortArray + "," + $PortsCount )
       #end
   #end
   !
   #set( $SwitchPorts = $PortArray.split(",") ) ## Number of ports in the switches in stack
   !
   #foreach( $Switch in [1..${Switches}] )
       #set( $ID = $Switch - 1 )
       interface ${Switch}/0/1 - $SwitchPorts[$ID]
       desc test
   #end
```

Another way we may work with arrays is to use the add operator. This method would look like this.

```vtl
   #set( $PortArray = [] )
   #set( $PortsCount = 48 )
   !
   #set( $Switches = 8 )
   #foreach( $Switch in [1..${Switches}] )
       #set( $unused = $PortArray.add($PortsCount))
   #end
   !$PortArray
   !
   #foreach( $Switch in [1..${Switches}] )
       #set( $ID = $Switch - 1 )
       interface ${Switch}/0/1 - $PortArray[$ID]
       desc test
   #end
```

### Working with Stacks of 9300/9200 and Powerstacking

One area we need to address is how to effectively deal with stacking 9300's and how to deal with a stack of 8 switches where a powerstack only allows 4. Although not supported by TAC this is supported from a platform point of view. Essentially you would build the data stack of 8 switches, and then build two powerstacks of four switches in each. In the following example I share the code which allows this to happen which was co-written by Josh Bronikowski. 

In order to acomplish this we need to first identify how many switches are in the stack... please use this example. 

```vtl
   #set( $StackPIDs = $ProductID.split(",") )
   #set( $StackMemberCount = $StackPIDs.size() )
```
Then we need a logical construct which iterates through each switch setting not only the priority correctly but also setting the powerstack correctly.
mod

```vtl
   #if( $StackMemberCount > 1 )
      stack-power stack Powerstack1
      mode redundant strict
      #if( $StackMemberCount > 4 )
         stack-power stack Powerstack2
         mode redundant strict
      #end
      #foreach( $Switch in [1..$StackMemberCount] )
         stack-power switch ${Switch}
         #if( $Switch <= ($StackMemberCount/2 + $StackMemberCount%2) or $StackMemberCount < 5 )
            stack Powerstack1
         #elseif( $Switch > ($StackMemberCount/2 + $StackMemberCount%2) )
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
#### Explained here...

1. The code shared will run only if the number of switches in the stack is found to be greater than 1.

```vtl
   #if( $StackMemberCount > 1 )
```

2. The next step is to correctly set the number of powerstack required. If the number of switches exceeds 4 then we need two powerstacks set up.

```vtl
   stack-power stack Powerstack1
   mode redundant strict
   #if( $StackMemberCount > 4 )
      stack-power stack Powerstack2
      mode redundant strict
   #end
```

3. The next step is to iterate through the switches in the stack setting the stackpower appropriately for each switch and adding them to the correct powerstack 

```vtl
   #foreach( $Switch in [1..$StackMemberCount] )
      #if( $Switch < 5 )
         stack-power switch ${Switch}
         stack Powerstack1
      #elseif( $Switch > 4 )
         stack-power switch ${Switch}
         stack Powerstack2
      #end
    #end
```
4. Lastly, we will set the switch priority appropriately on each switch for master and standby, and then for the remaining switches within the stack so that switch numbering matches the priority levels.

```vtl
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
```

### Working port counts within Catalyst 9k

One area we need to address is how to effectively deal configuring multiple ports. For this we will make use of multiple concepts as we build out this use case.

First we would need to identify how many ports we have on each switch or linecard, and how many linecards or switches within the stack or chassis there are. For this example we are using a stack of 9300's, but you can build this for 9400's.

We set up variables to track in Array format the number of ports per switch.

```vtl
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

The next step would be to build macros and vlans to configure the various ports.

```vtl
   vlan ${data_vlan_number}
     name ${site_code}-Employees
   vlan ${voice_vlan_number}
     name ${site_code}-Voice
   vlan ${iot_vlan_number}
     name ${site_code}-IOT
   vlan ${guest_vlan_number}
     name ${site_code}-Guests
   vlan ${ap_vlan_number}
     name ${site_code}-AP
   
   #macro( uplink_interface )
       switchport trunk allowed vlan add ${voice_vlan_number},${iot_vlan_number},${guest_vlan_number},${ap_vlan_number}     
   #end
   
   #macro( access_interface )
     description base port config
     switchport mode access
     switchport access vlan ${data_vlan_number}
     switchport voice vlan ${voice_vlan_number}
     spanning-tree portfast
     spanning-tree bpduguard enable
   #end
   
   #foreach( $Switch in [0..$offset] )
     #set( $SwiNum = $Switch + 1 )
     interface range gi ${SwiNum}/0/1 - $PortTotal[$Switch]
       #access_interface
   #end
   
   interface portchannel 1
    #uplink_interface
```

While this would configure the access ports, and modify the port channel for upstream connectivity we could do more to automate we will look at that next.

## Network Profile Compliance 

To exclude specific commands from compliance checks in Catalyst Center, you can use the **ignore-compliance** flags. These flags, added to your templates, tell Catalyst Center to bypass compliance checks for commands within those boundaries. Specifically, you can enclose the commands you want to omit with:

```J2
 ! @ start-ignore-compliance 
 
 ! @ end-ignore-compliance
```

Here's a breakdown:

### What is Compliance?

Catalyst Center uses templates to define the desired configuration for your network devices. It then compares the device's running configuration against these templates to ensure they are compliant. 

### Why Omit?
There might be situations where you need to make changes to a device's configuration that don't align with the template, but you still want to keep the overall compliance status in check. For example, you might need to temporarily disable a feature for testing or make a specific change that deviates from the standard configuration. 

#### How to Omit Commands

**! @ start-ignore-compliance**: This flag indicates the start of a section in the template that should be excluded from compliance checks.

**! @ end-ignore-compliance**: This flag indicates the end of the section that should be excluded from compliance checks.

Example: 

```sh
    interface GigabitEthernet1/0/1
     ! @ start-ignore-compliance
     no switchport
     ! @ end-ignore-compliance
     switchport mode trunk
     switchport trunk allowed vlan 100,200
```

In this example, Catalyst Center will ignore the **no switchport** command for compliance checks. 

### Important Considerations

#### When to use:

Use ignore-compliance only for specific scenarios where a deviation from the template is necessary, but you want to maintain overall compliance. 

#### Documentation:

Refer to the official Catalyst Center documentation for the most up-to-date information on compliance features and how to use them. 

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

Special mention to: https://explore.cisco.com/dnac-use-cases/apache-velocity as examples and extrapolations were made using this documentation and Adam Radford and Josh Bronikowski for his help with some of the concepts discussed.

> [**Return to Main Menu**](../README.md)