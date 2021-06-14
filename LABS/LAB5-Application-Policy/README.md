# Application Policys - under development - ETA - 06 / 18 / 2021

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

The Application Visibility service lets Cisco DNA Center connect with external authoritative sources like Cisco's NBAR Cloud, Infoblox or the Microsoft Office 365 Cloud Connector to help classify the unclassified traffic or help generate improved signatures. Through CBAR we can discover applications from sources such as Cisco's NBAR Cloud, Infoblox, or Microsofts 0365 and catagorize them for use on our network. Additionally, unclassified traffic can come from any flow that the CBAR-enabled device identifies but that is not recognized by the NBAR engine. In such cases, the applications that have a meaningful bit rate are reported as unclassified and can be imported and used as applications within application sets within Cisco DNA Center.

![json](./images/CBAR-Sources.png?raw=true "Import JSON")

As the number of applications is always changing and protocol packs are always being updated we can keep those current on the network through CBAR as well. Visibility somteimes can be lost from end-to-end with outdated protocol packs whcih do not allow some application to be correctly recognized which can cause not only visibility holes within the network but also incorrect queuing or forwarding issues. CBAR solves that issue by allowing the push of updated protocl packs across the network.

![json](./images/CBAR-ProtocolPacks.png?raw=true "Import JSON")

Lets get started.

### Step 1 - ***Enabling Controller Based Application Recognition***
The first step will be to enable the CBAR service. During the course of this operation we will enable CBAR on the switch, as well as instantiate feeds and connect with external authoritative sources at Cisco and Microsofts 0365.

1. Navigate to the **Application Visibility** within DNA Center through the menu *Provision>Services>Application Visibility*.
   ![json](./images/DNAC-CBAR-Navigation.png?raw=true "Import JSON")
2. In the Application Visibility page, click Next. A pop-up window for enabling the Application Visibility service appears. Click Yes in the pop-up window to enable CBAR on Cisco DNA Center.
   ![json](./images/DNAC-CBAR-Enable.png?raw=true "Import JSON")
3. Check the Enable CBAR on all Ready Devices check box or choose the switch within CBAR Readiness Status in Ready state. Click Next to enable CBAR on the devices.
   ![json](./images/DNAC-CBAR-EnableDevice.png?raw=true "Import JSON")
4. We will now configure the external authoritative sources:
   #### NBAR Cloud
   1. First we will connect to Cisco's NBAR Cloud. First select **Configure** under *NBAR Cloud*. Then click the **Cisco API Console** to configure the connection on the Cisco side.
      ![json](./images/DNAC-CBAR-NBARCLOUD.png?raw=true "Import JSON")
   2. A new browser tab should open after authenticaiton to the **Cisco API COnsole**. This allows you to configure multiple connections to various API services within Cisco. Click **Register a New App**
      ![json](./images/DNAC-NBARCLOUDAPI.png?raw=true "Import JSON")
   3. On the next page name your **Application** which in our case will be `DCLOUD DNAC`
      ![json](./images/DNAC-NBARCLOUD-1.png?raw=true "Import JSON")
   4. Scroll down and **select all the checkboxes** including the **acceptance of terms** and click the **Register** button
      ![json](./images/DNAC-NBARCLOUD-2.png?raw=true "Import JSON")
   5. A success page should appear. Click the **My Keys & Apps** link within it.
      ![json](./images/DNAC-NBARCLOUD-SUCCESS.png?raw=true "Import JSON")
   6. You will then select the *Application* tab and from it the **Application Name**, as well as the **Key** and the **Client Secret** and one by one copy them into the previous window
      ![json](./images/DNAC-NBARCLOUD-SVC.png?raw=true "Import JSON")
   7. Ensure that the Service is **Enabled** that the **Client ID** AKA **Key** is entered along with the **Client Secret**. Additionally enter the **Organization Name** aka the **Application** and click **Save**.
      ![json](./images/DNAC-CBAR-NBARCLOUD_SETTINGS.png?raw=true "Import JSON")
   #### MS Office O365 Cloud
   1. To Enable the MS Office 365 Cloud connector enable the selector switch
      ![json](./images/DNAC-CBAR-0365.png?raw=true "Import JSON")
   2. Click Yes on the popup to enable the connection and click **Finish** to finish enabing the service
      ![json](./images/DNAC-CBAR-0365-YES.png?raw=true "Import JSON")
5. At this point CBAR application will display.
   ![json](./images/DNAC-CBAR.png?raw=true "Import JSON")

### Step 2 - ***Updating Protocol Packs***
Within the CBAR Application, we will now update the protocol pack for the **ACCESS-C9300-1-ASW** switch. 

1. To initiate the *Protocol Pack Update* select the device to be updated, and then click the *Update Protocol Pack* and then submenu *Selected Devices*
   ![json](./images/DNAC-Device-Update.png?raw=true "Import JSON")
2. In the Pop-up that appears select the **update** link beside the version that you wish to update to, and then click **Yes** to initiate it.
   ![json](./images/DNAC-Device-Select-Pack.png?raw=true "Import JSON")
3. On the CBAR Application Portal the protocol pack will show as *updating*.
   ![json](./images/DNAC-Protocol-Updating.png?raw=true "Import JSON")
3. Eventually the protocol pack will show as *updated*.
   ![json](./images/DNAC-Protocol-Updating.png?raw=true "Import JSON")

   
   






The Overview page provides a quick view of the application registry, device recognition method, device CBAR readiness, application observed in the network for the past 2, 24, or 48 hours (valid only if CBAR is enabled on at least one device), service health, and CBAR health score.




