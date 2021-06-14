# Application Policys - under development - ETA for delivery 18 June 2021

## Overview
This Lab is designed to be used after first completing labs 1 through 4 and has been created to address how to properly deal with Quality of Service with regard to DNA Center. During the lab we will use Application Policies and apply Quality of Service (QoS) within DNA Center. We will also discuss, set up and use Controller Based Application Recognition. This allows Network Administrators the ability to configure network devices in an ongoing and programmatic manner from within DNA Center to make sure application policies are consistent throughout networks whether using SD-Access or Legacy Network Concepts.

## General Information
There are a number of hurdles to applying Quality of Service. If we were to read and study the Quality of Service whitepaper we would still have hours of work to determine the correct MQC policies to be deployed for the various linecards and chassis within our network. DNA Center allows us to do three things:
1. Update all protocol packs and dynamic URL's used for Application Discovery.
2. Deploy a consistent end-to-end QoS policy.
3. Monitor application usage to assure application and user satisfaction
In order to accomplish this we will discuss all the relevant aspects of these goals along with how we accomplish them in this lab.

## Lab Section 1 - Controller Based Application Recognition
The Application Visibility service lets you manage your built-in and custom applications and application sets. The Application Visibility service, hosted as an application stack within Cisco DNA Center, lets you enable the **C**ontroller-**B**ased **A**pplication **R**ecognition (CBAR) function on a specific device to classify thousands of network and home-grown applications and network traffic. This allows us to deal with applications beyond the capabilities of NBAR 2 which is some 1400 applications currently. 

![json](./images/CBAR.png?raw=true "Import JSON")

The following packages must be installed and are in the dCLOUD environment:
1. *Application Policy*: Lets you automate QOS policies across LAN, WAN, and wireless within your campus and branch.
2. *Application Registry*: Lets you view, manage, and create applications and application sets.
3. *Application Visibility Service*: Provides application classification using Network-Based Application Recognition (NBAR) and CBAR techniques.

The Day-N Application Visibility page provides a quick view of application registry, device recognition method, device CBAR readiness, application observed in the network for the past 2, 24, or 48 hours, and CBAR health.

The Application Visibility service lets Cisco DNA Center connect with external authoritative sources like Cisco, Infoblox or the Microsoft Office 365 Cloud Connector to help classify the unclassified traffic or help generate improved signatures. Through CBAR we can discover applications from sources such as Cisco, Infoblox, or Microsofts 0365 and catagorize them for use on our network. Additionally, unclassified traffic can come from any flow that the CBAR-enabled device identifies but that is not recognized by the NBAR engine. In such cases, the applications that have a meaningful bit rate are reported as unclassified and can be imported and used as applications within application sets within Cisco DNA Center.

![json](./images/CBAR-Sources.png?raw=true "Import JSON")

As the number of applications is always changing and protocol packs are always being updated we can keep those current on the network through CBAR as well. Visibility somteimes can be lost from end-to-end with outdated protocol packs whcih do not allow some application to be correctly recognized which can cause not only visibility holes within the network but also incorrect queuing or forwarding issues. CBAR solves that issue by allowing the push of updated protocl packs across the network.

![json](./images/CBAR-ProtocolPacks.png?raw=true "Import JSON")

Lets get started.

### Step 1 - ***TBD***
Day 0 Setup Wizard to Enable Application Visibility Service
Follow the Day 0 Setup wizard to enable the Application Visibility service in Cisco DNA Center.

Procedure
Step 1	
In the Cisco DNA Center GUI, click the Menu icon () and choose Provision > Services > Application Visibility.

You can view a brief introduction about the Application Visibility feature.

Step 2	
In the Application Visibility page, click Next.

A pop-up window for enabling the Application Visibility service appears. Click Yes in the pop-up window to enable CBAR on Cisco DNA Center.

Step 3	
(Optional) Check the Enable CBAR on all Ready Devices check box or choose devices with CBAR Readiness Status in Ready state.

If you want to choose a device that is not ready for enabling CBAR, follow the info message to move it to Ready state before proceeding in the Setup wizard.

Step 4	
Click Next to enable CBAR on the devices.

Step 5	
(Optional) Choose an external authoritative source, such as Microsoft Office 365 Cloud Connector, to either help classify the unclassified traffic or help generate improved signatures.

Step 6	
Click Finish.

The Overview page provides a quick view of the application registry, device recognition method, device CBAR readiness, application observed in the network for the past 2, 24, or 48 hours (valid only if CBAR is enabled on at least one device), service health, and CBAR health score.




