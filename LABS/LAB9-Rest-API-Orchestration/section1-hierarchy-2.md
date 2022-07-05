# Use Case 1.1 - Building Hierarchy - lablet *[1](./section1-hierarchy-1.md)*
**[2]** *[3](./section1-hierarchy-2.md)*
Within Postman we will utilize the collection `Build Hierarchy Student` to build out the Hierarchy of DNA Center in which to associate settings and discover devices. This Collection may be run whenever you wish to create a new section of the Hierarchy to either add additional Areas, Buildings, or floors.

## Student Hierarchy Build and the Postman Collection Runner
Postman being a powerful tool for editing and creating Rest-API calls, allows us to utilize a number of features to accomplish every day tasks. In this short tutorial, we will cover a simple set of Rest-API which have been grouped into a Postman Collection.

### Collections
Collections are groupings of API, which allow us to have flows for specific defined tasks. 

To investigate the collections we have built follow these steps:

1. Navigate and open the Collection through the following steps:
   1. Within Postman click on the Collection shortcut in the sidebar
   2. Expand the collection `DNE LAB 1.0 - Build Hierarchy Student` by clicking the arrow.
   3. The tab with the API within the collection will appear to the right
   4. You can view the configuration of the API through these tabs. As a quick reference a green dot appears wherever configuration is applied.
      ![json](./images/Postman-Collection-Token-Begin.png?raw=true "Import JSON")
2. Within the API you will notice the following:
   1. The method **POST** is used for this API
   2. The URL *https://***{{DNACip}}***/dna/system/api/v1/auth/token* where the Environmental variable **{{DNACip}}** holds the actual IP. Hover briefly over the variable to display the current data.
   3. Click the `Authorization` tab to to display the Authorization parameters
   4. Here we see that this API is using Basic Auth to get a TOKEN
   5. Two environmental variables **{{DNACuser}}** and **{{DNACpwd}}** are used and can be viewed by hovering over the variables presented
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
       3.       tests["Body has Token"] = true;
       4.       postman.setEnvironmentVariable("TOKEN", jsonData["Token"]); 
       5.     }
       6.     else {
       7.       tests["Body has no Token"] = false;
       8.       postman.setNextRequest("null");
       9.     }
       10.    postman.setNextRequest("Create Area")
      ```

         As we double click here we see the line associating the response from the API and    loading it into a variable jsonDATA in line 1.
         
         In line 2 we begin an conditional if statement to determine if the JSON response    contains a field called Token with a token in it.
         
         Within the if condition in line 4 we load the Token from the field within the    JSON response into the environmentatl variable.
         
         We culminate the section by calling for the next API within the collection.

## Summary
All the following API are called one after the other in sequence until the chain of events within the collection is complete.

In certain API ther may be more Headers used, or in the Pre-request script Environmental variables may be loaded for use in the body required for executing the API, but fundamantally all API calls are the same. 

Additionally if there is time, take a look at the various API within the Collection and look for Environmental variables in the Pre-request scripts and Body to become more familiar.


