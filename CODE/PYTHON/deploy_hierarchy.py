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

import os
import time
import requests
import urllib3
import json
import sys
import logging
import datetime
import yaml
import csv

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
#from dotenv import load_dotenv
from dnacentersdk import DNACenterAPI
from pprint import pprint
from datetime import datetime
from requests.auth import HTTPBasicAuth  # for Basic Auth
from pathlib import Path  # used for relative path to "templates_jenkins" folder

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

os.environ['TZ'] = 'America/Los_Angeles'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

# logging, debug level, to file {application_run.log}
logging.basicConfig(level=logging.INFO)
current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
date_time_str = str(datetime.now().strftime('%m-%d-%Y_%H-%M-%S'))
logging.info('App "deploy_hierarchy.py" Start, ' + current_time)

# project path
project_details_path = Path(__file__).parent/'../DEVWKS-2176/project_details.yml'
with open(project_details_path, 'r') as file:
    project_data = yaml.safe_load(file)
DNAC_URL = 'https://' + project_data['dna_center']['ip_address']
DNAC_USER = project_data['dna_center']['username']
DNAC_PASS = project_data['dna_center']['password']

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)

def get_dnac_token(dnac_auth):
    """
    Create the authorization token required to access Cisco DNA Center
    Call to Cisco DNA Center - /api/system/v1/auth/login
    :param dnac_auth - Cisco DNA Center Basic Auth string
    :return Cisco DNA Center Token
    """
    url = DNAC_URL + '/dna/system/api/v1/auth/token'
    header = {'content-type': 'application/json'}
    response = requests.post(url, auth=dnac_auth, headers=header, verify=False)
    response_json = response.json()
    dnac_jwt_token = response_json['Token']
    return dnac_jwt_token

def get_site_hierarchy(dnac_token):
    """
    This function will return the site hierarchy
    :param dnac_token: Cisco DNA Center auth token
    :return: response in JSON
    """
    url = DNAC_URL + '/dna/intent/api/v1/site'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.get(url, headers=header, verify=False)
    response_json = response.json()
    return response_json

def create_site(dnac_token, type, parent_name, type_name, address):
    """
    This function will create a new site with the hierarchy {site_hierarchy}
    :param site_hierarchy: site hierarchy, for example {Global/OR/PDX-1/Floor-2}
    :param dnac_token: Cisco DNA Center auth token
    :return: response in JSON
    """
    if type == 'area':
        payload = {
            "type": type,
            "site": {
                "area": {
                    "name": type_name,
                    "parentName": parent_name
                }
            }
        }
    elif type == 'building':
        payload = {
            "type": type,
            "site": {
                "building": {
                    "name": type_name,
                    "address": address,
                    "parentName": parent_name
                }
            }
        }
    else:
        payload = {
            "type": type,
            "site": {
                "floor": {
                    "name": type_name,
                    "parentName": parent_name,
                    "rfModel": "Cubes And Walled Offices",
                    "width": "100",
                    "length": "100",
                    "height": "10"
                }
            }
        }
    
    url = DNAC_URL + '/dna/intent/api/v1/site'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json

def main():
    """
    This app will create a new site specified in the param provided.
    """

    # logging basic
    logging.basicConfig(level=logging.INFO)

    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('App "deploy_hierarchy.py" Start, ' + current_time)

    # parse the input data
    with open('DNAC-Design-Settings.csv', 'r') as file:
        reader = csv.DictReader(file)
        
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
            
            # Create a DNACenterAPI "Connection Object"
            dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.2.2.3', verify=False)
        
            # get Cisco DNA Center Auth token
            dnac_auth = get_dnac_token(DNAC_AUTH)
        
            # create a new fabric at site
            logging.info('  Working on new campus at site: ' + site_hierarchy)

            json_response = get_site_hierarchy(dnac_auth)
            json_response = json.dumps(json_response)

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
                    response = create_site(dnac_auth, type, parentHierarchy, building_name, address)
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

if __name__ == '__main__':
    sys.exit(main())

