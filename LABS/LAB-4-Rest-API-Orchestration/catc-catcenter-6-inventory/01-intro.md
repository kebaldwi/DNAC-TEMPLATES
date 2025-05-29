# Retrieve Device Inventory

In this module, we will use *Postman* to retrieve the device inventory of the hierarchy within Catalyst Center. 

Catalyst Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network.

##  Catalyst Center Inventory Background

DNA Center keeps a detailed inventory of the devices discovered or onboarded from the network. The inventory is used to reference devices in the Catalyst Center UI but also offers a place to see detailed information about the Product ID, Hostname, Software Image, and much more.

The inventory could be used in reports to determine compliance or to reference the devices within the system for either deploying templates or issuing show commands with the command runner used earlier.

For example we may pull the device inventory to determine what we may need to upgrade for code, or to pull the Unique Identifier for a device that we may want to push a specific configuration to via template. There are many needs for this type of request.

> **Prerequisites**: **Completed** the previous section **Configuration Archiving**

> [**Next Section**](./02-deploy.md)

> [**Return to LAB Menu**](../README.md)