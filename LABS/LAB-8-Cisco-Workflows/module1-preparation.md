# Preparation - Getting Started Guide

## Overview

This module 

## General Information

As you may recall, 

We will be utilizing the lab in this manner:

![json](./images/DCLOUD_Topology_PnPLab2.png?raw=true "Import JSON")

## Lab Credentials:

| Platform:       | IP Address:    | Username | Password   | 
|-----------------|----------------|----------|------------|
| something       | 198.18.129.100 | admin    | C1sco12345 |

## Catalyst Center and ISE Integration

In this lab our focus changes 

### Step 1 - Prepare ISE for Catalyst Center Integration

You must have a Meraki Account that has full Organizational Administrator permissions for an
Organization that is hosted in NORTH AMERICA for this lab. If you already have an account with full
Organizational Administrator permissions on an account in North America, you only need to complete
step 3, Enable Automate Workflows. If you do not, there are 3 steps that you will need to complete before
you can start the lab.
1. Create a Meraki Organization
2. Create a Meraki Network
3. Enable Automate Workflows
Create a Meraki Organization in North America
If you do not have a Meraki account with these permissions hosted in North America, you can create one
here: https://account.meraki.com/login/new_account
NOTE: You MUST select North America as your region!
If you already have a Meraki account, you can use that, but DO NOT USE Cisco SSO that only has access
to the Cisco demo account.
Later, when you sign in, choose Sign in to personal account. Do
not select Sign in with Cisco SSO.
Create a Network
If you have created a new Meraki Organization, you will need to create a placeholder network.
NOTE: This step is not required if you already have a Meraki Organization with at least one network.
On the left hand menu, select Network and Create a network
Enter a Network name and click Create network. Note: This network will not be used in the lab.
Enable Automate Workflows
Once you are logged in to your new Meraki account, select Organization -> Early Access
In the Early Access window, enable AI Assistant and Automate Workflows.
NOTE: You will get a Opt in settings pop up, just click on Save.

## Summary

The next step ... 

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Continue to module 2 Orientation**](./module2-orientation.md)

> [**Return to LAB Menu**](./README.md)