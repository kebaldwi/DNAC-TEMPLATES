# Lab Setup

Within the cloned directory are two files that we need to modify specific to our pod. They are both YAML files, and are used to store data to be used in the pipelines and python to set connectivity to the pod and fill pod specific variable information. 

YAML files are very specific about indentation. try not to disturb that when making alterations.

## Project Details YAML

This file has the following information stored in it. 

```YAML
dna_center:
  ip_address: 198.18.129.100
  username: admin
  password: C1sco12345

github:
  username: kebaldwi
  token: replace_me
  repository: kebaldwi/devnet_test
  repository_paths:
    inventory: kebaldwi/devnet_test/inventory
    reports: kebaldwi/devnet_test/reports
    templates: kebaldwi/devnet_test/templates

project:
  name: PYTHON-LAB
  pod: POD-10
```

We will use NANO to make the required changes. Open the following file using NANO with the command shown:

```SHELL
sudo nano /root/PYTHON-LAB/project_details.yml
```

Scroll down to the line `pod: POD-10` and change the number to whatever number you are using in the session.

Save the file by using **^o** then exit with **^x**.

## Site Operations YAML

This file has the following information stored in it. 

```YAML
project:
  name: PYTHON-LAB
  pod: POD-10

template_info:
  border:
    templates: templates/8000v.txt
  edge:
    templates: templates/9000v_1.txt,templates/9000v_2.txt

area_info:
  name: DevNet
  hierarchy: Global

building_info:
  name: DevNet-Building

floor_info:
  name: Floor-1-DevNet

devices_info_wired:
  managementIP: [198.18.133.145,198.19.1.2,198.19.2.2]
  device_roles: [border, edge, edge]

devices_info_wireless:
  hostname: [198.18.134.100]
  device_roles: [controller]

border_devices:
  ip: [198.18.133.145]
  templates: 8000v.txt
  routing_protocol: OSPF
  internal_interfaces: GigabitEthernet0/1,GigabitEthernet0/2

edge_devices:
  ip: [198.19.1.2,198.19.2.2]
  templates: 9000v_1.txt,9000v_2.txt
```

We will use NANO to make the required changes. Open the following file using NANO with the command shown:

```SHELL
sudo nano /root/PYTHON-LAB/site_operations.yml
```

Scroll down to the line `pod: POD-10` and change the number to whatever number you are assigned in the session.

Save the file by using **^o** then exit with **^x**.

At this point we are ready to proceed with the lab.

> [**Next Section**](./06-summary.md)