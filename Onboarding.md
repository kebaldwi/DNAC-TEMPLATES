# Onboarding Templates and Flows
In this section will go through the flow involved in creating a Template from an IOS configuration script for a Catalyst switch and various thoughts around how to link it to a Switch profile and deploy it through DNAC using Plug and Play workflows.

DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates. Typically customers will start by building out an Onboarding Template which might deploy only enough information to bring the device up initially or might include the entire configuration for a traditional network.

A good thing to note is that the idea behind Onboarding templates is that they are deployed one time only when the device is being brought online. While there is nothing wrong in doing only this, its important to understand that there is a lot more power gained by being able to modify templates and redeploy them or parts of them for ongoing changes and modifications.

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the *Design >Network Settings >* applications within DNA Center. If the Design component is used you cannot deploy the text code to the device. Its a decision you have to make upfront and avoids a lot of lines in the templates. 

As a guidance try and use Design settings for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing.

## DNA Center Design Preparation
Before DNA Center can automate the deployment we have to do a couple of tasks to prepare:

1. The Hierarchy within DNA Center. This will be used to roll out code and configurations ongoing so my guidance around this is to closely align this to the change management system. If you need change management down to floors or even Intermediate/Main Distribution Facilities then its a good idea to build your hierarchy to suit this. There are plenty of blogs and guides about how to do this.
2. The Network Settings can then be added hierarchically being either inherited and or overidden at each level throughout the hierarchy. The following is a description of the Network Settings that can be pushed here:
   1. test
   2.
   

