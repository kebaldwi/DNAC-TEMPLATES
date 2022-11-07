# Application QoS Policys - in Development
![json](./images/underconstruction.png?raw=true "Import JSON")
## Overview
This Lab is designed to be used after first completing labs 1 through 4 and has been created to address how to properly deal with Quality of Service with regard to DNA Center. During the lab we will use Application Policies and apply Quality of Service (QoS) within DNA Center. We will also discuss, set up and use Controller Based Application Recognition. This allows Network Administrators the ability to configure network devices in an ongoing and programmatic manner from within DNA Center to make sure application policies are consistent throughout networks whether using SD-Access or Legacy Network Concepts. This set of concepts requires ***Advantage Licensing***.

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

As the number of applications is always changing and protocol packs are always being updated we can keep those current on the network through CBAR as well. Visibility sometimes can be lost from end-to-end with outdated protocol packs whcih do not allow some application to be correctly recognized which can cause not only visibility holes within the network but also incorrect queuing or forwarding issues. CBAR solves that issue by allowing the push of updated protocl packs across the network.

![json](./images/CBAR-ProtocolPacks.png?raw=true "Import JSON")

Lets get started.

<details closed>
<summary> Click for Details and Sub Tasks</summary>

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

</details>

## Lab Section 2 - Building and Deploying an Application Policy
The Application Policy methodology within DNA Center allows for two types of policies to be constructed, wired and wireless. During this section we will build and deploy an Application Policy for a wired environment.

<details closed>
<summary> Click for Details and Sub Tasks</summary>

### Step 1 - ***Build Application Policy Draft***
1. Navigate to **Application Policy** within DNA Center through the menu *Policy>Application*.
   ![json](./images/DNAC-AppPolicyNavigate.png?raw=true "Import JSON")
2. In the Application Policy page, click **Add Policy**. 
   ![json](./images/DNAC-AppPolicy-0-Start.png?raw=true "Import JSON")
3. Enter `DNAC-Template-Lab` as the name for the Application Policy Name.
   ![json](./images/DNAC-AppPolicy-1-Name.png?raw=true "Import JSON")
   #### Site to Apply Policy
4. Click the **Site** and then on the popup on the right click **Edit Scope**
   ![json](./images/DNAC-AppPolicy-2-Site.png?raw=true "Import JSON")
5. Put a tick next to *Floor 1*. Click **Save**  
   ![json](./images/DNAC-AppPolicy-3-SiteEdit.png?raw=true "Import JSON")
6. Please note that the gear icon you may have noticed on the right of the floor allows access to either exclude devices or interfaces from the QoS Policy should it be required. 
   ![json](./images/DNAC-AppPolicy-4-SiteExclude.png?raw=true "Import JSON")
   #### Queuing Policy to Apply
7. Click the **CVD_QUEUING_PROFILE** link to open the Queuing Profile Editor.
   ![json](./images/DNAC-AppPolicy-5-Queue.png?raw=true "Import JSON")
8. If you wished to deviate from the CVD Queuing Profile you could click **Add Profile**
   ![json](./images/DNAC-AppPolicy-6-QueueCVD.png?raw=true "Import JSON")
9. Within the Queuing Profile Editor you would name the new profile and then adjust the sliders to set your queuing policy. Once complete you would click **Select** to use that policy. We will not deviate from the CVD standard at this time so click **Cancel**.
   ![json](./images/DNAC-AppPolicy-7-QueueCustom.png?raw=true "Import JSON")
   #### Host Tracking
10. Click the **Host Tracking Slider** to allow for QoS policy to work with endpoint mobility. When host tracking is turned on, Cisco DNA Center tracks the connectivity of the collaboration endpoints within the site scope and automatically reconfigures the ACL entries when the collaboration endpoints connect to the network or move from one interface to another. 
   ![json](./images/DNAC-AppPolicy-8-Tracking.png?raw=true "Import JSON")
   #### Saving Draft Policy
