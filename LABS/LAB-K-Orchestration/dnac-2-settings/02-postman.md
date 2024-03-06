# Postman and External Data Sources

Within Postman, we will utilize the collection `Assign Settings Creds` to assign settings and credentials to the Hierarchy of Cisco DNA Center in order to associate `settings` and `credentials` to devices. 

This Collection may be run whenever you wish to assign or modify the `settings` and `credentials` of the Hierarchy to either **add** or **modify** settings and or credentials. 

Accompanying the Collection is a required Comma Separated Value (CSV) file, which is essentially an answer file for the values used to build the design. The CSV may be found here.

> **Download**: <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-I-Rest-API-Orchestration/csv/DNAC-Design-Settings.csv" target="_blank">⬇︎ Cisco DNA Center Design Settings CSV ⬇︎ </a>

We will **open** but **not save** the CSV file to view the hierarchy that will be built during the lab. 

As you review the CSV file, you will see each row has hierarchal information, settings, credentials, and other information. **Be Careful NOT to modify the file**; if you feel you have modified the file, please download it again.

<p align="center"><img src="./images/csv.png" width="800" height="345"></p>

> **Note**: You can see the settings begin to the right of the hierarchy.

> [**Next Section**](03-deploy.md)
