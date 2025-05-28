# DayN Provisioning

## Configuring Network Profile

In this section we will prepare the Network Profile to allow for provisioning of the Greenfield and Brownfield network devices. In order to accomodate the fact that we have two types of templates to use, one for the distribution and one for access, both of which will be used on 9300, we need to be able to effectively choose between the templates for the specific use cases.

In this situation we will inlist the use of **TAGs** to identify the use case for the template and filter accordingly.

### Step 1 - Create and Apply the Device TAGs

We will Create and Assign **TAGs** to the **ACCESS** switch and the **DISTRO** switch as follows:

   1. Within Cisco Catalyst Center Navigate to **`Provision > Network Devices > Inventory`**      

      ![json](../../ASSETS/LABS/CATC/MENU/catc-menu-3.png?raw=true "Import JSON")

   2. We will **TAG** the device **c9300-1** as **ACCESS**, complete the following:

      1. Select **c9300-1** on the left
      2. Click the **Tag** link and in the menu provided
      3. Enter **`ACCESS`** in the search field for the **TAG** 
      4. Click the option **Create new tag (ACCESS)**   

      ![json](../../ASSETS/LABS/DAY0DAYN/LAB3-DAYN-PROVISION/c9300-1-provision-1.png?raw=true "Import JSON")

   3. At this point the switch **c9300-1** should be tagged accordingly as shown:    

      ![json](../../ASSETS/LABS/DAY0DAYN/LAB3-DAYN-PROVISION/c9300-1-provision-2.png?raw=true "Import JSON")

### Step 2 - Modify the Network Profile for the DayN Templates

Assign the DayN Templates for both the Greenfield and Brownfield 9300's to a site using the Network Profile. As there is an existing network profile for the site, we **must** reuse that one as you can only have one switching profile associated to a specific site. **(required)** 

We will Modify and Assign **DayN Templates** to the switches using **ACCESS** and **DISTRO** **TAGs** as follows:

   1. Navigate to Network Profiles by selecting **`Tools > Template Hub`**.

      ![json](../../ASSETS/LABS/CATC/MENU/catc-menu-5.png?raw=true "Import JSON")

   2. Use the filter on the Left to Filter for the **DayN-Templates-J2** Project and click **Attach** link for the composite **PnP-Templates-J2** template created earlier.  

      ![json](../../ASSETS/LABS/TEMPLATEEDITOR/DAYNTEMPLATE/Composite/mod-dayn-composite-14.png?raw=true "Import JSON")

   3. Select the site **CATC Templates Lab Floor 1** and click **Save** 

      ![json](../../ASSETS/LABS/TEMPLATEEDITOR/DAYNTEMPLATE/Composite/mod-dayn-composite-15.png?raw=true "Import JSON")

## DayN Provisioning

In this section we will apply a DayN template to the device **c9300-1** which we onboarded through the use of Plug and Play (PnP). This device had no configuration on it and as such we will now expand on the configuration.

### Step 1 - Provisioning the Device

At this point, Cisco Catalyst Center is set up and ready to provision composite template to the device. This next set of sequences will push the various Network Settings, Services, and DayN Template to the **Greenfield** device.

We will now provision the switch using DayN Templates. To do this, do the following:

   1. Within Cisco Catalyst Center Navigate to **`Provision > Network Devices > Inventory`**.      

      ![json](../../ASSETS/LABS/CATC/MENU/catc-menu-3.png?raw=true "Import JSON")

   2. Put a checkmark next to the device **c9300-1** to be provisioned.
   3. Click the **Actions > Provision > Provision Device** link and walk through the workflow presented:    

      ![json](../../ASSETS/LABS/DAY0DAYN/LAB3-DAYN-PROVISION/c9300-1-provision-3.png?raw=true "Import JSON")

      1. The floor was already selected as part of the claim so click **next**    

         ![json](../../ASSETS/LABS/DAY0DAYN/LAB3-DAYN-PROVISION/c9300-1-provision-4.png?raw=true "Import JSON")

      2. Select **c9300-1** on the left and ensure the two tick boxes at the top of the page are ticked, then click **next**  

         ![json](../../ASSETS/LABS/DAY0DAYN/LAB3-DAYN-PROVISION/c9300-1-provision-5.png?raw=true "Import JSON")
         
      3. Review the information to be deployed and click **Deploy**.

         ![json](../../ASSETS/LABS/DAY0DAYN/LAB3-DAYN-PROVISION/c9300-1-provision-6.png?raw=true "Import JSON")

      4. With **`Now`** selected, click **Apply** on the Provision Device pop-up screen.

         ![json](../../ASSETS/LABS/DAY0DAYN/LAB3-DAYN-PROVISION/c9300-1-provision-7.png?raw=true "Import JSON")

   4. You can monitor the deployment on the Inventory page. Return to the Inventory via the menu, and change to the **Provisioning** Focus as shown.

      ![json](../../ASSETS/LABS/DAY0DAYN/LAB3-DAYN-PROVISION/c9300-1-provision-8.png?raw=true "Import JSON")
       
## Summary

Congratulations, at this point we have onboarded a device and successfully pushed configuration via Onboarding and DayN Templates. Our DayN automation for the Greenfield device used a **Composite** template composed of **Regular** templates. Take some time and review the templates and logic used.

> [!CAUTION]
> If you populate the UI with settings, those parameters should **NOT** be in your templates as they will **conflict**, and the deployment through provisioning will fail. While it is easy to populate these settings, it is best to test with a switch to see what configuration is pushed.

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Return to Lab Menu**](./README.md)