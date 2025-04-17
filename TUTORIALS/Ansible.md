# Ansible and Cisco Catalyst Center [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

## Ansible and Cisco Catalyst Center

[Ansible](https://docs.ansible.com/ansible/latest/getting_started/introduction.html) is a popular, open-source, platform agnostic configuration management framework that's used across the IT landscape.  Many of the largest networking vendors offer Ansible Modules for their products.  Ansible is commonly used to manage the configuration of servers in the datacenter and has collections to manage cloud resources in AWS, Azure, GCP, and OCI.  This flexibility allows for Ansible to function as an orchestrator across the domains of an organization, allowing for complex service delivery across network, server, storage, firewall, wan and cloud.  Cisco publishes Ansible collections for IOS, IOS-XE, NX-OS, IOS-XR, ACI, ASA, ISE, Meraki, Intersight, NSO, UCS & Cisco Catalyst Center. See the [Cisco Collections Index](https://docs.ansible.com/ansible/latest/collections/cisco/index.html) for all collections in the Cisco namespace. 

## Why use Ansible with Cisco Catalyst Center

If Ansible is so powerful and if Cisco offers Ansible collections for IOS and IOS-XE, why should we use Ansible with Cisco Catalyst Center? Why not just use Ansible directly with our Campus and WAN infrastructure?  Alternately, Cisco Catalst Center has powerful features to manage and deploy configuration, why would you need to add Ansible to the mix?

Catalyst Center's strength is that it is a complete Day-0 through Day-N management and assurance platform.  It does more than just configuration management.  It provides a host of other capabilities including inventory management, software image management, zero-touch provisioning, and Assurance.  Ansible is a strong configuration management tool with multi-vendor capabilities.  

The benefits of combining Ansible and Catalyst Center are:

1. Inventory Management and a Single Touchpoint:  Catalyst Center is a single touchpoint and manages the inventory, so there is no need to maintain complex Ansible inventory files or script dynamic inventories.
2. Source of Truth:  Catalyst Center maintains Configuration archives and Config drift entries to show how the device configuration has changed over time.
3. API Abstraction:  Catalyst Center has a powerful set of APIs.  Ansible Modules allow access to those APIs without the need for programming expertise.
4. Cross-Architecture, Cross-Vendor Orchestration:  Ansible is architecture and vendor agnostic.  It is a powerful tool for configuring heterogeneous networks and performing service orchestration across architectures.  It is also an established component in common DevOps deployments.
5. Catalyst Center Capabilites:  For those who have an existing Ansible practice and are heavy users of Ansible, incorporating Catalyst Center makes the capabilities of Catalyst Center available from Ansible playbooks. 

The Ansible collection for Cisco Catalyst center is called *cisco.dnac*.  Take a moment to review the documetation for the [cisco.dnac](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/index.html#plugins-in-cisco-dnac) collection for details on the modules available in the collection.

### The Basics of Ansible

In Ansible, you use a *Control Node* to manage the configuration of a *Managed Node*.  In an enterprise deployment, the Control Node can be a dedicated server or Ansible Automation Platform deployment.  For testing purposes, the control node could be your laptop or a lightweight Linux container or VM. If your laptop is running Windows, [Windows Subsystem for Linux, WSL](https://learn.microsoft.com/en-us/windows/wsl/install) is a good option for testing Ansible. Managed Nodes are specified in *inventories*.  

Some key components of Ansible are the configuration file, inventory, and playbooks, which we will review in the next section.  

#### The Basics of Ansible: The Ansible Configuration

The Ansible configuration, a file in ini format usually called *ansible.cfg* is where Ansible settings are defined.  The Ansible configuration file allows you to control Ansible's look and feel, the locations where Ansible looks for the inventory, collections and roles, whether you use strict host key checking, default users, and many others.  See the [Ansible Configuration Settings](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings) gude for the full list of settings that can be configured. 

Ansible will look for a configuration file and select one to use based on a documented order of precedence.  View the [configuration order of precedence](https://docs.ansible.com/ansible/latest/reference_appendices/general_precedence.html#configuration-settings) guide for more information.  You can view which Ansible configuration is being used with the ```ansible --version``` command which we will cover further below.  Ansible assumes the default for any settings not defined in the configuration file, so your *ansible.cfg* can be only a few lines.  Here is an example Ansible configuration with only two settings:

```ini
[defaults]
inventory = inventory.ini
host_key_checking = False
```
In the above configuration file, the only settings that are not default are ```inventory = inventory.ini``` (the default inventory file name), and ```host_key_checking = False``` which disables SSH Strict Host Key Checking.  Disabling Strict Host Key Checking is only appropriate in a lab setting. 

#### The Basics of Ansible: The Ansible Inventory

The next key component of Ansible is the inventory file where the list of managed nodes is maintaintained.  Ansible inventories are a broad topic.  There are numerous capabilities including groups, host and group variables and dynamic inventories via scripting or third-party integration.  This guide will cover only the basics of inventories.  

In the simplest terms, an inventory includes the list of managed nodes and associated information for the Ansible control node to communicate with the managed nodes.  The managed nodes can be localhost (the machine from which you are running the playbook), servers, routers, switches, firewalls, cloud resources, sensors, and more.  Managed nodes are identified via IP address or DNS name and are organized into groups.  Host or Group-specific variables can also be defined in inventories, but once the scale and complexity of your Ansible use cases begins to expand, it makes more sense to use group or host variable files to separate the variables out of the inventory file.  Here is an example inventory file:

```ini
[access]
10.1.1.15
switch2.cisco.com

[core]
10.1.1.14
192.168.4.4

[wan]
10.1.1.13

[switches:children]
access
core

[all:vars]
ansible_network_os=cisco.ios.ios
ansible_become=yes
ansible_user=netadmin
ansible_become_method=enable
ansible_ssh_pass=Ap@sswor4
ansible_become_password=Ap@sswor4
```
This simple example inventory file is in ini format, but inventories can also be in YAML format.  In the ini format, groups are defined with the bracket notation *\[group name\]*.  In the inventory above we have four groups:  access, core, wan, and switches.  Groups can be nested.  We can see that the group *switches* is comprised of the groups *access* and *core*.  The \[group name**:children**\] notation specifies that the members of the group are other groups.  There is another hidden group called *all* that is created by default and includes all nodes in the inventory file.  Lastly, variables are defined in this inventory file.  

The notation \[group name**:vars**\] specifies that these variables are applicable to all nodes in the group.  The variables defined in \[all:vars\] in our inventory apply to nodes in the group *all*.  We could have created varaibles that apply to any of the other groups or to a specific node, if needed.  For example, if one of our nodes or groups of nodes had a different username, SSH port, or OS type we could specify that here.  

This inventory contains only five devices, but is 21 lines long.  It is easy to see how complex and hard to manage an inventory file could be at scale--especially if you are defining variables within the inventory file.

> **Note:** Before we move on, it is important to note that this inventory file is a __security nightmare__.  It contains plaintext credentials.  It could be read by anyone, or heaven forbid, accidentally committed to a public repository in Github. Putting plaintext credentials into an inventory is bad practice no matter how well protected your control node is.  It is only done here for learning purposes.  There are many straightforward and secure methods for protecting secrets in Ansible, such as using environment variables, [Ansible vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html), or third party secrets management solutions. If you are exploring Ansible for use in your enterprise, never let an inventory like this go further than the lab.  We will explore secrets management in a later tutorial.

#### The Basics of Ansible: Ansible Playbooks

Ansible instructions are defined in *playbooks*.  A playbook will be a list of one or more plays.  A play is a group of tasks and a hosts statement that defines the managed node or nodes that the tasks will run against.  

Here is a very simple playbook that will return the hostname and serial number of all network devices specified in the inventory file.  

```yaml
---
# Use IOS Facts Module to verify connectivity and get some info on our devices

- hosts: all
  connection: ansible.netcommon.network_cli
  gather_facts: yes
    
  tasks:
    - name: Display Device Serial Number
      debug:
        msg:
          - "Hostname: {{ ansible_net_hostname }} , Serial Number: {{ ansible_net_serialnum }}"

```

Let's take a moment to explore all of the components of this Ansible playbook.  The first section specifies the managed nodes targeted by this play with ``` hosts: all ```.  Remember from the previous section that the group *all* includes every managed node defined in the inventoory.   The line: ``` connection: ansible.netcommon.network_cli``` specifies the connection plugin, or method that Ansible will use to interact with the devices.  ansible.netcommon.network_cli is the full name, but is often shortened to simply ```network_cli```.  There are many other [connection plugins](https://docs.ansible.com/ansible/latest/collections/index_connection.html). One example is ```ansible.netcommon.netconf``` for NETCONF access to network devices.

The line ```gather_facts: yes``` specifies that upon connection to the device, Ansible should pull information from the device.  To see what information is gathered from a Cisco IOS-XE device, see the documentation on the [cisco.ios.ios_facts](https://docs.ansible.com/ansible/latest/collections/cisco/ios/ios_facts_module.html) module.

The *tasks* section is the list of instructions.  Each instruction in the list begins with the *name* statement.  The name can be whatever you choose, but at runtime, the name will be displayed for each task as it is executed, so it is best to make it descriptive. 

Tasks trigger one or more modules that are executed. The module specified in our task is *debug*.  The *debug* module simply prints the output specified by the *msg* parameter.  Our task is using the debug module to output information collected by gather_facts.  The line ```- "Hostname: {{ ansible_net_hostname }} , Serial Number: {{ ansible_net_serialnum }}"``` is the format and content of our message.   Variables in Ansible playbooks are denoted by the double curly brace: \{\{\}\}.  

> **Note:** It is possible to limit the facts gathered from a Cisco IOS-XE device.  See the documentation on the [gather_network_resources](https://docs.ansible.com/ansible/latest/collections/cisco/ios/ios_facts_module.html#parameter-gather_network_resources) and [gather_subset](https://docs.ansible.com/ansible/latest/collections/cisco/ios/ios_facts_module.html#parameter-gather_subset) parameters. 

See the output of this playbook:

![json](../ASSETS/display_serial_num.png?raw=true "IOS Facts Output")

This playbook is very basic and was just used for a primer on the components of a playbook.  We will now pivot to installing Ansible and using it with Cisco Catalyst Center.

### Installing Ansible

If you have a Linux-based system (including MacOS) and have Python installed, the simplest way to install Ansible is by using pip. Ansible offers a full Ansible package including many collections called ```ansible``` and a minimal package which leaves out most of the collections called ```ansible-core```.  For cleanliness, I suggest using a [virtual environment](https://docs.python.org/3/library/venv.html).

```
pip3 install ansible 
```

or

```
pip3 install ansible-core
```

To verify the version of Ansible you have installed and see other information run:

```
ansible --version
``` 

<img src="../ASSETS/ansible_version.png" 
     width="850" 
     height="200"
     alt="Ansible Version Command Output" />

The output of this command shows the version of ansible currently running along with other useful information, such as the specific Ansible config file being referenced, the default inventory file, and the module paths.  

### Ansible & Catalyst Center Dependencies

Using Ansbile to manage Cisco Catalyst Center requires the correct version of the [cisco.dnac] collection for your Catalyst Center version.  The cisco.dnac collection is included in the full Ansible package by default.  However, the collection depends on the [Cisco Catalyst Center SDK](https://dnacentersdk.readthedocs.io/en/latest/index.html).  The SDK must be installed on the control node.  If you have installed the full Ansible package, the cisco.dnac collection is included, but it may not be the correct version for your Catalyst Center deployment.  See the compatibility matrix [table](https://galaxy.ansible.com/ui/repo/published/cisco/dnac/docs/) on Ansible Galaxy for compatibility information:

![json](../ASSETS/compatibility_matrix.png?raw=true "Compatibility Matrix")

> **Note:** This image of the table was current at the time of writing.  The source at the link provided above should be referenced in the future. 

You install the [Cisco Catalyst Center Python SDK](https://dnacentersdk.readthedocs.io/en/latest/) using pip or by downloading the source code and running a setup script in a virtual environment \(recommended\) or in the global Python installation on a host. If you are unfamiliar with pip or Python or you would like a deeper look at using the SDK outside of Ansible to write code directly, review the [Python tutorial](./Python.md).

To install the Cisco Catalyst Center Python SDK using pip, run the following:

```
pip3 install dnacentersdk==#.#.#
```

In my case, the command was:

```
pip3 install dnacentersdk==2.5.5
```

Next, install the cisco.dnac Ansible collection.  To verify that the cisco.dnac collection is installed and to validate the version, run the command ```ansible-galaxy collection list```.  This will show you a list of all collections installed on your control node.  There will be multiple lists separated by install location.  Possible locations include the global ansible_collections directory and within the .ansible directory of the current user.  You can also use grep to narrow down the output:  ```ansible-galaxy collection list | grep cisco.dnac```

> **Note:** If the command ```ansible-galaxy collection list``` is not found on your system, your version of Ansible is too old.  

<img src="../ASSETS/ansible-galaxy.png" 
     width="600" 
     height="60"
     alt="Ansible Galaxy Collection List Command Output" />

You can see in the above output that there are two listings for the cisco.dnac collection.  The first is the version that was installed with the ansible package.  The second, in the user .ansible directory, was installed later.  To install the specific version that matches the compatibility matrix, use following command:  

```
ansible-galaxy collection install cisco.dnac:#.#.#
```

In my case the command was:

```
ansible-galaxy collection install cisco.dnac:6.6.4
```

This will install the collection and any dependencies.  Once you have the collection and SDK installed, you are ready to create playbooks that interact with Cisco Catalyst Center.   

### Your first Catalyst Center Playbook

The cisco.dnac collection contains many modules that allow us to manage Catalyst Center.  In this section we will start with a simple playbook that will get device information for every access switch in the Catalyst Center Inventory using the *cisco.dnac.network_device_info* module and write that information out to a file.  This exercise will help you understand the general syntax and requirements of working with the cisco.dnac Ansible Collection.  

An important skill when developing an Ansible practice is to get comfortable with the Ansible documentation.  Review the documentation for the [*cisco.dnac.network_device_info*](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/network_device_info_module.html#ansible-collections-cisco-dnac-network-device-info-module) module.

Here is our playbook:

```yaml
- hosts: localhost
  gather_facts: no
  vars_files: vars/dnac_vars.yaml
  vars:
    dnac_conn: &dnac_conn
        dnac_host: "{{dnac_host}}"
        dnac_username: "{{dnac_username}}"
        dnac_password: "{{dnac_password}}"
        dnac_verify: "{{dnac_verify}}"
        dnac_port: "{{dnac_port}}"
        dnac_debug: "{{dnac_debug}}"    

  tasks:
    - name: Get Devices
      cisco.dnac.network_device_info:
        <<: *dnac_conn
        role: "ACCESS"
      register: devices

    - name: Write Selected Info to File
      when: devices | length > 0
      ansible.builtin.template:
        src: "template.j2"
        dest: "devices.txt"
```

First, the host that we will run this playbook on is our control node, as it is where we have the SDK installed.  So, our hosts entry contains *localhost*.  But then how will we work with Catalst Center?  The answer is in the set of variables that we use with the modules in the cisco.dnac collection.  There is a set of variables all starting with *dnac* that describe our connection to Catalyst Center. Using these variables we specify the IP, credentials, and ports that we use to connect to Catalyst Center. This information must be available for each module \( Remember the documentation that you reviewed for the network_device_info module\).  

To avoid many redundant lines in our playbooks, we make use of YAML [*anchors and aliases*](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_advanced_syntax.html).  The line ```dnac_conn: &dnac_conn``` specifies an anchor *dnac_conn*. We can then *alias* this block later in our playbook with an alias as represented by this text: ```<<: *dnac_conn```.  This line simply means copy the anchor into this spot in the playbook.  You'll notice that each of these variables references another variable of the same name as noted by the \{\{\}\} notation.  The values for these variables are defined in the variable file *dnac_vars.yaml* referenced in the *vars_files* parameter right above.  This keeps our credentials out of the playbook itself, while still allowing us to reference them.  A variable file is a YAML file containing variable names and values separated with a colon. Variable files are a good way to separate and organize variables for playbooks.

Our first task uses the aforementioned *network_device_info* module to pull information on all network devices from Catalyst Center with a role of ACCESS and saves that information to a variable called *devices*. Any parameter returned by the network_device_info module can be used to filter the output and we can limit the number of returned devices using the limit parameter.  Review the documentation to explore the possibilities. 

The next module simply writes out the return data to a file called "devices.txt" in a format we specify in the Jinja2 Template file "template.j2".  We will explore this briefly, but there are comprehensive writeups on Jinja2 Templating on this repository already.  See this guide to [Jinja2](./Jinja2.md) and this guide to [Advanced Jinja2](./AdvancedJinja2.md) as Catalyst Center uses Jinja2 for nework device configuration templates.  See the contents of our template file:

```j2
{# Pull Data from Catalyst Center Inventory#}

{% for device in devices.dnac_response.response %}
{{ device.hostname }} | {{ device.managementIpAddress }} | {{ device.upTime }}
{% endfor %}
```
The \{\#\#\} notation specifies a comment explaining what we're doing in this file.  Below that is a for loop that iterates through the output from the network_device_info module and prints the hostname, IP address and uptime for each device returned.  We have used a pipe as the delimeter because the uptime value usually contains commas, but it is possible to massage that input to modify the commas so that you can write a csv file for ingestion into other systems.

To run this playbook, simply use the ansible-playbook command as above.

```
ansible-playbook ourfirstccplaybook.yaml
```
The resulting devices.txt file looks like this:
```
access | 10.1.1.15 | 1 day, 3:07:04.00
core | 10.1.1.14 | 1 day, 3:08:09.00
wan-1 | 10.1.1.13 | 1 day, 3:38:18.40
```

### Bringing Devices into Catalyst Center

The previous example playbook was simply to illustrate the general overview of interacting with Catalyst Center via Ansible.  Now we will explore playbooks that help us create sites and bring devices into Catalyst Center.

Here's our execution flow:

1. Use the [cisco.dnac.site_intent](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/site_intent_module.html#ansible-collections-cisco-dnac-site-intent-module) module to create an Area, Building and Floor in Catalyst Center. 
2. Use the [cisco.dnac.site_info](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/site_info_module.html#ansible-collections-cisco-dnac-site-info-module) module to collect the site ID of the newly created floor.  
3. Use the [cisco.dnac.network_device](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/network_device_module.html#ansible-collections-cisco-dnac-network-device-module) module to discover network devices and bring them into the Catalyst Center inventory.  
4. Use the [cisco.dnac.assign_device_to_site](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/assign_device_to_site_module.html#ansible-collections-cisco-dnac-assign-device-to-site-module) to assign the device to the correct site.

In addition to these we'll use the *wait_for* Ansible module to pause for a couple of seconds to ensure that Catalyst Center completes our previous task before starting on the next.  This may not be required with your deployment, but for a very busy Catalyst Center, it can be useful.

Let's view the playbook:

```yaml
- hosts: localhost
  gather_facts: no
  vars_files: vars/dnac_vars_1.yaml
  vars:
    dnac_conn: &dnac_conn
        dnac_host: "{{dnac_host}}"
        dnac_username: "{{dnac_username}}"
        dnac_password: "{{dnac_password}}"
        dnac_verify: "{{dnac_verify}}"
        dnac_port: "{{dnac_port}}"
        dnac_debug: "{{dnac_debug}}"  

  tasks:
    - name: Create site - area, building and floor
      cisco.dnac.site_intent:
        <<: *dnac_conn
        state: "merged"
        config:
        - type: "{{ item.type }}"
          site: "{{ item.site }}"
      with_items: '{{ site_details }}'

    - name: Wait 2 Seconds
      wait_for:
        timeout: 2

    - name: Get Site ID for The Floor
      cisco.dnac.site_info:
        <<: *dnac_conn
        name: "{{ site_name }}"
      register: site_result 

    - name: Add Devices to DNAC Inventory
      cisco.dnac.network_device:
        <<: *dnac_conn
        state: present
        cliTransport: "{{ item.cli_transport }}"
        ipAddress:
        - "{{ item.ip }}"
        userName: "{{ item.username }}"
        password: "{{ item.password }}"
        snmpRWCommunity: "{{ item.snmp_rw }}"
        snmpVersion: "{{ item.snmp_version }}"
        netconfPort: "{{ item.netconf_port }}"
      with_items: '{{ device_details }}'

    - name: Wait 2 Seconds
      wait_for:
        timeout: 2

    - name: Assign Devices to Floor
      cisco.dnac.assign_device_to_site:
        <<: *dnac_conn
        device:
        - ip: "{{ item.ip }}"
        siteId: "{{ site_result.dnac_response.response[0].id }}"
      with_items: '{{ device_details }}'  
```
The playbook itself is very straightforward.  The only unfamiliar syntax from previous playbooks are the *with_items* and *state* keyword.  State is used to control the outcome of the task.  *Merged* means add what we have configured to what is present.  *Present* means create the resource if it doesn't already exist and do nothing if it does.  *With_items* is used to allow the task to iterate over a list.  We use it with the site_intent & network_device modules as we have multiple sites and network devices.  All of the specific information needed, including the site names, building addresses, and network device IPs & credentials are in the vars file. The details of what parameters are needed for each module are found in the documentation. Here is a sample vars file for this playbook:

```yaml
dnac_host: 192.168.12.109
dnac_port: 443
dnac_username: admin
dnac_password: Ap@sswor4
dnac_verify: False
dnac_debug: True 
site_details:
  - type: "area"
    site:
      area:
        name: "Pod 1"
        parentName: "Global"
  - type: "building"
    site:
      building:
        name: "Pod 1 Building"
        parentName: "Global/Pod 1"
        address: "110 West Tasman Drive, San Jose, California 95134, United States"
  - type: "floor"
    site:
      floor:
        name: "Pod 1 Floor"
        parentName: "Global/Pod 1/Pod 1 Building"
        rfModel: "Cubes And Walled Offices"
        width: "100.0"
        length: "100.0"
        height: "10.0" 
site_name: "Global/Pod 1/Pod 1 Building/Pod 1 Floor"
device_details:
  - ip: "10.1.1.15"
    cli_transport: "ssh"
    snmp_rw: "private"
    snmp_version: "v2"
    username: "netadmin"
    password: "Ap@sswor4"
    netconf_port: "830"
  - ip: "10.1.1.14"
    cli_transport: "ssh"
    snmp_rw: "private"
    snmp_version: "v2"
    username: "netadmin"
    password: "Ap@sswor4"
    netconf_port: "830"
  - ip: "10.1.1.13"
    cli_transport: "ssh"
    snmp_rw: "private"
    snmp_version: "v2"
    username: "netadmin"
    password: "Ap@sswor4"
    netconf_port: "830"

```
You'll notice that the vars file is in YAML format.  The YAML format is human-readible, plaintext, and white space sensitive.  It uses a *key: "value"* structure and lists are defined with sets of dashes \(\-\).    

### Summary

This was a brief overview of getting started with Ansible & Catalyst Center.  There are many great use cases for using the two together, and please explore the documentation for what's possible.  Watch this space for more on this topic.

> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Return to Main Menu**](../README.md)