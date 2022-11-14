# Application QoS Policys

## Overview
This Lab is designed to be used after first completing labs 1 through 4 and has been created to address how to properly deal with Quality of Service with regard to DNA Center. During the lab we will use Application Policies and apply Quality of Service (QoS) within DNA Center. We will also discuss, set up and use Controller Based Application Recognition. This allows Network Administrators the ability to configure network devices in an ongoing and programmatic manner from within DNA Center to make sure application policies are consistent throughout networks whether using SD-Access or Legacy Network Concepts. This set of concepts requires ***Advantage Licensing***.

## General Information
There are a number of hurdles to applying Quality of Service. If we were to read and study the Quality of Service whitepaper we would still have hours of work to determine the correct MQC policies to be deployed for the various linecards and chassis within our network. DNA Center allows us to do three things:
1. Update all protocol packs and dynamic URL's used for Application Discovery.
2. Deploy a consistent end-to-end QoS policy.
3. Monitor application usage to assure application and user satisfaction
In order to accomplish this we will discuss all the relevant aspects of these goals along with how we accomplish them in this lab.

Previously we have built and deployed during [Lab 5](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB5-Application-Policy/) an Application Policy and Controller-based Application Recognition otherwise known as SDAVC. Please refer to that section to complete the building of the wired section and deploy SDAVC.

## Lab Section 1 - Building and Deploying a Wireless Application Policy
The Application Policy methodology within DNA Center allows for two types of policies to be constructed, wired and wireless. During this section we will build and deploy an Application Policy for a wireless environment.

<details closed>
<summary> Click for Details and Sub Tasks</summary>

### Step 1 - ***Build Application Policy Draft***
1. Navigate to **Application Policy** within DNA Center through the menu *Policy>Application*.
   ![json](./images/module4-applicationqos/dnac-menu-appqos.png?raw=true "Import JSON")
2. In the Application Policy page, click **Add Policy**. 
   ![json](./images/module4-applicationqos/dnac-menu-appqos-addpolicy?raw=true "Import JSON")
3. Complete the following steps:
   1. Enter `Wireless-CAMPUS-PSK` as the name for the Application Policy Name. 
   2. Select **Wireless** as the type of Application Policy to be built.
      ![json](./images/module4-applicationqos/dnac-menu-appqos-policy-name.png?raw=true "Import JSON")
4. Select **Yes** in the popup window that appears.
   ![json](./images/module4-applicationqos/dnac-menu-appqos-policy-wifi.png?raw=true "Import JSON")

#### Site to Apply Policy
5. Click the **Site** and then on the popup on the right click **Edit Scope**
   ![json](./images/module4-applicationqos/dnac-menu-appqos-policy-wifi-sites?raw=true "Import JSON")
6. Put a tick next to *Building*. Click **Save**  
   ![json](./images/module4-applicationqos/dnac-menu-appqos-policy-wifi-sites-edit.png?raw=true "Import JSON")

#### Queuing Policy to Apply
7. Click the **CVD_QUEUING_PROFILE** link to open the Queuing Profile Editor.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-5-Queue.png?raw=true "Import JSON")
8. If you wished to deviate from the CVD Queuing Profile you could click **Add Profile**
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-6-QueueCVD.png?raw=true "Import JSON")
9. Within the Queuing Profile Editor you would name the new profile and then adjust the sliders to set your queuing policy. Once complete you would click **Select** to use that policy. We will not deviate from the CVD standard at this time so click **Cancel**.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-7-QueueCustom.png?raw=true "Import JSON")

#### Host Tracking
10. Click the **Host Tracking Slider** to allow for QoS policy to work with endpoint mobility. When host tracking is turned on, Cisco DNA Center tracks the connectivity of the collaboration endpoints within the site scope and automatically reconfigures the ACL entries when the collaboration endpoints connect to the network or move from one interface to another. 
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-8-Tracking.png?raw=true "Import JSON")

#### Saving Draft Policy
11. At this point we could save a copy of the Application Policy by selecting the three dots beside Deploy a pop up menu will appear.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-8.5-Menu.png?raw=true "Import JSON")
12. Click **Save Draft** from the pop up menu 
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-9-SaveDraft.png?raw=true "Import JSON")

### Step 2 - ***Deploying Application Policy***
#### Preview Policy
1. Click the three dots beside Deploy a pop up menu will appear.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-8.5-Menu.png?raw=true "Import JSON")
2. Click **Preview** on the popup menu to preview the policy.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-10-PreviewStart.png?raw=true "Import JSON")
3. Click **Generate** on the popup on the right to generate the policy.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-11-PreviewGenerate.png?raw=true "Import JSON")
4. Click **View** on the popup on the right to view the policy.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-12-PreviewView.png?raw=true "Import JSON")
5. Take a look at the policy in the popup on the right.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-13-Preview.png?raw=true "Import JSON")

#### Deploy Policy
6. Click the **Deploy** and click **Yes** on the pop up that will appear.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-14-Deploy.png?raw=true "Import JSON")
7. Click the **Apply** on the pop up on the right that will appear. You could alternatively schedule this task.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-15-Apply.png?raw=true "Import JSON")
8. Another pop up will appear with the word *configuring* to symbolize the policy push.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-16-Configuring.png?raw=true "Import JSON")
9. The word *Success* should be displayed shortly after to symbolize the policy has been pushed. Click the Success link to view the deployed policy.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-17-Success.png?raw=true "Import JSON")
10. Another pop up will appear with the deployed policy which has been pushed.
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-18-DeployedPolicy.png?raw=true "Import JSON")
11. After closing the popups you will notice two elements in the Application Policy page. The Draft Policy which can be reused and the Policy as pushed to the site..
   ![json](./images/module4-applicationqos/DNAC-AppPolicy-19-DraftAndPolicy.png?raw=true "Import JSON")

At this point you have successfully pushed a CVD QoS Policy to the network.

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
