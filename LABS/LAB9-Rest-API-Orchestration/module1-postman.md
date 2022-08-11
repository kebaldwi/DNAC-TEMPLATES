
# Module 1 - Postman Preparation
In this module we will get the postman client operational and ready for use in the various sections of this lab. The first step will be to either import the collections and enviroment into postman, or to them in from the publicly shared workspace.

## Orientation
**Collections** are groupings of requests within postman. They are logical structures which allow for requests to be grouped and run as a collection within Postman. Within this lab we have built collections around specific use cases. Each collection can be exported and imported separately, or together within a workspace. **Workspaces** are separate tenants within Postman and operate separately from each other. 

Within a **Workspace** you may have multiple **Collections** and **Environments**. **Environments** utilize variables which are shared across multiple collections and requests. **Variables** can be localized to **Environments**, and **Collections**.

In order to give the use case a better flow each API call has been built with **Tests** within **Test** scripts to explain what did or did not happen during the API call and to stop the flow in the event of an error. Secondarily the test script calls the next subsequent API call in the chain when using the **Collection Run** methodology.

# DNA Center Authentication API - Postman
Cisco DNA Center APIs use token-based authentication and HTTPS Basic Authentication to generate an authentication cookie and security token that is used to authorize subsequent requests.

HTTPS Basic uses Transport Layer Security (TLS) to encrypt the connection and data in an HTTP Basic Authentication transaction.

This type of request is built into every collection.

# Preparing Postman for use with DNA Center
In order to utilize Postman with DNA Center we will first import the collection and environment into our workspace. 

## Option 1 - Easy Button to Import Collection and Environment
There is a Public Workspace, which can be easily added to Postman via the following link. This will allow you to rapidly start using the Rest-API suite created for this lab. Click the following link and log into your Postman account and the workspace including the collections and the environment will be automatically added. (see image below)

[Public DNA Center Use-Case API Collection](https://www.postman.com/dark-capsule-39992/workspace/dna-center-use-case-api-collections)

![json](./images/Postman-Public-Workspace.png?raw=true "Import JSON")

## Option 2 - Postman Collection and Environment Import
To prepare Postman for the lab please download the following collection and environment zip file and upload them into Postman. Download the following Student Collection which includes 7 collections and one environment. To do this right click and open this link in a new tab to download them:
   
<a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB9-Rest-API-Orchestration/postman/DNACenter-UseCase-API-Collection.zip" target="_blank">⬇︎DNACenter Use-Case API Collection⬇︎</a>

Once the file has been downloaded uncompress/unzip it and import all the files into Postman.

Follow these steps:

1. First click on the postman shortcut on the desktop, here it is shown in Windows, but you will have a similar icon on MAC
![json](./images/Postman.png?raw=true "Import JSON")
2. Click the import button and a window for importing files will appear
![json](./images/Postman-Import-Begin.png?raw=true "Import JSON")
3. Click the upload file button to begin the files select process
![json](./images/Postman-Import-File.png?raw=true "Import JSON")
4. Select the files from the Folder by highlighting and click open
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

To continue your learning experience continue on to the next module in the series which is module 2 below.

## Lab Modules
The use cases we will cover are the following which you can access via links below:

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