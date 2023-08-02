# Archiving Configurations

In this module, we will use *Postman* to download an archive of the running and startup configurations of a device in the hierarchy within Cisco DNA Center. 

Cisco DNA Center uses hierarchy to logically align intent (code and configuration) against infrastructure. This allows the network administrator to align changes and modifications to the network within maintenance windows.

## Configuration Archive Background

Cisco DNA Center allows for the Archiving of both the `Running` and `Startup` Configurations for devices within the `inventory` of Cisco DNA Center. In the earlier Cisco DNA Center GUI's, there was no capability to export or archive the configurations apart from this REST-API-based approach. Additional capabilities have been added to the most recent version of Cisco DNA Center, but there remain good use cases for this capability.

One such use case is configuration `compliance`. Suppose we wanted to create a python-based `compliance` tool that utilized the Device Inventory and the configuration files. In that case, we could keep track of devices' **code** and **configurations** to ensure that the code was of a specific version and perhaps certain lines of code were included in the configuration. 

> **Prerequisites**: **Completed** the previous section on **Template Deployment**

> [**Next Section**](02-deploy.md)
