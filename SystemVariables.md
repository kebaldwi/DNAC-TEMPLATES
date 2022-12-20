
## DNAC System Variables

### What are System Varibles?

Cisco DNAC has a lot of information about devices.  It collects inventory data from discovered devices and keeps track of what site, network profile and settings are applied to the devices in your network.  You can use this information in your templates by calling system variables.  System variables extend the benefits of adding variables to your templates by augmenting the dynamic capabilities of templates while also reducing the number of manual inputs required from engineering staff at provisioning time.   

For example, there is a system variable called **__interface**.  This variable, part of the Inventory category, is an object containing an entry for each interface on a network device and within the entry for each interface, you can surface interface details, such as admin status, speed and duplex, IP Address, port name and many others.  

Using this variable allows you to create templates that are agnostic to the types and names of interfaces (GigabitEthernet or TenGigabitEthernet), as well as allowing you to iterate through all interfaces on a device and apply configuration to interfaces that match the conditions you set, such as applying configuration only to access interfaces, only interfaces m-n or those with a specific description.

#### What System Variables are available?

The definitive list of available system variables for a particular version of Cisco DNAC is the Template Editor UI itself.  Within the template view, you will see a link the UI called "Template System Variables":  

![json](./images/button.png?raw=true "Import JSON")  

Clicking on this link will show you a full listing of the available system variables organized by source.  The sources are:

* NetworkProfile
* CommonSettings
* CloudConnect
* Inventory

Note that when you access the Template System Variables window, all variables are not immediately visibile, click "Show More" at the bottom to access the full list.

![json](./images/template_system_main.png?raw=true "Import JSON") 

To continue with our example of using the **__interface** system variable, we can expand this variable entry in the Template System Variables window and see all of the data points available for each interface within this object:

![json](./images/template_system_interfaces_1.png?raw=true "Import JSON") 
![json](./images/template_system_interfaces_2.png?raw=true "Import JSON") 
![json](./images/template_system_interfaces_3.png?raw=true "Import JSON")
![json](./images/template_system_interfaces_4.png?raw=true "Import JSON")  


You can also find high-level details on the available system variables for your version of Cisco DNAC in the [Cisco DNAC User Guide](https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/dna-center/2-3-4/user_guide/b_cisco_dna_center_ug_2_3_4/b_cisco_dna_center_ug_2_3_4_chapter_01000.html#id_92757).  This links to version 2.3.4.x, which was current at the time of writing.

#### Using System Variables in Templates

Now that we have explored what system variables are available, we can look at how to incorporate them into our templates.  I will use the Jinja2 format in the below examples, but Velocity will work as well.

#### Calling System Variables with no operator interaction

The first example we can explore is manually calling system variables under the hood in order to perform an action.  See the below very simple example.  We will iterate over all of the interfaces and if they are physical interfaces (eg, excluding the App interface, SVIs, tunnels, etc..) and they are assigned to VLAN 1, we want to change the vlan assignment.

![json](./images/set_vlan.png?raw=true "Import JSON") 

You might be concerned that we didn't check to make sure that the port mode was set to access.  We could do that, but keep in mind that interfacess in the down state, are considered to be dynamic_auto, not access, so you'll have to check for both of those states, otherwise you'll only match interfaces that are up.

Here is that template if you wish to copy it:

```
{%- macro access_interface()  %}
  switchport access vlan {{ access_vlan }}
  switchport voice vlan {{ voice_vlan }}
{%- endmacro -%}

vlan {{ access_vlan }}
  name access
vlan {{ voice_vlan }}
  name voice

{% for interface in __interface %}
  {% if interface.vlanId == 1 and interface.interfaceType == 'Physical'  %}
    interface {{ interface.portName }}
      {{ access_interface() }}
  {% endif %}
{% endfor %}

```
#### Calling System Variables for Operator Selection

Consider the example that we've been working with so far, but with an alternate slant.  What if we want the operator to select the interfaces to apply our vlan configuration?  We could put a text box in the template and have the operator type or copy/paste an interface range, but if we want to reduce the possibility of manual error, we can use what we call **Source Binding** or **Variable Binding**.

Let's make a single modification to our template.  Here we will remove the reference to **__interface** and replace it with a custom variable name called
**selected_interfaces**.  Our template now looks like this:

![json](./images/set_vlan_2.png?raw=true "Import JSON") 

Here is that template if you wish to copy it:

```
{%- macro access_interface()  %}
  switchport access vlan {{ access_vlan }}
  switchport voice vlan {{ voice_vlan }}
{%- endmacro -%}

vlan {{ access_vlan }}
  name access
vlan {{ voice_vlan }}
  name voice

{% for interface in selected_interfaces %}
  {% if interface.vlanId == 1 and interface.interfaceType == 'Physical'  %}
    interface {{ interface.portName }}
      {{ access_interface() }}
  {% endif %}
{% endfor %}

```

Note:  If you are following along, don't forget to save your template before moving on.  We could remove the if statement if we're confident our operators will only choose unconfigured physical interfaces, but we'll leave it in for this example.

Next we need to specify that this variable is going to be bound.  If we go to the **Input Form** view by clicking on the calculator icon:

![json](./images/calculator_icon.png?raw=true "Import JSON") 

We can select our new variable **selected_interfaces** and apply the settings needed to make this a multi-select field from a list of interfaces on a device.

![json](./images/Input_Form_SystemVariables.png?raw=true "Import JSON") 

These steps will set **selected_interfaces** to be an object that will contain the interfaces of the target switch that are selected by the operator at runtime.  We are giving the operator access to the contents of **__interface[interface]** for each interface and allowing them to select the specific interfaces they want added to the **selected_interfaces** object.  Note that you can also use this UI to filter on an attribute, so if the if statement only had a single option, you could apply it here as a filter.

Note:  If you are following along, don't forget to save your template before moving on.

Now would be a good time to use the **Simulation** feature of the Cisco DNAC Template Editor to check our work.  [Click here to explore the Simulator](./SystemVariables_Simulations.md).


#### One More Example

Lastly let's take a look at using a different system variable.  This very simple 4-line template will check the snmp location field on a device, and if it is empty, it will fill in the field with the location specified by the subdomain in the device FQDN.  For example, if the hostname is switch1.boston.mycompany.com, it will place "boston" in the snmp location field.  This is a very simple example, but it does show how to pull information from a system variable and manipulate it for your own needs.

![json](./images/set_snmp_location.png?raw=true "Import JSON") 

```
{% if __device.snmpLocation == ''  %}
    {% set snmp_location  = __device.hostname | split(".") %}
    snmp-server location {{ snmp_location[1] }}
{% endif %}
```


#### Wrapping Up

Hopefully, this document helped you to get an idea of what system variables are and how they can be used with the Cisco DNAC Template Editor.  System Variables help to reduce manual entry and errors, make your templates more flexible so you need less of them and ease provisioning.  Thanks for reading!


