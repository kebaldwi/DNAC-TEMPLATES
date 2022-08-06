
# Module 1 - Postman Preparation
While a more extensive set of settings can be built out for deployment, we will limit the configuration to the minimum necessary to perform these steps. 

Should you desire to deploy rapidly and build the lab faster then use the following approach:

### Step 1 - ***Import Postman Collection***
1. Download and import the collection within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB9/postman/DCLOUD_DNACTemplatesLab_Workflow.postman_collection.json">⬇︎DCLOUD_DNACTemplateLab_Workflow.postman_collection.json⬇︎</a> file.
2. Extract the file to the desktop using **Winrar** to expand them
3. Open the **postman** application from the desktop. Once the application is open select *Collections* then click the *Import* link. 
![json](./images/Postman-Pre-Collection-Import.png?raw=true "Import JSON")
4. A window should appear on the file upload page. Click the upload button and select desktop from the windows explorer. Select the file named `DCLOUD_DNACTemplatesLab_Workflow.postman_collection.json` and click open. 
![json](./images/Postman-Collection-Select.png?raw=true "Import JSON")
5. Then click import and the collection should be loaded into the collections as shown.
![json](./images/Postman-Post-Collection-Import.png?raw=true "Import JSON")

### Step 2 - ***Import Postman Environment***
1. Download and import the environment within the ***Postman*** using the <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB9/postman/DCLOUD_DNACTemplateLabs.postman_environment.json">⬇︎DCLOUD_DNACTemplateLabs.postman_environment.json⬇︎</a> file.
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

# Orientation
Each grouping of API's within the uploaded files is known as a **Collection**. Collections as you can see have been built around specific use cases. These specific use cases are built out to be run against DNA Center using the **Environment** which utilizes variables which are shared across multiple API calls.

In order to give the use case a better flow each API call has been built with tests to explain what did or did not happen during the API call and to stop the flow in the event of an error. Secondarily the tests call the next subsequent API call in the chain when using the **Collection Runner**.

# DNA Center Authentication API - Postman
Cisco DNA Center APIs use token-based authentication and HTTPS Basic Authentication to generate an authentication cookie and security token that is used to authorize subsequent requests.

HTTPS Basic uses Transport Layer Security (TLS) to encrypt the connection and data in an HTTP Basic Authentication transaction.

This type of request is built into every collection.

# Preparing Postman for use with DNA Center
In order to utilize Postman with DNA Center we will first import the collection and environment into our workspace. 

## Postman Collection and Environment Import
To prepare Postman for the lab please download the following collection and environment zip file and upload them into Postman. Download the following Student Collection which includes 6 collections and one environment. To do this right click and open this link in a new tab to download them:
   
- <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB9-Rest-API-Orchestration/postman/Student-Collection.zip" target="_blank">⬇︎Student-Collection⬇︎</a>

Once the file has been downloaded uncompress/unzip it and import all the files into Postman.

Follow these steps:

1. First click on the postman shortcut on the desktop, here it is shown in Windows, but you will have a similar icon on MAC
![json](./images/Postman.png?raw=true "Import JSON")
2. Click the import button and a window for importing files will appear
![json](./images/Postman-Import-Begin.png?raw=true "Import JSON")
3. Click the upload file button to begin the files select process
![json](./images/Postman-Import-File.png?raw=true "Import JSON")
4. Select the files from the Student Folder by highlighting and click open
![json](./images/Postman-Import-Select-Open.png?raw=true "Import JSON")
5. You will see the files listed for import, then click import
![json](./images/Postman-Import-Upload.png?raw=true "Import JSON")
6. Confirm all the Collections are present.
![json](./images/Postman-Collection-Confirm.png?raw=true "Import JSON")
7. Confirm the environment is present.
![json](./images/Postman-Environment-Confirm.png?raw=true "Import JSON")

The next step is to set up the client with the correct environmental variables and SSL settings.

## Postman Environment Variables
To ensure we have uniformity across all calls made from the client when we use different collections we will make use of Environmental Variables. These variables form a database, which can be used in various collections allowing for uniformity. Additionally, this allows us to build specific collections for various functions, to keep them devoted for specific use cases.

Follow these steps:

1. Navigate to the environment on the left sidebar.
![json](./images/Postman-Environment-Confirm.png?raw=true "Import JSON")
2. Hovering over the environment listed you will notice a checkmark to set active
![json](./images/Postman-Environment-Check.png?raw=true "Import JSON")
3. Click checkmark to set the environment active
![json](./images/Postman-Environment-Active.png?raw=true "Import JSON")

This environment is prepopulated with the information to build DNA Center. At specific points in the lab we will customize it for your use.

## SSL Settings and disabling Validation
For lab purposes DNA Center utilizes a self signed certificate which would fail any validation precheck. In order to test in the lab we will therefore disable this setting.

Follow these steps:

1. Click the settings gear icon on the top right of postman to select settings.
![json](./images/Postman-Settings-Menu.png?raw=true "Import JSON")
2. Deselect the `SSL certificate verification`
![json](./images/Postman-Settings-SSL-Validation-On.png?raw=true "Import JSON")
3. It should look as shown and then close the settings window.
![json](./images/Postman-Settings-SSL-Validation-Off.png?raw=true "Import JSON")

# Summary
At this point you have set up the postman client with a collection the environment and the necessary settings to complete the lab. In the following sextions we will utilize the environment variables within each collection to perform a task on DNA Center.

We have performed a few operations in the client, and you have seen the areas we will be working in briefly, those being the Collections where the REST-API are configured and the Environment, where the data is stored in variables within the database. Take additional time to navigate postman to become more familiar. 


