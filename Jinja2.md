# Jinja2 Scripting [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
This section will describe the various tools and techniques used to make a powerful script out of normal CLI statement collections which are used by organizations on IOS devices around the world. This section is an attempt to demystify the hows and to bring clarity on what is truely possible. While it is possible to take a CLI script for one device and create a template for one device at a time, that would leave us with a lot of templates and make it harder to make changes on an ongoing basis. Using the techniques below will allow us to deploy equipment with scripts which can be reused, allowing us to keep configurations similar for conformity reasons but also to reduce the number of places where changes would have to be made. 

To that end it is important to write modular scripts which make use of all the power of programming but allow us to do it within the DNAC platform as templates. 

The Jinja2 language typically allows for logical constructs, macros and more. Its heredity is from the Python language and so a lot of its form, nomenclature and features will be very familiar to programmers familiar with Python.

## Comment Statements
Comment statements are a useful tool for scripting and allow for descriptive text to be used to explain the design or functionality of code. In simple IOS configurations anything after a '!' is not implemented but this is not true in Jinja2. To that end anything with a '!' is rendered as actual code so if something is desired not to be processed within this templating language please use `{#...#}` encapsulation. This makes sure the included text is not evaluated nor rendered.

```j2
{# Comments can be placed here #}
```

## Variable Usage
Variables when combined in Jinja2 for the most part you can use them by calling them with Formal notation.

```j2
Formal Notation:        {{ Switch }} 
```

There are occassions where those variables will need to be used in descriptions or other areas where we would typically have a string. In logical constructs like conditional statements where we encapsulate the variable within `{%...%}` we will not need to enclose the Variable within the double braces `{{...}}`. 

Take this example of a macro with an interface description, pay attention to the macro command:

```j2
{% macro (uplink_interface(site_code, closet) %}
 description {{ site_code }} - {{ closet }}
{% endmacro %}
```

### Combining Bind Variables
You can also extrapolate variables from known values once the device has been onboarded into the inventory. If the device was populated with the pnp startup-vlan command value then then the native vlan would be set to follow that automatically on the target switch. You could bind a variable and then use that to determine many other values for the device automatically.

```j2
{% set voice_offset = 4000 %}
{% set data_offset = 100 %}
{% set integer = 0 %}
{% set native_vlan_var = native_bind %}
{% set native_vlan = native_vlan_var | int %}
{% set data_vlan = native_vlan + data_offset  %}
{% set voice_vlan = data_vlan + voice_offset  %}
```

## Conditional Statements
IF statements are a useful tool for scripting and allow for a decision tree in which under certain circumstances various commands can be used alone or in combination. To create an IF statement examples have been provided below. That said it is important to understand that the IF statement may be used alone or in combination with the following;

```j2
{% if %}
{% endif %}

{% if %}
{% else %}
{% endif %}

{% if %}
{% elif %}
{% else %}
{% endif %}
```

That said it is important to understand that these decisions allow for you to script for multiple circumstances or platforms allowing you to write code which can be reused and therefore modular.

If/elif/else construct with a check to see if data in variable contains a string:

```j2
{% if hostname.contains("edge") %}
    {# some commands #}
{% elif hostname.contains("border") %}
    {# some more commands #}
{% else %}
    {# even more commands #}
{% endif %}
```
 
## Macro's
A Macro is a snippit of code which can be called over and over again within a template. Take the following example into consideration. Alone the Macro does not seem that powerful but when combined with the previous sections conditional statements it suddenly allows for a more powerful script.

Macro format is as follows:

```j2
      [{%] macro macro-name(arg1,...argn) [%}] ...{# Jinja2 code #}... [{%] endmacro [%}]

      Usage:

            macro-name      - Name used to call the Macro (macro-name)
            arg1 ... argn   - Arguments or Variables to the Macro. There can be any number of arguments, but the number 
                              used at invocation must match the number specified in the definition, unless 
                              there is a default value provided for missing parameters.
            Jinja2 code     - Any valid Jinja2 code, anything you can put into a template, can be put into a Macro

```

