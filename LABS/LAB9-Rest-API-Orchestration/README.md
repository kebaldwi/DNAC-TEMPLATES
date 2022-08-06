# Rest-API Orchestration 
## Overview
This Lab is designed as a standalone lab to help customers with varying challenges in Automating and Orchestrating their network infrastructure. Within the lab we will make use of various tools and techniques to Automate various tasks, and orchestrate over DNA Center.

## General Information
Up until this point we have used Rest-API for some basic set up tasks, but their are so many varying situations that can be solved or at least eased utilizing Rest-API inconjunction with DNA Center. In this lab we will use a complete set of REST-API collections which will build upon the foundational knowledge acquired in the previous labs. For this lab we will concentrate on DNA Center configuration, and how DNA Center can be automated to perform various functions which we have already covered. 

This page will serve as the landing page for this lab section due to the amount of content it will cover and the need to expand on it over time. 

The lab will utilize a set of collections publically shared on postmans workspaces and those collections will also be expanded to keep in line with this lab.

## Lab Modules
The use cases we will cover are the following which you can access via links below:

1. [**Postman Orientation**](./postman.md)
2. [**Building Hierarchy**](./labs/dnac-101-1-hierarchy/1.md)
3. [**Assign Settings and Credentials**](./labs/dnac-101-2-settings/1.md)
4. [**Device Discovery**]()
5. [**Template Deployment**](./labs/dnac-101-4-templates/1.md)
6. [**Configuration Archive**](./labs/dnac-101-6-archive/1.md)
7. [**Retrieving Network Inventory**](./labs/dnac-101-5-inventory/1.md)
8. [**Running Show Commands**](./labs/dnac-101-3-cmd-run/1.md)

## Preparation
In order to compete this module, its best to connect to the dCloud lab environment using your own laptop so that you can get accustomed to and begin using the tools. In the event that you cannot install postman though it is possible to complete all tasks via the workstation in the dCloud environment.

Our screen shots will alll be from the jump host, but remember you can use your own laptop.

If you would like to connect to the dCloud environment please ensure you install the following

### Lab Requirements
This lab is designed to be run in Cisco dClouds - Enterprise Network Sandbox Lab. It was developed in version 4 which includes DNA Center 2.2.3.5 and equipment running at least 17.x versions of code.

### Tools Required
Please utilize the following tools to effectively run the lab, and ensure they are installed on your workstation/laptop prior to the class.

1. Cisco AnyConnect VPN Client
2. Postman
3. Google Chrome

#### Cisco AnyConnect VPN Client
This software is required to connect your workstation to Cisco dCloud. For an explanation into AnyConnect and how to use it with dCloud please visit the following URL: 

- <a href="https://dcloud-cms.cisco.com/help/android_anyconnect" target="_blank">dCloud AnyConnect Documentation</a>

If you do not have the anyconnect client please visit 

- <a href="https://dcloud-rtp-anyconnect.cisco.com" target="_blank">⬇︎AnyConnect Download Site⬇︎</a>

#### Postman
Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration so you can create better APIs—faster.

Once Postman has been downloaded to your desktop it is advisable to set up an account and sign in so that all your changes can be used within any system with the client or a web browser much in the same way as a chrome or firefox profile work. This additional capability I have found incredibly useful when working in multiple environments. 

- <a href="https://www.postman.com/downloads/" target="_blank">⬇︎Postman Download⬇︎</a>

##### Postman Documentation
For an understanding of postman please visit this site:

- <a href="https://learning.postman.com/docs/getting-started/introduction/" target="_blank">Postman Documentation</a>

#### Google Chrome
Google Chrome is the optimal browser of choice when working in the DNA Center UI. 

To download Google Chrome please visit 

- <a href="https://www.google.com/chrome/downloads/" target="_blank">⬇︎Chrome Download⬇︎</a>

## Summary
This lab is intended for educational purposes only. Use outside of a lab environment should be done at the operators risk. Cisco assumes no liability for incorrect usage.
