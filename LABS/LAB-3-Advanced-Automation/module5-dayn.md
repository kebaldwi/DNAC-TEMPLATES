# DayN Provisioning - In Development

![json](../../ASSETS/COMMON/BUILD/underconstruction.png?raw=true "Import JSON")

> [!WARNING]
> The contents of this lab are not ready for public use. Do not use this lab or attempt to use it until this header is removed entirely from the lab.

### Section 2 - Configuring Network Profile

In this section we will prepare the Network Profile to allow for provisioning of the Greenfield and Brownfield network devices. In order to accomodate the fact that we have two types of templates to use, one for the distribution and one for access, both of which will be used on 9300, we need to be able to effectively choose between the templates for the specific use cases.

In this situation we will inlist the use of **TAGs** to identify the use case for the template and filter accordingly.

#### Step 1 - Create and Apply the Device TAGs

We will Create and Assign **TAGs** to the **ACCESS** switch and the **DISTRO** switch as follows:

   1. Within Cisco Catalyst Center Navigate to **`Provision > Network Devices > Inventory`**      

      ![json](./images/DNAC-NavigateInventory.png?raw=true "Import JSON")

   2. We will **TAG** the device **c9300-1** as **ACCESS**, complete the following:

      1. Select **c9300-1** on the left
      2. Click the **Tag** link and in the menu provided
      3. Enter **`ACCESS`** in the search field for the **TAG** 
      4. Click the option **Create new tag (ACCESS)**   

            ![json](./images/CATC-Inventory-TAG-9300-1-ACCESS.png?raw=true "Import JSON")

   3. We will **TAG** the device **c9300-2** as **DISTRO**, complete the following:

      1. Select **c9300-2** on the left
      2. Click the **Tag** link and in the menu provided
      2. Enter **`DISTRO`** in the search field for the **TAG** 
      3. Click the option **Create new tag (DISTRO)**   

            ![json](./images/CATC-Inventory-TAG-9300-2-DISTRO.png?raw=true "Import JSON")

   4. At this point the two switches **c9300-1** and **c9300-2** should be tagged accordingly as shown:    

      ![json](./images/CATC-Inventory-TAG-9300s-RESULT.png?raw=true "Import JSON")

#### Step 2 - Modify the Network Profile for the DayN Templates

Assign the DayN Templates for both the Greenfield and Brownfield 9300's to a site using the Network Profile. As there is an existing network profile for the site, we **must** reuse that one as you can only have one switching profile associated to a specific site. **(required)** 

We will Modify and Assign **DayN Templates** to the switches using **ACCESS** and **DISTRO** **TAGs** as follows:

   1. Navigate to Network Profiles by selecting **`Design > Network Profiles`**.

      ![json](./images/DNAC-NavigateProfile.png?raw=true "Import JSON")


   2. Click the **Edit** link next to the **CATC Template Lab Floor 1** switching profile created earlier.  

      ![json](./images/DNAC-ProfileEdit.png?raw=true "Import JSON")

   3. Within the Profile Editor, select the **Day-N Template(s)** tab click **⨁ Add Template** 

         ![json](./images/DNAC-ProfileDayNAdd.png?raw=true "Import JSON")   

   4. Within the **Add Template** side tile complete the following:

      For the **`CATC Template Labs DayN Composite Jinja2`** Template do the following:

      1. Select the **`CATC Template Labs DayN Composite Jinja2`** Template from the list as shown
      2. Click the **APPLICABLE DEVICE TAGS** search window 
      3. Select the **ACCESS** tag
      4. The **ACCESS** tag should now appear as shown in the **APPLICABLE DEVICE TAGS** section
      5. Click **Add**

         ![json](./images/DNAC-ProfileDayN-ACCESS.png?raw=true "Import JSON")   

      For the **`c9300-2-Setup-Configuration`** Template do the following:

      1. Select the **`c9300-2-Setup-Configuration`** Template from the list as shown
      2. Click the **APPLICABLE DEVICE TAGS** search window and type **DISTRO**
      3. Select the **DISTRO** tag
      4. The **DISTRO** tag should now appear as shown in the **APPLICABLE DEVICE TAGS** section
      5. Click **Add**

         ![json](./images/DNAC-ProfileDayN-DISTRO.png?raw=true "Import JSON")   

   5. Click **X** to close the **Add Template** window.

         ![json](./images/DNAC-ProfileCloseAddTemplate.png?raw=true "Import JSON")   

   6. You will notice both templates as shown click the **view Device Tag** link on the **`c9300-2-Setup-Configuration`** Template and verify the **DISTRO** tag appears as shown.

      ![json](./images/DNAC-ProfileSuccess-1.png?raw=true "Import JSON")   

   7. You will notice both templates as shown click the **view Device Tag** link on the **`c9300-2-Setup-Configuration`** Template and verify the **DISTRO** tag appears as shown.

      ![json](./images/DNAC-ProfileSuccess-2.png?raw=true "Import JSON")   

   8. Click **Save** to save the modifications to the Network Profile.

      ![json](./images/DNAC-ProfileSuccess.png?raw=true "Import JSON")   

