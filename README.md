# DNAC-TEMPLATES
## Overview

This Repository will give examples of templates used in DNA Center that can be modified. Additional information will be included to hopefully give a well rounded explanation of Automation methods with Templates using DNA Center and flows with both Onboarding and DayN Templates and concepts.

The section will include scripts and examples with the following:
1. Velocity Scripting
2. Variables
3. Binding Variables
4. Composite Templates

## PnP Workflow

The PnP workflow is as follows:

### Scripting

#### Velocity Scripting

Velocity language typically allows for If/elseif/else constructs, macros and more.

##### IF Statements
IF statements are a useful tool for scripting and allow for a decision tree in which under certain circumstances various commands can be used alone or in combination. To create an IF statement examples have been provided below. That said it is important to understand that the IF statement may be used alone or in combination with the following;

```
#if
#end

#if
#else
#end

#if
#elseif
#else
#end

```
That said it is important to understand that these decisions allow for you to script for multiple circumstances or platforms allowing you to write code which can be reused and therefore modular.

If/elseif/else construct with a check to see if data in variable contains a string:

 ```
 #if( $hostname.contains("C9300-48") )
    !some commands
 #elseif( $hostname.contains("C9300-24") )
    !some more commands
 #else
    !even more commands
 #end
 
 ```
 
##### Macro's
A Macro is a snippit of code which can be called over and over again within a template. Take the following example into consideration. Alone the Macro does not seem that powerful but when combined with the previous sections IF statement it suddenly allows for a more powerful script.

```
#macro (Interfaces)
int lo 0
  desc mgmt address
  ip address 10.0.0.${Switch} 255.255.255.255
!
int vlan 1
  desc mgmt vlan - with pnp
  ip address 10.1.1.${Switch} 255.255.255.0
!
#end

```

When combined with the IF statements below, the above Macro allows for various IP's to be set on the same interface on multiple switches as long as the hostname variable contains a specific string value.

```
#if( $hostname.contains("C9300-48") )
#set( $Switch = 30 )
#Interfaces
#elseif( $hostname.contains("C9300-24") )
#set( $Switch = 20 )
#Interfaces
#else
#set ( $Switch = 10 )
#Interfaces
#end

```

#### Variables
Variables may be defined in a couple of ways but the data entered will either numerical or string.

```
${Switch}
$Switch

```

Data may be set to the variables via a set command

```
#set( $StringVariable = "text" )
#set( $NumericVariable = 10 )

```
or alternatively using the UI

![json](images/variable-type.png?raw=true "Import JSON")


