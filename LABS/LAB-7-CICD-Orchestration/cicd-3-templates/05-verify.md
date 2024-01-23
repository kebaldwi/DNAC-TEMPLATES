# Template Deployment Verification

To verify that the template was deployed successfully, we will inspect the template editor within Cisco Catalyst Center.

Follow these steps:

1. If Cisco Catalyst Center is not already open, use a browser and navigate to `https://198.18.129.100`, where you may see an SSL Error displayed as depicted. Click the `Proceed to https://192.18.129.100 (unsafe)` link to continue if presented

   ![json](./images/DNAC-SSLERROR.png?raw=true "Import JSON")

2. If required, log into Cisco Catalyst Center using the username of `admin` and the password `C1sco12345`.

   ![json](./images/DNAC-Login.png?raw=true "Import JSON")

3. When the Cisco Catalyst Center Dashboard is displayed, Click the  icon to display the menu'

   ![json](./images/DNAC-Menu.png?raw=true "Import JSON")

4. Select `Tools>Template Editor` from the menu to continue.

   ![json](./images/DNAC-Menu-TemplateEditor.png?raw=true "Import JSON")

5. Expand the Project with your Area Name on the left to show your specific Project with the template, then select it and view it on the right. 

   ![json](./images/Templates_editor.png?raw=true "Import JSON")

6. Within the Inventory select the two switches, then `Actions>Other>Command Runner` and run the two commands shown:

   ![json](./images/command_run1.png?raw=true "Import JSON")
   ![json](./images/command_run2.png?raw=true "Import JSON")

7. Open a ssh connection to the C9300-1 switch from the script server to verify the deployment of the configuration:

```SHELL
   ssh netadmin@198.19.1.2
```
   - when prompted enter the password: `C1sco12345`

> [**Next Section**](./06-summary.md)