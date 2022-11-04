# Wireless LAN Design
Within this lab module, we will concentrate our efforts on the design aspects of creating Wireless LANs (WLANs) via **DNA Center**. Previously we have discovered the Wireless LAN Controller by **Cisco DNA Center**, and assigned it to a site within the hierarchy. At this point we will configure the various settings for the Wireless Design.

Within this lab we will concentrate on the following which are typical in most Enterprise Networks today:
1. Wireless LAN Creation
2. Wireless Profiles
3. RF Profiles
4. FlexConnect 
5. Controller Provisioning

### Logical Topology
To review the lab envionment that is available is depicted here:

For routing in the environment an OSPF IGP process has been created to propogate internal route information. Within the access switches which are connected at Layer 3 to the router, we have estansiated a layer 2 port channel between them and initiated various vlans for Access Point connectivity and for the clients, whose gateway is built on an HSRP instance shared between the two switches.

The 9130AX Access Points are connected to both access switches and the ports are automatically configured via the AUTOCONF feature.

![json](./images/DCLOUD_Topology_Wireless-v1.png?raw=true "Import JSON")

The clients will be connected connected to the network via FlexConnect due to the nature of the DCLOUD labs design. Where applicable we will call out the differences between FlexConnect and Local Mode Design.

The Wireless Clients will associate and connect to the SSID's within the lab and will then be dropped into one of the following VLAN via the trunk from the FlexConnect Access Point.

1. Vlan 20 - datavlan - 192.168.20.0/24
2. Vlan 30 - voicevlan - 192.168.30.0/24
3. Vlan 40 - guestvlan - 192.168.40.0/24

For simplicity we may utilize the Vlan 30 as a second Data network when proving out CoA or AAA Overide features.

## Lab Section 1 - Wireless LAN's
To get started with Wireless Controller configuration and automation we first need to build the settings, Wireless LAN environments and associated profiles for deployment. Each Wireless LAN can be built by DNA Center and all settings may be deployed either through the UI, from Model-Based Config (covered separately), and by Templates (covered separately)for extranious configuration which might be required.

This section will be devoted to building Wireless LAN's. Subsequent sections will cover the profiles and provisioning.

### Building a PreShared Key (PSK) Wireless LAN
In this subsection we will build a Wireless LAN for PSK authentication. 

<details closed>

#### Step 1 - ***Create SSID***
1. Open a web browser on the Windows Workstation Jump host. Open a connection to DNA Center and select the hamburger menu icon to open the menu. Select `Design>Network Settings`.

![json](./images/module2-wlans/dnac-menu-network-settings.png?raw=true "Import JSON")

2. On the Network page click the `Wireless` tab to navigate to the wireless page.

![json](./images/module2-wlans/dnac-navigation-wireless-settings.png?raw=true "Import JSON")

3. On the **Wireless** page click `Add` above the *SSID* section to create a new Wireless LAN

![json](./images/module2-wlans/dnac-wireless-ssid-psk-begin.png?raw=true "Import JSON")

4. A Wireless SSID workflow will begin with *BASIC Settings* which will guide you through the build process of the WLAN. Complete the following steps:
   1. Enter the **Wireless Network Name (SSID)** as `CAMPUS-PSK`
   2. **Dual Band Operation (2.4 Ghz and 5 Ghz)** *enables the SSID for dual band operation*
   3. **Voice and Data** *configuring best practices for Both Voice and Data*
   4. **Admin Status** *enables the SSID*
   5. **Broadcast SSID** *enables the SSID to be broadcast allowing clients to see it*
   6. Click **Next** to continue

   ![json](./images/module2-wlans/dnac-wireless-ssid-psk-basic.png?raw=true "Import JSON")

5. The Wireless SSID workflow will continue with *Security Settings*. Complete the following steps:
   1. In the *Level of Security* section select **Personal**
   2. Additionally in the *Level of Security* section select **WPA2**
   3. For *Passphrase Type* select **ASCII**
   4. Enter `C1sco12345C1sco12345` for the *Passphrase*
   5. In the *AAA Configuration section* select **Fast Lane**
   6. Click **Next** to continue

   ![json](./images/module2-wlans/dnac-wireless-ssid-psk-security.png?raw=true "Import JSON")

6. The Wireless SSID workflow continues with *Advance Settings*. Complete the following steps:
   1. Leave all sections here as default as shown
   2. Click **Next** to continue

   ![json](./images/module2-wlans/dnac-wireless-ssid-psk-advance.png?raw=true "Import JSON")

