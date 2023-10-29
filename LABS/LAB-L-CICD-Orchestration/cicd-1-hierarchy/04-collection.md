# Hierarchy Build Collection

Postman is a powerful tool for editing and creating REST-API calls and allows us to utilize several features to accomplish everyday tasks. In this section of the tutorial, we will use a simple REST-API set, which has been grouped into a Postman Collection.

## Collections
Collections are groupings of API, which allow us to have workflows defined for specific tasks. 

To investigate this collection, follow these steps:

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

> [**Next Section**](05-deploy.md)
>