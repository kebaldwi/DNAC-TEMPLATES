# Adding Devices with REST API using Ansible

To use Cisco DNA Center for monitoring with Assurance, devices must be first added to the Cisco DNA Center inventory and assigned to a site. The playbook **device-add.yaml** will:

1. Create a Site Hierarchy containing an area, building, and floor.
2. Add the wireless lan controller in your Pod to the Cisco DNA Center Inventory.
3. Assign the controller to the floor created in the first step.

This will allow Cisco DNA Center to begin collecting telemetry from the device and after a few minutes, you will be able to take advantage of the Cisco DNA Assurance capabilities to monitor your infrastructure.

Let's step through **device-add.yaml.**

The beginning of the playbook contains the familiar hosts and variables section of the playbook that you reviewed in the preceding section. Let's review the tasks in the playbook. 

The first three tasks create an area, building and floor within the Cisco DNA Center site hierarchy using the [cisco.dnac.site_intent](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/site_intent_module.html#ansible-collections-cisco-dnac-site-intent-module) module and variables from the variable file, pause for 5 seconds and then retrieve and save the new floor's details using the [cisco.dnac.site_info](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/site_info_module.html) module. 

The pauses are in place to slow the rate of API calls to the shared Cisco DNA Center and ensure that the previous tasks are completed:

```YAML
    - name: Create sites - area, building and floor
      cisco.dnac.site_intent:
        <<: *dnac_conn
        state: "merged"
        config:
        - type: "{{ item.type }}"
          site: "{{ item.site }}"
      with_items: '{{ site_details }}'

    - name: Wait 5 Seconds
      wait_for:
        timeout: 5 

    - name: Get Site ID for The Floor
      cisco.dnac.site_info:
        <<: *dnac_conn
        name: "{{ site_name }}"
      register: site_result 
```

The next task in the playbook adds devices to the inventory one by one using the [cisco.dnac.network_device](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/network_device_module.html) module and then pauses for 2 more seconds. 

```YAML
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

    - name: Wait 5 Seconds
      wait_for:
        timeout: 5      

```
Alternatively, the [cisco.dnac.discovery](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/discovery_module.html) allows you to pull in many devices by IP Range, CDP, or LLDP and is a better option than going device by device for large install bases. Discovery via IP Range is the most common method of adding devices to the Cisco DNA Center inventory.

The final playbook task assigns the devices to the floor using the [cisco.dnac.assign_device_to_site](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/assign_device_to_site_module.html) module using the site ID gleaned from the site_result we registered earlier in the playbook:

```YAML
    - name: Assign Devices to Floor
      cisco.dnac.assign_device_to_site:
        <<: *dnac_conn
        device:
        - ip: "{{ item.ip }}"
        siteId: "{{ site_result.dnac_response.response[0].id }}"
      with_items: '{{ device_details }}'
```

Run the playbook **device_add.yaml.** 

```SHELL
cd ~
ansible-playbook dnac/device_add.yaml
```

The playbook takes a while to run and produces significant output. It should complete with no errors. In the next section, we will validate that our devices have been successfully added to Cisco DNA Center.

> [**Next Section**](07-verify.md)