#### Step 2 - ***Associate SSID to Profile***
1. The Wireless SSID workflow continues with *Associate SSID to Profile*. As no *Wireless Profile* exists, we must click **Add Profile** to add one to DNA Center.

   ![json](./images/module2-wlans/dnac-wireless-ssid-psk-profile-begin.png?raw=true "Import JSON")

2. The Wireless SSID workflow continues with *Associate SSID to Profile*. Complete the following steps:
   1. Enter the **Profile Name** as `DNAC-WIRELESS`
   2. Select **No** *under Fabric*
   3. Select **Interface**
   4. Select **management** for the *Interface Name*
   5. Select **No** for *do you need Anchor for the SSID*
   6. Select **FlexConnect Local Switching** for the SSID
   7. Enter **20** for *Local to VLAN*
   8. Click **Next** to continue

   ![json](./images/module2-wlans/dnac-wireless-ssid-psk-profile-campus-psk.png?raw=true "Import JSON")

3. The Wireless SSID workflow continues with *Associate SSID to Profile*. On the left the Profile **DNAC-WIRELESS** will be displayed with a green checkmark.
   1. Click **Next** to continue

   ![json](./images/module2-wlans/dnac-wireless-ssid-psk-profile-campus-psk-associated.png?raw=true "Import JSON")

4. The Wireless SSID workflow continues with a *Summary* page. On the left the a summary of all the changes will be displayed.
   1. Click **Next** to continue

   ![json](./images/module2-wlans/dnac-wireless-ssid-psk-profile-campus-psk-summary.png?raw=true "Import JSON")

5. The Wireless SSID workflow completes with a *Results* page displaying that both the SSID and the Profiles were successfully saved and updated. 
   1. Click **Configure Network Profile** to assign the profile to a site.

   ![json](./images/module2-wlans/dnac-wireless-ssid-psk-profile-campus-psk-results.png?raw=true "Import JSON")

#### Step 3 - ***Assign Sites to Network Profile***
1. On the *Network Profile* page select **Assign** beside the wireless profile **DNAC-WIRELESS**

   ![json](./images/module2-wlans/dnac-wireless-network-profile-assign.png?raw=true "Import JSON")

2. On the *Add Sites to Profile* slide out page select **Floor 1** to assign the site to the wireless networkk profile. 
3. Click ***Save*** to complete the assignment

   ![json](./images/module2-wlans/dnac-wireless-network-profile-add-sites.png?raw=true "Import JSON")

4. On the *Network Profile* page note **1 Site** appears under *Sites* for the wireless profile **DNAC-WIRELESS**

   ![json](./images/module2-wlans/dnac-wireless-network-profile-assigned.png?raw=true "Import JSON")

5. Return to the **Wireless Settings** page and you should see now our new *SSID* **CAMPUS-PSK**.

   ![json](./images/module2-wlans/dnac-wireless-ssid-psk-results.png?raw=true "Import JSON")
</details>

### Creating a Wireless Radio Frequency RF Profile
In this subsection we will build a Wireless Radio Frequency (RF) Profile. This helpful tool, allows the administrator to tune the RF spectrum for the type of environment, and channels which are needed to support clients within their carpeted and non carpeted spaces. 

There are many things that can be accomplished from an RF Profile, to tweek the environment, from channels used, to data rates, to power settings deployed. Access points when deployed will utilize these RF Profiles to deploy the SSID's and the intention is to have the best wireless experience for the clients served in a specific area.

#### Step 1 - ***Create RF Profile***
1. To create an RF Profile, first open a web browser on the Windows Workstation Jump host. Open a connection to DNA Center and select the hamburger menu icon to open the menu. Select `Design>Network Settings`.

![json](./images/module2-wlans/dnac-menu-network-settings.png?raw=true "Import JSON")

2. On the Network page click the `Wireless` tab to navigate to the wireless page.

![json](./images/module2-wlans/dnac-navigation-wireless-settings.png?raw=true "Import JSON")

3. On the **Wireless** page click `Add` above the *RF Profile* section to create a new Wireless RF Profile

![json](./images/module2-wlans/dnac-wireless-rfprofile-begin.png?raw=true "Import JSON")

4. The Create RF Profile page displays with *Wireless > Create RF Profile*. Complete the following steps:
   1. Enter the **Profile Name** as `DNAC-WIRELESS`
   2. Under the 2.4 Ghz Section set the *Supported Data Rates* to start at **12**
   3. Set the *Mandatory Data Rates* to **12** and **24** as shown
   4. Scroll down continue

   ![json](./images/module2-wlans/dnac-wireless-rfprofile-24ghz.png?raw=true "Import JSON")

