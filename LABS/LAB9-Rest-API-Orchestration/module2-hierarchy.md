# Module 2 - Building Hierarchy
In this module, we will use *Postman* to build and deploy a hierarchy within DNA Center. DNA Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network.

## Hierarchy Background
The Design area is where you create the structure and framework of your network, including the logical topology, network settings, and device type profiles that you can apply to devices throughout your network.

You can create a network hierarchy that represents your network's geographical locations. Your network hierarchy can contain sites, which in turn contain buildings and areas. You can create sites and buildings to easily identify where to apply design settings or configurations later. By default, there is one site called Global.

The network hierarchy has a predetermined hierarchy:

**Areas** or **Sites** do not have a physical address, such as the United States. You can think of areas as the largest element. Areas can contain buildings and subareas. For example, an area named `United States` can contain a California subarea, and the subarea California can contain a San Jose subarea.

**Buildings** have a physical address and contain floors and floor plans. When you create a building, you must specify a physical address or latitude and longitude coordinates. Buildings cannot contain areas. By creating buildings, you can apply settings to a specific location.

**Floors** are within buildings and consist of cubicles, walled offices, wiring closets, and so on. You can add floors only to buildings.

## Lab Preparation
### DNA Center and ISE Integration
In this lab, our focus changes slightly as we start to automate host onboarding. A large component of host onboarding is the authentication of hosts and assignments within the network. In this section, and in preparation for the steps which follow, we will integrate DNA Center with Identity Services Engine. This integration allows pxGrid communication between the DNA Center and ISE. For this reason, the PxGrid personal does need to be enabled on at least 1 ISE Node within an ISE Cluster. This has already been completed in the sandbox. PxGrid integration between the DNA Center and ISE allows configuration automation from DNA Center within ISE for Network Access Devices, SGT creation, and SGACL builds via Contracts and Policy.

#### Step 1 - ***Prepare ISE for DNA Center Integration***
1. Open a web browser on the Windows Workstation Jump host. Open a connection to Identity Services Engine (ISE) and select the hamburger menu icon to open the system menu.

![json](./images/ise-dashboard.png?raw=true "Import JSON")

2. From the system menu under Administration, select PxGrid Settings

![json](./images/ise-menu.png?raw=true "Import JSON")

3. On the PxGrid Settings page, select both options and click Save to allow DNA Center to integrate.

![json](./images/ise-pxgrid-settings.png?raw=true "Import JSON")
![json](./images/ise-pxgrid-setup.png?raw=true "Import JSON")

#### Step 2 - ***DNA Center and ISE Integration***
1. Open a web browser on the Windows Workstation Jump host. Open a connection to DNA Center, select the hamburger menu icon, and navigate to the System > Settings menu item.

![json](./images/dnac-system-settings.png?raw=true "Import JSON")

2. Within the System Settings page, navigate down the list on the left and select the Authentication and Policy Server section.

![json](./images/dnac-system-settings-aaa.png?raw=true "Import JSON")

3. On the page, select from the dropdown ISE to configure ISE integration.

![json](./images/dnac-system-settings-aaa-ise.png?raw=true "Import JSON")

4. Enter the information as seen on the page and click save.

![json](./images/dnac-system-settings-aaa-ise-config.png?raw=true "Import JSON")

5. A popup will appear as the ISE node uses an untrusted SelfSigned Certificate. For lab purposes, accept the certificate; this may appear a couple of times, as shown.

![json](./images/dnac-system-settings-aaa-ise-trust.png?raw=true "Import JSON")

6. You will see the various stages of integration proceed and, finally, a success message as shown below.

![json](./images/dnac-system-settings-aaa-ise-done.png?raw=true "Import JSON")
![json](./images/dnac-system-settings-aaa-ise-complete.png?raw=true "Import JSON")

## Building Hierarchy
### Objectives
- Authenticate and retrieve a token from Cisco DNA Center.
- Build an **Area**, **Building**, and **Floor** in the Hierarchy.

