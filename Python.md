# Python and Cisco DNA Center [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

## Python and DNA Center

It is no secret that Python programming language has gained tremendous popularity in the developer community. 
As reported by 2021 Stack Overflow Developer Survery, Python was identified as the number one most wanted language among developers who are not currently using it. Cisco DNA Center has a large number of very powerful automation workflows already built into the product (ie Plug and Play, SWIM, SDA, Templates etc), which are also exposed to the operator via programmable API interfaces which can be leverged to further integrate DNA Center into more complex or customized automation workflows.

Given Python popularity, it makes sense to review how you can apply basic programming practices to automate common tasks in your own network with Cisco DNA Center APIs.

![json](images/dnac_python_automation.png?raw=true "DNA Center APIs")

When developing with Python for DNA Center, you will find your code operating in one of these categories:

- Cisco DNA Center capability augmentation. In these scenarios, the extensie Cisco DNA Center native automation workflows may not be sufficient or customized enough to meet the organizations need. Some examples of these use cases may include requirements like extensive configuration compliance, long term report retention or integrations with other vendors in the environment requiring functionality in addition to what is already built in Cisco DNA Center. This category of use-cases is addressed with [DNA Center Intent Based APIs](https://developer.cisco.com/dnacenter/intentapis/)
- DNA Center integration with Top Level Orchestrators. With this, you want to take advantage of your organizations established Orchestration strategy relying on other tools (Terraform, Ansible, NSO, ServiceNow etc) where majority of processes and business logic is already built out. In these scenarios you are no longer expecting Network Operators interfacing with DNA Center GUI, and instead submitting abstracted change requests at the Top Level Orchestrator. This is where custom developed, or 3rd Party maintained Python code can help seamlessly integrate DNA Center into those existing pipelines. This category of use-cases is addressed with both [DNA Center Intent Based APIs](https://developer.cisco.com/dnacenter/intentapis/) and [DNA Center Integration Flows](https://developer.cisco.com/dnacenter/integrationapis/)
- Cisco DNA Center integration with 3rd Party NOC tools. The Cisco DNA Center platform provides the ability to publish event notifications that enable third party applications to listen to any issues detected by Cisco DNA Assurance, as well as System-level and task-based operational notifications from Cisco DNA Center, and more. This category of use-cases is addressed with [DNA Center Events and Notifications Services](https://developer.cisco.com/dnacenter/eventsandnotifications/)

## DNA Center with Python vs other tools

You may find yourself pondering over which tool is best suited for developing automation workflows leveraging extensive Cisco DNA Center API capabilities. Based on NetDevOps Survey conducted in 2020, the following is the breakdown of tools used in the field for automating the generation and/or the deployment of configurations at scale, [NetDevops 2020 Config Generation Tools Breakdown](results/2020/netdevops_survey_2020_config-gen-deploy_tool.png). By far, one of the most popular Automation platforms cited is RedHat Ansible. Given its popularity, it may be conducive to consider Ansible and its mature Cisco DNA Center Module Galaxy collection as a starting point, [Redhat Ansible DNA Center Galaxy Collection](https://galaxy.ansible.com/cisco/dnac). At its core, Ansible DNA Center module collection is a set of Python directives, abstracting DNA Center native REST API and integrating those into Ansible constructs. As such, one of the biggest benefits of leveraging Ansible DNA Center Galaxy collection is standardization and abstraction from underlying REST API implementation details. This approach works great in organizations that od not have dedicated developer teams who are tasked with maintaining Python code responsible for DNA Center Integrations. However, Ansible approach brings its own set of challenges when it comes to building anything more than just linear, sequential workflows. Playbooks containing even moderately complex business logic become unwieldy and start growing in complexity exponentially. Another aspect to consider in same context is large datasets which DNA Center API may return in some of the larger deployments, and the requirement to 'parse' or 'tokenize' that data if it were two be operated on through Ansible.

This is where it becomes more practical to consider Python for developing such workflows. Python offers the utmost flexibility and elegance of developing your own applications or integrations with DNA Center. Python's dependency on DNA Center version-specific REST API implementation is further abstracted by Cisco maintained DNA Center Python SDK. 

DNA Center programmable REST API capabilities are covered in our previous tutorial section, [REST API](./RestAPI.md) - REST API and Cisco DNA Center. This section will build upon API foundational concepts introduced in that earlier section

In this section we will cover Python integrations with Cisco DNA Center's "Business and Network Intent APIs".

Before diving into developing your own Python automation scripts with DNA Center, we will work through initial steps required to setup your development environment by installing:

- Python environment 
- Python PIP module manager
- Cisco DNA Center Python SDK

With minimum set of requirements above satisfied, we will then build a simple python program to:

1. authenticate with Cisco DNA Center and obtain authentication token
2. retrieve a list of network devices managed by Cisco DNA Center and displaying the list on the screen. We will initially build it with Python compiling each REST API call individually with Python **requests** library, and subsequently will show how we can leverage Cisco DNA Center Python SDK to abstract from individual API call syntax in our program

## Prerequisites

* It is assumed that the reader has general level familiarity with Python language before proceeding with examples outlined in this section. 
* Please ensure that you have Python v3.x installed on your machine
* In the next set of steps, we will go through minimal preparation required to have Python environment ready for developing with Cisco DNA Center

### Python installation, MacOS

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

### Python installation, Windows

* [Installing Python](https://www.python.org/downloads/) - Python distributions

Lets ensure that we have Python module manager PIP installed

```shell
python -m ensurepip --upgrade
```

## Python DNA Center SDK

As previously stated, the combination of Python programming language with the rich Cisco DNA Center API collection offers the utmost flexibility and power in developing custom applications or workflows.

As with any other Vendor Automation Controller, Cisco DNA Center Rest API capabilities get extended and maintained with each new release of DNA Center software. This presents a challenge to a Python developer, as code REST API syntax and parameters may change over time requiring the developer to revisit earlier developed code. To help developers abstract from DNA Center specific version implementation, [DNA Center SDK](https://dnacentersdk.readthedocs.io/en/latest/api/api.html) toolkit was introduced.

Simply put, SDK is a set of tools, libraries and documentation to simplify interacting with a REST API. The Cisco DNA Center SDK is written in Python and provides a Python library in PyPI and associated documentation. PyPI is the official python package index, and simplifies installation of the library.

### Cisco DNA Center SDK installation

* To isolate the installation folder structure from other libraries create a virtual environment, and activate it. Each time you want to come back and make changes to your code please remember to activate the virtual environment in your terminal (see below)

```shell
python -m venv dnacentersdk
source dnacentersdk/bin/activate
```

* Install DNA Center SDK in newly created virtual environment

```shell
pip install dnacentersdk
```

The SDK is ready for use!

## Cisco DNA Center - simple example with Python and requests library

In this example, we are going to demonstrate a simple Python based application that implements two basic functions:

* Generate DNA Center Authentication Token
* Retrieve a list of devices from DNA Center

Authentication method obtains a security token that identifies the privileges of an authenticated REST caller.
Cisco DNA Center authorizes each requested operation according to the access privileges associated with the security token that accompanies the request.

HTTPS Basic uses Transport Layer Security (TLS) to encrypt the connection and data in an HTTP Basic Authentication transaction.

For purposes of this tutorial, we will use Cisco DevNet always on [DNA Center Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology) since it has some devices already in the inventory that we can poll.

For the Labs contained in this repository, please use Cisco **DCLOUD** environment (Refer to details in [LABS/README](./LABS/README.md) for details).

To obtain the Auth token, we will need the details of how DNA Center implements this API Endpoint.
Open Cisco DNA Center GUI console in your browser, authenticate and navigate to Platform > Developer Toolkit > APIs.
Under "Authentication" section, Select "Authentication API". We can see the following information required for a successfull Authentication API Call:

1. The Request:
   * Method: POST to API Endpoint: https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token
2. Request Header Parameters:
   * Content-Type: 'application/json'
   * Authorization: 'Basic BASE64(username:password)

> **Note:** String composed of “Basic”, followed by a space, followed by the Base64 encoding of “username:password”, NOT including the quotes. For example “Basic YWRtaW46TWFnbGV2MTIz”, where YWRtaW46TWFnbGV2MTIz is the Base 64 encoding.

### Cisco DNA Center - simple example with Python and requests library

Let's use the Python **requests** library to create a function that when called, will return an Authorization Token following above notation.

In the same Terminal App where we have just activated Python virtual environment:

```shell
pip install requests
```

1. Create dnac_config.py file containing DNA Center credentials. This code will allow us to set the parameters either as environment variables (note env var names in CAPS), or use default values supplied if the corresponding environment variable is not set.

> **Note:** It is considered to be a best practice to not store credentials in plain text, and instead leveraging environment variables. This example is for simplicity and demonstration purposes only.

> **Note:** Please ensure to update DNAC URL, and credentials to match Cisco DNA Center environment you are working with (in this case, parameters are for devnet sandbox).

```python
import os
DNAC=os.environ.get('DNAC','sandboxdnac.cisco.com')
DNAC_USER=os.environ.get('DNAC_USER','devnetuser')
DNAC_PASSWORD=os.environ.get('DNAC_PASSWORD','Cisco123!')
```

2. Create dnac_simple_python.py file:
   * requests is the library of choice to make the api request. Note the 'verify=False' parameter passed, which disables DNA Center self-signed certificate validation. In production, DNA Center appliance will be likely signed by a recognized CA and this parameter will not be required
   * HTTPBasicAuth is part of the requests library and is used to encode the credentials to Cisco DNA Center
   * dnac_config.py is a Python file that contains Cisco DNA Center connectivity and authentication info we created in previous step

```python
import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC, DNAC_USER, DNAC_PASSWORD

def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    auth_api_endpoint =  '/dna/system/api/v1/auth/token'    # AUTH API Endpoint 
    url = 'https://{DNAC}{API}'.format(DNAC=DNAC,API=auth_api_endpoint) # complete API URL
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), verify=False)  # Make the POST Request
    token = resp.json()['Token']    # Retrieve the Token from the returned JSON
    print("Token Retrieved: {}".format(token))  # Print out the Token
    return token    # Create a return statement to send the token back for later use

if __name__ == "__main__":
    """
    Program entry point
    """
    get_auth_token()
```

Execute to confirm we can succesfully obtain the Authentication Token

```shell
python3 dnac_simple_python.py
questWarning: Unverified HTTPS request is being made to host 'sandboxdnac.cisco.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
Token Retrieved: <token>
```

Let us now extend this example by defining two more functions in the same dnac_simple_python.py file:

* get_device_list() which will call on DNA Center network device API and retrieve json formatted list of devices
* print_device_list () which will print the json data structure of devices retrieved. It simply iterates over the json dictionary and prints out the relevant fields to the screen

Let us review how we can compile an API request to DNA Center to retrieve list of managed devices. Open Cisco DNA Center GUI in your browser, authenticate, and navigate to Platform > Developer Toolkit, and under 'Know Your Network' select 'Devices'. 

From the list of available API Calls, click 'Get Device List'. We can see the following information required for a successfull Get Device List API Call:
 
1. The Request:
   * Method: POST to API Endpoint: https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device
2. Request Header Parameters:
   * You will see a long list of parameters which can be supplied to refine the query for the list of devices, however note that they are all tagged with 'Required: No'. For a simple request that will return all of devices with no filters, we can omit this.

```python
def get_device_list():
    """
    Building out function to retrieve list of devices. Using requests.get to make a call to the network device Endpoint
    """
    token = get_auth_token() # Get Token
    network_devices_api_endpoint = '/api/v1/network-device' # Device list API Endpoint
    url = 'https://{DNAC}{API}'.format(DNAC=DNAC,API=network_devices_api_endpoint) # complete API URL
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    resp = requests.get(url, headers=hdr, verify=False)  # Make the Get Request
    device_list = resp.json()
    print_device_list(device_list)
```

```python
def print_device_list(device_json):
    """
    Custom pretty-print function to display relevant output to the screen
    """
    print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
          format("hostname", "mgmt IP", "serial","platformId", "SW Version", "role", "Uptime"))
    for device in device_json['response']:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        if device['serialNumber'] is not None and "," in device['serialNumber']:
            serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
        else:
            serialPlatformList = [(device['serialNumber'], device['platformId'])]
        for (serialNumber, platformId) in serialPlatformList:
            print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
                  format(device['hostname'],
                         device['managementIpAddress'],
                         serialNumber,
                         platformId,
                         device['softwareVersion'],
                         device['role'], uptime))
```

And finally, instead of calling on the Auth function as we did in previous example, lets modify our dnac_simple_python.py file main function to call the new get_device_list() function when the python code gets executed

```python
if __name__ == "__main__":
    """
    Program entry point
    """
    get_device_list()
```

Execute to confirm we can succesfully authenticate, retrieve list of network devices, and output the list to the screen of the terminal:

```shell
python3 dnac_simple_python.py
Token Retrieved: <token>

hostname                                  mgmt IP          serial      platformId        SW Version  role            Uptime
sw1                                       10.10.20.175     9SB9FYAFA2O C9KV-UADP-8P      17.9.20220318:182713DISTRIBUTION    19 days, 4:41:37.00
sw2                                       10.10.20.176     9SB9FYAFA21 C9KV-UADP-8P      17.9.20220318:182713DISTRIBUTION    116 days, 13:02:14.00
sw3                                       10.10.20.177     9SB9FYAFA22 C9KV-UADP-8P      17.9.20220318:182713ACCESS          3 days, 21:00:59.00
sw4                                       10.10.20.178     9SB9FYAFA23 C9KV-UADP-8P      17.9.20220318:182713ACCESS          116 days, 13:02:27.00
```

### Cisco DNA Center - simple example with Python DNA Center SDK

In previous example, we relied on Python **requests** library and specified each API endpoint URL explicitely in our code. 

While this is a fine approach, it introduces a level of dependency between our Python code and the specific Cisco DNA Center version that we are interacting with. It is possible that newer versions of Cisco DNA Center introduce changes in its implementation of each REST API endpoint, which may lead to revisit and re-test our code with new version of the controller. To help remove this dependency, let us see how we can leverage Cisco DNA Center Python SDK we installed previously. 

Let us create a new Python file, dnac_sdk_python.py as follows below.

You will notice that we are re-using the same dnac_config.py file which contains Cisco DNA Center IP/URL, and authentication parameters as in the previous example above. We are re-writing the two functions (authentication, device list) to call Cisco DNA Center SDK functions instead of constructing our own API call with its syntax dependencies. You will notice how much cleaner our code gets.

```python
from dnacentersdk import api
from dnac_config import DNAC, DNAC_USER, DNAC_PASSWORD


def get_auth_dnac():
    """
    Leverage SDK to return a DNAC object
    """
    dnac = api.DNACenterAPI(base_url="https://{DNAC}".format(DNAC=DNAC),
                            username=DNAC_USER,password=DNAC_PASSWORD,verify=False)
    return dnac

def get_device_list():
    dnac = get_auth_dnac() # Authenticate to DNA Center. Instead of acquiring with Auth Token, we get an object with Token supplied as one of its properties
    devices = dnac.devices.get_device_list() # Call SDK to acquire list of managed devices. Again, no explicit reference to REST API endpoint here
    print_device_list(devices) # Pretty print the list of devices to the screen
    return devices

def print_device_list(device_json):
    """
    Custom pretty-print function to display relevant output to the screen
    """
    print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
          format("hostname", "mgmt IP", "serial","platformId", "SW Version", "role", "Uptime"))
    for device in device_json['response']:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        if device['serialNumber'] is not None and "," in device['serialNumber']:
            serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
        else:
            serialPlatformList = [(device['serialNumber'], device['platformId'])]
        for (serialNumber, platformId) in serialPlatformList:
            print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
                  format(device['hostname'],
                         device['managementIpAddress'],
                         serialNumber,
                         platformId,
                         device['softwareVersion'],
                         device['role'], uptime))


if __name__ == "__main__":
    """
    Program entry point
    """
    get_device_list()
```

Execute to confirm we can succesfully authenticate, retrieve list of network devices, and output the list to the screen of the terminal:

```shell
python3 dnac_sdk_python.py
hostname               mgmt IP          serial      platformId      SW Version            role            Uptime         
sw1                    10.10.20.175     9SB9FYAFA2O C9KV-UADP-8P    17.9.20220318:182713  DISTRIBUTION    24 days, 4:41:00.00
sw2                    10.10.20.176     9SB9FYAFA21 C9KV-UADP-8P    17.9.20220318:182713  DISTRIBUTION    121 days, 13:01:37.00
sw3                    10.10.20.177     9SB9FYAFA22 C9KV-UADP-8P    17.9.20220318:182713  ACCESS          8 days, 21:00:22.00
sw4                    10.10.20.178     9SB9FYAFA23 C9KV-UADP-8P    17.9.20220318:182713  ACCESS          121 days, 13:01:50.00
```

### Cisco DNA Center - Postman as a tool to generate Python

In the above two examples, we spent some time understanding how one would develop a Python based application leveraging native Python constructs such as **requests** library to generate REST API calls to DNA Center, as well as an abstraction method with DNA Center SDK hiding individual API syntax from the developer. Either of these approaches are fine for someone who has familiarity with both Python as well as DNA Center API mechanics. You will find that once you have started developing simple Python applications for Cisco DNA Center, in a very short amount of time you will have accumulated a collection of your own code snippets that can be re-used quite easily. 

For someone who is new to development and or to DNA Center, there is also a **rapid prototyping** approach leveraging a very well known developer tool called Postman to quickly stitch together a workflow in a graphical fashion, and have Postman automatically generate Python skeleton code that will help you overcome the initial challenge of starting with a blank sheet of paper. Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration so you can create better APIs faster.

A more indepth introduction to Postman with Cisco DNA Center is covered in [Rest-API Orchestration](https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-I-Rest-API-Orchestration/)

In your browser, navigate to [Cisco DNA Center - Postman collection](https://developer.cisco.com/docs/dna-center/#!postman-collections), you should see a section called 'Postman Collections' under 'Developer Resources'. Under 'Postman Collections', click 'Run in Postman' navigation button which will take to you the repository portal. Before proceeding to next step, ensure that you Login on this page (top right corner, you can setup a free Postman account if you dont have one). 
Once you have logged in, on the same Postman **Cisco DNA Center APIs** collection click 'Fork' in the top right corner, and select the name of the Workspace to which you want to clone it to. As next step, in the same page - click 'Workspaces' dropdown menu in top left corner and select the Workspace to which we have just cloned the Collection.

The DNA Center Postman Collection **Cisco DNA Center APIs** will appear in the list of Collections under your Postman Workspace. You will also notice a small fork icon next to it, with the name of the original Collection from which we have forked it.

![json](images/dnac_python_postman_intro.png?raw=true "Postman - Developer view")

The **Cisco DNA Center APIs** Postman Collection of API calls is neatly organized into categories that allows you to quickly drill down and navigate. For the purposes of this excersice, we are going to require two **GET** API calls from this collection:

1. Authentication 
2. Network Devices

To simplify automation workflows, Postman has very rich capability set built in. One of indespensible features is the notion of Postman 'Environment' which allows a developer to define an environment variable which can be variablized and re-used in subsequent calls transparently. The **Cisco DNA Center APIs** Collection includes a built-in Environment with parameters pre-defined to access [DNA Center Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology).

When working with Postman, it is a good practice to always check which Environment you are configured for before executing any of the API workflows to ensure the calls will be made to the intended destination.

Let us inspect what parameters are set in the sample Environment for **Cisco DNA Center APIs** Collection.

In your browser, while on the same Postman collection portal - select 'Environments' in the vertical menu on the left, and Select 'DNAC-Sandbox'. This will open a new tab, and you can see the Variable names, 'Initial value' and 'Current value' parameters for each.

For example, you should recognize the Variable named 'dnac' which is set to 'sandboxdnac.cisco.com' URL, 'username', 'password' etc.

Throughout your API workflows in Postman, individual Variable values may change while others will remain static. As an example, 'token' Variable will not have any 'Initial value' set until you make an Authentication API call to DNA Center, at which point its 'Current value' will be populated with the Auth Token if authentication was successfull. 

Once you have a good understanding of the  **Cisco DNA Center APIs** Collection, you will want to clone the 'DNAC-Sandbox' Environment, and modify Environment variables to suit your own developer environment different from sandbox. While in the DNAC-Sandbox Environment view tab, click the '...' button in top right corner, and select 'Duplicate' to create a new Environment Set that you can modify.

Now that we are familiar with Postman 'DNAC-Sandbox' Environment variables - let us select 'DNAC-Sandbox' Environment as our current operating Environment in the top right corner dropdown menu. With 'DNAC-Sandbox' Environment selected, any API call executed through Postman will be sent to the DNA Center Sandbox.

In your browser Postman, select 'Collections' in the Menu and return to **Cisco DNA Center APIs**. under Authentication, select the Postman POST call. Lets examine main elements of this Postman API call definition:

* Type: POST
* API Endpoint: https://{{dnac}}/api/system/v1/auth/token
* Authorization Tab
  Type: Basic Auth
  Username: 
  Password:
* Headers Tab:
  content-type: application/json

You quickly realize these are the same parameters we defined in the two Python program examples above.

This time Postman is the platform that allows us to graphically define the same in a much simplified fashion.

Of importance is to expect the 'Tests' tab, which will contain:

```python
var data = JSON.parse(responseBody);
postman.setEnvironmentVariable("token", data.Token);
```

As you are aware, REST API calls are stateless - meaning with each execution of an API call data is returned but not stored or 'tracked' by the controller. When interacting with Cisco DNA Center through REST API interface, each call requires an Auth Token as part of any API call.

Since Postman API Authentication call to Cisco DNA Center is stateless, we need a variable to store the resulting token which can later be re-used in the subsequent API call to obtain device list information. Code snippet above does eactly that - it extracts the 'data' field from the JSON responde from the Authentication API call, and updates the Postman current Environment variable set (ie DNAC-Sandbox) varibale called 'token' with the responses Token key.

Lets hit 'Send' to execute this API call in Postman. If the call is succesfull, you will observe Status: **200 OK** in Postman. 
The 'Body' tab will contain the JSON API call response, similar to below

```python
{
    "Token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTY5MjM5MDg4MSwiaWF0IjoxNjkyMzg3MjgxLCJqdGkiOiJiNTU0YTZiMi1jNGM1LTQ0MGUtOGIwOS02YTYzOTg2NTc1MzYiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.a0mKUlW1hemLSTushuhiBaJ6GP17OnHhWQf8e-mko6_ls3UAya7_5u04VKNJHz5uKCgi3ONu4ieRsHa6FylBygazqVimDy5wswdztyDBGeD2fXtf4bTG_764zD2pAh3LP1Q_p42WiXNCZH4yGtWKD-9a5Wxa-57RgTgT_wVhI2_Uj3Td0q1I9yfJbakFmErApBlV17EGZATaXdEM3A2rmzxKN_2wGQsevsxpd1wl9Ehdnr0JiQYq5HFpmlT-OShjSZdSdZ35R1ulUh0QugAzlu22ohGWpTKKEOm-00WiXmCOqVzbkJzbDw9Y28JNPGO5l-lwiS1tzdRrDFKJB08O8g"
}
```

Inspecting the response, you will realize that it contains 'Token' field, with the Auth Token value assigned to it. 
This 'Token' key is what is being assigned by Postman to 'token' Environment variable as part of the Tests section of this call definition we examined above.

Great, progress! We have just completed the Authentication component of our workflow using Postman GUI. Lets now examine how Postman can help us generate Python code from this REST API Collection call definition. While in the same 'POST' tab in your browser Portal, select 'Code' button in the vertical menu on the right. Since we are going to be developing in Python, and we want to leverage **requests** Python library,  under 'Code snippet' select 'Python - Requests'. Postman will generate a skeleton Python code corresponding to the REST API Call definition as part of the **Cisco DNA Center APIs** Collection we just executed:

```python
import requests

url = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"

payload = ""
headers = {
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

If you still have your Terminal App opened with the previous excercise from this section, lets create a new file dnac_postman_python.py and paste Postman generated code into it. If you had to re-open the Terminal app, please do not forget to activate the virtual environment before executing Python:

```python
source dnacentersdk/bin/activate
```

Initial execution attempt will likely result in the error below:

```shell
python dnac_postman_python.py
Traceback (most recent call last):
...
requests.exceptions.SSLError: HTTPSConnectionPool(host='sandboxdnac.cisco.com', port=443): Max retries exceeded with url: /api/system/v1/auth/token (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:997)')))
```

We have seen the SSLError above, where DNA Center SSL Certificate validation step fails with self-signed certificate. Lets adjust the code suggested by Postman to address this condition by adding 'verify=False' parameter to **requests** call, and also folding the logic into function definition that would return the Auth Token when called.

Let us also import **json** library to help us parse (convert) the API Call response text into a JSON object such that we can access key:value pairs more easily

```python
import requests
import json

def get_auth_dnac():
    url = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"

    payload = ""
    headers = {
    'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
    }

    # create a **requests** call, disable SSL certificate validation
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    # JSON string is part of the 'text' property of the response
    # call loads function to parse (ie convert) string to a JSON object
    # and access the 'Token' key
    auth_token = json.loads(response.text)['Token']
    print(auth_token)

    return auth_token


if __name__ == "__main__":
    """
    Program entry point
    """
    get_auth_dnac()
```

Subsequent execution should yield the Auth Token printed to the screen

```shell
python dnac_postman_python.py
/.pyenv/versions/3.10.3/lib/python3.10/site-packages/urllib3/connectionpool.py:1043: InsecureRequestWarning: Unverified HTTPS request is being made to host 'sandboxdnac.cisco.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
  warnings.warn(
{"Token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTY5MjM5MjA2OCwiaWF0IjoxNjkyMzg4NDY4LCJqdGkiOiI4NDEyMmFjYS0wNjE2LTQ0MWQtYjAxNS05MGM2YzQxMjgyYWQiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.YpbEAOUrWn11ole57R7yfxCaAgS_6a2zFLQhthRLLhG6WkvVaGSzAPFOdL0-qC1QKrBZgQInSh59mXq0KFH28JuXGT4vbGecqP17QsjLtz5rjyS2gBFhCOSoUMW2krSKdLoI17dzmwO3r7OK0BXlpNUNeFx9DO_1G8Vx3_Rn-RaTJmu_wK6vNn6yMFHaUN8iPdw_kHeWh5lPv58oTu3ImckTp-wU0XfKD4pLF4ojfrbLBzWeU4gudmHci2K8EwYBD0wyFc7kl6ZwjB0xWUB7RO0L2EK0sRfeVWnmMgc3-w9Xue1Wb5Wet7fxYbSj4lG1nK_Y0D4AOS3K324e_ZIEWg"}
```

As in the previous excercise, lets now move on to using Postman to generate Python code for obtaining a list of devices managed by Cisco DNA Center.

In our Postman view, under **Cisco DNA Center APIs** collection, navigate to '2. Network Devices' section, and select the first 'GET' network-device API Call.

Lets examine main elements of this Postman API call definition:

* Type: GET
* API Endpoint: https://{{dnac}}/dna/intent/api/v1/network-device (Note: please adjust the URI to match, as you may have additional filters applied after 'network-device' section. For purposes of this excercise we simply want to obtain a complete list of devices with no additional query modifiers)
* Authorization Tab
  Type: Inherit Auth from parent
* Headers Tab:
  x-auth-token: {{token}} (Note: this is first time we are seeing Variable re-use. This '{{}}' notation indicates that we want to substitue the value of 'token' variable from our Environment set and assign it to 'x-auth-token' key)

Lets hit 'Send' and we should get a Status: **200 OK** with a JSON payload as part of the Body tab.

JSON responses can be quite lengthy and are difficult for a human eye to enterpret beyond a few lines.

In our Postman 'network-device' API tab, select 'Visualize' tab to get a pretty tabular view representing data contained in the JSON Payload.

![json](images/dnac_python_postman_visualize.png?raw=true "Postman - JSON payload Visualization")

Similar to how we used Postman to generate Python code for the Authentication function, let us click on 'Code' button on the vertical menu on the right of the screen, select 'Python - Requests' under 'Code Snippet' section. You should get the following skeleton Python code suggested by Postman

```python
import requests

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload = {}
headers = {
  'x-auth-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTY5MjM5MDg4MSwiaWF0IjoxNjkyMzg3MjgxLCJqdGkiOiJiNTU0YTZiMi1jNGM1LTQ0MGUtOGIwOS02YTYzOTg2NTc1MzYiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.a0mKUlW1hemLSTushuhiBaJ6GP17OnHhWQf8e-mko6_ls3UAya7_5u04VKNJHz5uKCgi3ONu4ieRsHa6FylBygazqVimDy5wswdztyDBGeD2fXtf4bTG_764zD2pAh3LP1Q_p42WiXNCZH4yGtWKD-9a5Wxa-57RgTgT_wVhI2_Uj3Td0q1I9yfJbakFmErApBlV17EGZATaXdEM3A2rmzxKN_2wGQsevsxpd1wl9Ehdnr0JiQYq5HFpmlT-OShjSZdSdZ35R1ulUh0QugAzlu22ohGWpTKKEOm-00WiXmCOqVzbkJzbDw9Y28JNPGO5l-lwiS1tzdRrDFKJB08O8g'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

Lets incorporate the above call into our dnac_postman_python.py application while re-using (this is a good example of code re-use I mentioned earlier in this tutorial) a previously defined function to pretty-print the devices to the screen

```python
import requests
import json

def get_auth_dnac():
    url = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"

    payload = ""
    headers = {
    'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    auth_token = json.loads(response.text)['Token']
    print(auth_token)

    return auth_token

def get_device_list():
    auth_token = get_auth_dnac()

    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

    payload = {}
    headers = {
    'x-auth-token': auth_token
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    devices = json.loads(response.text)

    return devices

def print_device_list(device_json):
    """
    Custom pretty-print function to display relevant output to the screen
    """
    print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
          format("hostname", "mgmt IP", "serial","platformId", "SW Version", "role", "Uptime"))
    for device in device_json['response']:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        if device['serialNumber'] is not None and "," in device['serialNumber']:
            serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
        else:
            serialPlatformList = [(device['serialNumber'], device['platformId'])]
        for (serialNumber, platformId) in serialPlatformList:
            print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
                  format(device['hostname'],
                         device['managementIpAddress'],
                         serialNumber,
                         platformId,
                         device['softwareVersion'],
                         device['role'], uptime))


if __name__ == "__main__":
    """
    Program entry point
    """
    devices = get_device_list()
    print_device_list (devices)
```

An execution of the above code should yield the predictable output:

```shell
python dnac_postman_python.py
...
hostname                                  mgmt IP          serial      platformId        SW Version  role            Uptime         
sw1                                       10.10.20.175     9SB9FYAFA2O C9KV-UADP-8P      17.9.20220318:182713DISTRIBUTION    28 days, 4:40:28.00
sw2                                       10.10.20.176     9SB9FYAFA21 C9KV-UADP-8P      17.9.20220318:182713DISTRIBUTION    125 days, 13:01:05.00
sw3                                       10.10.20.177     9SB9FYAFA22 C9KV-UADP-8P      17.9.20220318:182713ACCESS          12 days, 20:59:50.00
sw4                                       10.10.20.178     9SB9FYAFA23 C9KV-UADP-8P      17.9.20220318:182713ACCESS          125 days, 13:01:18.00
```

## Summary

In this tutorial we covered the basics of preparing your Python development environment for Cisco DNA Center.

We also reviewed two approaches to writing Python programs to interface with Cisco DNA Center. We first used Cisco DNA Center REST API URL to construct a **requests** call to obtain a simple Auth Token, which was used to obtain the list of managed devices.

The same approach was further simplified when we instead used Cisco DNA Center Python SDK to achieve the same outcome.

In the last example, we demonstrated how a **rapid-prototyping** approach can be achieved leveraging Postman as the development tool to help us build workflows visually and convert them to Python code which requires minimal modifications to achieve the outcome

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Return to Main Menu**](./README.md)