5. Continue creating the RF Profile by completing the following steps:
   1. Under the 5 Ghz Section set the *Channel Width* to **20 Mhz**
   2. Set the *Mandatory Data Rates* to **12** and **24** as shown
   3. Click **Save** continue

   ![json](./images/module2-wlans/dnac-wireless-rfprofile-5ghz.png?raw=true "Import JSON")

6. The `Wireless` tab will reappear with the new *RF Profile* as displayed.

![json](./images/module2-wlans/dnac-wireless-rfprofile-results.png?raw=true "Import JSON")

### Creating a FlexConnect Local Vlans
In this subsection we will add additional vlans for local switching for our FlexConnect deployment. *Note: If we were utilizing* ***Local Mode*** *for the Access Points we would add additional Wireless Interfaces or vlan groups respectively to the Controller.* 

In this lab, we need to utilize FlexConnect, and so to allow for CoA of clients to other Vlans we need to add those to the configuration of our Access Points. 

#### Step 1 - ***Add FlexConnect VLANs***
1. To create an RF Profile, first open a web browser on the Windows Workstation Jump host. Open a connection to DNA Center and select the hamburger menu icon to open the menu. Select `Design>Network Settings`.

![json](./images/module2-wlans/dnac-menu-network-settings.png?raw=true "Import JSON")

2. On the Network page click the `Wireless` tab to navigate to the wireless page.

![json](./images/module2-wlans/dnac-navigation-wireless-settings.png?raw=true "Import JSON")

3. On the **Wireless** page scroll down to the *FlexConnect VLAN* section and enter the following:
   1. Enter *Native VLAN ID* as `10`
   2. Under *AAA Override VLAN* Section click the **⨁**
   3. In the first *AAA Overide VLAN* set the *VLAN ID* to start at **30**
   4. Set the *VLAN Name* to **voicevlan** as shown
   5. In the second *AAA Overide VLAN* set the *VLAN ID* to start at **40**
   6. Set the *VLAN Name* to **guestvlan** as shown
   7. Click **Save** continue

   ![json](./images/module2-wlans/dnac-wireless-flexconnect-vlan.png?raw=true "Import JSON")

### Wireless Controller Provisioning
In this subsection we will provision the Wireless Controller with the settings for network services, credentials, telemetry and the additional wireless settings of WLAN's, RF Profiles, FlexConnect Vlans.

This can be augmented with Model-Based Configurations as well as Templates which we will discuss in future modules.

#### Step 1 - ***Provisioning Workflow for the Wireless Controller***
1. Open a web browser on the Windows Workstation Jump host. Open a connection to DNA Center and select the hamburger menu icon to open the menu. Select `Provision>Network Devices>Inventory`.

![json](./images/module2-wlans/dnac-menu-provision-inventory.png?raw=true "Import JSON")

2. On the Inventory page click the `Inventory` tab and complete the following:
   1. Select the *C9800-WLC.dcloud.cisco.com* device as shown
   2. Select from the *Actions* submenu
   3. Select *Provision*
   4. Select *Provision Device*

![json](./images/module2-wlans/dnac-menu-provision-inventory-begin.png?raw=true "Import JSON")

3. The **Inventory > Provision Devices** 5 stage workflow will begin. Make no changes on screen 1 and click **Next** to continue.

![json](./images/module2-wlans/dnac-menu-provision-inventory-stage1.png?raw=true "Import JSON")

4. On screen 2 of the **Inventory > Provision Devices** workflow select *Managing 1 Primary location(s)* which is where we tell **DNA Center** where the Access Points will be that this Wireless Controller will manage.

![json](./images/module2-wlans/dnac-menu-provision-inventory-stage2.png?raw=true "Import JSON")

5. On the slideout window select **Floor 1** which is where our Access Points will be that this Wireless Controller will manage. Click **Save** to continue.

![json](./images/module2-wlans/dnac-menu-provision-inventory-stage2-manage.png?raw=true "Import JSON")

6. It is recommended to enable the *AP Reboot Percentage* which aides in upgrades by selecting how many Acee Points are upgraded at any one time. For purposes of the lab we will **Enable** this feature and select **25%** from the dropdown menu. Click **Next** to continue.

![json](./images/module2-wlans/dnac-menu-provision-inventory-stage2-reboot.png?raw=true "Import JSON")