### Prerequisites
The prerequisite steps for preparing for the lab are the following;
1. Download and install the [AnyConnect client](./README.md#tools-required)
2. Download and install [Postman](./README.md#tools-required)
3. Import and set up [Postman](./module1-postman.md)

### CSV Data Source
Within Postman, we will utilize the collection `Build Hierarchy` to build out the Hierarchy of DNA Center into which we associate settings and discover devices. This Collection may be run whenever you wish to create a new section of the Hierarchy to add additional Areas, Buildings, or floors. 

Accompanying the Collection is a required Comma Separated Value (CSV) file, which is essentially an answer file for the values used to build the design. The CSV may be found here. 

<a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB9-Rest-API-Orchestration/csv/DNAC-Design-Settings.csv" target="_blank">⬇︎DNA Center Design Settings CSV⬇︎</a>

We will **open** but **not save** the CSV file to view the hierarchy that will be built during the lab. You will see each row has hierarchal information, settings, credentials, and other information. **Be Careful NOT to modify the file**; if you feel you have modified the file, please download it again.

<p align="center"><img src="./images/csv.png" width="800" height="385"></p>

The hierarchy the CSV will build will be this:

```text
Global > State
Global > State > California > Building10 > Floor1
Global > State > California > Building10 > Floor2
Global > State > California > Building10 > Floor3
Global > State > NorthCarolina > Building3 > Floor1
Global > State > NorthCarolina > Building3 > Floor2
Global > State > Texas > Building1 > Floor1
```

### Hierarchy Build and the Postman Collection Run
Postman is a powerful tool for editing and creating Rest-API calls and allows us to utilize several features to accomplish everyday tasks. In this short tutorial, we will use a simple Rest-API set, which has been grouped into a Postman Collection.

#### Collections
Collections are groupings of API, which allow us to have flows for specifically defined tasks. 

To investigate the collections we have built, follow these steps:

1. Navigate and open the Collection through the following steps:
   1. Within Postman, click on the Collection shortcut in the sidebar
   2. Expand the collection `DNA Center API LAP 100 - Build Hierarchy` by clicking the arrow.
   3. The tab with the API within the collection will appear to the right
   4. You can view the configuration of the API through these tabs. As a quick reference, a green dot appears wherever configuration is applied.
      ![json](./images/Postman-Collection-Token-Begin.png?raw=true "Import JSON")
2. Within the API, you will notice the following:
   1. The method **POST** is used for this API
   2. The URL *https://***{{DNACip}}***/dna/system/api/v1/auth/token* where the Environmental variable **{{DNACip}}** holds the actual IP. Hover briefly over the variable to display the current data.
   3. Click the `Authorization` tab to display the Authorization parameters
   4. Here, we see that this API is using Basic Auth to get a TOKEN
   5. Two environmental variables **{{DNACuser}}** and **{{DNACpwd}}** are used and can be viewed by hovering over the variables presented. The values are pulled from the environment variables.
      ![json](./images/Postman-Collection-Token-Auth.png?raw=true "Import JSON")
3. Within the API, we will investigate the Headers through the following:
   1. Click the `Headers` tab to display the Header parameters:
   2. The API is using the **Content-Type** `application/json`
      ![json](./images/Postman-Collection-Token-Header.png?raw=true "Import JSON")
4. Within the API, we will investigate the Tests through the following:
   1. Click the `Tests` tab to to display the Test parameters:
   ![json](./images/Postman-Collection-Token-Test.png?raw=true "Import JSON")
   2. The API has the following defined:

      ``` js
       1.     var jsonData = JSON.parse(responseBody);
       2.     if (jsonData.Token) {
       3.       pm.test("Token acquired",() => {pm.expect(pm.response.text()).to.include("Token");});
       4.       postman.setEnvironmentVariable("TOKEN", jsonData["Token"]); 
       5.     }
       6.     else {
       7.       pm.test("Token not acquired",() => {pm.expect(pm.response.text()).to.include("Token");});
       8.       postman.setNextRequest("null");
       9.     }
       10.    postman.setNextRequest("Get SiteIDs PreCheck")
      ```

         As we double click here, we see the line associating the response from the API and    loading it into a variable jsonDATA in line 1.
         
         In line 2, we begin a conditional if statement to determine if the JSON response    contains a field called Token with a token in it.
         
         Within the if condition in line 4, we load the Token from the field within the    JSON response into the environmental variable.
         
         We culminate the section by calling for the next API within the collection.

## Hierarchy Build Collection Run
We will now build the Hierarchy using the CSV variables previously discussed.

Follow these steps:

1. Navigate and open the desired collection runner through the following:
   1. Within Postman, click on the collection shortcut in the sidebar
   2. Hover over the collection `DNA Center API LAP 100 - Build Hierarchy`
   3. Click the `Run Collection` submenu option
      ![json](./images/Postman-Collection-Hierarchy.png?raw=true "Import JSON")
2. To run the collection, do the following:
   1. Ensure all the sub-components of the `Runner` are selected
   2. On the right under data, click *select* 
   3. Browse and select the CSV using explorer
   4. Click Open to select the file to be used
      ![json](./images/Postman-Collection-Hierarchy-Run-CSV.png?raw=true "Import JSON")
   5. Click  the `Run DNA Center API LAP 100 - Build Hierarchy` button
      ![json](./images/Postman-Collection-Hierarchy-Runner.png?raw=true "Import JSON")
3. Select `View Results` to view the following summary, which will slowly appear as the collection is processed. Notice APIs are only run when they are required. You may view the pre and post-script logic that causes this behavior. Each iteration is a row of the CSV being processed.
   ![json](./images/Postman-Collection-Hierarchy-Summary.png?raw=true "Import JSON")

## Verifying Hierarchy Build
To verify that the Hierarchy was built successfully, we will inspect the site in DNA Center.

Follow these steps:

1. Open a browser and navigate to `https://198.18.129.100`, where an SSL Error is displayed as depicted. Click the `Proceed to https://192.18.129.100 (unsafe)` link to continue
![json](./images/DNAC-SSLERROR.png?raw=true "Import JSON")
2. Log into DNA Center using the username of `admin` and the password `C1sco12345`.
![json](./images/DNAC-Login.png?raw=true "Import JSON")
3. When the DNA Center Dashboard is displayed, Click the  icon to display the menu'
![json](./images/DNAC-Menu.png?raw=true "Import JSON")
4. Select `Design>Network Hierarchy` from the menu to continue.
![json](./images/DNAC-Menu-Hierarchy.png?raw=true "Import JSON")
5. Expand the Hierarchy on the left to show your specific `Area`
![json](./images/DNAC-Hierarchy-Verify.png?raw=true "Import JSON")

## Summary
At this point, we have built the Hierarchy utilizing environment variables and REST-API's within the collection runner. To continue your learning, look at the various REST-API's used to complete this task. Notice that there was a task to create a **{{Token}}** for authentication, which was used and proceeded with the calls to create the Area, Building, and Floor. Each layer of the hierarchy was a singular call. 

Additionally, if there is time, look at the pre and post-scripts.

To continue your learning experience, continue to the next module in the series, which is module 3 below.

## Lab Modules
The use cases we will cover are the following which you can access via the links below:

1. [**Postman Orientation**](./module1-postman.md)
2. [**Building Hierarchy**](./module2-hierarchy.md)
3. [**Assign Settings and Credentials**](./module3-settings.md)
4. [**Device Discovery**](./module4-discovery.md)
5. [**Template Deployment**](./module5-templates.md)
6. [**Configuration Archive**](./module6-archive.md)
7. [**Retrieving Network Inventory**](./module7-inventory.md)
8. [**Running Show Commands**](./module8-commands.md)

## Main Menus
To return to the main menus
1. [Rest-API Orchestration Main Menu](./README.md)
2. [DNAC-TEMPLATES-LABS Main Menu](../README.md)
3. [DNAC-TEMPLATES Repository Main Menu](.../README.md)

## Feedback
If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.