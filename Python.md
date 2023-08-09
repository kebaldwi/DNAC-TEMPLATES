# Python and Cisco DNA Center [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

## Python and DNA Center
It is no secret that Python programming language has gained tremendous popularity in the developer community. 
As reported by 2021 Stack Overflow Developer Survery, Python was identified as the number one most wanted language among developers who are not currently using it. DNA Center has a large number of very powerful automation workflows already built into the product (ie Plug and Play, SWIM, SDA, Templates etc), which are also exposed to the operator via programmable API interfaces which can be leverged to further integrate DNA Center into more complex or customized automation workflows.
Given Python popularity, it makes sense to review how you can apply basic programming practices to automate common tasks in your own network with DNA Center APIs.

When developing with Python for DNA Center, you will find your code operating in one of these categories:
- DNA Center capability augmentation. In these scenarios, the extensie DNA Center native automation workflows may not be sufficient or customized enough to meet the organizations need. Some examples of these use cases may include things like extensive configuration compliance, long term report retention or integrations with other vendors in the environment requiring functionality in addition to what is already built in DNA Center. This category of use-cases is addressed with [DNA Center Intent Based APIs](https://developer.cisco.com/dnacenter/intentapis/)
- DNA Center integration with Top Level Orchestrators. In such scenarios you want to take advantage of your organizations established Orchestration strategy with other tools (Terraform, Ansible, NSO, ServiceNow etc) where majority of processes and business logic is already built out. In these scenarios you are no longer expecting Network Operators interfacing with DNA Center GUI, and instead submitting abstracted change requests at the Top Level Orchestrator. This is where custom developed, or 3rd Party maintained Python code can help seamlessly integrate DNA Center into those existing pipelines. This category of use-cases is addressed with both [DNA Center Intent Based APIs](https://developer.cisco.com/dnacenter/intentapis/) and [DNA Center Integration Flows](https://developer.cisco.com/dnacenter/integrationapis/)
- DNA Center integration with 3rd Party NOC tools. The Cisco DNA Center platform provides the ability to publish event notifications that enable third party applications to listen to any issues detected by Cisco DNA Assurance, as well as System-level and task-based operational notifications from Cisco DNA Center, and more. This category of use-cases is addressed with [DNA Center Events and Notifications Services](https://developer.cisco.com/dnacenter/eventsandnotifications/)

## DNA Center with Python vs other tools
You may find yourself pondering over which tool is best suited for developing automation workflows leveraging extensive DNA Center API capabilities. Based on NetDevOps Survey conducted in 2020, the following is the breakdown of tools used in the field for automating the generation and/or the deployment of configurations at scale, [NetDevops 2020 Config Generation Tools Breakdown](results/2020/netdevops_survey_2020_config-gen-deploy_tool.png). By far, one of the most popular Automation platforms cited is RedHat Ansible. Given its popularity, it may be conducive to consider Ansible and its very mature Cisco DNA Center Module Galaxy collection as a starting point, [Redhat Ansible DNA Center Galaxy Collection](https://galaxy.ansible.com/cisco/dnac). At its core, Ansible DNA Center module collection is a set of Python directives, abstracting DNA Center native REST API and integrating those into Ansible constructs. As such, one of the biggest benefits of leveraging Ansible DNA Center Galaxy collection is standardization and abstraction from underlying REST API implementation details. This approach works great in organizations that od not have dedicated developer teams who are tasked with maintaining Python code responsible for DNA Center Integrations. However, Ansible approach brings its own set of challenges when it comes to building anything more than just linear, sequential workflows. Playbooks containing even moderately complex business logic become unwieldy and start growing in complexity exponentially. Another aspect to consider in same context is large datasets which DNA Center API may return in some of the larger deployments, and the requirement to 'parse' or 'tokenize' that data if it were two be operated on through Ansible. 
This is where it becomes more practical to consider Python for developing such workflows. Python offers the utmost flexibility and elegance of developing your own applications or integrations with DNA Center. Python's dependency on DNA Center version-specific REST API implementation is further abstracted by Cisco maintained DNA Center Python SDK. 

DNA Center programmable REST API capabilities are covered in our previous tutorial section, [REST API](./RestAPI.md) - REST API and Cisco DNA Center. This section will build upon API foundational concepts introduced in that earlier section

In this section we will cover Python integrations with Cisco DNA Center's "Business and Network Intent APIs".

Before diving into developing your own Python automation scripts with DNA Center, we will work through initial steps required to setup your development environment by installing:
- Python environment 
- Python PIP module manager
- Cisco DNA Center Python SDK

## Prerequisites
> It is assumed that the reader has general level familiarity with Python language before proceeding with examples outlined in this section. 
> Please ensure that you have Python v3.x installed on your machine 

### Python installation, MacOS

* Install Homebrew package manager
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

* Install PyEnv using HomeBrew. PyEnv is a CLI utility that helps you manage Python installations on your computer.
```
brew install pyenv
pyenv init

nano ~/.zshrc
Paste the eval line at the end of the file
eval "$(pyenv init -)"

press Control + X, type Y and press Enter when prompted for the file name

Now that PyEnv is installed and configured, exit and reload the Terminal
```

With PyEnv is installed and configured, we can install Python. Example below is installing Python version 3.9.1

```
pyenv install 3.9.1
pyenv global 3.9.1
```

And finally, verification of installed Python environment

```
pyenv version
```

Lets ensure that we have Python module manager PIP installed

```
python -m ensurepip --upgrade
```

### Python installation, Windows
* [Installing Python](https://www.python.org/downloads/) - Python distributions

Lets ensure that we have Python module manager PIP installed

```
python -m ensurepip --upgrade
```

## Python DNA Center SDK
As previously stated, the combination of Python programming language with the rich Cisco DNA Center API collection offers the utmost flexibility and power in developing custom applications or workflows. 
As with any other Vendor Automation Controller, DNA Center Rest API capabilities get extended and maintained with each new release of DNA Center software. This presents a challenge to a Python developer, as code REST API syntax and parameters may change over time. To help developers abstract from DNA Center specific version implementation, [DNA Center SDK](https://dnacentersdk.readthedocs.io/en/latest/api/api.html) toolkit was introduced.
Simply put, SDK is a set of tools, libraries and documentation to simplify interacting with a REST API. The Cisco DNA Center SDK is written in Python and provides a Python library in PyPI and associated documentation. PyPI is the official python package index, and simplifies installation of the library.

### Cisco DNA Center SDK installation
* To isolate the installation folder structure from other libraries create a virtual environment
```
python -m venv env3
source env3/bin/activate
```

* Install DNA Center SDK in newly created virtual environment
```
pip install dnacentersdk
```
The SDK is ready for use!

## Cisco DNA Center Platform Overview
Cisco DNA Center is at the heart of Cisco's Intent-based network architecture.
Cisco DNA Center supports the expression of business intent for network use-cases, such as base automation capabilities in the enterprise network. Cisco customers and partners can use the Cisco DNA Center platform to create value-added applications that leverage the native capabilities of Cisco DNA Center

![json](images/dnac_python_automation.png?raw=true "Business and Network Intent APIs")

### Intent API (Northbound)
The Intent API is a Northbound REST API that exposes specific capabilities of the Cisco DNA Center platform.
The Intent API provides policy-based abstraction of business intent, allowing focus on an outcome rather than struggling with individual mechanisms steps.
The RESTful Cisco DNA Center Intent API uses HTTPS verbs (GET, POST, PUT, and DELETE) with JSON structures to discover and control the network. For more information, see [Intent API](https://developer.cisco.com/dnacenter/intentapis/).
The Intent API is grouped, hierarchically into functional 'domains' and 'subdomains' of service. These are:
- Authentication Domain
- Know Your

Authentication method obtains a security token that identifies the privileges of an authenticated REST caller.
Cisco DNA Center authorizes each requested operation according to the access privileges associated with the security token that accompanies the request.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Return to Main Menu**](./README.md)