# REST API and Cisco Catalyst Center [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

## What are REST API?

**REST API** stands for **Representational State Transfer Application Programming Interface**. It is a set of guidelines that allow software to communicate with each other over the internet. **REST APIs** use HTTP requests to retrieve and send data, and they typically return data in a format like JSON or XML. They are commonly used to build web and mobile applications, and can be a powerful tool for integrating different software systems.

## How are REST API used with Cisco Catalyst Center?

**REST APIs** are used with Cisco Catalyst Center to programmatically interact with the Cisco Catalyst Center platform. This allows you to automate tasks, retrieve data, and integrate Cisco Catalyst Center with other systems. With **REST APIs**, you can perform tasks like provisioning network devices, configuring network policies, and retrieving network analytics data. This can help simplify network management and reduce the time and effort required for network operations. Additionally, **REST APIs** allow you to build custom applications and integrations that leverage the capabilities of Cisco Catalyst Center.

![json](../ASSETS/dnac-api.png?raw=true "Import JSON")

## What can REST API do for Cisco Catalyst Center?

**REST APIs** with Cisco Catalyst Center can be used to accomplish a variety of tasks, including:

1. Provisioning and configuring network devices, such as routers, switches, and access points.

2. Retrieving information about network devices, users, and applications, including inventory data, device status, and network performance metrics.

3. Creating and managing network policies, such as access control lists (ACLs), quality of service (QoS) policies, and security policies.

4. Automating network operations tasks, such as software upgrades, patching, and configuration backups.

5. Integrating Cisco Catalyst Center with other systems, such as IT service management (ITSM) platforms, security information and event management (SIEM) systems, and cloud orchestration platforms.

6. Building custom applications and integrations that leverage the capabilities of Cisco Catalyst Center to meet specific business needs.

Overall, **REST APIs** with Cisco Catalyst Center can help simplify network management, reduce operational costs, and improve network performance and security.

## What types of API Integrations are there?

### Cisco Catalyst Center Built in REST API Integrations

Cisco Catalyst Center has several built-in integrations that use REST APIs, including:

1. **Cisco Identity Services Engine (ISE)**: ISE is a network access control (NAC) platform that can be integrated with Cisco Catalyst Center to enforce network access policies. The integration uses **REST APIs** to exchange information about network devices, users, and policies.

2. **Cisco Stealthwatch**: Stealthwatch is a network security platform that can be integrated with Cisco Catalyst Center to monitor network traffic and detect security threats. The integration uses **REST APIs** to exchange information about network flows, devices, and events.

3. **Cisco ThousandEyes**: ThousandEyes is a network monitoring platform that can be integrated with Cisco Catalyst Center to monitor network performance and troubleshoot issues. The integration uses **REST APIs** to retrieve data about network paths, devices, and applications.

4. **Cisco Meraki**: Meraki is a cloud-managed networking platform that can be integrated with Cisco Catalyst Center to manage Meraki devices alongside other Cisco network devices. The integration uses **REST APIs** to exchange information about network devices, users, and policies.

5. **Cisco SDWAN**: Cisco SD-WAN Viptela can also be integrated with Cisco Catalyst Center using REST APIs. This integration allows you to manage and monitor both your SD-WAN and SD-Access network devices from a single platform and Fabric.

![json](../ASSETS/crossdomain-integrations.png?raw=true "Import JSON")

6. **ServiceNow**: ServiceNow is an IT service management (ITSM) platform that can be integrated with Cisco Catalyst Center to automate incident management and change management processes. The integration uses **REST APIs** to exchange information about network devices, users, and incidents.

7. **Infoblox || Bluecat**: Both Infoblox and Bluecat IP address management suites (IPAM) may be leveraged with Cisco Catalyst Center thorugh direct integrations. This allows for Cisco Catalyst Center to automatically learn from the IPAM about address pools and facilitate the building of Virtual Networks within the infrastructure. Additionally the IPAM's DNS system can help inform the automatic discovery of internal FQDN for internal applications discovered on the network to help keep QoS up to date.

8. **Liveaction and Tableaux**: can integrate with Cisco Catalyst Center to visualize the events and telemetry gathered from the network infrastructure to help facilitate notifications and awareness.

![json](../ASSETS/partner-integrations.png?raw=true "Import JSON")

Overall, these built-in integrations can help streamline network management and improve security and performance by leveraging the capabilities of Cisco Catalyst Center and other Cisco platforms.

### Published REST API for Cisco Catalyst Center

