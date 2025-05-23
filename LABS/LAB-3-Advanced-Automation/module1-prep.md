# Lab Preparation - In Development

![json](../../ASSETS/COMMON/BUILD/underconstruction.png?raw=true "Import JSON")

> [!WARNING]
> The contents of this lab are not ready for public use. Do not use this lab or attempt to use it until this header is removed entirely from the lab.

Within this section we will prepare the DCLOUD lab for use with the tasks contained in this lab. 

Prior to starting the work in this lab please ensure you have checked the [LAB Readiness](../DCLOUD.md#dcloud-lab-readiness-checks-and-troubleshooting) to ensure that the LAB automation has stood it up properly for you.

## Lab Section 1 - Catalyst Center and ISE Integration

In this lab our focus changes slightly as we start to automate for host onboarding. A large component of host onboarding is the authentication of hosts and assignment within the network. In this section and in preparation for the steps which follow we will integrate Catalyst Center with Identity Services Engine. This integration allows pxGrid communication between the two and allows for automation of configuration within ISE for Network Access Devices, SGT, SGACL, and Policys.

### Lab Topology

The lab envionment that we will be building is depicted here:

For routing in the environment an OSPF IGP process has been created to propogate internal route information. Within the access switches which are connected at Layer 3 to the router, we have estansiated a layer 2 port channel between them and initiated various vlans for Access Point connectivity and for the clients, whose gateway is built on an HSRP instance shared between the two switches.

The 9130AX Access Points are connected to both access switches and the ports are automatically configured via the AUTOCONF feature.

![json](../../ASSETS/COMMON/DCLOUD/DCLOUD_Topology3.png?raw=true "Import JSON")

### Lab Credentials:

| Platform:       | IP Address:    | Username | Password   | 
|-----------------|----------------|----------|------------|
| Catalyst Center | 198.18.129.100 | admin    | C1sco12345 |
| ISE             | 198.18.133.27  | admin    | C1sco12345 |
| Windows AD      | 198.18.133.1   | admin    | C1sco12345 |
| Script Server   | 198.18.133.28  | root     | C1sco12345 |
| 9800-1          | 198.19.11.2    | admin    | C1sco12345 |
| 9800-2          | 198.19.11.3    | admin    | C1sco12345 |
| Router          | 198.18.133.145 | netadmin | C1sco12345 |
| C 9300 1        | 198.18.128.22  | netadmin | C1sco12345 |
| C 9300 2        | 198.18.128.23  | netadmin | C1sco12345 |
| AP-1            | DHCP Assigned  | Cisco    | Cisco      |
| AP-2            | DHCP Assigned  | Cisco    | Cisco      |

### Step 1 - ***Prepare ISE for Catalyst Center Integration***

1. Open a web browser on the Windows Workstation Jump host. Open a connection to Identity Services Engine (ISE) and select the hamburger menu icon to open the system menu.

   ![json](../../ASSETS/LABS/ISE/ise-dashboard.png?raw=true "Import JSON")

2. From the system menu under Administration select PxGrid Settings

   ![json](../../ASSETS/LABS/ISE/ise-menu-pxgrid.png?raw=true "Import JSON")

3. On the PxGrid Settings page select both of the available options and click Save to allow Catalyst Center to integrate.

   ![json](../../ASSETS/LABS/ISE/ise-pxgrid-settings.png?raw=true "Import JSON")
   ![json](../../ASSETS/LABS/ISE/ise-pxgrid-setup.png?raw=true "Import JSON")

### Step 2 - ***Catalyst Center and ISE Integration***

1. Open a web browser on the Windows Workstation Jump host. Open a connection to Catalyst Center and select the hamburger menu icon and navigate to the System > Settings menu item.

   ![json](../../ASSETS/LABS/CATC/catc-menu-systemsettings.png?raw=true "Import JSON")

2. Within the System Settings page navigate down the list on the left and select the Authentication and Policy Server section.

   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-aaa.png?raw=true "Import JSON")

3. On the page select from the dropdown ISE to configure ISE integration.

   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-ise.png?raw=true "Import JSON")

4. Enter the information as seen on the page and click save.

   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-ise-config.png?raw=true "Import JSON")

5. A popup will appear as the ISE node is using an untrusted SelfSigned Certificate. For lab purposes Accept the certificate, this may appear a couple of times as shown.

   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-ise-trust.png?raw=true "Import JSON")

6. You will see the the various stages of integration proceed and finally a success message as shown below.

   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-ise-done.png?raw=true "Import JSON")
   ![json](../../ASSETS/LABS/CATC/catc-systemsettings-ise-complete.png?raw=true "Import JSON")

## Lab Section 2 - DHCP & DNS Service Preparation

In this section we will prepare Domain Name System (DNS) and Dynamic Host Configuration Protocol (DHCP) on the Windows Server for the lab environment. The reasons for the configurations made here are detailed heavily in Lab 1 titled [LAB1-Wired-Automation](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-1-Wired-Automation/module1-pnpprep.md)