11. At this point we could save a copy of the Application Policy by selecting the three dots beside Deploy a pop up menu will appear.
   ![json](./images/DNAC-AppPolicy-8.5-Menu.png?raw=true "Import JSON")
12. Click **Save Draft** from the pop up menu 
   ![json](./images/DNAC-AppPolicy-9-SaveDraft.png?raw=true "Import JSON")
### Step 2 - ***Deploying Application Policy***
   #### Preview Policy
1. Click the three dots beside Deploy a pop up menu will appear.
   ![json](./images/DNAC-AppPolicy-8.5-Menu.png?raw=true "Import JSON")
2. Click **Preview** on the popup menu to preview the policy.
   ![json](./images/DNAC-AppPolicy-10-PreviewStart.png?raw=true "Import JSON")
3. Click **Generate** on the popup on the right to generate the policy.
   ![json](./images/DNAC-AppPolicy-11-PreviewGenerate.png?raw=true "Import JSON")
4. Click **View** on the popup on the right to view the policy.
   ![json](./images/DNAC-AppPolicy-12-PreviewView.png?raw=true "Import JSON")
5. Take a look at the policy in the popup on the right.
   ![json](./images/DNAC-AppPolicy-13-Preview.png?raw=true "Import JSON")
   #### Deploy Policy
6. Click the **Deploy** and click **Yes** on the pop up that will appear.
   ![json](./images/DNAC-AppPolicy-14-Deploy.png?raw=true "Import JSON")
7. Click the **Apply** on the pop up on the right that will appear. You could alternatively schedule this task.
   ![json](./images/DNAC-AppPolicy-15-Apply.png?raw=true "Import JSON")
8. Another pop up will appear with the word *configuring* to symbolize the policy push.
   ![json](./images/DNAC-AppPolicy-16-Configuring.png?raw=true "Import JSON")
9. The word *Success* should be displayed shortly after to symbolize the policy has been pushed. Click the Success link to view the deployed policy.
   ![json](./images/DNAC-AppPolicy-17-Success.png?raw=true "Import JSON")
10. Another pop up will appear with the deployed policy which has been pushed.
   ![json](./images/DNAC-AppPolicy-18-DeployedPolicy.png?raw=true "Import JSON")
11. After closing the popups you will notice two elements in the Application Policy page. The Draft Policy which can be reused and the Policy as pushed to the site..
   ![json](./images/DNAC-AppPolicy-19-DraftAndPolicy.png?raw=true "Import JSON")

At this point you have successfully pushed a CVD QoS Policy to the network.

</details>

## Lab Section 3 - Building and Deploying a Custom Application
The Application Policy methodology within DNA Center allows for two types of policies to be constructed, wired and wireless. During this section we will build and deploy an Application Policy for a wired environment.

<details closed>
<summary> Click for Details and Sub Tasks</summary>

### Step 1 - ***Building a Custom Application***
1. Navigate to **Application Sets** within DNA Center from the Application Policies tab select **Application Sets** and then the redirect.
   ![json](./images/DNAC-AppPolicy-1-Start.png?raw=true "Import JSON")
2. In the Application Set page, click **Add Application Set**. 
   ![json](./images/DNAC-AppPolicy-2-AppSet-Add.png?raw=true "Import JSON")
3. In the Add Application Set pop up, enter `DNAC-Template-Lab` as the **Application Set Name** then click **Save**. 
   ![json](./images/DNAC-AppPolicy-3-AppSet-Save.png?raw=true "Import JSON")
4. Click the **Application** tab then click **Add Application**. 
   ![json](./images/DNAC-AppPolicy-4-App.png?raw=true "Import JSON")
5. In the Add Application Pop Up:
   1. Enter `DNAC-Template-Lab-VUDU` as the Application Name.
   2. Select **URL** then enter `www.vudu.com`.
   3. Click the dropdown for Application Set.
   ![json](./images/DNAC-AppPolicy-5-App-Add.png?raw=true "Import JSON")
