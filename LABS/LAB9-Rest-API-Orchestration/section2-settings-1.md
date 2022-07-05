# Use Case 1.2 - Defining Settings and Credentials
In this lablet we will use *Postman* to deploy settings and credentials to a hierarchy within DNA Center. DNA Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network.

## Settings and Credentials Background
The Design area is where you create the structure and framework of your network, including the logical topology, network settings, and device type profiles that you can apply to devices throughout your network.

The settings and credentials which we assign to the hierarchy allow us to be deterministic in where we inherit settings from parent objects and where we overide settings in the child objects.

This allows for us to deploy not only changes to the network, with localized maintenance windows but also to slowly role out changes through multiple sites without impact to the entire network. 

As with all the Design, Policy & Provisioning elements they are all tied to the hierarchial nature of DNA Center. 

## Student Environment
To ensure you are working on all your changes and not interfering with others, we will modify the settings and Hierarchy to personalize it for your use within the lab. We did this step in the previous lablet, but for confirmation please ensure it is complete.

Follow these steps:

1. Navigate and open the desired environment and modify the variables indicated in the following steps:
   1. Within Postman click on the environment shortcut in the sidebar
   2. Clicking the environment `DNAC Template Labs Student`
      ![json](./assets/Postman-Environment.png?raw=true "Import JSON")
2. Scroll down in the Environment variables shown:
   1. Find the variable `HierarchyArea`
   2. Edit the data in the forth column with your student info `Student-12` 
   3. Click the `Save` button to commit the changes
      ![json](./assets/Postman-Environment-Area-Modify.png?raw=true "Import JSON")

Within the environment please review the DNS, DHCP, TimeZone, and other components which are utilized within the settings of the environment. Please feel free to modify the DNS, or DHCP settings with your own values.

## Summary
At this point we have reviewed the settings within the environment and ensured we will be targeting the correct hierarchy and we are ready to continue pushing the settings and credentials to our newly created hierarchy.
