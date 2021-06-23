# Advanced Automation - In Development
## Overview
This Lab is designed to be used after first completing labs 1 through 4 and has been created to address how to use some advanced automation concepts not previously touched on in the previous labs. This is an enablement type lab and is designed to help customers to reach beyond what they currently understand and try new concepts and really push the boundaries of automation.

During this lab we will cover various topics with regard to template logic to solve various use cases. Some of these concepts have been previously covered but perhaps not with as indepth a focus.

## General Information
As previously discussed, DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates customers will start by building out an Onboarding Template which typically deploys only enough information to bring the device up initially. While it might include the entire configuration for a traditional network device, this is better served by Day N Templates and for more flexibility Composite Templates. as they can be used to apply ongoing changes and to allow device modifications after initial deployment. 

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* application within DNA Center. If the Design component is used you should **not** deploy the same feature from cli code in a template to configure the device. Its a decision you have to make upfront and avoids a lot of lines in the templates and allows for a more UI centric configuration which is easier to maintain. 

As a guidance try and use **Design Settings** for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing.

With these things in mind we will cover various aspects and use cases which perhaps allow for a more programamtic approach.

## Topics
The various topics covered in the lab will be:





## Availability Information
This lab is under development please come back soon. ETA for delivery June 30 2021.



