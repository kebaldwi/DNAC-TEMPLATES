
# Cisco Catalyst Center System Variables [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

## What are System Variables?

Cisco Catalyst Center maintains a lot of information about devices.  It collects inventory data from discovered devices and keeps track of what site, network profile and settings are applied to the devices in your network.  You can use this information in your templates by calling system variables.  System variables extend the benefits of adding variables to your templates by augmenting the dynamic capabilities of templates while also reducing the number of manual inputs required from engineering staff at provisioning time.   

For example, there is a system variable called **__interface**.  This variable, part of the Inventory category, is an object containing an entry for each interface on a network device. By referencing this variable, you can access interface details, such as admin status, speed and duplex, IP Address, port name and many others.  

Using this variable allows you to create Templates that are agnostic to the types and names of interfaces (GigabitEthernet or TenGigabitEthernet), as well as allowing you to iterate through all interfaces on a device and apply configuration to interfaces that match the conditions you set, such as applying configuration only to access interfaces, only interfaces m-n or those with a specific description.

### What System Variables are available?

The definitive list of available system variables for a particular version of Cisco Catalyst Center is the Cisco Catalyst Center Template Editor UI itself.  Within the template view, you will see a link the UI called "Template System Variables":  

![json](../ASSETS/button.png?raw=true "Import JSON")  

Clicking on this link will show you a full listing of the available system variables organized by source.  The sources are:

* NetworkProfile
* CommonSettings
* CloudConnect
* Inventory

> **Note:** that when you access the Template System Variables window, all variables are not immediately visibile, click "Show More" at the bottom to access the full list.

![json](../ASSETS/template_system_main.png?raw=true "Import JSON") 

To continue with our example of using the **__interface** system variable, we can expand this variable entry in the Template System Variables window and see all of the data points available for each interface within this object:

![json](../ASSETS/template_system_interfaces_1.png?raw=true "Import JSON") 
![json](../ASSETS/template_system_interfaces_2.png?raw=true "Import JSON") 
![json](../ASSETS/template_system_interfaces_3.png?raw=true "Import JSON")
![json](../ASSETS/template_system_interfaces_4.png?raw=true "Import JSON")  


