# Running Show Commands

In this module, we will use *Postman* to run some `show` commands on network devices within the infrastructure that Cisco Catalyst Center manages. This allows a method of getting troubleshooting information in the event we need to populate 3rd party management systems. We can use this set of commands to pull parts of the configuration or even make queries via CDP or LLDP to determin neighbor information.

This type of request allows us flexibility in pragmatically determining specific information whcih we may use in programming logic to determine next steps in an automation flow.

## Command Runner Background

The Command Runner tool allows you to run cli commands from the Inventory window on platforms. 

The platform commands that you can run are those such as `ping`, `traceroute`, and `snmpget` to troubleshoot device reachability issues. Additionally, `show` commands may also help or aid in troubleshooting.

> **Prerequisites**: **Completed** the previous section **Retrieving Device Inventory**

> [**Next Section**](./02-deploy.md)

> [**Return to LAB Menu**](../README.md)