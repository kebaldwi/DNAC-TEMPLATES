# Device Discovery via Python

The **Python** programming language is a powerful tool for building programs related to **REST-API** calls and allows us to utilize several features to accomplish everyday tasks. In this section of the tutorial, we will use a simple REST-API set, which has been grouped into a **Python** program. We will then use these programs to automate device discovery for devices within the network and assign them to the correct tier within the hierarchy within Catalyst Center.

## Device Discovery Python Program

These **Python** program files are groupings of API, which allow us to have workflows defined for specific tasks. Programs also have modules included in them which allows for the reusability of code. 

To investigate this collection, follow these steps:

1. On the **script server** do the following:

   1. Open the program using NANO in Read Only

```SHELL
      sudo nano -v /root/PYTHON-LAB/device_discovery.py
```

   2. As you scroll through the lines of the program take note of the following:

      - **import** statements for dependant modules and libraries
      - **YAML** a YAML file is used for environment settings
      - **definitions** functions are defined to build API interactions 
      - **main** the sequence of the definitions which are called

      ![json](../assets/discovery-python.png?raw=true "Import JSON")
   
      Let's examine the **Python Program** in more detail:

      ```py
      def main():
          """
          This app will create a new discovery if the devices in the file do not exist in the inventory
          """
      
          # logging basic
          logging.basicConfig(level=logging.INFO)
      
          current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
          date_time_str = str(datetime.now().strftime('%m-%d-%Y_%H-%M-%S'))
          responsecheck = "has been accepted"
          logging.info('  App "device_discovery.py" run start, ' + current_time)
      
          # parse the input data
          with open('/root/PYTHON-LAB/DNAC-Design-Settings.csv', 'r') as file:
              reader = csv.DictReader(file)
      ```

      In the first block of code above in **main** we open the CSV file and start looping through the data.

      ```py
              # iniialize variables
              parent_name = ''
              area_name = ''
              building_name = ''  
              floor_name = ''
      
              # loop through the csv file
              for row in reader:
                  # get the site hierarchy
                  parent_name = row.get('HierarchyParent','')
                  area_name = row.get('HierarchyArea','')
                  building_name = row.get('HierarchyBldg','')
                  floor_name = row.get('HierarchyFloor','')
                  address = row.get('HierarchyBldgAddress','')
      
                  site_hierarchy = 'Global/'
                  if area_name:
                      site_hierarchy += area_name + '/'
                  if building_name:
                      site_hierarchy += building_name + '/'
                  if floor_name:
                      site_hierarchy += floor_name
                  # Remove trailing slash if it exists
                  if site_hierarchy.endswith('/'):
                      site_hierarchy = site_hierarchy[:-1]
                  
                  #get the device ip and credentials
                  device_list = row.get('DeviceList','')
                  dcloud_user = row.get('DcloudUser','')
                  dcloud_password = row.get('DcloudPwd','')
                  dcloud_snmp_RO_desc = row.get('DcloudSnmpRO-Desc','')
                  dcloud_snmp_RO = row.get('DcloudSnmpRO','')
                  dcloud_snmp_RW_desc = row.get('DcloudSnmpRW-Desc','')
                  dcloud_snmp_RW = row.get('DcloudSnmpRW','')
      ```

      In the next block of code above in **main** we read from each row in the CSV file.

      ```py                 
                  if device_list:
                      # get Cisco DNA Center Auth token
                      dnac_auth = get_dnac_token(DNAC_AUTH)
          
                      # Get the target site id 
                      TargetSiteId = get_target_site_id(dnac_auth, parent_name, area_name, building_name, floor_name)
                      # Get the site credentials
                      dcloud_user_id, dcloud_snmp_RO_id, dcloud_snmp_RW_id = get_site_credentials(dnac_auth, dcloud_user,       dcloud_snmp_RO_desc, dcloud_snmp_RW_desc)
                      response = get_netconf_credential(dnac_auth)
                      dcloud_netconf_id = response[0]['response'][0]['id']
          
                      # ERROR HANDLING on credentials
                      if dcloud_user_id == "ERROR" or dcloud_snmp_RO_id == "ERROR" or dcloud_snmp_RW_id == "ERROR":
                          logging.info('CLI Credentials not found - repairing')
                          dcloud_user_id, dcloud_snmp_RO_id, dcloud_snmp_RW_id = create_site_credentials(dnac_auth,       TargetSiteId, dcloud_user, dcloud_password, dcloud_snmp_RO_desc, dcloud_snmp_RO, dcloud_snmp_RW_desc,       dcloud_snmp_RW)
                              
                      # Create the discovery if device_list is not empty and the device is not in the inventory
                      if device_list:
                          # First see if the device is in the inventory
                          device_inventory = get_device_list()
                          devices = device_list.split(',')
                          device_missing = []
      
                          for device in devices:
                              if device not in device_inventory:
                                  # Create the discovery
                                  device_missing.append(device)
                                  logging.info('    Device ' + device + ' needs to be added to inventory')
                              else:
                                  logging.info('    Device ' + device + ' already exists in inventory')
                          if device_missing:
                              response = create_discovery(dnac_auth, site_hierarchy, device_missing, dcloud_user_id,       dcloud_snmp_RO_id, dcloud_snmp_RW_id, dcloud_netconf_id)
                              response = json.dumps(response)
                              if 'taskId' in response:
                                  logging.info('    Discovery successfully created for ' + str(device_missing))
                              else:
                                  logging.info('    Discovery failed to create for ' + str(device_missing))
                              time.sleep(15)
                          logging.info('    *** Waiting 5 mins for Discovery to finish ***')
                          time.sleep(300)
                          # assign the device to the site
                          response, status_code = assign_device(dnac_auth, TargetSiteId, device_list) 
                          if responsecheck in response['message'] and status_code == 202:
                              logging.info('    Device successfully assigned to ' + site_hierarchy)
                          else:
                              logging.info('    Device failed to assign to ' + site_hierarchy)
                          time.sleep(15)
      ```

      We then open a connection to Catalyst Center and Progammatically above we program the device discovery and subsequently add the discovered devices to the sites in the hierarchy.

      ```py           

          #get_device_inventory()
          date_time = str(datetime.now().replace(microsecond=0))
          logging.info('  App "device_discovery.py" end, : ' + date_time)
      
      if __name__ == '__main__':
          sys.exit(main())
      ```

   3. This set of **REST-API** are built utilizing the developer site [**developer.cisco.com/docs/dna-center/**](https://developer.cisco.com/docs/dna-center/). This documentation is kept up to date with the latest **REST-API**.

> [**Next Section**](./03-deploy.md)