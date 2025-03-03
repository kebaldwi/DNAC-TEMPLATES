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

from pprint import pprint
from github import Github
from pathlib import Path  # used for relative path to "templates_jenkins" folder

from dnacentersdk import DNACenterAPI
from datetime import datetime
#from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth  # for Basic Auth

#load_dotenv('environment.env')

# project path
project_details_path = Path(__file__).parent/'/root/PYTHON-LAB/project_details.yml'
with open(project_details_path, 'r') as file:
    project_data = yaml.safe_load(file)
DNAC_URL = 'https://' + project_data['dna_center']['ip_address']
DNAC_USER = project_data['dna_center']['username']
DNAC_PASS = project_data['dna_center']['password']
GITHUB_USERNAME = project_data['github']['username']
GITHUB_TOKEN = project_data['github']['token']
GITHUB_REPO = project_data['github']['repository']
DEVNET_POD = project_data['project']['pod']

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


def time_sleep(time_sec):
    """
    This function will wait for the specified time_sec, while printing a progress bar, one '!' / second
    Sample Output :
    Wait for 10 seconds
    !!!!!!!!!!
    :param time_sec: time, in seconds
    :return: none
    """
    print('\nWait for ' + str(time_sec) + ' seconds')
    for i in range(time_sec):
        print('!', end='')
        time.sleep(1)
    return


