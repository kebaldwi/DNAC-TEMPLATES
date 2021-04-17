# Troubleshooting Templates [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
This section will describe the various advanced techniques used to troubleshoot the templating engine and the provisioning of a device via Day0|Onboarding and DayN Templates as deployed by DNA Center. While the methods described here are useful, they are not the only methods for troubleshooting and what is given here is a set of methods I use to troubleshoot templates. 

The assumption will be that the device is able to be provisioned with an IP address via DHCP, and that it is able to land in the PNP section of the provisioning page within DNA Center. If this is not the case please see the section on PNP Workflow in the previous section wich explains the preliminary steps required for Zero Touch Provisioning [PnP Workflow](./PnP-Workflow.md#pnp-workflow).

Below will be examples of various use cases that could be implemented.

### Template not deployed on target device
The assumption is that no errors were visible in the template and that it seems to either partially work or not at all on the target device. The second assumption is that we are using a DayN template. Remember the Onboarding template should be kept to minimal code, so that it can deal with many use case devices, and so that you can reuse code more effectively in the DayN projects.

In this situation it helps to understand where in the template we are experiencing an issue. To find that deploy this code temporarily on the device. This will allow the commands deployed from the template 

```
event manager applet CLI_COMMANDS-->
 event cli pattern ".*" sync no skip no
 action 1 syslog msg "$_cli_msg"
!
term mon
```
This will allow for the logs to reflect the changes in an ongoing manner as deployed line by line from DNA Center and it will be very granular and clear where the template stopped. Many thanks to Joshua Bronikowski.

The next step will be to look at the last logical constructs within the template and ensure that there are no missing end statements and or other formatting errors that might be causing issues. The other thing to watch out for is integers versus strings. If we attempt to incorrectly apply arithmatical expressions to string variables that can also cause issues on deployment which might not show up in the simulations.


