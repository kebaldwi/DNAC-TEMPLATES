# Hierarchy Build Python Pipeline

The **Python** programming language is a powerful tool for building programs related to **REST-API** calls and allows us to utilize several features to accomplish everyday tasks. In this section of the tutorial, we will use a simple REST-API set, which has been grouped into a **Python** program. We will then use these programs to automate the provisioning of the hierarchy that may be modified in the **CSV** and pushed to Cisco Catalyst Center.

## Deploy Hierarchy Python Program

These **Python** program files are groupings of API, which allow us to have workflows defined for specific tasks. Programs also have modules included in them which allows for the reusability of code. 

To investigate this collection, follow these steps:

1. On the **script server** do the following:

   1. Open the program using NANO in Read Only

```SHELL
      sudo nano -v /root/PYTHON-LAB/deploy_hierarchy.py
```

   2. As you scroll through the lines of the program take note of the following:

      - **import** statements for dependant modules and libraries
      - **YAML** a YAML file is used for environment settings
      - **definitions** functions are defined to build API interactions 
      - **main** the sequence of the definitions which are called

      ![json](./assets/hierarchy-python.png?raw=true "Import JSON")
   
      Let's examine the **Python Program** in more detail:

      ```py
      def main():
          """
          This app will create a new site specified in the param provided.
          """
      
          # logging basic
          logging.basicConfig(level=logging.INFO)
      
          current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
          logging.info('App "deploy_hierarchy.py" Start, ' + current_time)
      
          # parse the input data
          with open('/root/PYTHON-LAB/DNAC-Design-Settings.csv', 'r') as file:
              reader = csv.DictReader(file)
      ```

      In the first block of code in **main** we open the CSV file and start looping through the data.

      ```py
              #iniialize variables
              parent_name = ''
              area_name = ''
              building_name = ''  
              address = ''   
              floor_name = ''
      
              # loop through the csv file
              for row in reader:
                  parent_name = row['HierarchyParent']
                  area_name = row['HierarchyArea']
                  building_name = row['HierarchyBldg']
                  floor_name = row['HierarchyFloor']
                  address = row['HierarchyBldgAddress']
      
                  # Create the site hierarchy
                  #site_hierarchy = 'Global/' + area_name + '/' + building_name + '/' + floor_name
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
      ```

      In the next block of code above in **main** we read from each row in the CSV file.

      ```py           
                  # Create a DNACenterAPI "Connection Object"
                  dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL,          version='2.2.2.3', verify=False)
              
                  # get Cisco DNA Center Auth token
                  dnac_auth = get_dnac_token(DNAC_AUTH)
              
                  # create a new fabric at site
                  logging.info('  Working on new campus at site: ' + site_hierarchy)
      
                  json_response = get_site_hierarchy(dnac_auth)
                  json_response = json.dumps(json_response)
      ```

      We then open a connection to Catalyst Center and pull the site hierarchy reading it.
      Then Progammatically below we determine if the elements in the CSV file are reflected in the hierarchy. If they are we explain they are and move to the next line. If an element is not there we pragmatically add it.

      ```py           
      
                  if area_name:
                      type = 'area'
                      parentHierarchy = parent_name
                      tgt_hierarchy = (f'{parent_name}/{area_name}')
                      if tgt_hierarchy in json_response:
                          logging.info('  Site campus area already exists, skipping creation.')
                      else:
                          response = create_site(dnac_auth, type, parentHierarchy, area_name, address)
                          logging.info('  Created new campus area at site: ' + site_hierarchy)
                  if building_name:
                      type = 'building'
                      parentHierarchy = (f"{parent_name}/{area_name}")
                      tgt_hierarchy = (f'{parent_name}/{area_name}/{building_name}')
                      if tgt_hierarchy in json_response:
                          logging.info('  Site campus building already exists, skipping creation.')
                      else:
                          response = create_site(dnac_auth, type, parentHierarchy, building_name,          address)
                          logging.info('  Created new campus building at site: ' + site_hierarchy)
                  if floor_name:
                      type = 'floor'
                      parentHierarchy = (f"{parent_name}/{area_name}/{building_name}")
                      tgt_hierarchy = (f'{parent_name}/{area_name}/{building_name}/{floor_name}')
                      if tgt_hierarchy in json_response:
                          logging.info('  Site campus floor already exists, skipping creation.')
                      else:
                          response = create_site(dnac_auth, type, parentHierarchy, floor_name, address)
                          logging.info('  Created new campus floor at site: ' + site_hierarchy)
                  time.sleep(15)
                  address = ''
           
          date_time = str(datetime.now().replace(microsecond=0))
          logging.info('  App "deploy_hierarchy.py" end, : ' + date_time)
      ```

   3. This set of **REST-API** are built utilizing the developer site [**developer.cisco.com/docs/dna-center/**](https://developer.cisco.com/docs/dna-center/). This documentation is kept up to date with the latest **REST-API**.

> [**Next Section**](./05-deploy.md)
