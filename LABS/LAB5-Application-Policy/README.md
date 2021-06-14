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
The Application Visibility service lets you manage your built-in and custom applications and application sets. The Application Visibility service, hosted as an application stack within Cisco DNA Center, lets you enable the Controller-Based Application Recognition (CBAR) function on a specific device to classify thousands of network and home-grown applications and network traffic.

The following packages must be installed and are in the dCLOUD environment:

Application Policy: Lets you automate QOS policies across LAN, WAN, and wireless within your campus and branch.
Application Registry: Lets you view, manage, and create applications and application sets.
Application Visibility Service: Provides application classification using Network-Based Application Recognition (NBAR) and CBAR techniques.

The Day-N Application Visibility page provides a quick view of application registry, device recognition method, device CBAR readiness, application observed in the network for the past 2, 24, or 48 hours, and CBAR health.

The Application Visibility service lets Cisco DNA Center connect with external authoritative sources like Cisco, Infoblox or the Microsoft Office 365 Cloud Connector to help classify the unclassified traffic or help generate improved signatures. Through CBAR we can discover applications from sources such as Cisco, Infoblox, or Microsofts 0365 and catagorize them for use on our network. Additionally, unclassified traffic can come from any flow that the CBAR-enabled device identifies but that is not recognized by the NBAR engine. In such cases, the applications that have a meaningful bit rate are reported as unclassified and can be imported and used as applications in Cisco DNA Center.

This allows us to deal with applications beyond the capabilities of NBAR 2 which is some 1400 applications currently. As the number of applications is always changing and protocol packs are always being updated we can keep those current on the network through CBAR as well.




### Step 1 - ***TBD***



