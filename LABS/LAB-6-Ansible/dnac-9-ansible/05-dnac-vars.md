# Setting Ansible Variables

Within this section we are making use of locally executed scripts and variables. The host specified in our Catalyst Center playbook will be localhost. Additionally, we must specify our Cisco DNAC connection details in each task. Let's explore the variables in our first Cisco DNAC Ansible playbook.

Review the Ansible Playbook **get-sys-info.yaml** in the **dnac** directory. The purpose of this simple playbook is to verify that we can successfully connect to our Cisco DNAC instance with Ansible. 

The playbook uses the [cisco.dnac.system_health_info](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/system_health_info_module.html#ansible-collections-cisco-dnac-system-health-info-module) module to return some basic information about our Cisco DNAC cluster and the most recent system health event reported.

The playbook reads variables from a variable file, **dnac_vars.yaml**, and also introduces the concept of [**anchors and aliases**](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_advanced_syntax.html#yaml-anchors-and-aliases-sharing-variable-values).

Review the variables in the **dnac_vars.yaml** file below. It is in the dnac/vars directory within the Ansible Lab directory. Beyond the Catalyst Center connection variables, you will see several variables used in the next playbook.

```YAML
dnac_host: 198.18.129.100
dnac_port: 443
dnac_username: admin
dnac_password: C1sco12345
dnac_verify: False
dnac_debug: True 
site_details:
  - type: "area"
    site:
      area:
        name: "State"
        parentName: "Global"
  - type: "area"
    site:
      area:
        name: "California"
        parentName: "Global/State"
  - type: "building"
    site:
      building:
        name: "Building 4"
        parentName: "Global/State/California"
        address: "275 E Tasman Dr, San Jose, CA 95134"
  - type: "floor"
    site:
      floor:
        name: "Floor 1"
        parentName: "Global/State/California/Building 4"
        rfModel: "Cubes And Walled Offices"
        width: "100.0"
        length: "100.0"
        height: "10.0" 
site_name: "Global/State/California/Building 4/Floor 1"
device_details:
  - ip: "198.18.134.100"
    cli_transport: "ssh"
    snmp_rw: "private"
    snmp_version: "v2"
    username: "admin"
    password: "C1sco12345"
    netconf_port: "830"
```

**Anchors** and **aliases** allow you to define a set of variables with the **'&'** symbol and reference this set with the **'*'** notation later. Aliases are useful when the set of anchored variables must be referenced multiple times. 

The modules in the **cisco.dnac** Ansible collection require the Catalyst Center connection variables to be defined for each task, so anchoring can be useful in reducing the number of lines in your playbooks.

```YAML
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
    - name: Get System Info
      cisco.dnac.system_health_info:
        <<: *dnac_conn
        summary: true
      register: result

    - name: Show Health
      debug:
        msg:
          - "{{ result }}"
```

We will not run this particular playbook as the Catalyst Center is running `2.2.3.4` which is quite out of date. If we were to run the playbook **get-sys-info.yaml.** using Catalyst Center `2.3.3.7` we would do it like this:

```SHELL
cd ~
ansible-playbook dnac/get-sys-info.yaml
```

It would run without errors and return data on the Catalyst Center system. See the following for an example. 

![json](./images/get_sys_info.png?raw=true "Import JSON")

> [**Next Section**](06-add-devices.md)
