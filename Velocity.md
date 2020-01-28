

### Velocity Scripting
This section will describe the various tools and techniques used to make a powerful script out of normal CLI command scripts which are used by organizations on IOS devices around the world. This section is an attempt to demystify the hows and to bring clarity on what is truely possible. While it is possible to take a CLI script for one device and create a template for one device at a time, that would leave us with a lot of templates and make it harder to make changes on an ongoing basis. Using the techniques below will allow us to deploy equipment with scripts which can be reused, allowing us to keep configurations similar for conformity reasons but also to reduce the number of places where changes would have to be made. 

To that end it is important to write modular scripts which make use of all the power of programming but allow us to do it within the DNAC platform as templates. 

Velocity language typically allows for If/elseif/else constructs, macros and more.

#### IF Statements
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
 
#### Macro's
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

#### Foreach Loops
A Foreach loop allows for multiple iterations of a sequence of commands perhaps including some of the constructs mentioned above to iterate through and on each occasion use a different value.

Command Construct:

```
#[{]foreach[}] ( $ref in arg ) statements [#[{]else[}] alternate statements] #[{]end[}]

Usage:
    $ref                 - The first variable reference is the item.
    arg                  - May be one of the following: a reference to a list 
                           (i.e. object array, collection, or map), an array list, or the range operator.
    statements           - What is output each time Velocity finds a valid item in the list denoted above as arg. 
                           This output is any valid VTL and is rendered each iteration of the loop.
    alternate statements - What is to display whenever Velocity did not enter the loop (
                           when arg is null, empty, or doesn't have any valid iterator).
```
Additionally you can use these methods within the loop:

```
    $foreach.count : 1-based loop index
    $foreach.index : 0-based loop index
    $foreach.first : true on the first iteration
    $foreach.last : true on the last iteration
    $foreach.hasNext : false on the last iteration
    $foreach.stop() : exists the loop, synonym for #break
```

An example of a Foreach Loop


    Reference: #foreach ( $item in $items ) $item #else no item #end
    Array list: #foreach ( $item in ["Not", $my, "fault"] ) $item #end
    Range operator: #foreach ( $item in [1..3] ) $item #end

