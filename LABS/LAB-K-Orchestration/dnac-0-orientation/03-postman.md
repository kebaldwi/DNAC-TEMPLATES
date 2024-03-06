# Preparing Postman for use with Cisco DNA Center

To utilize Postman with Cisco DNA Center, we will first import the collection and environment into our workspace. 

## Postman Collection and Environment Import

To prepare Postman for the lab, please download the following collection and environment zip file and upload them into Postman. Download the following Student Collection, which includes seven collections and one environment. To do this right, click and open this link in a new tab to download them:
   
> **Download**: <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-I-Rest-API-Orchestration/postman/DNACenter-UseCase-API-Collection.zip" target="_blank">⬇︎ Cisco DNA Center Use-Case API Collection ⬇︎</a>

After you download the file, uncompress it and import all the files into Postman.

Follow these steps:

1. Click on the Postman shortcut on the desktop.

   ![Postman icon](./images/Postman.png)

2. Click **Import**. A window for importing files appears.

   ![Postman Import Begin](./images/Postman-Import-Begin.png)

3. Click **Upload File** to begin the file select process.

   ![Postman Import Files](./images/Postman-Import-File.png)

4. Select the files from the Student Folder and click **Open**.

   ![Postman Import Select](./images/Postman-Import-Select-Open.png)

5. Postman shows a list of files ready for import. Click **Import**.

   ![Postman Import Upload](./images/Postman-Import-Upload.png)

6. Confirm all the Collections are present.

   ![Postman Collections](./images/Postman-Collection-Confirm.png)

7. Confirm that the environment is present.

   ![Postman Environments](./images/Postman-Environment-Confirm.png)

## Postman Environment Variables

To ensure uniformity across all calls made from the client when we use different collections, we will use Environmental Variables. These variables form a database, which can be used in various collections allowing for uniformity. Additionally, this will enable us to build specific collections for multiple functions to keep them devoted to specific use cases.

Follow these steps:

1. Navigate to the environment on the left sidebar.

2. Hovering over the environment in the list. Notice a box to set it to **active**

   ![json](./images/Postman-Environment-Check.png?raw=true "Import JSON")

3. Select the check box.

   ![json](./images/Postman-Environment-Active.png?raw=true "Import JSON")

> **Note**: This environment is prepopulated with the information to build Cisco DNA Center. At specific points in the lab, we will customize it for your use.

> [**Next Section**](04-ssl.md)