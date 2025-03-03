# Deploying Settings and Credentials

In this module, we will use **Python** to build and deploy settings and credentials within Cisco Catalyst Center. 

Cisco Catalyst Center uses hierarchy to logically align intent (code and configuration) against infrastructure. This allows the network administrator to align changes and modifications to the network within maintenance windows.

## Settings and Credentials Background

The Design area is where you create the structure and framework of your network, including the logical topology, network settings, and device type profiles that you can apply to devices throughout your network.

The settings and credentials which we assign to the hierarchy allow us to be deterministic in where we inherit settings from parent objects and where we override settings in the child objects.

This allows us to deploy changes to the network with localized maintenance windows and or slowly roll out changes through multiple sites without impacting the entire network. 

As with all the Design, Policy & Provisioning elements, they are all tied to the hierarchical nature of Cisco Catalyst Center. 

> **Prerequisites**: **Completed** the previous section [**Hierarchy**](../python-1-hierarchy/01-intro.md)

> [**Next Section**](./02-examine.md)
