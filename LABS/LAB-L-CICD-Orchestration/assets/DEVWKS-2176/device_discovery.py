#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2022 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Keith Baldwin SE, CA-CoE"
__email__ = "kebaldwi@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2022 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import json
import logging
import os
import time
import yaml
import base64
import requests
import datetime

from dnac_api_kb import *
from pprint import pprint
from github import *
from pathlib import Path  # used for relative path to "templates_jenkins" folder

from dnacentersdk import DNACenterAPI
#from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth  # for Basic Auth

#load_dotenv('environment.env')

# project path
project_details_path = Path(__file__).parent/'../DEVWKS-2176/project_details.yml'
with open(project_details_path, 'r') as file:
    project_data = yaml.safe_load(file)
DNAC_URL = 'https://' + project_data['dna_center']['ip_address']
DNAC_USER = project_data['dna_center']['username']
DNAC_PASS = project_data['dna_center']['password']
GITHUB_USERNAME = project_data['github']['username']
GITHUB_TOKEN = project_data['github']['token']
GITHUB_REPO = project_data['github']['repository']

# Example from .env
"""
DNAC_URL = os.getenv('DNAC_URL')
DNAC_USER = os.getenv('DNAC_USER')
DNAC_PASS = os.getenv('DNAC_PASS')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPO = 'dnacenter_day_n_inventory'
"""

os.environ['TZ'] = 'America/Los_Angeles'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)

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
    with open('DNAC-Design-Settings.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        #iniialize variables
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

            if device_list:
                # get Cisco DNA Center Auth token
                dnac_auth = get_dnac_token(DNAC_AUTH)
    
                # Get the target site id 
                TargetSiteId = get_target_site_id(dnac_auth, parent_name, area_name, building_name, floor_name)
                # Get the site credentials
                dcloud_user_id, dcloud_snmp_RO_id, dcloud_snmp_RW_id = get_site_credentials(dnac_auth, dcloud_user, dcloud_snmp_RO_desc, dcloud_snmp_RW_desc)
                response = get_netconf_credential(dnac_auth)
                dcloud_netconf_id = response[0]['response'][0]['id']
    
                # ERROR HANDLING on credentials
                if dcloud_user_id == "ERROR" or dcloud_snmp_RO_id == "ERROR" or dcloud_snmp_RW_id == "ERROR":
                    logging.info('CLI Credentials not found - repairing')
                    dcloud_user_id, dcloud_snmp_RO_id, dcloud_snmp_RW_id = create_site_credentials(dnac_auth, TargetSiteId, dcloud_user, dcloud_password, dcloud_snmp_RO_desc, dcloud_snmp_RO, dcloud_snmp_RW_desc, dcloud_snmp_RW)
                        
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
                        response = create_discovery(dnac_auth, site_hierarchy, device_missing, dcloud_user_id, dcloud_snmp_RO_id, dcloud_snmp_RW_id, dcloud_netconf_id)
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
    
    #get_device_inventory()

    date_time = str(datetime.now().replace(microsecond=0))
    logging.info('  App "device_discovery.py" end, : ' + date_time)

if __name__ == '__main__':
    sys.exit(main())
