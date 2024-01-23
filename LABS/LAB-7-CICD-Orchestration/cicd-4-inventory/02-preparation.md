# Python and External Data Sources

Within Postman, we will utilize the Python program `device_inventory.py` to **retrieve** the network infrastructure **inventory** for the **routers**, **switches** and **wireless** network devices and **compliance data** for them. 

This Python program will be run by the **CI/CD Pipeline** whenever a change is noticed in the **CSV** and may be run whenever you wish to to get the up to date inventory of Cisco Catalyst Center. This python command could augment the previous pipeline and be used after the devices had been discovered and again after the templates had been deployed.

Accompanying the **Python Program** is a required Comma Separated Value **CSV** file, which is essentially an answer file for the values used to build the design. The **CSV** was added to the directory in the preceding **Modules** and is a tracked trigger for this pipeline. 

For reference **ONLY** it is here:

> **Download:** <a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-L-CICD-Orchestration/assets/csv/DNAC-Design-Settings.csv" target="_blank">⬇︎ Cisco Catalyst Center Design Settings CSV ⬇︎</a>

> **IMPORTANT NOTE:** We will **open** but **not save** the CSV file to view the hierarchy that will be built during the lab. 
  As you review the CSV file, you will see each row has hierarchal information, settings, credentials, and other information. **Be Careful NOT to modify the file**; if you feel you have modified the file, please download it again.

To view the file on the **script server** do the following:

```SHELL
cat /root/DEVWKS-2176/DNAC-Design-Settings.csv
```

<p align="center"><img src="./images/csv2.png" width="800" height="174.55"></p>

> **Note**: You can see the devices all the way to the right of the file.

> [**Next Section**](./03-pipeline.md)
