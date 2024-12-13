# Wireless Lab Preparation 

> **Note:** Not required if you completed Lab 1 - Wired Automation

Within this section we will prepare the DCLOUD lab for use with the Wireless tasks contained in this lab. If you have just completed the Wired Automation Lab, **DO NOT USE** this section and proceed with module 1 and start the Controller Onboarding. 

## Lab Section 1 - DNA Center and ISE Integration

In this lab our focus changes slightly as we start to automate for host onboarding. A large component of host onboarding is the authentication of hosts and assignment within the network. In this section and in preparation for the steps which follow we will integrate DNA Center with Identity Services Engine. This integration allows pxGrid communication between the two and allows for automation of configuration within ISE for Network Access Devices, SGT, SGACL, and Policys.

## Lab Credentials:

| Platform:       | IP Address:    | Username | Password   | 
|-----------------|----------------|----------|------------|
| Catalyst Center | 198.18.129.100 | admin    | C1sco12345 |
| ISE             | 198.18.133.27  | admin    | C1sco12345 |
| Windows AD      | 198.18.133.1   | admin    | C1sco12345 |
| Script Server   | 198.18.133.28  | root     | C1sco12345 |
| 9800-1          | 198.19.11.2    | admin    | C1sco12345 |
| 9800-2          | 198.19.11.3    | admin    | C1sco12345 |
| Router          | 198.18.133.145 | netadmin | C1sco12345 |
| Switch 1        | 198.18.128.22  | netadmin | C1sco12345 |
| Switch 2        | 198.18.128.23  | netadmin | C1sco12345 |
| AP-1            | DHCP Assigned  | Cisco    | Cisco      |
| AP-2            | DHCP Assigned  | Cisco    | Cisco      |

### Step 1 - ***Prepare ISE for DNA Center Integration***

1. Open a web browser on the Windows Workstation Jump host. Open a connection to Identity Services Engine (ISE) and select the hamburger menu icon to open the system menu.

   ![json](./images/module0-preparation/ise-dashboard.png?raw=true "Import JSON")

2. From the system menu under Administration select PxGrid Settings

   ![json](./images/module0-preparation/ise-menu.png?raw=true "Import JSON")

3. On the PxGrid Settings page select both of the available options and click Save to allow DNA Center to integrate.

   ![json](./images/module0-preparation/ise-pxgrid-settings.png?raw=true "Import JSON")
   ![json](./images/module0-preparation/ise-pxgrid-setup.png?raw=true "Import JSON")

### Step 2 - ***DNA Center and ISE Integration***

1. Open a web browser on the Windows Workstation Jump host. Open a connection to Dna Center and select the hamburger menu icon and navigate to the System > Settings menu item.

   ![json](./images/module0-preparation/dnac-system-settings.png?raw=true "Import JSON")

2. Within the System Settings page navigate down the list on the left and select the Authentication and Policy Server section.

   ![json](./images/module0-preparation/dnac-system-settings-aaa.png?raw=true "Import JSON")

3. On the page select from the dropdown ISE to configure ISE integration.

   ![json](./images/module0-preparation/dnac-system-settings-aaa-ise.png?raw=true "Import JSON")

4. Enter the information as seen on the page and click save.

   ![json](./images/module0-preparation/dnac-system-settings-aaa-ise-config.png?raw=true "Import JSON")

5. A popup will appear as the ISE node is using an untrusted SelfSigned Certificate. For lab purposes Accept the certificate, this may appear a couple of times as shown.

   ![json](./images/module0-preparation/dnac-system-settings-aaa-ise-trust.png?raw=true "Import JSON")

6. You will see the the various stages of integration proceed and finally a success message as shown below.

   ![json](./images/module0-preparation/dnac-system-settings-aaa-ise-done.png?raw=true "Import JSON")
   ![json](./images/module0-preparation/dnac-system-settings-aaa-ise-complete.png?raw=true "Import JSON")

## Lab Section 2 - DHCP & DNS Service Preparation

In this section we will prepare Domain Name System (DNS) and Dynamic Host Configuration Protocol (DHCP) on the Windows Server for the lab environment. The reasons for the configurations made here are detailed heavily in Lab B titled [Onboarding Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-B-Onboarding-Template/)

### Step 1 - ***Configuring DHCP and DNS via Powershell***

1. Download the powershell script to the ***windows server*** using the <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/POWERSHELL/powershell.ps1">⬇︎powershell.ps1⬇︎</a> file.
2. Once downloaded, extract the file.

   ![json](./images/module0-preparation/Powershell-Extract.png?raw=true "Import JSON")
   ![json](./images/module0-preparation/Powershell-Extract-Location.png?raw=true "Import JSON")