You can also find high-level details on the available system variables for your version of Cisco Catalyst Center in the **[Cisco Catalyst Center User Guide](https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/dna-center/2-3-4/user_guide/b_cisco_dna_center_ug_2_3_4/b_cisco_dna_center_ug_2_3_4_chapter_01000.html#id_92757)**.  This links to version 2.3.4.x, which was current at the time of writing.

### Using System Variables in Templates

Now that we have explored what system variables are available, we can look at ways to incorporate them into our templates.  I will use the Jinja2 format in the below examples, but Velocity will work as well.

### Calling System Variables with no operator interaction

The first example we can explore is manually calling system variables under the hood in order to perform an action.  See below as a simple example.  We will iterate over all of the interfaces and if they are physical interfaces (eg, excluding the App interface, SVIs, tunnels, etc..) and they are assigned to VLAN 1, we want to change the vlan assignment.

![json](../ASSETS/set_vlan.png?raw=true "Import JSON") 

You might be concerned that we didn't check to make sure that the port mode was set to access.  We could do that, but keep in mind that interfacess in the down state, are considered to be dynamic_auto, not access, so you'll have to check for both of those states, otherwise you'll only match interfaces that are up.

Here is that template if you wish to copy it:

```J2
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
### Calling System Variables for Operator Selection

Consider the example that we've been working with so far, but with an alternate use case.  What if we want the operator to select the interfaces to apply our vlan configuration?  We could put a text box in the template and have the operator type or copy/paste an interface range, but if we want to reduce the possibility of manual error, we can use what we call **Source Binding** or **Variable Binding**.

Let's make a single modification to our template.  Here we will remove the reference to **__interface** and replace it with a custom variable name called
**selected_interfaces**.  Our template now looks like this:

![json](../ASSETS/set_vlan_2.png?raw=true "Import JSON") 

Here is that template if you wish to copy it:

```J2
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

> **Note:** If you are following along, don't forget to save your template before moving on.  We could remove the if statement if we're confident our operators will only choose unconfigured physical interfaces, but we'll leave it in for this example.

Next we need to specify that this variable is going to be bound.  If we go to the **Input Form** view by clicking on the calculator icon:

![json](../ASSETS/calculator_icon.png?raw=true "Import JSON") 

We can select our new variable **selected_interfaces** and apply the settings needed to make this a multi-select field from a list of interfaces on a device.
1. Select Variable
2. Choose Type
3. Check Bind to Source
4. Choose which system variable to bind

![json](../ASSETS/Input_Form_SystemVariables.png?raw=true "Import JSON") 

These steps will set **selected_interfaces** to be an object that will contain the interfaces of the target switch that are selected by the operator at runtime.  We are giving the operator access to the contents of **__interface[interface]** for each interface and allowing them to select the specific interfaces they want added to the **selected_interfaces** object.  

> **Note:** that you can also use this UI to filter on an attribute, so if the if statement only had a single option, you could apply it here as a filter.

> **Note:** If you are following along, don't forget to save your template before moving on.

Now would be a good time to use the **Simulation** feature of the Cisco Catalyst Center Template Editor to check our work.  

### Simulations

If you want to verify that the template is going to operate as expected, you can use the Simulator to run through the logic of your template and generate the output configuration for a target device.  This will not make any changes to your devices and can be a good way to test your templates as you work through them.  

You can access the Simulator by clicking on the "play" icon in the top left.

![json](../ASSETS/play_icon.png?raw=true "Import JSON")

Next, click **Create Simulation**.  When you reach the Simulation Input Page, you'll have to give the simulation a name and then supply values for any variables.  For our bound variables to work, we also need to supply a target device to test against.

![json](../ASSETS/create_simulation.png?raw=true "Import JSON")

When you reach the Simulation Input Page, you'll have to give the simulation a name and then supply values for any variables.  For our bound variables to work, we also need to supply a target device to test against.

1. Choose the Device as a target
2. Enter the name of the simulation
3. Fill in variable value for access_vlan
4. Fill in variable value for voice_vlan

![json](../ASSETS/simulation_input.png?raw=true "Import JSON")

Once you've selected a device, then you'll see our **selected_interfaces** options and can select the ones you want to test with:

![json](../ASSETS/interfaces_options.png?raw=true "Import JSON")

Once you have completed your selections, click the run button at the bottom right of the screen.

If your Simulation was successful, meaning that there were no syntax errors that caused the simulation to fail to render configuration, the resulting configuration will show in the right-hand side of the window:

![json](../ASSETS/simulation_output.png?raw=true "Import JSON")

> **Note:** Due to Jinja2 whitespace handling, the configuration may look messy or misaligned, but these whitespace issues will not affect provisioning.

This output provides highly beneficial detail on what configuration would be pushed to a target device based on our template logic and allows the architect to ensure that the template will render as expected when it is time to provision.

### One More Example

Lastly let's take a look at using a different system variable.  This very simple 4-line template will check the snmp location field on a device, and if it is empty, it will fill in the field with the location specified by the subdomain in the device FQDN.  For example, if the hostname is switch1.boston.mycompany.com, it will place "boston" in the snmp location field.  This is a very simple example, but it does show how to pull information from a system variable and manipulate it for your own needs.

![json](../ASSETS/set_snmp_location.png?raw=true "Import JSON") 

```J2
{% if __device.snmpLocation == ''  %}
    {% set snmp_location  = __device.hostname | split(".") %}
    snmp-server location {{ snmp_location[1] }}
{% endif %}
```

### Summary

Hopefully, this document helped you to get an idea of what system variables are and how they can be used with the Cisco Catalyst Center Template Editor. System Variables help to reduce manual entry and errors, make your templates more flexible so you need less of them and ease provisioning. Thanks for reading!

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Return to Main Menu**](./README.md)