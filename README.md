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

Examples of If/elseif/else construct with a check to see if data in variable contains a string:

 ```
 #if( $hostname.contains("C9300-48") )
    !some commands
 #elseif( $hostname.contains("C9300-24") )
    !some more commands
 #else
    !even more commands
 #end
 
 ```

#### Variables
Variables may be defined in a couple of ways

```
${Switch}
$Switch

```

Data may be set to the variables using entry or via a set command

```
#set( $Switch = 20 )

```

