# JSON YAML XML Explained  [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)

# Why you Need Structured Data

Automation depends on structured data. Data must be stored and transmitted in such a way that a process knows how to read it.  There are many structured data formats, but this tutorial will focus on three common data structures used in network automation: JSON (Javascript Object Notation), YAML (YAML Aint Markup Language), and XML Extensible Markup Language.

# JSON

JSON is a very popular data structure.  It's human and machine readible and commonly used in many programming languages for passing text data.  If you are familiar with the Python programming language, you'll find JSON syntax looks very familiar. JSON formats data as attribute-value pairs and uses curly braces \{\} as an object delimeter.  Let's explore JSON in more detail.


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







> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Return to Main Menu**](../README.md)