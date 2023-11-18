# Template Deployment

In this module, we will use *Postman* to **build** and **deploy** `Projects` and a `Regular Templates` for a specific site within the hierarchy within Cisco DNA Center. 

Cisco DNA Center uses hierarchy to logically align intent (code and configuration) against infrastructure. This allows the network administrator to align changes and modifications to the network within maintenance windows.

## Template Background

Cisco DNA Center has a `Template Editor`, which allows for the import and export of custom templates written in **Jinja2** or **Velocity** scripting languages. The templates are encapsulated within JSON inside Cisco DNA Center.

These templates and associated parameters allow for the `configuration` of devices when associated with the hierarchy through a `Network Profile`. 

`Templates`, both `Regular` and `Composite`, are grouped logically into `Projects`.

In this lab, we will `deploy` a `regular template` within a project to be ready for deployment later. 

> **Note**: Included in the repository is a Deployment API, which is there for informational purposes and should not be invoked due to the nature of the lab environment.

> **Prerequisites**: **Completed** the previous section **Device Discovery**

> [**Next Section**](02-postman.md)
