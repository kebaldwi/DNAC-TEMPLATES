# Template Deployment

In this module, we will use a **CI/CD Pipeline** to **build** and **deploy** **Template Projects** and within it **Regular Templates** for a specific site within the hierarchy within Catalyst Center. 

Catalyst Center uses hierarchy to logically align intent (code and configuration) against infrastructure. This allows the network administrator to align changes and modifications to the network within maintenance windows.

## Template Background

Catalyst Center has a **Template Editor||Template Hub**, which allows for the import and export of custom templates written in **Jinja2** or **Velocity** scripting languages. The templates are encapsulated within JSON inside Catalyst Center.

These templates and associated parameters allow for the **configuration** of devices when associated with sites in the hierarchy through a **Network Profile**. 

Typically **Templates**, both **Regular** and **Composite**, are grouped logically into **Projects**. When utilizing **REST API** it is possible to deploy **templates** without associating them to **Network Profiles**. This allows for greater flexibility when onboarding devices, or when using Catalyst Center as an automation engine during orchestrated processes.

In this lab, we will **build** a set of **regular templates** within a **project** and **deploy** them to the devices. 

> **Prerequisites**: **Completed** the previous section **Device Discovery**

> [**Next Section**](./02-preparation.md)