### Section 3 - Greenfield DayN Provisioning Sequence

In this section we will apply a DayN template to the device **c9300-1** which we onboarded through the use of Plug and Play (PnP). This device had no configuration on it and as such we will now expand on the configuration.

#### Step 1 - Provisioning the Device

At this point, Cisco Catalyst Center is set up and ready to provision composite template to the device. This next set of sequences will push the various Network Settings, Services, and DayN Template to the **Greenfield** device.

We will now provision the switch using DayN Templates. To do this, do the following:

   1. Within Cisco Catalyst Center Navigate to **`Provision > Network Devices > Inventory`**.      

      ![json](./images/DNAC-NavigateInventory.png?raw=true "Import JSON")

   2. Put a checkmark next to the device **c9300-1** to be provisioned.
   3. Click the **Actions > Provision > Provision Device** link and walk through the workflow presented:    

      ![json](./images/DNAC-ProvisionBegin.png?raw=true "Import JSON")

      1. The floor was already selected as part of the claim so click **next**    

         ![json](./images/DNAC-ProvisionSite.png?raw=true "Import JSON")

      2. Select **c9300-1** on the left and ensure the two tick boxes at the top of the page are ticked, then click the **SystemManagement-Configuration** tab. Enter `Building10` as the location  

         ![json](./images/DNAC-ProvisionAdvConfig-1.png?raw=true "Import JSON")
      
      3. Click the **Interfaces-Configuration** tab. Select the following as shown:

         1. Vlan Schema: **`A`**  
         1. Access Point Interfaces: **`GigabitEnthernet1/0/2`**  
         1. Then click **Next** to continue

            ![json](./images/DNAC-ProvisionAdvConfig-2.png?raw=true "Import JSON")
      
      4. Review the information to be deployed and click **Deploy**.

         ![json](./images/DNAC-ProvisionDeploy.png?raw=true "Import JSON")

      5. Select **`Generate Configuration Preview`** and then click **Apply** on the Provision Device pop-up screen.

         ![json](./images/DNAC-ProvisionApply.png?raw=true "Import JSON")

   4. The task will be submitted, and the deployment will run. Click on **Work Items** to display the configuration rendered prior to provisioning.

      ![json](./images/DNAC-ProvisionTask.png?raw=true "Import JSON")

   5. The configuration will be rendered, and you can click the preview to show it, and continue the deployment. Within the preview page click **Deploy** and the deployment will run. 

      ![json](./images/DNAC-ProvisionTasking.png?raw=true "Import JSON")

   6. You will be presented with a screen to schedule the deployment, select **Now** and click **Apply**. A screen will pop up after this asking whether you wish to delete the task, click **No** to keep a history.

      ![json](./images/DNAC-ProvisionScheduled.png?raw=true "Import JSON")

      ![json](./images/DNAC-ProvisionScheduled-2.png?raw=true "Import JSON")

   7. You can monitor the deployment on the Inventory page. Return to the Inventory via the menu, and change to the **Provisioning** Focus as shown.

      ![json](./images/DNAC-InventoryProvision.png?raw=true "Import JSON")
       
At this point, we have onboarded a device and successfully pushed configuration via Onboarding and DayN Templates. Our DayN automation for the Greenfield device used a **Composite** template composed of **Regular** templates. Take some time and review the templates and logic used.

> [!CAUTION]
> If you populate the UI with settings, those parameters should **NOT** be in your templates as they will **conflict**, and the deployment through provisioning will fail. While it is easy to populate these settings, it is best to test with a switch to see what configuration is pushed.

## Summary

The next step will be to build Composite Template to include the Day N regular templates created in this lab for the switches to be pushed out to the various devices in the network infrastructure. 

## Summary

Congratulations you have completed xxx

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Continue to Rest API Deployment Module**]()

> [**Return to Lab Menu**](./README.md)