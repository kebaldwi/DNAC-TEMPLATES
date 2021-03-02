# Advanced Velocity
This section will describe the various advanced techniques used to make a powerful script out of normal CLI command scripts which are used by organizations on IOS devices around the world. This section builds on the previous sections and is an attempt to demystify the hows and to bring clarity on what is truely possible. While it is possible to take a CLI script for one device and create a template for one device at a time, that would leave us with a lot of templates and make it harder to make changes on an ongoing basis. Using the techniques below will allow us to deploy equipment with scripts which can be reused, allowing us to keep configurations similar for conformity reasons but also to reduce the number of places where changes would have to be made. 

Below will be examples of various use cases that could be implemented.

### Parsing Integers from String Variables
In the following example a variable is bind to DNA Centers database and a value is called for the Native Vlan. As all data within the database is essentially in string format, if we wish to use it with some mathematics tto calculate other values, we would first need to change it from a string to a integer.

In order to acomplish this we need to use this example. First we need to create an integer variable to be used to parse the bind variable too. Then set the result of that equation into a variable called native_vlan. We can then perform mathematical equations to extrapolate other values.

```
#set( $integer = 0 )
#set( $native_vlan = $integer.parseInt($native_vlan_bind) )
#set( $data_vlan = $native_vlan + 10 )
```

### Working with Arrays or Lists
To create an array we have to perform the following. First we need to concatenate the values into a variable with some kind of delimiter. Then using the delimiter we can split the values into separate elements within the array and call them separately.

```
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

```
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





If you found this section helpful please fill in the survey and give feedback on how it could be improved.

Special mention to: https://explore.cisco.com/dnac-use-cases/apache-velocity as examples and extrapolations were made using this documentation and Adam Radford for his help with some of the concepts discussed.
