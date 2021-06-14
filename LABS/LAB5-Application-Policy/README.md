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



You can create Day N Composite Templates within the ***Template Editor*** within **DNA Center**. Go to the ***Template Editor*** to complete the next task. In this lab, we will deploy a Composite Template and additional Regular Templates within a project.  The import and export function within **DNA Center** allows both the import and export of templates and projects, along with the ability to clone them.
NBAR2 – Network Based Application Recognition that is supported on
Routers/Switches/WLC which uses various techniques including DPI to
identify applications
Protocol Packs – The signatures supported by NBAR2 on devices are
delivered via Protocol packs
CBAR – Controller based Application Recognition a.k.a Application Visibility
Service on Cisco DNA Center

### Step 1 - ***Import Project with Templates***



