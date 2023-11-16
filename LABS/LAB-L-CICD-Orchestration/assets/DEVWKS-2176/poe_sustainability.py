#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2023 Cisco and/or its affiliates.
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

__author__ = "Gabriel Zapodeanu TME, ENB"
__email__ = "gzapodea@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2023 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import json
import logging
import os
import time
import yaml
import sys
import base64
import requests
import dnac_apis
import meraki_apis

from dotenv import load_dotenv
from pprint import pprint

from datetime import datetime
from requests.auth import HTTPBasicAuth  # for Basic Auth

load_dotenv('environment.env')

# Cisco DNA Center
DNAC_URL = os.getenv('DNAC_URL')
DNAC_USER = os.getenv('DNAC_USER')
DNAC_PASS = os.getenv('DNAC_PASS')

# Meraki
MERAKI_URL = "https://api.meraki.com"
MERAKI_AP_NAME = 'CAE_MR33'

MERAKI_API_KEY = os.getenv('MERAKI_API_KEY')
MERAKI_SW_SN = os.getenv('MERAKI_SW_SN')

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


def current_time():
    """
    This function will return the current time, Y-M-D H:M:S
    :return:
    """
    local_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return local_time


def main():
    """
    This application will automate PoE management for Cisco DNA Center and Meraki networks
    :return: none
    """

    # logging, debug level, to file {application_run.log}
    logging.basicConfig(level=logging.INFO)

    logging.info(current_time() + ' - App "poe_sustainability.py" Start')
    logging.info(current_time() + ' - Cisco DNA Center PoE Sustainability')

    # identify what operation will be executed, UP or DOWN
    local_time_hour = datetime.now().hour
    logging.info(current_time() + ' - Local time hour: ' + str(local_time_hour))
    operation = 'NONE'

    if 0 <= local_time_hour <= 7:
        operation = 'UP'

    if 18 <= local_time_hour <= 24:
        operation = 'DOWN'

    if operation == 'NONE':
        logging.info(current_time() + ' - No PoE operation performed at this time, during business hours')
        return

    logging.info(current_time() + ' - Operation based on local time: ' + operation)

    #
    # Cisco DNA Center APs operations
    #

    # get a Cisco DNA Center Auth token
    dnac_auth_token = dnac_apis.get_dnac_jwt_token(dnac_auth=DNAC_AUTH)

    # get the device info list
    device_list = []
    device_list = dnac_apis.get_device_info_family(family='Unified AP', dnac_jwt_token=dnac_auth_token)
    logging.info(current_time() + ' - Collected the device list from Cisco DNA Center')

    # create ap inventory [{"hostname": "", "device_ip": "","device_id": "", "version": "", "device_family": "",
    #  "role": "", "site": "", "site_id": ""},...]
    ap_inventory = []
    logging.info(current_time() + ' - AP inventory from Cisco DNA Center:')
    for device in device_list:
        # select which inventory to add the device to
        if device['family'] == 'Unified AP':
            device_details = {'hostname': device['hostname']}
            device_details.update({'device_ip': device['managementIpAddress']})
            device_details.update({'device_id': device['id']})
            device_details.update({'version': device['softwareVersion']})
            device_details.update({'device_family': device['type']})
            device_details.update({'role': device['role']})
            logging.info(current_time() + ' - AP name: ' + device_details['hostname'] + ', AP Management IP Address: ' +
                  device_details['device_ip'])
            ap_inventory.append(device_details)

    logging.info(current_time() + ' - Collected the AP inventory from Cisco DNA Center')

    # get the physical topology
    topology_links = dnac_apis.get_physical_topology(dnac_jwt_token=dnac_auth_token)

    # loop through each AP to disable the access switchport
    logging.info(current_time() + ' - PoE Operations for each AP')

    for ap in ap_inventory:
        logging.info(current_time() + ' - AP hostname: ' + ap['hostname'])
        # try to identify the physical topology
        for link in topology_links:
            try:
                if link['startPortIpv4Address'] == ap['device_ip']:  # AP is source port
                    connected_port_id = link['endPortID']
                else:
                    if link['endPortIpv4Address'] == ap['device_ip']:  # AP is target port
                        connected_port_id = link['sourcePortID']
                # enable/disable the port
                task_id = dnac_apis.update_interface_admin(interface_id=connected_port_id,
                                                           admin_status=operation,
                                                           dnac_jwt_token=dnac_auth_token)
            except:
                connected_port = None
                connected_device_hostname = None

    # save ap inventory to json and yaml formatted files
    with open('inventory/ap_inventory.json', 'w') as f:
        f.write(json.dumps(ap_inventory))
    logging.info(current_time() + ' - Saved the device inventory to file "ap_inventory.json"')

    with open('inventory/ap_inventory.yaml', 'w') as f:
        f.write('ap_inventory:\n' + yaml.dump(ap_inventory, sort_keys=False))
    logging.info(current_time() + ' - Saved the device inventory to file "ap_inventory.yaml"')

    #
    # Meraki APIs operations
    #

    logging.info(current_time() + ' - Meraki PoE Management')
    logging.info(current_time() + ' - Meraki Switch Serial Number: ' + MERAKI_SW_SN)
    logging.info(current_time() + ' - Meraki AP Name: ' + MERAKI_AP_NAME)
    response = meraki_apis.update_interface_admin(switch_sn=MERAKI_SW_SN, port_id='1', admin_status=operation)
    logging.info(current_time() + ' - Meraki switchport admin status: ' + str(response['enabled']))
    logging.info(current_time() + ' - End of Application "uno_cae_poe_management.py" Run')
    return


if __name__ == '__main__':
    main()
