# Use Case 1.1 - Building Hierarchy - lablet *[1](./section1-hierarchy-1.md)*
*[2](./section1-hierarchy-2.md)* **[3]**
Within Postman we will utilize the collection `Build Hierarchy Student` to build out the Hierarchy of DNA Center in which to associate settings and discover devices. This Collection may be run whenever you wish to create a new section of the Hierarchy to either add additional Areas, Buildings, or floors.

## Student Hierarchy Environment Modifications
To ensure you are working on all your changes and not interfering with others, we will modify the settings and Hierarchy to personalize it for your use within the lab. This step simulates what you would do to utilize the collection in the real world.

Follow these steps:

1. Navigate and open the desired environment and modify the variables indicated in the following steps:
   1. Within Postman click on the environment shortcut in the sidebar
   2. Clicking the environment `DNAC Template Labs Student`
      ![json](./images/Postman-Environment.png?raw=true "Import JSON")
2. Scroll down in the Environment variables shown:
   1. Find the variable `HierarchyArea`
   2. Edit the data in the forth column with your student info `Student-12` 
   3. Click the `Save` button to commit the changes
      ![json](./images/Postman-Environment-Area-Modify.png?raw=true "Import JSON")

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
