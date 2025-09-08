# Preparation - Getting Started Guide

## Module Overview

You must have a Meraki Account that has full Organizational Administrator permissions for an Organization that is hosted in NORTH AMERICA to be able to complete this lab. 

If you already have an account with full Organizational Administrator permissions on an account in North America, you will only need to complete [Step 3](#step-3---enable-automate-workflows) and Enable Automate Workflows.

If you do not, complete all of the following steps.

### Step 1 - Create a Meraki Organization

1. If you do not have a Meraki account with these permissions hosted in North America,  create one here: [account.meraki.com](https://account.meraki.com/login/new_account)

   ![json](../../ASSETS/LABS/WORKFLOWS/CreateAccount1.png?raw=true "Import JSON")

> [!NOTE]
> You MUST select North America as your region!

2. If you already have a Meraki account, you can use that. If you are a Cisco Employee **DO NOT USE** the Cisco SSO as that only has access to the Cisco demo account.

   ![json](../../ASSETS/LABS/WORKFLOWS/CreateAccount2.png?raw=true "Import JSON")

3. When you sign in, choose Sign in to personal account. Do
not select Sign in with Cisco SSO.

   ![json](../../ASSETS/LABS/WORKFLOWS/CreateAccount3.png?raw=true "Import JSON")

### Step 2 - Create a Meraki Network

If you have created a new Meraki Organization, you will need to create a placeholder network.

> [!NOTE]
> This step is not required if you already have a Meraki Organization with at least one network.

1. On the left hand menu, select Network and Create a network

   ![json](../../ASSETS/LABS/WORKFLOWS/CreateNetwork1.png?raw=true "Import JSON")

2. Enter a Network name and click Create network. 

   ![json](../../ASSETS/LABS/WORKFLOWS/CreateNetwork2.png?raw=true "Import JSON")

> [!NOTE]
>  This network will not be used in the lab.

### Step 3 - Enable Automate Workflows

Once you are logged in to your new Meraki account:

1. Select **`Organization > Early Access`**

   ![json](../../ASSETS/LABS/WORKFLOWS/EnableWorkflows1.png?raw=true "Import JSON")

2. In the Early Access window, enable AI Assistant and Automate Workflows.

   ![json](../../ASSETS/LABS/WORKFLOWS/EnableWorkflows2.png?raw=true "Import JSON")

   ![json](../../ASSETS/LABS/WORKFLOWS/EnableWorkflows3.png?raw=true "Import JSON")

> [!NOTE]
> You will get a Opt in settings pop up, just click on Save.

## Summary

Congratulations, you are now ready to make use of Cisco Workflows, in the next section we will take a look at UI and the general functionality of the platform.

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Continue to module 2 Orientation**](./module2-orientation.md)

> [**Return to LAB Menu**](./README.md)