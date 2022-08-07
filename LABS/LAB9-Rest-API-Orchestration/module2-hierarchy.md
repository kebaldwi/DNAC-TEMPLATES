# Module 2 - Building Hierarchy
In this module we will use *Postman* to build and deploy a hierarchy within DNA Center. DNA Center uses hierarchy to align infrastructure needs logically against intent. This allows the network administrator to align change requests and outage windows to allow for changes and modifications to the network.

## Hierarchy Background
The Design area is where you create the structure and framework of your network, including the logical topology, network settings, and device type profiles that you can apply to devices throughout your network.

You can create a network hierarchy that represents your network's geographical locations. Your network hierarchy can contain sites, which in turn contain buildings and areas. You can create site and building IDs to easily identify where to apply design settings or configurations later. By default, there is one site called Global.

The network hierarchy has a predetermined hierarchy:

**Areas** or **Sites** do not have a physical address, such as the United States. You can think of areas as the largest element. Areas can contain buildings and subareas. For example, an area called United States can contain a subarea called California, and the subarea California can contain a subarea called San Jose.

**Buildings** have a physical address and contain floors and floor plans. When you create a building, you must specify a physical address and latitude and longitude coordinates. Buildings cannot contain areas. By creating buildings, you can apply settings to a specific area.

**Floors** are within buildings and consist of cubicles, walled offices, wiring closets, and so on. You can add floors only to buildings.

## Objectives
- Authenticate and retrieve a token from Cisco DNA Center.
- Build an **Area**, **Building** and **Floor** in the Hierarchy.

