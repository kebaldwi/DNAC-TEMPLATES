### DAY N Templates and Flows

In this section will go through the flow involved in creating a Template from an IOS configuration script for a Catalyst switch and various thoughts around how to link it to a Switch profile and deploy it through DNAC using Plug and Play workflows.

DNA Center can be used for not only Plug and Play but also Day N or Ongoing Templates. Typically customers will start by building out an Onboarding Template which might deploy only enough information to bring the device up initially or might include the entire configuration for a traditional network. Customers also need to be able to deploy ongoing changes to the network infrastructure.

Please remember that Onboarding templates are deployed one time only when the device is being brought online. For that reason sometimes it is better to keep the configuration limited to general connectivity and leave the complexitities of the rest of the configuration to the Day N template. This will allow you the administrator the ablity to modify templates and redeploy them or parts of them for ongoing changes and modifications.

Another important consideration is that part of a typical configuration would include some lines of code which will be built out with the Design >Network Settings application within DNA Center. If the Design component is used you cannot deploy that text within a template to the device. Using the settings means that you can avoids a lot of lines in the templates and avoid having to transition from one method to another later.

As a guidance try and use Design settings for as much of the configurations as you can leaving Templates light and nimble for configurations which might change ongoing. Day N templates allows for administrators to build either single templates and add them to workflows, or to build composite templates for use in provisioning. 

The use of composite templates allows you to reuse templates and code that you have previously used on other deployments without duplicating it on DNA Center. This allows you to manage those smaller templates or modules allowing for easier management moving forward.




