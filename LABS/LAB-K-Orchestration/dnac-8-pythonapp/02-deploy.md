# Using Python Applications

We will now utilize a python application to pull useful information from Cisco DNA Center and export all the Template Projects within Cisco DNA Centers Template Editor.

To get started lets first download the python program to the desktop from a well known GitHub Repository `DNAC-Templates`.

> **Download**: Get the required Python Application here: <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/LABS/LAB-I-Rest-API-Orchestration/python/DNACenterRecon.zip" target="_blank">⬇︎ Cisco DNA Center Python Recon ⬇︎</a>

Once the file is downloaded to your laptop please extract it within the folder  `C:\Users\administrator\Downloads>`.

## Activities

Once the files are extracted to the Downloads folder, these steps:

1. Open the Command Line application within windows `CMD`. A shortcut is on the taskbar below. Within `CMD` change directory to the folder and then show the directory of the folder:

```SHELL
   cd C:\Users\administrator\Downloads
   dir
```

   ![json](./images/Python-CMD-Begin.png?raw=true "Import JSON")

2. Now install the various requirements for the Python application to run. Within the Terminal issue the following command:

 ```SHELL
   pip install -r requirements.txt
```

   ![json](./images/Python-CMD-Requirements.png?raw=true "Import JSON")

3. To run the Python Application, do the following:

   1. Issue the command: ``` python DNAC-recon.py ```

      ![json](./images/Python-CMD-Execute.png?raw=true "Import JSON")

   2. When the application runs enter the following:

      - IP Address of: `198.18.129.100`
      - Username of: `admin`
      - Password of: `C1sco12345`

        ![json](./images/Python-CMD-Creds.png?raw=true "Import JSON")

   3. For the next set of tasks you will hit `enter` after eah task for the next acction in the application.
   
      1. First an API call is made and a `Authorization Token` is displayed. This is how you will know you are connected.

         ![json](./images/Python-CMD-Token.png?raw=true "Import JSON")

      2. The second API call is made and a `List of the Hierarchy` is displayed. Take a moment to compare each task.

         ![json](./images/Python-CMD-Hierarchy.png?raw=true "Import JSON")

      3. The third API call is made and a `List of the Settings` is displayed. Not all the settings were displayed to preserve screen size. There are many more that could have been displayed.

         ![json](./images/Python-CMD-Settings.png?raw=true "Import JSON")

      4. The fourth API call is made and a `List of the Devices` is displayed. Take a moment to compare to your device list. For bonus points what was different in the display to what you recieved?

         ![json](./images/Python-CMD-Devices.png?raw=true "Import JSON")


      5. The fifth API call is made and a `List of the Template Projects` is displayed. Take a moment to compare to the Template Editor. 

         ![json](./images/Python-CMD-Projects.png?raw=true "Import JSON")


      6. The Sixth group of API calls is made and a list of `downloads` is displayed. Take a moment to view the folder for the JSON files. 

         ![json](./images/Python-CMD-Export.png?raw=true "Import JSON")

         ![json](./images/Python-Folder.png?raw=true "Import JSON")

         > **ADVANCED**: Copy and rename the python program. Add a set of `definitions` to pull all the device configurations into the folder. Email it to the instructor for a chance to get the new book `The Power of Network Automation Using Cisco DNA Center` 

4. Open Visual Studio Code and examine the definitions and how the program was put together. You will notice that the Python SDK library was not used. This program was put together through the help of [DevNet Documentation](Developer.cisco.com/docs). Take a moment to view the site. 

   ![json](./images/VisualStudio-PythonApp.png?raw=true "Import JSON")

> [**Next Section**](03-summary.md)