## Prerequisites
The prerequisites steps for preparing for the lab are the following;
1. Download and install the [AnyConnect client](./README.md#tools-required)
2. Download and install [Postman](./README.md#tools-required)
3. Import and set up [Postman](./module1-postman.md)

## Building Hierarchy
Within Postman we will utilize the collection `Build Hierarchy` to build out the Hierarchy of DNA Center in which to associate settings and discover devices. This Collection may be run whenever you wish to create a new section of the Hierarchy to either add additional Areas, Buildings, or floors. 

Accompanying the Collection is a required Comma Separated Value (CSV) file which is essentially an answer file for the values used to build the design. The CSV may be found here. 

<a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB9-Rest-API-Orchestration/csv/DNAC-Design-Settings.csv" target="_blank">⬇︎DNA Center Design Settings CSV⬇︎</a>

## Hierarchy Build and the Postman Collection Runner
Postman being a powerful tool for editing and creating Rest-API calls, allows us to utilize a number of features to accomplish every day tasks. In this short tutorial, we will use a simple set of Rest-API which have been grouped into a Postman Collection.

### Collections
Collections are groupings of API, which allow us to have flows for specific defined tasks. 

To investigate the collections we have built follow these steps:

1. Navigate and open the Collection through the following steps:
   1. Within Postman click on the Collection shortcut in the sidebar
   2. Expand the collection `DNA Center API LAP 100 - Build Hierarchy` by clicking the arrow.
   3. The tab with the API within the collection will appear to the right
   4. You can view the configuration of the API through these tabs. As a quick reference a green dot appears wherever configuration is applied.
      ![json](./images/Postman-Collection-Token-Begin.png?raw=true "Import JSON")
2. Within the API you will notice the following:
   1. The method **POST** is used for this API
   2. The URL *https://***{{DNACip}}***/dna/system/api/v1/auth/token* where the Environmental variable **{{DNACip}}** holds the actual IP. Hover briefly over the variable to display the current data.
   3. Click the `Authorization` tab to to display the Authorization parameters
   4. Here we see that this API is using Basic Auth to get a TOKEN
   5. Two environmental variables **{{DNACuser}}** and **{{DNACpwd}}** are used and can be viewed by hovering over the variables presented. The values are pulled from the environment variables.
      ![json](./images/Postman-Collection-Token-Auth.png?raw=true "Import JSON")
3. Within the API we will investigate the Headers through the following:
   1. Click the `Headers` tab to to display the Header parameters:
   2. The API is using the **Content-Type** `application/json`
      ![json](./images/Postman-Collection-Token-Header.png?raw=true "Import JSON")
4. Within the API we will investigate the Tests through the following:
   1. Click the `Tests` tab to to display the Test parameters:
   ![json](./images/Postman-Collection-Token-Header.png?raw=true "Import JSON")
   2. The API has the following defined:

      ``` 
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

         As we double click here we see the line associating the response from the API and    loading it into a variable jsonDATA in line 1.
         
         In line 2 we begin an conditional if statement to determine if the JSON response    contains a field called Token with a token in it.
         
         Within the if condition in line 4 we load the Token from the field within the    JSON response into the environmentatl variable.
         
         We culminate the section by calling for the next API within the collection.

## Hierarchy Settings within the CSV
Wwe will **open** but **not save** the CSV file to view the hierarchy that will be built during the lab. You will see each row has hierarchal information as well as settings and credentials and other information. **Be Careful NOT to modify the file**, If you feel you have modified the file please download it again.

<p align="center"><img src="./images/csv.png" width="800" height="385"></p>

The hierarchy the CSV will build will be this:

```
Global > State
Global > State > California > Building10 > Floor1
Global > State > California > Building10 > Floor2
Global > State > California > Building10 > Floor3
Global > State > NorthCarolina > Building3 > Floor1
Global > State > NorthCarolina > Building3 > Floor2
Global > State > Texas > Building1 > Floor1
```

## Student Hierarchy Build
We will now build the Hierarchy using the environment variables modified in the previous step.

Follow these steps:

1. Navigate and open the desired collection runner through the following:
   1. Within Postman click on the collection shortcut in the sidebar
   2. Hover over the collection `DNE LAB 1.0 - Build Hierarchy Student`
   3. Click the `Run Collection` submenu option
      ![json](./images/Postman-Collection-Hierarchy.png?raw=true "Import JSON")
2. To run the collection do the following:
   1. Ensure all the sub-components of the `Runner` are selected
   2. Click  the `Run DNE LAB 1.0 - Build Hierarchy` button
      ![json](./images/Postman-Collection-Hierarchy-Runner.png?raw=true "Import JSON")
3. The following summary will slowly appear as the collection is processed
   ![json](./images/Postman-Collection-Hierarchy-Summary.png?raw=true "Import JSON")

## Verifying Student Hierarchy Build
To verify that the Hierarchy was built successfully we will inspect the site in DNA Center.

Follow these steps:

1. Open a browser and navigate to `https;//198.18.129.100` where you will see an SSL Error displayed as depicted. Click the `Proceed to https://192.18.129.100 (unsafe)` link to continue
![json](./images/DNAC-SSLERROR.png?raw=true "Import JSON")
2. Log into DNA Center using the username of `admin` and the password `C1sco12345`.
![json](./images/DNAC-Login.png?raw=true "Import JSON")
3. When the DNA Center Dashboard is displayed, Click the  icon to display the menu'
![json](./images/DNAC-Menu.png?raw=true "Import JSON")
4. Select `Design>Network Hierarchy` from the menu to continue.
![json](./images/DNAC-Menu-Hierarchy.png?raw=true "Import JSON")
5. Expand the Hierarchy on the left to show your specific `Area`
![json](./images/DNAC-Hierarchy-Student-Verify.png?raw=true "Import JSON")

## Summary
At this point we have built the Hierarchy utilizing environment variables and REST-API's within the collection runner. To continue your learning, lookk at the various REST-API utilized to complete this task. Notice that there was a task to create a **{{Token}}** for authentication which was used and prceeded the calls to create the Area, Building and Floor. Each layer of the hierarchy was a singular call. 

Additionally if there is time, look at the pre and post scripts.

