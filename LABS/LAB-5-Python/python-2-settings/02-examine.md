# Deploy Settings and Credentials via Python

The **Python** programming language is a powerful tool for building programs related to **REST-API** calls and allows us to utilize several features to accomplish everyday tasks. In this section of the tutorial, we will use a simple REST-API set, which has been grouped into a **Python** program. We will then use these programs to automate the provisioning of the hierarchy with settings and credentials that may be modified in the **CSV** and pushed to Catalyst Center.

## Deploy Settings and Credentials Python Program

These **Python** program files are groupings of API, which allow us to have workflows defined for specific tasks. Programs also have modules included in them which allows for the reusability of code. 

To investigate this collection, follow these steps:

1. On the **script server** do the following:

   1. Open the program using NANO in Read Only

```SHELL
      sudo nano -v /root/PYTHON-LAB/deploy_settings.py
```

   2. As you scroll through the lines of the program take note of the following:

      - **import** statements for dependant modules and libraries
      - **YAML** a YAML file is used for environment settings
      - **definitions** functions are defined to build API interactions 
      - **main** the sequence of the definitions which are called

      ![json](../assets/settings-python.png?raw=true "Import JSON")
   
      Let's examine the **Python Program** in more detail:

      ```py
      def main():
          """
          This app will add settings to the site specified with the param provided.
          """
      
          # logging basic
          logging.basicConfig(level=logging.INFO)
      
          responsecheck = "has been accepted"
          current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
          logging.info('App "deploy_settings.py" Start, ' + current_time)
      
          # parse the input data
          with open('/root/PYTHON-LAB/DNAC-Design-Settings.csv', 'r') as file:
              reader = csv.DictReader(file)
      ```

      In the first block of code above in **main** we open the CSV file and start looping through the data.

      ```py
              #iniialize variables
              parent_name = ''
              area_name = ''
              building_name = ''  
              address = ''   
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
                  
                  #get the site settings
                  domain_name = row.get('domainName','')
                  dns_server_primary = row.get('dnsServer1','')
                  dns_server_secondary = row.get('dnsServer2','')
                  dhcp_server_primary = row.get('dhcpServer1','')
                  dhcp_server_secondary = row.get('dhcpServer2','')
                  snmp_server = row.get('snmpServer','')
                  snmp_boolean = row.get('snmpBoolean','')
                  syslog_server = row.get('syslogServer','')
                  syslog_boolean = row.get('syslogBoolean','')
                  netflow_server = row.get('netflowServer','')
                  netflow_port = row.get('netflowPort','')
                  netflow_boolean = row.get('netflowBoolean','')
                  ntp_server_primary = row.get('ntpServer1','')
                  ntp_server_secondary = row.get('ntpServer2','')
                  timezone = row.get('timeZone','')
                  aaa_server = row.get('aaaEndpointServer','')
                  aaa_address = row.get('aaaEndpointIpAddress','')
                  aaa_protocol = row.get('aaaEndpointProtocol','')
                  aaa_secret = row.get('aaaEndpointSharedSecret','')
                  dcloud_user = row.get('DcloudUser','')
                  dcloud_password = row.get('DcloudPwd','')
                  dcloud_snmp_RO_desc = row.get('DcloudSnmpRO-Desc','')
                  dcloud_snmp_RO = row.get('DcloudSnmpRO','')
                  dcloud_snmp_RW_desc = row.get('DcloudSnmpRW-Desc','')
                  dcloud_snmp_RW = row.get('DcloudSnmpRW','')
                  dcloud_netconf = row.get('DcloudNetconf','')
                  banner_message = row.get('bannerMessage','')
                  banner_boolean = row.get('bannerBoolean','')
      ```

      In the next block of code above in **main** we read from each row in the CSV file.

      ```py                 
                  # get Cisco DNA Center Auth token
                  dnac_auth = get_dnac_token(DNAC_AUTH)
      
                  # Get the target site id 
                  TargetSiteId = get_target_site_id(dnac_auth, parent_name, area_name, building_name, floor_name)
                  #print(f"TargetSiteId: {TargetSiteId}")
                  # Create the site settings
                  response, status_code = create_site_settings(dnac_auth, TargetSiteId, domain_name, dns_server_primary,       dns_server_secondary, dhcp_server_primary, dhcp_server_secondary, snmp_server, snmp_boolean, syslog_server,       syslog_boolean, netflow_server, netflow_port, netflow_boolean, ntp_server_primary, ntp_server_secondary,       timezone, banner_message, banner_boolean, aaa_server, aaa_address, aaa_protocol, aaa_secret)
                  if responsecheck in response['message'] and status_code == 202:
                      logging.info('Site Settings successfully created for ' + site_hierarchy)
                  else:
                      logging.info('Site Settings failed to create for ' + site_hierarchy)
                  
                  # Get the site credentials
                  while True:
                      response, status_code = get_credentials(dnac_auth)
                      #print(f"Credentials: {response}")
                      # Get the site credential cli id
                      flag = False
                      if response['cli'] == []:
                          create_credentials(dnac_auth, dcloud_user, dcloud_password)
                          logging.info('CLI Credentials created for ' + site_hierarchy)
                          flag = False
                      if response['snmp_v2_read'] == []:
                          create_credentials(dnac_auth, '', '', dcloud_snmp_RO_desc, dcloud_snmp_RO)
                          logging.info('SNMP RO Credentials created for ' + site_hierarchy)
                          flag = False
                      if response['snmp_v2_write'] == []:
                          create_credentials(dnac_auth, '', '', '', '', dcloud_snmp_RW_desc, dcloud_snmp_RW)
                          logging.info('SNMP RW Credentials created for ' + site_hierarchy)
                          flag = False
                      time.sleep(15)
                      response, status_code = get_credentials(dnac_auth)
                      #print(f"Credentials: {response}")
                      for i in range(len(response['cli'])):
                          if response['cli'][i]['description'] == dcloud_user:
                              dcloud_user_id = response['cli'][i]['id']
                              #print(f"cli id: {dcloud_user_id}")
                              logging.info('CLI Credentials exist for ' + site_hierarchy)
                              flag = True
                              break
                          elif response['cli'][i]['description'] != dcloud_user and flag != True and i == len(response['cli'])       - 1:
                              create_credentials(dnac_auth, dcloud_user, dcloud_password)
                              logging.info('CLI Credentials created for ' + site_hierarchy)
                              flag = False
                      # Get the site credential snmp RO id
                      flag = False
                      for i in range(len(response['snmp_v2_read'])):
                          if response['snmp_v2_read'][i]['description'] == dcloud_snmp_RO_desc:
                              dcloud_snmp_RO_id = response['snmp_v2_read'][i]['id']
                              #print(f"snmp RO id: {dcloud_snmp_RO_id}")
                              logging.info('SNMP RO Credentials exist for ' + site_hierarchy)
                              flag = True
                              break
                          elif response['snmp_v2_read'][i]['description'] != dcloud_snmp_RO_desc and flag != True and i == len      (response['snmp_v2_read']) - 1:
                              create_credentials(dnac_auth, '', '', dcloud_snmp_RO_desc, dcloud_snmp_RO)
                              logging.info('SNMP RO Credentials created for ' + site_hierarchy)
                              flag = False
                      # Get the site credential snmp RW id
                      flag = False
                      for i in range(len(response['snmp_v2_write'])):
                          if response['snmp_v2_write'][i]['description'] == dcloud_snmp_RW_desc:
                              dcloud_snmp_RW_id = response['snmp_v2_write'][i]['id']
                              #print(f"snmp RW id: {dcloud_snmp_RW_id}")
                              logging.info('SNMP RW Credentials exist for ' + site_hierarchy)
                              flag = True
                              break
                          elif response['snmp_v2_write'][i]['description'] != dcloud_snmp_RW_desc and flag != True and i == len      (response['snmp_v2_write']) - 1:
                              create_credentials(dnac_auth, '', '', '', '', dcloud_snmp_RW_desc, dcloud_snmp_RW)
                              logging.info('SNMP RW Credentials created for ' + site_hierarchy)
                              flag = False
                      break
                  # Set the site credentials
                  try:
                      logging.info(f"Attempting to assign site credentials for site ID: {TargetSiteId}")
                      response, status_code = assign_site_credentials(dnac_auth, TargetSiteId,          dcloud_user_id, dcloud_snmp_RO_id, dcloud_snmp_RW_id)
                      #logging.info(f"Assign Site Credentials Response: {response}, Status Code:          {status_code}")
                      if responsecheck in response['message'] and status_code == 202:
                          logging.info('Credentials successfully set for ' + site_hierarchy)
                      else:
                          logging.info('Credentials failed to set for ' + site_hierarchy)
                  except Exception as e:
                      logging.error(f"Error assigning site credentials: {str(e)}")
                  time.sleep(15)
                  address = ''     
      ```

      We then open a connection to Catalyst Center and Progammatically above we program the settings and credentials to the sites in the hierarchy.

      ```py           
          date_time = str(datetime.now().replace(microsecond=0))
          logging.info('  App "deploy_settings.py" end, : ' + date_time)
      
      if __name__ == '__main__':
          sys.exit(main()
      ```

   3. This set of **REST-API** are built utilizing the developer site [**developer.cisco.com/docs/dna-center/**](https://developer.cisco.com/docs/dna-center/). This documentation is kept up to date with the latest **REST-API**.

> [**Next Section**](./03-deploy.md)