An example Macro of interface configurations:

```j2
{% macro Interfaces() %}
int lo 0
  desc mgmt address
  ip address 10.0.0.{{ Switch }} 255.255.255.255
!
int vlan 1
  desc mgmt vlan - with pnp
  ip address 10.1.1.{{ Switch }} 255.255.255.0
!
{% endmacro %}
```

When combined with the IF statements below, the above Macro allows for various IP's to be set on the same interface on multiple switches as long as the hostname variable contains a specific string value.

```j2
{% if hostname.contains("C9300-48") %}
   {% set Switch = 30 %}
   {{ Interfaces() }}
{% elif hostname.contains("C9300-24") %}
   {% set Switch = 20 %}
   {{ Interfaces() }}
{% else %}
   {% set Switch = 10 %}
   {{ Interfaces() }}
{% endif %}
```

## For Loops
A For loop allows for multiple iterations of a sequence of commands perhaps including some of the constructs mentioned above to iterate through and on each occasion use a different value.

Command Construct:

```j2
[{%] for ref in arg ) [%}] statements [{%] endfor [%}]

Usage:
    ref                  - The first variable reference is the item.
    arg                  - May be one of the following: a reference to a list 
                           (i.e. object array, collection, or map), an array list, or the range operator.
    statements           - What is output each time Jinja2 finds a valid item in the list denoted above as arg. 
                           This output is any valid J2 and is rendered each iteration of the loop.
```

An example of a For Loop

```j2
    Reference Example: 
    
    {% for Vlanid in Vlans ) 
         interface vlan {{ Vlanid }} 
    {% endfor %}
    
    Array List Example: 
    
    {% set ID = 15 %}
    {% for Vlanid in ["10", ID, "20"] %} 
         interface vlan {{ Vlanid }}
    {% endfor %}
    
    Range Operator Example: 
    
    {% for Vlanid in Range(3) %} 
       interface vlan {{ Vlanid }} 
    {% endfor %}
```

Inside of a for-loop block, you can access some special variables: Try these instead of modifying counters within looping blocks.

| **Variable** | **Description** |
|--------|-------------|
| loop.index | The current iteration of the loop. (1 indexed) |
| loop.index0 | The current iteration of the loop. (0 indexed) |
| loop.revindex | The number of iterations from the end of the loop (1 indexed) |
| loop.revindex0 | The number of iterations from the end of the loop (0 indexed) |
| loop.first | True if first iteration |
| loop.last | True if last iteration |
| loop.length | The number of items in the sequence |
| loop.cycle | A helper function to cycle between a list of sequences. See the explanation below |
| loop.depth | Indicates how deep in a recursive loop the rendering currently is. Starts at level 1 |
| loop.depth0 | Indicates how deep in a recursive loop the rendering currently is. Starts at level 0 |
| loop.previtem | The item from the previous iteration of the loop. Undefined during the first iteration |
| loop.nextitem | The item from the following iteration of the loop. Undefined during the last iteration |
| loop.changed(*val) | True if previously called with a different value (or not called at all) |


## Multi Line Commands
These can be used for building entries for multiple lines which need to be used within a command like with banners.

```j2
!BANNER LOGIN
<MLTCMD>banner login ^
  Session On $hostname Is Monitored!!!
  *****************************LEGAL WARNING************************************
  * This device is part of a Demonstration computer network and is provided for*
  * official use by authorized users ONLY. Any information, documents, or      *
  * materials in the network are the property of this firm. Unauthorized use,  *
  * duplication, or disclosure of information or systems in this network is    *
  * strictly prohibited by Federal Law (18 USC 10130). Use of this network     *
  * constitutes consent to monitoring which may be released to firm management *
  * and/or law enforcement agencies and may result in disciplinary action,     *
  * civil action, and/or criminal prosecution.                                 *
  ****************************LEGAL WARNING*************************************
^</MLTCMD>
```

If you found this repository or any section helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

Special mention to: https://jinja.palletsprojects.com/en/3.0.x/templates as examples and extrapolations were made using this documentation.
