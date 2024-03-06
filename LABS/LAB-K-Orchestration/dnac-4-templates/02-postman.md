# Postman and External Data Sources

Within Postman, we will utilize the collection `Template Deployment` to build projects within the `Template Editor` and add `Regular Templates` to them in order to `configure` devices. 

This Collection may be run whenever you wish to `configure` or `modify` the **configuration** of a `device` within Cisco DNA Center. 

Accompanying the Collection is a required Comma Separated Value (CSV) file, which is essentially an answer file for the values used to build the design. The CSV may be found here.

> **Download**: <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-I-Rest-API-Orchestration/csv/DNAC-Design-Settings.csv" target="_blank">⬇︎ Cisco DNA Center Design Settings CSV ⬇︎ </a>

We will **open** but **not save** the CSV file to view the hierarchy that will be built during the lab. 

As you review the CSV file, you will see each row has hierarchal information, settings, credentials, and other information. **Be Careful NOT to modify the file**; if you feel you have modified the file, please download it again.

<p align="center"><img src="./images/csv.png" width="800" height="345"></p>

Within the CSV, scroll to the right for the columns pertaining to this collection.

> [**Next Section**](03-deploy.md)