3. Right click on the file and run with powershell.

   ![json](./images/module0-preparation/Powershell-Run.png?raw=true "Import JSON")

4. You may see a security warning. If you do accept it by entering **Y**.

   ![json](./images/module0-preparation/Powershell-Security.png?raw=true "Import JSON")

At this point all the DNS and DHCP configuration on the ***windows server*** will be generated.

   ![json](./images/module0-preparation/DNS-DHCP.png?raw=true "Import JSON")

## Lab Section 3 - DNA Center Design Preparation

We will now prepare DNA Center and onboard the devices in preparation for use in the lab. The reasons for the configurations made here are detailed heavily in previous Labs within the series. While we could deploy more extensive settings for deployment, we will limit the configuration to the minimum necessary to create a working lab in which to facilitate wireless automation.

### Step 1 - ***Import Postman Collection***

1. Download and import the collection within the ***Postman*** using the <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/POSTMAN/lab-2-wireless-auto-postman-collection.json">⬇︎lab-2-wireless-auto-postman-collection.json⬇︎</a> file.
2. Extract the file to the desktop using **Winrar** to expand them
3. Open the **postman** application from the desktop. Once the application is open select *Collections* then click the *Import* link. 

   ![json](./images/module0-preparation/Postman-Pre-Collection-Import.png?raw=true "Import JSON")

4. A window should appear on the file upload page. Click the upload button and select desktop from the windows explorer. Select the file named `lab-2-wireless-auto-postman-collection.json` and click open. 

   ![json](./images/module0-preparation/Postman-Collection-Select.png?raw=true "Import JSON")

5. Then click import and the collection should be loaded into the collections as shown.

   ![json](./images/module0-preparation/Postman-Post-Collection-Import.png?raw=true "Import JSON")

### Step 2 - ***Import Postman Environment***

1. Download and import the environment within the ***Postman*** using the <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/POSTMAN/lab-2-wireless-auto-postman-environment.json">⬇︎lab-2-wireless-auto-postman-environment.json⬇︎</a> file.
2. Extract the file to the desktop using **Winrar** to expand them
3. If not open, open the **postman** application from the desktop. Once the application is open select *Environments* and then the *Import* link. 

   ![json](./images/module0-preparation/Postman-Pre-Environment-Import.png?raw=true "Import JSON")

4. A window should appear on the file upload page. Click the upload button and select desktop from the windows explorer. Select the file named 
`lab-2-wireless-auto-postman-environment.json` and click open. 

   ![json](./images/module0-preparation/Postman-Environment-Select.png?raw=true "Import JSON")

5. Then click import and the environment should be loaded into the environments as shown. 

   ![json](./images/module0-preparation/Postman-Post-Environment-Import.png?raw=true "Import JSON")

6. Next we will choose the environment by clicking the checkmark on the right of Environment in postman as shown here. 

   ![json](./images/module0-preparation/Postman-Environment-Selection.png?raw=true "Import JSON")

### Step 3 - ***Turn off SSL validation for LAB purposes within Postman***

1. Turn off SSL verification for lab purposes in the settings of Postman by click the **Gear** icon to select **settings** and **deselect** `SSL certificate verification` and then close the settings window. 

   ![json](./images/module0-preparation/Postman-SSL-Deselect.png?raw=true "Import JSON")

2. With these steps completed we are prepared to start the walk through of the sections below.

### Step 4 - ***Run the Collection within Postman***

This collection is built with a flow and delay timers wait for the collection to finish entirely.

1. If not open, open the **postman** application from the desktop. Once the application is open select *Collections* and then the '...' link and select **run collection**. </br>

   ![json](./images/module0-preparation/Postman-CollectionRunner.png?raw=true "Import JSON")

2. On the right ensure all API are selected and click run collection. 

   ![json](./images/module0-preparation/Postman-CollectionRunner-Run.png?raw=true "Import JSON")

3. After the entire collection has run you will see all of them listed on the left as shown, and two buttons on the top right, one for results and the other to run again.

   ![json](./images/module0-preparation/Postman-CollectionRunner-Results.png?raw=true "Import JSON")

4. Within DNA Center you should see 3 devices within the inventory and additionally you should observe a complete hierarchy as well as settings and telemetry configured. The Devices will be discovered in the Building level at this stage.

   ![json](./images/module0-preparation/Postman-Discovery.png?raw=true "Import JSON")
   ![json](./images/module0-preparation/Postman-Settings.png?raw=true "Import JSON")

## Summary

The lab is now prepared for the Wireless Automation modules of the lab. Please navigate to **Controller PnP or Discovery** to get started.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Continue to Wireless Controller Discovery Module**](../LAB-2-Wireless-Automation/module1-ctrlpnpdiscovery.md)

> [**Return to Lab Menu**](./README.md)
