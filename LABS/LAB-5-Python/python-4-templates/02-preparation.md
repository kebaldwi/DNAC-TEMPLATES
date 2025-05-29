# Python and External Data Sources

We will utilize the Python program **deploy_templates.py** to **build** and **deploy** **Template Projects** and within it **Regular Templates** for a specific site within the hierarchy within Catalyst Center. 

This Python program will be run by the **CI/CD Pipeline** whenever a change is noticed in a monitored folder on the system. The program will use a **YAML** file **site_operations.yml** which will provide specific data to the program as to how and where to deploy the templates. This process may be augmented to pull templates and push them from and too **GitHub**. 

> **Note:** Those components while **not active** in the pipeline **have been added** to the **python program**. 

Accompanying the **Python Program** is a required YAML Ain't Markup Language **YAML (YML)** file, which is essentially an answer file for the values used to deploy the templates. The **YAML (YML)** was added to the directory in the preceding **Modules**. 

For reference **ONLY** it is here:

> **Download:** <a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-L-CICD-Orchestration/assets/YAML/site_operations.yml" target="_blank">⬇︎ Site Operations YAML Example ⬇︎</a>

> **IMPORTANT NOTE:** We will **open** but **not save** the YML file to view the hierarchy that will be built during the lab. 
  As you review the YML file, you will see each row has operational information, devices, IP's, and other information. **Be Careful NOT to modify the file**; if you feel you have modified the file, please download it again.

To view the file on the **script server** do the following:

```SHELL
  sudo nano -v /root/DEVWKS-2176/site_operations.yml
```

<p align="center"><img src="./images/site_operations.png" width="800" height="789.33"></p>

> **Note**: You will notice devices and templates denoting type of template, or device.

> [**Next Section**](./03-pipeline.md)
