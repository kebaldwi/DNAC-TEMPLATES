# Python and External Data Sources

We will utilize the Python program **deploy_hierarchy.py** to build out the Hierarchy of Cisco Catalyst Center into which we later will associate **settings** and **discover devices**. 

This Collection may be run whenever you wish to create a new section of the Hierarchy to **add** additional **Areas**, **Buildings**, or **Floors**. 

Accompanying the **Python Program** is a **required** Comma Separated Value (CSV) file, which is essentially an **answer file** for the values used to build the design. The CSV which was pulled in the **Git Clone** may be found here for reference: 

> **Download:** <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/CODE/DATA/CSV/DNAC-Design-Settings.csv" target="_blank">⬇︎ Cisco Catalyst Center Design Settings CSV ⬇︎</a>

> **IMPORTANT NOTE:** We will **open** but **not save** the CSV file to view the hierarchy that will be built during the lab. 
  As you review the CSV file, you will see each row has hierarchal information, settings, credentials, and other information. **Be Careful NOT to modify the file**; if you feel you have modified the file, please download it again.

To view the file on the **script server** do the following:

```SHELL
nano /root/PYTHON-LAB/DNAC-Design-Settings.csv
```

<p align="center"><img src="./assets/csv2.png" width="800" height="174.55"></p>

Exit the file by using **^x**.

The hierarchy the CSV will build will be this:

```text
Global
Global > California
Global > California > San Jose > Building 10 > MDF
Global > California > San Jose > Building 10 > Floor 1
Global > California > San Jose > Building 10 > Floor 2
Global > California > San Jose > Building 10 > Floor 3
```

> [**Next Section**](./04-examine.md)
