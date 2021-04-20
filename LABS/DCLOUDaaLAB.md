# DCLOUD as a LAB [![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kebaldwi/DNAC-TEMPLATES)
## Overview
This section will explain which lab to utilize within the DCLOUD enviroment to run these LAB's. It will also discuss a customer POC environemnt and what can be done to successfully run these sections within a customer enviroment for localized testing.

## Disclaimer
Various labs are designed for use in the DCLOUD environment but can be easily modified for use elsewhere. What is important to realize is the impact for each type of test. For instance in the ***PnP Preparation*** lab we go through discovery methods such as ***option 43*** and ***DNS Discovery***. If we were to use the DHCP option 43 and place that in the server options on the DHCP server then it would affect multiple scopes. **Care** is required therefore to ensure you do not get unexpected results. Similarly with ***DNS Discovery*** if the sub domain used was available to all devices then more than one device would be able to discover DNA Center. This may be good for production in the future but detrimental during testing.

If you found this set of Labs helpful please fill in comments and [give feedback](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

