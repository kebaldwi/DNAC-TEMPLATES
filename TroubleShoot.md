# Troubleshooting Templates [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
This section will describe the various advanced techniques used to troubleshoot the templating engine and the provisioning of a device via Day0|Onboarding and DayN Templates as deployed by DNA Center. While the methods described here are useful, they are not the only methods for troubleshooting and what is given here is a set of methods I use to troubleshoot templates. 

The assumption will be that the device is able to be provisioned with an IP address via DHCP, and that it is able to land in the PNP section of the provisioning page within DNA Center. If this is not the case please see the section on PNP Workflow in the previous section.

Below will be examples of various use cases that could be implemented.

### Template not deployed on target device
The assum
```
#set( $integer = 0 )
#set( $native_vlan = $integer.parseInt($native_vlan_bind) )
#set( $data_vlan = $native_vlan + 10 )
```