def main():
    """
    This application will automate Day N operations, creating device inventories, using the Cisco DNA Center REST APIs
    App workflow:
        - create device inventory - hostname, device management IP address, device UUID, software version,
            device family, role, site, site UUID
        - create access point inventory - hostname, device management IP address, device UUID, software version,
            device family, role, site, site UUID
        - identify device image compliance state and create image non-compliant inventories
        - save all files to local folder, formatted using JSON and YAML
        - push the inventory files to GitHub repo
    :return:
    """

    # logging basic
    logging.basicConfig(level=logging.INFO)

    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    date_time_str = str(datetime.now().strftime('%m-%d-%Y_%H-%M-%S'))
    logging.info('  App "device_inventory.py" run start, ' + current_time)

    # create a DNACenterAPI "Connection Object" to use the Python SDK
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.2.3.3',
                            verify=False)

    # get the device count
    response = dnac_api.devices.get_device_count()
    device_count = response['response']
    logging.info('  Number of devices managed by Cisco DNA Center: ' + str(device_count))

    # get the device info list
    offset = 1
    limit = 500
    device_list = []
    while offset <= device_count:
        response = dnac_api.devices.get_device_list(offset=offset)
        offset += limit
        device_list.extend(response['response'])
    logging.info('  Collected the device list from Cisco DNA Center')

    # create device inventory [{"hostname": "", "device_ip": "","device_id": "", "version": "", "device_family": "",
    #  "role": "", "site": "", "site_id": ""},...]
    device_inventory = []
    ap_inventory = []
    for device in device_list:
        # select which inventory to add the device to
        if device.family != "Unified AP":
            device_details = {'hostname': device['hostname']}
            device_details.update({'device_ip': device['managementIpAddress']})
            device_details.update({'device_id': device['id']})
            device_details.update({'version': device['softwareVersion']})
            device_details.update({'device_family': device['type']})
            device_details.update({'role': device['role']})

            # get the device site hierarchy
            response = dnac_api.devices.get_device_detail(identifier='uuid', search_by=device['id'])
            site = response['response']['location']
            device_details.update({'site': site})

            # get the site id
            response = dnac_api.sites.get_site(name=site)
            site_id = response['response'][0]['id']
            device_details.update({'site_id': site_id})
            device_inventory.append(device_details)
        else:
            device_details = {'hostname': device['hostname']}
            device_details.update({'device_ip': device['managementIpAddress']})
            device_details.update({'device_id': device['id']})
            device_details.update({'version': device['softwareVersion']})
            device_details.update({'device_family': device['type']})
            device_details.update({'role': device['role']})

            # get the device site hierarchy
            response = dnac_api.devices.get_device_detail(identifier='uuid', search_by=device['id'])
            site = response['response']['location']
            device_details.update({'site': site})

            # get the site id
            response = dnac_api.sites.get_site(name=site)
            site_id = response['response'][0]['id']
            device_details.update({'site_id': site_id})
            ap_inventory.append(device_details)

    logging.info('  Collected the device inventory from Cisco DNA Center')

    # save device inventory to json and yaml formatted files
    with open(f'/root/PYTHON-LAB/inventory/{DEVNET_POD}-{date_time_str}_device_inventory.json', 'w') as f:
        f.write(json.dumps(device_inventory))
    logging.info(f'  Saved the device inventory to file "{DEVNET_POD}-{date_time_str}_device_inventory.json"')

    with open(f'/root/PYTHON-LAB/inventory/{DEVNET_POD}-{date_time_str}_device_inventory.yaml', 'w') as f:
        f.write(f'{DEVNET_POD}-device_inventory:\n' + yaml.dump(device_inventory, sort_keys=False))
    logging.info(f'  Saved the device inventory to file "{DEVNET_POD}-{date_time_str}_device_inventory.yaml"')

    # save ap inventory to json and yaml formatted files
    with open(f'/root/PYTHON-LAB/inventory/{DEVNET_POD}-{date_time_str}_ap_inventory.json', 'w') as f:
        f.write(json.dumps(ap_inventory))
    logging.info(f'  Saved the device inventory to file "{DEVNET_POD}-{date_time_str}_ap_inventory.json"')

    with open(f'/root/PYTHON-LAB/inventory/{DEVNET_POD}-{date_time_str}_ap_inventory.yaml', 'w') as f:
        f.write(f'{DEVNET_POD}-ap_inventory:\n' + yaml.dump(ap_inventory, sort_keys=False))
    logging.info(f'  Saved the device inventory to file "{DEVNET_POD}-{date_time_str}_ap_inventory.yaml"')

    # retrieve the device image compliance state
    image_non_compliant_devices = []
    response = dnac_api.compliance.get_compliance_detail(compliance_type='IMAGE', compliance_status='NON_COMPLIANT')
    image_non_compliant_list = response['response']
    for device in image_non_compliant_list:
        device_id = device['deviceUuid']
        for item_device in device_inventory:
            if device_id == item_device['device_id']:
                image_non_compliant_devices.append(item_device)
    logging.info('  Number of devices image non-compliant: ' + str(len(image_non_compliant_devices)))
    logging.info('  Image non-compliant devices: ')
    for device in image_non_compliant_devices:
        logging.info('      ' + device['hostname'] + ', Site Hierarchy: ' + device['site'])

    # save non compliant devices to json and yaml formatted files
    with open(f'/root/PYTHON-LAB/inventory/{DEVNET_POD}-{date_time_str}_non_compliant_devices.json', 'w') as f:
        f.write(json.dumps(image_non_compliant_devices))
    logging.info(f'  Saved the image non-compliant device inventory to file "{DEVNET_POD}-{date_time_str}_non_compliant_devices.json"')

    with open(f'/root/PYTHON-LAB/inventory/{DEVNET_POD}-{date_time_str}_non_compliant_devices.yaml', 'w') as f:
        f.write(f'{DEVNET_POD}-non_compliant:\n' + yaml.dump(image_non_compliant_devices, sort_keys=False))
    logging.info(f'  Saved the image non-compliant device inventory to file "{DEVNET_POD}-{date_time_str}_non_compliant_devices.yaml" ')

    # push all files to GitHub repo
    os.chdir('inventory')
    files_list = os.listdir()

    # authenticate to github
    g = Github(GITHUB_USERNAME, GITHUB_TOKEN)

    # searching for my repository
    repo = g.search_repositories(GITHUB_REPO)[0]

    # update inventory files
    for filename in files_list:
        try:
            contents = repo.get_contents(filename)
            if '.txt' not in filename:
                repo.delete_file(contents.path, 'remove' + filename, contents.sha)
        except:
            logging.info('  File does not exist: ' + filename)
        
        if '.txt' not in filename:
            with open(filename) as f:
                file_content = f.read()
            file_bytes = file_content.encode('ascii')
            base64_bytes = base64.b64encode(file_bytes)
    
            # create a file and commit n push
            repo.create_file(filename, "committed by Jenkins - Device Inventory build", file_content)
            logging.info('  GitHub push for file: ' + filename)

    date_time = str(datetime.now().replace(microsecond=0))
    logging.info('  App "device_inventory.py" run end: ' + date_time)

    return

if __name__ == '__main__':
    main()