Cisco Catalyst Center has a comprehensive set of published **REST APIs** that allow developers to programmatically interact with the platform. Some of the key published APIs include:

1. **Inventory APIs**: These APIs allow you to retrieve information about network devices, including their type, model, serial number, and software version.

2. **Site APIs**: These APIs allow you to manage network sites, including creating and deleting sites, and retrieving information about site topology and devices.

3. **Client APIs**: These APIs allow you to retrieve information about network clients, including their IP address, MAC address, and associated network devices.

4. **Assurance APIs**: These APIs allow you to retrieve network performance metrics, such as traffic flow data, device health status, and application usage statistics.

5. **Configuration APIs**: These APIs allow you to manage network configurations, including creating and updating network policies, templates, and profiles.

6. **Event APIs**: These APIs allow you to retrieve information about network events, such as device failures or configuration changes.

7. **Command Runner APIs**: These APIs allow you to execute CLI commands on network devices and retrieve the output.

![json](../ASSETS/dnac-api.png?raw=true "Import JSON")

Overall, the published **REST APIs** for Cisco Catalyst Center provide a wide range of capabilities for managing and monitoring your network infrastructure programmatically.

## Unpublished REST API for Cisco Catalyst Center

Although Cisco Catalyst Center has a comprehensive set of published **REST APIs** that allow developers to programmatically interact with the platform, there are times where it may be necessary for you to make use of a feature which has no published **REST API** to date. In that case you might want to develop a one off **REST API** call to facilitate the requirement doing the following:

Use Developer Mode on Chrome to see a **REST API** from Cisco Catalyst Center, follow these steps:

1. Open Google Chrome and navigate to the Cisco Catalyst Center web interface.

2. Press F12 on your keyboard to open the Developer Tools pane.

3. Click on the Network tab in the Developer Tools pane.

4. Perform an action on the Cisco Catalyst Center web interface that triggers a **REST API** call, such as retrieving information about a network device.

5. Look for the API call in the list of network requests shown in the Network tab. The API call will typically have a URL that starts with "https://" and includes the word "api".

6. Click on the API call to view additional details about the request and response, including the HTTP headers and payload.

7. You can also use the Developer Tools pane to test **REST API** calls by selecting the "Console" tab and entering API commands using JavaScript or other programming languages.

Overall, using Developer Mode on Chrome can be a helpful tool for troubleshooting **REST API** issues and gaining a better understanding of how Cisco Catalyst Center's APIs work.

> **Note:** it's important to note that unpublished APIs are typically not supported by the vendor and are not recommended for use in production environments. Using unpublished APIs can pose a security risk and may result in unexpected behavior or system instability. It's always best to stick to the published APIs and follow best practices for API usage to ensure the stability and security of your network infrastructure.

## How to get Started?

To get started developing **REST API** with Cisco Catalyst Center, you will need to:

1. Obtain access to a Cisco Catalyst Center instance and obtain credentials to authenticate API requests.

2. Familiarize yourself with the Cisco Catalyst Center **REST API** documentation, which can be found within Cisco Catalyst Center's **Developer Toolkit** or alternatively on the [**Cisco DevNet website**](https://developer.cisco.com/docs/dna-center/).

