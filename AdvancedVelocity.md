# Advanced Velocity
This section will describe the various advanced techniques used to make a powerful script out of normal CLI command scripts which are used by organizations on IOS devices around the world. This section builds on the previous sections and is an attempt to demystify the hows and to bring clarity on what is truely possible. While it is possible to take a CLI script for one device and create a template for one device at a time, that would leave us with a lot of templates and make it harder to make changes on an ongoing basis. Using the techniques below will allow us to deploy equipment with scripts which can be reused, allowing us to keep configurations similar for conformity reasons but also to reduce the number of places where changes would have to be made. 

Below will be examples of various use cases that could be implemented.

### Combining Bind Variables
You can also extrapolate variables from known values once the device has been onboarded into the inventory. If the device was populated with the pnp startup-vlan command value then then the native vlan would be set to follow that automatically on the target switch. You could bind a variable and then use that to determine many other values for the device automatically.

```
#set( $voice-offset = 4000 )
#set( $data_offset = 1 )
#set( $integer = 0 )
#set( $native_vlan_var = $native_bind )
#set( $native_vlan = $integer.parseInt($native_vlan_var) )
#set( $data_vlan = ${native_vlan}-${data_offset} )
#set( $voice_vlan = ${data_vlan}+${voice-offset} )
```

If you found this section helpful please fill in the survey and give feedback on how it could be improved.

Special mention to: https://explore.cisco.com/dnac-use-cases/apache-velocity as examples and extrapolations were made using this documentation and Adam Radford for his help with some of the concepts discussed.
