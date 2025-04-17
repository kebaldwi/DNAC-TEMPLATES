# JSON YAML XML Explained  [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

## Why you Need Structured Data

Automation depends on structured data. Data must be stored and transmitted in such a way that a process knows how to read it.  There are many structured data formats, but this tutorial will focus on three common data structures used in network automation: JSON (Javascript Object Notation), YAML (YAML Aint Markup Language), and XML Extensible Markup Language.

## JSON

JSON is a very popular data structure.  It's human and machine readible and commonly used in many programming languages for passing text data.  JSON is a common encoding format for REST API operations.  If you are familiar with the Python programming language--especially Python dictionaries and lists, you'll find JSON syntax looks very familiar. JSON formats data as attribute-value pairs and uses curly braces \{\} as an object delimeter.  Let's explore JSON in more detail.


```json
data = {
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet0/1",
    "description": "LAN",
    "enabled": true,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip":"172.16.0.2",
          "netmask":"255.255.255.0"
        },
        {
          "ip":"172.17.0.2",
          "netmask":"255.255.255.0"
        }
      ]
    }
  }
}
```

View the JSON block above.  The ```data``` is a JSON Object as noted by the opening and closing curly braces.  Within that object is a name-value pair with the name ```"ietf-interfaces:interface"```.  The value is another object which contains name-value pairs separated by commas.  The names are ```"name"```, ```"description"```, ```"enabled"```, and ```"ietf-ip:ipv4"```.  ```"ietf-ip:ipv4"``` contains and object ```"address"```, which is a list of objects, as denoted by the braces \[\].  

> **NOTE:** I am very recklessly interchanging the terms "array" and "list".  For introductory purposes, this is fine, but they are not always interchangeable terms.

JSON data types include numbers, strings, Booleans, arrays, objects and null.  Let's take a look at how some of these data types are represented above.

1. JSON Strings are enclosed with quotes.  ```"GigabitEthernet0/1"``` is a string.
2. JSON Boolean values are ```true``` and ```false```.
3. JSON Arrays or lists are a comma-separated group enclosed with braces \[\].  The value of ```"address"``` is a list containing two objects--in this example IP/Netmask pairs.

One of the more challenging aspects of working with JSON is understanding how to read or write data from a JSON object.  

For example, given the block of JSON above, how do you access the first IP address?  Let's talk through it and then write it up.  We need to access the object ```data```.  Within ```data```, we need to access the value of ```"ietf-interfaces:interface"```.  Within ```"ietf-interfaces:interface"```, we need to access the value of ```"ietf-ip:ipv4"```.  Wtihin ```"ietf-ip:ipv4"```, we need to access the value of ```"address"```.  Within ```"address"``` we need to access the first object in the array, and extract the value of ```"ip"```.  

So what does that look like?

```data["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"]```

There are many slightly different implementations of JSON, so make sure that you explore the particular implementation you need depending on the programming language you are using. [JSON.org](json.org) is a good place to start.


## YAML

YAML is a markup language used for storing data.  Initially the acroynm stood for *Yet Anotther Markup Language* but now it is considered to be a recursive acronym that stands for *YAML Ain't Markup Language* to clarify that YAML should be used for data storage.  YAML is popular due to its easy readability.  It is a widely used data storage format for Ansible, Python, and other automation uses cases. 

YAML is white space sensitive and makes use indentations, the colon and space ```: ``` for attribute value pairs and the dash ```-``` for list (sequence) elements. Each YAML document is started with three dashes ```---```.  YAML data types fall into the scalar (integer, string), sequence (ordered list), and mappings (unordered key,value pairs). YAML can get more in-depth, but for the purposes of storing data for Ansible playbooks or Python programs, this is a good primer. Let's review the same data represented in our JSON block above formatted into YAML:

```yaml
---
ietf-interfaces:interface:
  name: GigabitEthernet0/1
  description: LAN
  enabled: true
  ietf-ip:ipv4:
    address:
    - ip: 172.16.0.2
      netmask: 255.255.255.0
    - ip: 172.17.0.2
      netmask: 255.255.255.0
```

You'll note that the same data takes up less space, requires less punctuation, and is a bit easier for a human to follow than the JSON above, while still being simple for a machine to parse.  Assuming the above YAML was stored in a variable called "data", the method to access the first IP address from our JSON example, would work the same.

> **NOTE** For the full details on YAML and programming languange-specific implementations, view the [specification](https://yaml.org)

## XML

XML, or Extensible Markup Language, is oldest of the three data structures covered here, released in 1998, but it is still relevant today for many use cases.  One key use case for network automation is model-driven automation with NETCONF and model-driven telemetry with gNOI & gRPC.  NETCONF uses YANG Models, which can be expressed in XML format. XML is also an encoding option for REST APIs. 

> **NOTE** To learn more about Model-Driven Telemetry with NETCONF, see (Jeremy Cohoe's Cisco IOS-XE - YANG based Model Driven Telemetry Lab)[https://github.com/jeremycohoe/cisco-ios-xe-mdt]

XML has a number of formatting rules.  Here are some of the most crucial:

- XML is case sensitive
- All start tags must have end tags
- Elements must be properly nested
- XML declaration is the first statement
- Every document must contain a root element
- Attribute values must have quotation marks

Here is our data formatted into XML:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
 <root>
     <ietf-interfaces:interface>
         <name>GigabitEthernet0/1</name>
         <description>LAN</description>
         <enabled>true</enabled>
         <ietf-ip:ipv4>
             <address>
                 <ip>172.16.0.2</ip>
                 <netmask>255.255.255.0</netmask>
             </address>
             <address>
                 <ip>172.17.0.2</ip>
                 <netmask>255.255.255.0</netmask>
             </address>
         </ietf-ip:ipv4>
     </ietf-interfaces:interface>
 </root>

```

XML has a comparatively high level of overhead, so it is less popular than JSON in modern operations, however there are still many applications for which XML is appropriate or even preferred.  

> **NOTE** To learn more about XML, see the (specification)[https://www.w3.org/TR/xml/]


## Choosing a Data Format

The choice of which of these data formats to use is often based on the specific application. If the application supports all of them, consider the project's requirements on speed, readability and structure (e.g. are schemas and namespaces required).    All else being equal, use the structure that you and your team find most natural to work with.

> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Return to Main Menu**](../README.md)