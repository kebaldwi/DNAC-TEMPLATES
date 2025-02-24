# REST API Orchestration with Python - IN DEVELOPMENT

![json](../../ASSETS/underconstruction.png?raw=true "Import JSON")

## Overview

This Lab is designed as a standalone lab to help customers with varying challenges in Automating and Orchestrating their network infrastructure using Python. Within the lab, we will use various tools and techniques to Automate various tasks and orchestrate Catalyst Center. 

## General Information

Until this point, we have used Rest-API for some basic setup tasks in labs 1 and 2, but there are so many situations that can be solved or at least eased using Rest-API in conjunction with Catalyst Center. In this lab, we will use a complete set of REST-API collections which will build upon the foundational knowledge acquired in the previous labs. For this lab, we will concentrate on Catalyst Center configuration and how Catalyst Center can be automated to perform various functions which we have already covered. 

Ultimately we are all striving to completely automate the network infrastructure. The closer we get to full service automation the closer we get to business process orchestration. Continual Implementation Continual Deployment is a goal that some companies aspire to and one which the concepts here can stive towards. 

![json](./assets/cicd-pipeline2.png?raw=true "Import JSON")

This lab is meant to mirror the concepts of **[LAB 4 REST-API Orchestration with Postman](../LAB-4-Rest-API-Orchestration/README.md)** so as to build on the existing foundation of knowledge. If you have not done so already please do go through lab four to acquaint yourself with the general concepts.

The lab will utilize a set of python programs shared in the code section of the repository. These programs will also be expanded to keep in line with this lab.

## Lab Modules

The use cases we will cover are the following which you can access via the links below:

1. [**Python Orientation**](./python-0-orientation/01-intro.md)
2. [**Building Hierarchy**](./python-1-hierarchy/01-intro.md)
3. [**Assign Settings and Credentials**](./python-2-settings/01-intro.md)
4. [**Device Discovery**](./python-3-discovery/01-intro.md)
5. [**Template Deployment**](./python-4-templates/01-intro.md)
6. [**Configuration Archive**](./python-5-archive/01-intro.md)
7. [**Retrieving Network Inventory**](./python-6-inventory/01-intro.md)
8. [**Running Show Commands**](./python-7-cmd-run/01-intro.md)
9. [**Python REST API Application**]()

## Preparation

To complete this module, it's best to connect to the dCloud lab environment using your laptop so that you can get accustomed to and begin using the tools. If you cannot install python, completing all tasks via the workstation in the dCloud environment is possible via the script server.

Our screenshots will all be from the jump host but remember you can use your laptop.

If you would like to connect to the DCLOUD environment, please ensure you install the following.

### Lab Requirements

This lab is designed to be run in Cisco DCLOUD - Enterprise Network Sandbox Lab. It was developed in version 4, including DNA Center 2.2.3.5 and equipment running at least 17.x versions of code.

### Tools Required

Please utilize the following tools to run the lab effectively and ensure they are installed on your workstation/laptop before attempting the lab.

1. Cisco AnyConnect VPN Client
2. Postman
3. Google Chrome

### Cisco AnyConnect VPN Client

This software is required to connect your workstation to Cisco DCLOUD. For an explanation of AnyConnect and how to use it with DCLOUD, please visit the following URL: 

> **Documentation**: For AnyConnect Documentation visit: <a href="https://DCLOUD-cms.cisco.com/help/android_anyconnect" target="_blank">DCLOUD AnyConnect Documentation</a>

> **Download**: Get AnyConnect here: <a href="https://DCLOUD-rtp-anyconnect.cisco.com" target="_blank">⬇︎ AnyConnect Download Site ⬇︎</a>

### Python and Catalyst Center SDK

Python will be used in this Lab to interact with Catalyst Center using REST API through use of the Catalyst Center Python SDK and normal HTTP Requests. As previously stated, the combination of Python programming language with the rich Cisco Catalyst Center API collection offers the utmost flexibility and power in developing custom applications or workflows.

As with any other Vendor Automation Controller, Cisco Catalyst Center Rest API capabilities get extended and maintained with each new release of Cisco Catalyst Center software. This presents a challenge to a Python developer, as code REST API syntax and parameters may change over time requiring the developer to revisit earlier developed code. To help developers abstract from Cisco Catalyst Center specific version implementation, [Cisco Catalyst Center SDK](https://dnacentersdk.readthedocs.io/en/latest/api/api.html) toolkit was introduced.

Simply put, SDK is a set of tools, libraries and documentation to simplify interacting with a REST API. The Cisco Catalyst Center SDK is written in Python and provides a Python library in PyPI and associated documentation. PyPI is the official python package index, and simplifies installation of the library. 

#### Python installation, Linux based OS like MAC

* Install Homebrew package manager

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

* Install PyEnv using HomeBrew. PyEnv is a CLI utility that helps you manage Python installations on your computer.

```shell
brew install pyenv
pyenv init

nano ~/.zshrc
Paste the eval line at the end of the file
eval "$(pyenv init -)"

press Control + X, type Y and press Enter when prompted for the file name

Now that PyEnv is installed and configured, exit and reload the Terminal
```

With PyEnv is installed and configured, we can install Python. Example below is installing Python version 3.9.1

```shell
pyenv install 3.9.1
pyenv global 3.9.1
```

And finally, verification of installed Python environment

```shell
pyenv version
```

Lets ensure that we have Python module manager PIP installed

```shell
python -m ensurepip --upgrade
```

#### Python installation, Windows

* [Installing Python](https://www.python.org/downloads/) - Python distributions

Lets ensure that we have Python module manager PIP installed

```shell
python -m ensurepip --upgrade
```

#### Cisco Catalyst Center SDK installation

* To isolate the installation folder structure from other libraries create a virtual environment, and activate it. Each time you want to come back and make changes to your code please remember to activate the virtual environment in your terminal (see below)

```shell
python -m venv dnacentersdk
source dnacentersdk/bin/activate
```

* Install Cisco Catalyst Center SDK in newly created virtual environment

```shell
pip install dnacentersdk
```

The SDK is ready for use!

### Google Chrome

Google Chrome is the optimal browser of choice when working in the DNA Center UI. 

> **Download**: Get Google Chrome here: <a href="https://www.google.com/chrome/downloads/" target="_blank">⬇︎ Chrome Download ⬇︎</a>

## Summary

This lab is intended for educational purposes only. Use outside of a lab environment should be done at the operator's risk. Cisco assumes no liability for incorrect usage.

This lab is intended to help drive the adoption of Rest-API and will be added to over time with various use cases. The Public Workspace will also mirror the changes and be kept up to date. We hope this set of labs helps explain how the Rest-API may be used and goes a little further in helping define and document them.

> **Feedback**: If you found this set of Labs helpful, please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Return to LAB Main Menu**](../README.md)