7. On screen 3 of the **Inventory > Provision Devices** workflow we would see the Model-Based Configurations which would be deployed, but none are assigned at this time. This will be covered in later sections. Click **Next** to continue.

![json](./images/module2-wlans/dnac-menu-provision-inventory-stage3.png?raw=true "Import JSON")

8. On screen 4 of the **Inventory > Provision Devices** workflow we would see the Templates which would be deployed, but none are assigned at this time. This will be covered in later sections. Click **Next** to continue.

![json](./images/module2-wlans/dnac-menu-provision-inventory-stage4.png?raw=true "Import JSON")

9. On screen 5 of the **Inventory > Provision Devices** workflow we see a *Summary* of what will be configured. Please take time to review this section. Click **Deploy** to continue.

![json](./images/module2-wlans/dnac-menu-provision-inventory-stage5.png?raw=true "Import JSON")

10. A warning message about **Fastlane Configuration** is displayed to warn about wireless disruptions. Click **OK** to continue.

![json](./images/module2-wlans/dnac-menu-provision-inventory-stage5-deploy.png?raw=true "Import JSON")

11. A *Provision Device* Sidemenu appears, giving 3 options abut when to deploy. Choose the **3rd option** allows for you to review the configuration prior to deployment.. Click **Apply** to continue.

![json](./images/module2-wlans/dnac-menu-provision-inventory-stage5-generate.png?raw=true "Import JSON")

#### Step 2 - ***Deploying the Configuration for the Wireless Controller***
1. From **DNA Centers** hamburger menu icon, open the menu and select `Activities`.

![json](./images/module2-wlans/dnac-navigation-activities.png?raw=true "Import JSON")

2. On the *Activites* page select the **Work Items** tab. You will notice the work item *Provision Device - Configuration Preview* on the page. It will probably say in progress. Wait for it to say *success* before proceding.

![json](./images/module2-wlans/dnac-activities-psk-preview.png?raw=true "Import JSON")

3. When the work item *Provision Device - Configuration Preview* status displays *success* click the link to display the configuration.

![json](./images/module2-wlans/dnac-activities-psk-click.png?raw=true "Import JSON")

4. The Wireless Controller configuration will be displayed. Click **Deploy** to continue deploying the configuration.

![json](./images/module2-wlans/dnac-activities-psk-display.png?raw=true "Import JSON")

5. To continue to deploy the Wireless Controller configuration select **Now** and then click **Apply**.

![json](./images/module2-wlans/dnac-activities-psk-now.png?raw=true "Import JSON")

. A popup to ask if you want to delete the work item will appear, click **No** to keep a record of events.

![json](./images/module2-wlans/dnac-activities-psk-nodelete.png?raw=true "Import JSON")

#### Step 3 - ***Checking for successful configuration of the Wireless Controller***
1. Navigate back to the *Inventory*, and change the *Inventory Focus* to **Provision** to watch the progress of the provisioning.

![json](./images/module2-wlans/dnac-inventory-psk-focus-provision.png?raw=true "Import JSON")

2. When the *Provisioning Status* of the *C9800-WLC* shows as success, click **see details** to look at the logs.

![json](./images/module2-wlans/dnac-inventory-psk-seedetails.png?raw=true "Import JSON")

3. Click to display the logs and examine the output as much as possible.

![json](./images/module2-wlans/dnac-inventory-psk-success.png?raw=true "Import JSON")

## Summary
At this point you will have successfully configured the **Wireless Controller** from **DNA Center**. During this lab we configured SSID's, Wireless Network Profiles, RF Profiles, FlexConnect VLANs and deployed the configuration. The next step is **Access Point** provisioning.

## Lab Modules
The lab will be split into modules to concentrate on specific tasks. Eash is designed to build your knowledge in specific areas and they will call out any dependancies on previous modules. We will cover are the following which you can access via the links below:

1. [**Wireless Controller PnP or Discovery**](./module1-ctrlpnpdiscovery.md)
2. [**WLAN Creation**](./module2-wlans.md)
3. [**Controller HA**](./module3-controllerha.md)
4. [**AP Provisioning**](./module4-approvisioning.md)
5. [**Application QoS**](./module5-applicationqos.md)
6. [**Model Based Config**](./module6-modelbasedconfig.md)
7. [**Wireless Templates**](./module7-wirelesstemplates.md)

## Main Menus
To return to the main menus
1. [Wireless Automation Main Menu](./README.md)
2. [DNAC-TEMPLATES-LABS Main Menu](../README.md)
3. [DNAC-TEMPLATES Repository Main Menu](../../README.md)

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.
