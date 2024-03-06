# Postman and External Data Sources

Within Postman, we will utilize the collection `Build Hierarchy` to build out the Hierarchy of Cisco DNA Center into which we associate `settings` and `discover devices`. 

This Collection may be run whenever you wish to create a new section of the Hierarchy to **add** additional `Areas`, `Buildings`, or `floors`. 

Accompanying the Collection is a **required** Comma Separated Value (CSV) file, which is essentially an `answer file` for the values used to build the design. The CSV may be found here. 

> **Download**: <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-I-Rest-API-Orchestration/csv/DNAC-Design-Settings.csv" target="_blank">⬇︎ Cisco DNA Center Design Settings CSV ⬇︎</a>

We will **open** but **not save** the CSV file to view the hierarchy that will be built during the lab. 

As you review the CSV file, you will see each row has hierarchal information, settings, credentials, and other information. **Be Careful NOT to modify the file**; if you feel you have modified the file, please download it again.

<p align="center"><img src="./images/csv.png" width="800" height="345"></p>

The hierarchy the CSV will build will be this:

```text
Global > State
Global > State > California > Building10 > Floor1
Global > State > California > Building10 > Floor2
Global > State > California > Building10 > Floor3
Global > State > NorthCarolina > Building3 > Floor1
Global > State > NorthCarolina > Building3 > Floor2
Global > State > Texas > Building1 > Floor1
```

> [**Next Section**](04-collection.md)