6. Enter **DNA** in the search bar and click the Application Set **DNAC-Template-Lab**. 
   ![json](./images/DNAC-AppPolicy-6-App-AppSet.png?raw=true "Import JSON")
7. Click the dropdown for *Traffic Class* then choose **Multimedia Streaming**. 
   ![json](./images/DNAC-AppPolicy-7-App-Class.png?raw=true "Import JSON")
8. Click **Save** on the Add Application Pop Up. 
   ![json](./images/DNAC-AppPolicy-8-App-Save.png?raw=true "Import JSON")
9. Click **Application Set** then expand the **DNAC-Template-Lab** Application Set to see how it looks. 
   ![json](./images/DNAC-AppPolicy-9-AppSet-Final.png?raw=true "Import JSON")

### Step 2 - ***Deploying a Custom Application***
1. Navigate to **Application Policy** within DNA Center through the menu *Policy>Application*.
   ![json](./images/DNAC-AppPolicyNavigate.png?raw=true "Import JSON")
2. Click on the Application Policy then **Actions** and **Edit** from the submenu. 
   ![json](./images/DNAC-AppPolicy-10-Edit.png?raw=true "Import JSON")
3. Click **Unassigned Applications** to expand it. 
   ![json](./images/DNAC-AppPolicy-11-UnAssign.png?raw=true "Import JSON")
4. Click and hold the application set **DNAC-Template-Lab** and drag it to the Default section. 
   ![json](./images/DNAC-AppPolicy-12-Drag.png?raw=true "Import JSON")
5. Drop the application set **DNAC-Template-Lab** in the Default Section then click **Deploy** 
   ![json](./images/DNAC-AppPolicy-13-Drop.png?raw=true "Import JSON")
6. Click **Apply** to deploy the policy. 
   ![json](./images/DNAC-AppPolicy-14-Apply.png?raw=true "Import JSON")
7. Another pop up will appear with the word *configuring* to symbolize the policy push.
   ![json](./images/DNAC-AppPolicy-15-Configure.png?raw=true "Import JSON")
9. The word *Success* should be displayed shortly after to symbolize the policy has been pushed. Click the Success link to view the deployed policy.
   ![json](./images/DNAC-AppPolicy-16-Success.png?raw=true "Import JSON")
10. Another pop up will appear with the deployed policy which has been pushed.
   ![json](./images/DNAC-AppPolicy-17-Final.png?raw=true "Import JSON")

At this point you have successfully built and deployed a custom Application within a QoS Policy.

</details>

## Automating Application Policies
While it is possible to click through these processes manually, which can be time-consuming, we can handle this differently. We may automate them further via REST API.

## Summary
Congratulations you have completed building Application Policies and deploying QoS on both wired and wireless networks. It is important that both the wired and wireless network are set up correctly for QoS, and that protocol packs are maintained across the network infrastructure. CBAR helps facilitate that and closes with application discovery rounding out the story.

## Lab Modules
The lab will be split into modules to concentrate on specific tasks. Eash is designed to build your knowledge in specific areas and they will call out any dependancies on previous modules. We will cover are the following which you can access via the links below:

1. [**Wireless Controller PnP or Discovery**](./module1-ctrlpnpdiscovery.md)
2. [**WLAN Creation**](./module2-wlans.md)
3. [**AP Provisioning**](./module3-approvisioning.md)
4. [**Application QoS**](./module4-applicationqos.md)
5. [**Model Based Config**](./module5-modelbasedconfig.md)
6. [**Wireless Templates**](./module6-wirelesstemplates.md)
7. [**Controller HA**](./module3-controllerha.md)

## Main Menus
To return to the main menus
1. [Wireless Automation Main Menu](./README.md)
2. [DNAC-TEMPLATES-LABS Main Menu](../README.md)
3. [DNAC-TEMPLATES Repository Main Menu](../../README.md)

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
