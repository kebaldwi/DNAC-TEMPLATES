# Wireless Lab Preparation
## Lab Section 1 - DNA Center and ISE Integration
In this lab our focus changes slightly as we start to automate for host onboarding. A large component of host onboarding is the authentication of hosts and assignment within the network. In this section and in preparation for the steps which follow we will integrate DNA Center with Identity Services Engine. This integration allows pxGrid communication between the two and allows for automation of configuration within ISE for Network Access Devices, SGT, SGACL, and Policys.

### Step 1 - ***Prepare ISE for DNA Center Integration***
1. Open a web browser on the Windows Workstation Jump host. Open a connection to Identity Services Engine (ISE) and select the hamburger menu icon to open the system menu.

![json](./images/ise-dashboard.png?raw=true "Import JSON")

2. From the system menu under Administration select PxGrid Settings

![json](./images/ise-menu.png?raw=true "Import JSON")

3. On the PxGrid Settings page select both of the available options and click Save to allow DNA Center to integrate.

![json](./images/ise-pxgrid-settings.png?raw=true "Import JSON")
![json](./images/ise-pxgrid-setup.png?raw=true "Import JSON")

### Step 2 - ***DNA Center and ISE Integration***
1. Open a web browser on the Windows Workstation Jump host. Open a connection to Dna Center and select the hamburger menu icon and navigate to the System > Settings menu item.

![json](./images/dnac-system-settings.png?raw=true "Import JSON")

2. Within the System Settings page navigate down the list on the left and select the Authentication and Policy Server section.

![json](./images/dnac-system-settings-aaa.png?raw=true "Import JSON")

3. On the page select from the dropdown ISE to configure ISE integration.

![json](./images/dnac-system-settings-aaa-ise.png?raw=true "Import JSON")

4. Enter the information as seen on the page and click save.

![json](./images/dnac-system-settings-aaa-ise-config.png?raw=true "Import JSON")

5. A popup will appear as the ISE node is using an untrusted SelfSigned Certificate. For lab purposes Accept the certificate, this may appear a couple of times as shown.

![json](./images/dnac-system-settings-aaa-ise-trust.png?raw=true "Import JSON")

6. You will see the the various stages of integration proceed and finally a success message as shown below.

![json](./images/dnac-system-settings-aaa-ise-done.png?raw=true "Import JSON")
![json](./images/dnac-system-settings-aaa-ise-complete.png?raw=true "Import JSON")

## Lab Section 2 - DHCP & DNS Service Preparation
In this section we will prepare Domain Name System (DNS) and Dynamic Host Configuration Protocol (DHCP) on the Windows Server for the lab environment. The reasons for the configurations made here are detailed heavily in Lab 2 titled [Onboarding Templates](https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB2-Onboarding-Template/)

### Step 1 - ***Configuring DHCP and DNS via Powershell***
1. Download the powershell script to the ***windows server*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB10-Wireless-Automation/scripts/powershell.ps1">⬇︎powershell.ps1⬇︎</a> file.
2. Once downloaded, extract the file.
   ![json](./images/Powershell-Extract.png?raw=true "Import JSON")
   ![json](./images/Powershell-Extract-Location.png?raw=true "Import JSON")
3. Right click on the file and run with powershell.
   ![json](./images/Powershell-Run.png?raw=true "Import JSON")
4. You may see a security warning. If you do accept it by entering **Y**.
   ![json](./images/Powershell-Security.png?raw=true "Import JSON")
At this point all the DNS and DHCP configuration on the ***windows server*** will be generated.
   ![json](./images/DNS-DHCP.png?raw=true "Import JSON")

## Lab Section 3 - DNA Center Design Preparation
We will now prepare DNA Center and onboard the devices in preparation for use in the lab. The reasons for the configurations made here are detailed heavily in previous Labs within the series. While we could deploy more extensive settings for deployment, we will limit the configuration to the minimum necessary to create a working lab in which to facilitate wireless automation.

### Step 1 - ***Import Postman Collection***
1. Download and import the collection within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB10-Wireless-Automation/postman/DCLOUD_DNACTemplatesLab_Workflow.postman_collection.json">⬇︎DCLOUD_DNACTemplateLab_Workflow.postman_collection.json⬇︎</a> file.
2. Extract the file to the desktop using **Winrar** to expand them
3. Open the **postman** application from the desktop. Once the application is open select *Collections* then click the *Import* link. 
![json](./images/Postman-Pre-Collection-Import.png?raw=true "Import JSON")
4. A window should appear on the file upload page. Click the upload button and select desktop from the windows explorer. Select the file named `DCLOUD_DNACTemplatesLab_Workflow.postman_collection.json` and click open. 
![json](./images/Postman-Collection-Select.png?raw=true "Import JSON")
5. Then click import and the collection should be loaded into the collections as shown.
![json](./images/Postman-Post-Collection-Import.png?raw=true "Import JSON")

### Step 2 - ***Import Postman Environment***
1. Download and import the environment within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB10-Wireless-Automation/postman/DCLOUD_DNACTemplateLabs.postman_environment.json">⬇︎DCLOUD_DNACTemplateLabs.postman_environment.json⬇︎</a> file.
2. Extract the file to the desktop using **Winrar** to expand them
3. If not open, open the **postman** application from the desktop. Once the application is open select *Environments* and then the *Import* link. 
![json](./images/Postman-Pre-Environment-Import.png?raw=true "Import JSON")
4. A window should appear on the file upload page. Click the upload button and select desktop from the windows explorer. Select the file named `DCLOUD_DNACTemplateLabs.postman_environment.json` and click open. 
![json](./images/Postman-Environment-Select.png?raw=true "Import JSON")
5. Then click import and the environment should be loaded into the environments as shown. 
![json](./images/Postman-Post-Environment-Import.png?raw=true "Import JSON")
6. Next we will choose the environment by clicking the checkmark on the right of Environment in postman as shown here. 
![json](./images/Postman-Environment-Selection.png?raw=true "Import JSON")

### Step 3 - ***Turn off SSL validation for LAB purposes within Postman***
1. Turn off SSL verification for lab purposes in the settings of Postman by click the **Gear** icon to select **settings** and **deselect** `SSL certificate verification` and then close the settings window. 
![json](./images/Postman-SSL-Deselect.png?raw=true "Import JSON")
2. With these steps completed we are prepared to start the walk through of the sections below.

### Step 4 - ***Run the Collection within Postman***
This collection is built with a flow and delay timers wait for the collection to finish entirely.
1. If not open, open the **postman** application from the desktop. Once the application is open select *Collections* and then the '...' link and select **run collection**. </br>
![json](./images/Postman-CollectionRunner.png?raw=true "Import JSON")
2. On the right ensure all API are selected and click run collection. 
![json](./images/Postman-CollectionRunner-Run.png?raw=true "Import JSON")
3. After the entire collection has run you will see all of them listed on the left as shown, and two buttons on the top right, one for results and the other to run again.
![json](./images/Postman-CollectionRunner-Results.png?raw=true "Import JSON")
4. Within DNA Center you should see 3 devices within the inventory and additionally you should observe a complete hierarchy as well as settings and telemetry configured. The Devices will be discovered in the Building level at this stage.
![json](./images/Postman-Discovery.png?raw=true "Import JSON")
![json](./images/Postman-Settings.png?raw=true "Import JSON")

## Summary
The lab is now prepared for the Wireless Automation modules of the lab. Please navigate to **Controller PnP or Discovery** to get started.

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
