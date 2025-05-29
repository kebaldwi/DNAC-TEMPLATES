# Lab Setup

Within the cloned directory are three files that we need to modify specific to our pod. 

The first are both YAML files, and are used to store data to be used in the pipelines and python to set connectivity to the pod and fill pod specific variable information. 

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

## External Data Sources

The second file type we need to modify is the **CSV** data file. We will utilize a set of Python programs to build out the **Hierarchy**, **Settings**, and **deployment** of the network via **Catalyst Center**.

Accompanying the **Python Programs** is a **required** Comma Separated Value (CSV) file, which is essentially an **answer file** for the values used to build the design. The CSV which was pulled in the **Git Clone** may be found here for reference: 

> **Download:** <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/CODE/DATA/CSV/DNAC-Design-Settings.csv" target="_blank">⬇︎ Catalyst Center Design Settings CSV ⬇︎</a>

> **IMPORTANT NOTE:** We will **open** but **not save** the CSV file to view the hierarchy that will be built during the lab. 
  As you review the CSV file, you will see each row has hierarchal information, settings, credentials, and other information. **Be Careful NOT to modify the file**; if you feel you have modified the file, please download it again.

To view the file on the **script server** do the following:

```SHELL
nano /root/PYTHON-LAB/DNAC-Design-Settings.csv
```

<p align="center"><img src="../assets/csv2.png" width="800" height="174.55"></p>

Should you need to modify for your POD make the changes necessary to the **CSV** and write the file changes by using **^o**.

Exit the file by using **^x**.

To modify the file complete the following tasks:

1. 
2. ...

At this point we are ready to proceed with the lab.

> [**Next Section**](./07-summary.md)