### Step 1 - ***Configuring DHCP and DNS via Powershell***

1. Download the powershell script to the ***windows server*** using the <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/POWERSHELL/powershell.ps1">⬇︎powershell.ps1⬇︎</a> file.
2. Once downloaded, locate the file in the download folder.
3. Right click on the file and run with powershell.

   ![json](../../ASSETS/LABS/AD/Powershell-Run.png?raw=true "Import JSON")

4. You may see a security warning. If you do accept it by entering **Y**.

   ![json](../../ASSETS/LABS/AD/Powershell-Security.png?raw=true "Import JSON")

At this point all the DNS and DHCP configuration on the ***windows server*** will be generated.

   ![json](../../ASSETS/LABS/AD/DNS-DHCP.png?raw=true "Import JSON")

## Lab Section 3 - Catalyst Center Design Preparation

We will now prepare Catalyst Center and onboard the devices in preparation for use in the lab. The reasons for the configurations made here are detailed heavily in previous Labs within the series. While we could deploy more extensive settings for deployment, we will limit the configuration to the minimum necessary to create a working lab in which to facilitate advanced automation lab.

### Step 1 - ***Import Postman Collection and Environment***

1. Download the **collection** and **environment** from the following links:

   <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/POSTMAN/lab-3-advanced-auto-postman-collection.json">⬇︎lab-3-advanced-auto-postman-collection.json⬇︎</a></br>
   <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/POSTMAN/lab-3-advanced-auto-postman-environment.json">⬇︎lab-3-advanced-auto-postman-environment.json⬇︎</a>

2. Locate the file in the download folder.
3. Open the **postman** application from the desktop. Once the application is open select *Collections* then click the *Import* link. 

   ![json](../../ASSETS/LABS/POSTMAN/LAB3/Postman-Pre-Collection-Import.png?raw=true "Import JSON")

4. A window should appear on the file upload page. Click the upload button and select desktop from the windows explorer. Select the files named `lab-2-wireless-auto-postman-collection.json`, and `lab-2-wireless-auto-postman-environment.json` then click open. 

   ![json](../../ASSETS/LABS/POSTMAN/LAB3/Postman-Collection-Select.png?raw=true "Import JSON")

5. Then click import and the collection and environment should be loaded into the postman as shown.

   ![json](../../ASSETS/LABS/POSTMAN/LAB3/Postman-Post-Collection-Import.png?raw=true "Import JSON")

6. Next we will choose the environment by clicking the checkmark on the right of Environment in postman as shown here. 

   ![json](../../ASSETS/LABS/POSTMAN/LAB3/Postman-Environment-Selection.png?raw=true "Import JSON")

### Step 2 - ***Turn off SSL validation for LAB purposes within Postman***

1. Turn off SSL verification for lab purposes in the settings of Postman by click the **Gear** icon to select **settings** and **deselect** `SSL certificate verification` and then close the settings window. 

   ![json](../../ASSETS/LABS/POSTMAN/COMMON/Postman-SSL-Deselect.png?raw=true "Import JSON")

2. With these steps completed we are prepared to start the walk through of the sections below.

### Step 3 - ***Run the Collection within Postman***

This collection is built with a flow and delay timers wait for the collection to finish entirely.

1. If not open, open the **postman** application from the desktop. Once the application is open select *Collections* and then the '...' link and select **run collection**. </br>

   ![json](../../ASSETS/LABS/POSTMAN/LAB3/Postman-CollectionRunner.png?raw=true "Import JSON")

2. On the right ensure all API are selected and click run collection. 

   ![json](../../ASSETS/LABS/POSTMAN/LAB3/Postman-CollectionRunner-Run.png?raw=true "Import JSON")

3. After the entire collection has run you will see all of them listed on the left as shown, and two buttons on the top right, one for results and the other to run again.

   ![json](../../ASSETS/LABS/POSTMAN/LAB3/Postman-CollectionRunner-Results.png?raw=true "Import JSON")

4. Within Catalyst Center you should see 2 devices within the inventory and additionally you should observe a complete hierarchy as well as settings and telemetry configured. The Devices will be discovered in the Building level at this stage.

   ![json](../../ASSETS/LABS/POSTMAN/LAB3/Postman-Inventory.png?raw=true "Import JSON")
   ![json](../../ASSETS/LABS/POSTMAN/LAB3/Postman-Settings.png?raw=true "Import JSON")

   Lastly, you will find in the PnP Section a switch ready for claiming.

   ![json](../../ASSETS/LABS/POSTMAN/LAB3/Postman-PnP.png?raw=true "Import JSON")


## Summary

The lab is now prepared for the Advanced Automation modules of the lab. Please navigate to **Onboarding Templates** to get started.

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Onboarding Templates Module**](../LAB-3-Advanced-Automation/module2-day0-template.md)

> [**Return to Lab Menu**](./README.md)
