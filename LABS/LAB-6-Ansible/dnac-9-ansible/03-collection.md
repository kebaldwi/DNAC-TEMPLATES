# Ansible Collection Dependencies

Catalyst Center can augment a companies Ansible automation and orchestration strategy. 

The [**cisco.dnac**](https://docs.ansible.com/ansible/latest/collections/cisco/dnac/index.html) Ansible collection can be utilized by development engineers to build robust playbooks for Ansible that interact with Catalyst Center. 

> **Documentation**: For Installation Instructions and Caveats visit: [**Ansible Galaxy**](https://galaxy.ansible.com/cisco/dnac). 

The Catalyst Center Ansible collection depends on the [**Catalyst Center Python SDK**](https://dnacentersdk.readthedocs.io/en/latest/) and the version of the SDK must align with the version of Catalyst Center that is in use. 

![json](./images/dnacentersdk_compatibility.png?raw=true "Import JSON")

The latest compatibility information is available in the [**SDK Github Repository**](https://github.com/cisco-en-programmability/dnacentersdk) or [**Ansible Galaxy**](https://galaxy.ansible.com/cisco/dnac) Documentation. 

## Ansible

First lets make sure Ansible is at the required version:

```
ansible --version
```

![json](./images/ansible-version.png?raw=true "Import JSON")

This should show Ansible at version `2.13.10` if not use the following command to update it now:

```SHELL
sudo pip install 'ansible==6.6.0'
```

You should see something like this:

![json](./images/install-ansible.png?raw=true "Import JSON")

> [**Next Section**](04-ansible-prep.md)
