# Module 2 - Building Hierarchy
In this module we will use *Postman* to build and deploy a hierarchy within DNA Center. DNA Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network.

## Hierarchy Background
The Design area is where you create the structure and framework of your network, including the logical topology, network settings, and device type profiles that you can apply to devices throughout your network.

You can create a network hierarchy that represents your network's geographical locations. Your network hierarchy can contain sites, which in turn contain buildings and areas. You can create site and building IDs to easily identify where to apply design settings or configurations later. By default, there is one site called Global.

The network hierarchy has a predetermined hierarchy:

**Areas** or **Sites** do not have a physical address, such as the United States. You can think of areas as the largest element. Areas can contain buildings and subareas. For example, an area called United States can contain a subarea called California, and the subarea California can contain a subarea called San Jose.

**Buildings** have a physical address and contain floors and floor plans. When you create a building, you must specify a physical address and latitude and longitude coordinates. Buildings cannot contain areas. By creating buildings, you can apply settings to a specific area.

**Floors** are within buildings and consist of cubicles, walled offices, wiring closets, and so on. You can add floors only to buildings.

## Objectives
- Authenticate and retrieve a token from Cisco DNA Center.
- Build an **Area**, **Building** and **Floor** in the Hierarchy.

## Prerequisites
The prerequisites steps for preparing for the lab are the following;
1. Download and install the [AnyConnect client](../README.md#cisco-anyconnect-vpn-client)
2. Download and install [Postman](https://wwwin-github.cisco.com/kebaldwi/llabsource-DNAC-102-LL#postman)
3. Import and set up [Postman](https://wwwin-github.cisco.com/kebaldwi/llabsource-DNAC-102-LL/blob/master/labs/dnac-101-0-orientation/1.md#preparing-postman-for-use-with-dna-center)
4. Connect to the dCloud environment the details of which will be displayed by the instructor within the class