3. Choose a *programming language* or *toolset* that you are comfortable with, and use it to send **HTTP requests** to Cisco Catalyst Center. Some examples of toolsets include an **IDE** like [**Visual Studio**](https://code.visualstudio.com/download), or [**Sublime**](https://www.sublimetext.com/) and [**Postman**](https://www.postman.com/downloads/) for code creation and testing.

4. Start with *simple API calls* to retrieve information about network devices, users, or other resources, and *gradually build more complex* integrations as you become more familiar with the API.

5. Test your API integrations thoroughly, and ensure that you are following best practices for security and performance.

6. Finally, consider joining the [**Cisco DevNet community**](https://developer.cisco.com/site/coi/) to connect with other developers and access additional resources and support for developing with Cisco Catalyst Center APIs.

## Building Production Code with REST API for Cisco Catalyst Center

To build production ready code for **REST API** for Cisco Catalyst Center, it's important to follow best practices for software development and API usage. Here are some general steps to consider:

1. Choose a *programming language* or *toolset* that is appropriate for your organization's needs and development environment. Some examples of toolsets include an **IDE** like [**Visual Studio**](https://code.visualstudio.com/download), or [**Sublime**](https://www.sublimetext.com/) and [**Postman**](https://www.postman.com/downloads/) for code creation and testing.

2. Follow a disciplined software development process, including *version control*, *automated testing*, and *code reviews*.

3. Use secure coding practices, such as input validation, output encoding, and error handling, to prevent security vulnerabilities.

4. Use caching and other performance optimization techniques to ensure that your API calls are fast and efficient.

5. Follow the principles of RESTful design, including using HTTP verbs correctly, using resource-oriented URLs, and providing consistent response formats.

6. Use appropriate authentication and authorization mechanisms to ensure that only authorized users and applications can access your API.

7. Monitor your API usage and performance using tools like Cisco Catalyst Center's analytics and reporting capabilities.

8. Continuously improve your API by incorporating feedback from users and monitoring industry best practices for API design and usage.

Overall, building production code for **REST API** for Cisco Catalyst Center requires a disciplined approach to software development and API usage, as well as a commitment to security, performance, and usability.

## Python and Cisco Catalyst Center REST API

Cisco provides a **Python SDK library** for use with Cisco Catalyst Center, which can help simplify the process of building **REST API** integrations. The SDK is available on the Cisco DevNet website and can be installed using pip, the Python package manager. This augments the previously mentioned Developer Toolkit in Cisco Catalyst Center and Cisco's DevNet Documentation on **REST API**.

The ultimate goal of most organizations considering CICD Pipelines with Cisco Catalyst Center is to augment the platform to provide a way of continual development, balanced with continual deployment. Sometimes *Orchestration Platforms* like **Ansible**, or **Teraform** are considered to help orchestrate through Cisco Catalyst Center.  

![json](../ASSETS/cicd-pipeline2.png?raw=true "Import JSON")

In the case above a repository, holds templates in JSON and settings in YAML which are tested for vulnerabilities and syntax and against CML. After successful testing the CICD pipeline builds the configurations and settings on Cisco Catalyst Center through a Ansible Playbook. Then the pipeline kicks off a deployment playbook which provisions the configurations from Cisco Catalyst Center toward the network infrastructure.

In the heart of all this is **REST APIs** which are how code and configuration are built on Cisco Catalyst Center and through which are provisioned to the network.

Here are some key features of the Cisco Catalyst Center Python SDK:

1. **Simplified API calls**: The SDK provides a simple and intuitive interface for making **REST API** calls to Cisco Catalyst Center, reducing the amount of code required to build integrations.

2. **Object-oriented design**: The SDK uses an object-oriented design, with Python classes and methods that map to Cisco Catalyst Center's **REST API** resources, making it easier to work with complex data structures.

3. **Error handling**: The SDK provides robust error handling capabilities, including the ability to catch and handle exceptions, which can help improve the reliability of your integrations.

4. **Authentication**: The SDK includes built-in support for authenticating API requests using Cisco Catalyst Center's token-based authentication mechanism.

5. **Documentation**: The SDK includes comprehensive documentation, including code samples and API reference materials, which can help accelerate the development process.

Overall, the Cisco Catalyst Center Python SDK can help simplify the process of building **REST API** integrations with Cisco Catalyst Center and reduce the amount of time and effort required to develop robust and reliable integrations.

## Labs Overview

We include in the Repository a full set of Labs designed to help customers with varying challenges in Automating and Orchestrating their network infrastructure. Within the lab, we will use a complete set of **REST API** collections which will build upon the foundational knowledge. For this lab, we concentrate on Cisco Catalyst Center configuration and how Cisco Catalyst Center can be orchestrated via **REST API** to perform various functions: 

1. [**Postman Orientation**](../LABS/LAB-I-Rest-API-Orchestration/module1-postman.md)
2. [**Building Hierarchy**](../LABS/LAB-I-Rest-API-Orchestration/module2-hierarchy.md)
3. [**Assign Settings and Credentials**](../LABS/LAB-I-Rest-API-Orchestration/module3-settings.md)
4. [**Device Discovery**](../LABS/LAB-I-Rest-API-Orchestration/module4-discovery.md)
5. [**Template Deployment**](../LABS/LAB-I-Rest-API-Orchestration/module5-templates.md)
6. [**Configuration Archive**](../LABS/LAB-I-Rest-API-Orchestration/module6-archive.md)
7. [**Retrieving Network Inventory**](../LABS/LAB-I-Rest-API-Orchestration/module7-inventory.md)
8. [**Running Show Commands**](../LABS/LAB-I-Rest-API-Orchestration/module8-commands.md)

> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Return to Main Menu**](../README.md)