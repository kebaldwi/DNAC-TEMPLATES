# In Development
![json](../../ASSETS/underconstruction.png?raw=true "Import JSON")

# Advanced Automation

## Overview

In the previous labs you became familiar with an overview into **[Wired](../LAB-1-Wired-Automation/README.md)** and **[Wireless](../LAB-2-Wireless-Automation/README.md)** Automation. These both utilized the idea of utilizing **[Intent](../../TUTORIALS/ManagementScale.md)** which concentrates itself around the Network Settings, Network Profiles and aligns those to the Hierarchy. 

> [!TIP]
> For many reasons and specifically with Wireless the Wireless Settings, and Feature Templates in the UI are the best way I can recommend for managing Wireless controllers at scale, with or without Fabric. The reason, is that Per Device Configuration is just as it sounds iterating through settings on multiple controllers, whicch will never be as quick or nimble at scale as the UI. I also do not advocate for building templates for controllers as often the radio resets become painful at scale. This is elegantly solved by Wireless Intent.

This Lab will focus on the creation and development of Templates, and how to choose and adopt settings in the UI toward adopting **[Intent](../../TUTORIALS/ManagementScale.md)**. This will take some of the previous concepts and expand upon them while concentrating on the build of the templates for switching. It will culminate in the provisioning of a switch via REST-API.

## General Information

As previously discussed, Catalyst Center can be used for the following:

- Onboarding via Plug-and-Play 
- Day N

### Onboarding

This concentrates on initializing the device with the correct software or code to support the features we will use, along with a stable configuration for either a Layer 2 or 3 connection to the infrastructure. It culminates in the device being onboarded into Catalyst Centers inventory.

Conceptually, Network Settings together with the Image from the repository together with the Templates and or configuration deployed via LAN automation build the device utilizing the PnP process. 

### Day N 

This concentrates on the building of features deployed to support the connected devices and concentrating on host onboarding. It utilizes the Network Settings and either Fabric or Template Provisioning or a combination of the two.

> [!TIP]
> It is important to consider that the **Network Settings** deploy configuration, and that you should make a choice between that which is to be built via the UI and that which is to be built via a **Template**. One must also ask whether it is worth building that which already exists and which is supported. If the **Design component** is **used**, you should **not** deploy the same feature from a **template**. 

As guidance, try and use **Design Settings** for as many of the configurations as you can, leaving Templates light and nimble for configurations that might change ongoing.

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 
