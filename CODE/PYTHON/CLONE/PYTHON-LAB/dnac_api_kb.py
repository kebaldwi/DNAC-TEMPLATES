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

# Various API calls to DNAC for working with CICD with CSV

# Imports
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
import re
import base64
from github import *

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
#from dotenv import load_dotenv
from dnacentersdk import DNACenterAPI
from datetime import datetime
from pprint import pprint
from requests.auth import HTTPBasicAuth  # for Basic Auth
from pathlib import Path  # used for relative path to "templates_jenkins" folder

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

os.environ['TZ'] = 'America/Los_Angeles'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

# project path
project_details_path = Path(__file__).parent/'/root/PYTHON-LAB/project_details.yml'
with open(project_details_path, 'r') as file:
    project_data = yaml.safe_load(file)
DNAC_URL = 'https://' + project_data['dna_center']['ip_address']
DNAC_USER = project_data['dna_center']['username']
DNAC_PASS = project_data['dna_center']['password']

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)

# logging, debug level, to file {application_run.log}
def logging_start(module_name):
    logging.basicConfig(level=logging.INFO)
    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('App "' + module_name + '" Start, ' + current_time)
    return

def logging_stop(module_name):
    logging.basicConfig(level=logging.INFO)
    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('App "' + module_name + '" Stop, ' + current_time)
    return

# get_dnac_token
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


# get_site_hierarchy
def get_site_hierarchy(dnac_token):
    """
    This function will return the site hierarchy
    :param dnac_token: Cisco DNA Center auth token
    :return: response in JSON
    """
    url = (f"{DNAC_URL}/dna/intent/api/v1/site")
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.get(url, headers=header, verify=False)
    response_json = response.json()
    return response_json, response.status_code

# get_target_site_id
def get_target_site_id(dnac_token, parent_name, area_name, building_name, floor_name):
    response, status_code = get_site_hierarchy(dnac_token)
    #print(f"Looking in: {response}")
    #print(f"looking for:{parent_name},{area_name},{building_name},{floor_name}")
    # Get the target site id
    #jsonData = json.loads(responseBody)
    parent = parent_name
    if area_name != "":
        area = (f"{parent_name}/{area_name}")
    else:
        area = ""
    if building_name != "":
        bldg = (f"{parent_name}/{area_name}/{building_name}")
    else:
        bldg = ""
    if floor_name != "":
        floor = (f"{parent_name}/{area_name}/{building_name}/{floor_name}")
    else:
        floor = ""
    #print(f"parent: {parent}, area: {area}, bldg: {bldg}, floor: {floor}")
    if parent_name == "Global":
        if area_name != "":
            for i in range(len(response["response"])):
                if response["response"][i]["siteNameHierarchy"] == area:
                    TargetSiteId = response["response"][i]["id"]
                    logging.info('Area Site Id acquired.')
                    #print(TargetSiteId)
                    break
        else:
            for i in range(len(response["response"])):
                if response["response"][i]["siteNameHierarchy"] == parent:
                    TargetSiteId = response["response"][i]["id"]
                    logging.info('Global Site Id acquired.')
                    #print(TargetSiteId)
                    break
    else:
        for i in range(len(response["response"])):
            if response["response"][i]["siteNameHierarchy"] == floor:
                TargetSiteId = response["response"][i]["id"]
                logging.info('Floor Site Id acquired.')
                #print(TargetSiteId)
                break
    return TargetSiteId

# create_site_settings    
def create_site_settings(dnac_token, TargetSiteId, domainName, dnsServer1, dnsServer2, dhcpServer1, dhcpServer2, snmpServer, snmpBoolean, syslogServer, syslogBoolean, netflowServer, netflowPort, netflowBoolean, ntpServer1, ntpServer2, timeZone, bannerMessage, bannerBoolean, aaaServer=None, aaaIpAddress=None, aaaProtocol=None, aaaSecret=None):
    """
    This function will create the site settings
    """
    payload = {
        "settings": {
            "dhcpServer": [dhcpServer1],
            "dnsServer": {
                "domainName": domainName,
                "primaryIpAddress": dnsServer1
            },
               "syslogServer": {
                "ipAddresses": [syslogServer],
                "configureDnacIP": syslogBoolean
            },
            "snmpServer": {
                "ipAddresses": [snmpServer],
                "configureDnacIP": snmpBoolean
            },
            "netflowcollector": {
                "ipAddress": netflowServer,
                "port": netflowPort,
                "configureDnacIP": netflowBoolean
            },
            "ntpServer": [ntpServer1],
            "timezone": timeZone,
            "messageOfTheday": {
                "bannerMessage": bannerMessage,
                "retainExistingBanner": bannerBoolean
    		}
        }
    }
    # Check if dnsServer2 is not empty
    if dnsServer2:
        # Add the second DNS server IP to the dnsServer dictionary
        payload["settings"]["dnsServer"]["secondaryIpAddress"] = dnsServer2
    # Check if dhcpServer2 is not empty
    if dhcpServer2:
        # Add the second DHCP server IP to the dhcpServer list
        payload["settings"]["dhcpServer"].append(dhcpServer2)
    # Check if ntpServer2 is not empty
    if ntpServer2:
        # Add the second NTP server IP to the ntpServer list
        payload["settings"]["ntpServer"].append(ntpServer2)
    # Check if aaaServer is not empty
    # Check if aaaIpAddress is not empty
    if aaaServer:
        # Add the aaaServer settings to the payload dictionary
        payload["settings"]["clientAndEndpoint_aaa"] = {
		    "servers": aaaServer,
		    "ipAddress": aaaIpAddress,
		    "network": aaaIpAddress,
		    "protocol": aaaProtocol,
            "sharedSecret": aaaSecret
		} 
    url = DNAC_URL + f'/dna/intent/api/v1/site/{TargetSiteId}'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.put(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json, response.status_code

# create_credentials
def create_credentials(dnac_token, dcloudUser=None, dcloudPwd=None, dcloudSnmpRO_desc=None, dcloudSnmpRO=None, dcloudSnmpRW_desc=None, dcloudSnmpRW=None):
    """
    This function will create the credentials
    """
    payload = {
        "settings": {}
    }
    
    if dcloudUser != '' or dcloudUser != None:
        payload["settings"]["cliCredential"] = [
            {
                "description": dcloudUser,
                "username": dcloudUser,
                "password": dcloudPwd,
                "enablePassword": dcloudPwd
            }
        ]
    
    if dcloudSnmpRO != '' or dcloudSnmpRO != None:
        payload["settings"]["snmpV2cRead"] = [
            {
                "description": dcloudSnmpRO_desc,
                "readCommunity": dcloudSnmpRO
            }
        ]
    
    if dcloudSnmpRW != '' or dcloudSnmpRW != None:
        payload["settings"]["snmpV2cWrite"] = [
            {
                "description": dcloudSnmpRW_desc,
                "writeCommunity": dcloudSnmpRW
            }
        ]
    
    url = DNAC_URL + '/dna/intent/api/v1/device-credential'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json, response.status_code

# create_credentials
def create_all_credentials(dnac_token, dcloudUser, dcloudPwd, dcloudSnmpRO_desc, dcloudSnmpRO, dcloudSnmpRW_desc, dcloudSnmpRW):
    """
    This function will create the credentials
    """
    payload = {
        "settings": {
            "cliCredential": [
                {
                    "description": dcloudUser,
                    "username": dcloudUser,
                    "password": dcloudPwd,
                    "enablePassword": dcloudPwd
                }
            ],
            "snmpV2cRead": [
                {
                    "description": dcloudSnmpRO_desc,
                    "readCommunity": dcloudSnmpRO
                }
            ],
            "snmpV2cWrite": [
                {
                    "description": dcloudSnmpRW_desc,
                    "writeCommunity": dcloudSnmpRW
                }
            ]
        }
    }
    url = DNAC_URL + '/dna/intent/api/v1/device-credential'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json, response.status_code

# get_credentials
def get_credentials(dnac_token):
    """
    This function will return the credentials
    """
    url = DNAC_URL + f'/dna/intent/api/v1/device-credential'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.get(url, headers=header, verify=False)
    response_json = response.json()
    return response_json, response.status_code

# get_netconf_credential
def get_netconf_credential(dnac_token):
    """
    This function will return the netconf credential
    """
    url = DNAC_URL + f'/dna/intent/api/v1/global-credential?credentialSubType=NETCONF'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.get(url, headers=header, verify=False)
    response_json = response.json()
    return response_json, response.status_code

# get_site_credentials
def get_site_credentials(dnac_token,dcloud_user, dcloud_snmp_RO_desc, dcloud_snmp_RW_desc):
    # Get the site credentials
    while True:
        response, status_code = get_credentials(dnac_token)
        # Get the site credential cli id
        flag = False
        for i in range(len(response['cli'])):
            if response['cli'][i]['description'] == dcloud_user:
                dcloud_user_id = response['cli'][i]['id']
                logging.info('Acquired CLI Credential ID')
                flag = True
                break
            elif response['cli'][i]['description'] == dcloud_user and i == len(response['cli']) - 1:
                dcloud_user_id = "ERROR"
                logging.info('CLI Credential not found')
        # Get the site credential snmp RO id
        flag = False
        for i in range(len(response['snmp_v2_read'])):
            if response['snmp_v2_read'][i]['description'] == dcloud_snmp_RO_desc:
                dcloud_snmp_RO_id = response['snmp_v2_read'][i]['id']
                logging.info('Acquired SNMP RO Credential ID')
                flag = True
                break
            elif response['snmp_v2_read'][i]['description'] != dcloud_snmp_RO_desc and i == len(response['snmp_v2_read']) - 1:
                dcloud_snmp_RO_id = "ERROR"
                logging.info('SNMP RO Credentials not found')
        # Get the site credential snmp RW id
        flag = False
        for i in range(len(response['snmp_v2_write'])):
            if response['snmp_v2_write'][i]['description'] == dcloud_snmp_RW_desc:
                dcloud_snmp_RW_id = response['snmp_v2_write'][i]['id']
                logging.info('Acquired SNMP RW Credential ID ')
                flag = True
                break
            elif response['snmp_v2_write'][i]['description'] != dcloud_snmp_RW_desc and i == len(response['snmp_v2_write']) - 1:
                dcloud_snmp_RW_id = "ERROR"
                logging.info('SNMP RW Credentials not found')
        break
    # return site credentials
    return dcloud_user_id, dcloud_snmp_RO_id, dcloud_snmp_RW_id

def create_site_credentials(dnac_token, TargetSiteId, dcloud_user, dcloud_password, dcloud_snmp_RO_desc, dcloud_snmp_RO, dcloud_snmp_RW_desc, dcloud_snmp_RW):
    """
    This function will create the site credentials
    """
    responsecheck = "has been accepted"
    while True:
        response, status_code = get_credentials(dnac_token)
        # Check the site credential cli id
        flag = False
        for i in range(len(response['cli'])):
            if response['cli'][i]['description'] == dcloud_user:
                logging.info('CLI Credentials exist')
                flag = True
                break
            elif response['cli'][i]['description'] != dcloud_user and flag != True and i == len(response['cli']) - 1:
                create_credentials(dnac_token, dcloud_user, dcloud_password)
                logging.info('CLI Credentials created for ' + dcloud_user)
                flag = False
        # Check the site credential snmp RO id
        flag = False
        for i in range(len(response['snmp_v2_read'])):
            if response['snmp_v2_read'][i]['description'] == dcloud_snmp_RO_desc:
                logging.info('SNMP RO Credentials exist')
                flag = True
                break
            elif response['snmp_v2_read'][i]['description'] != dcloud_snmp_RO_desc and flag != True and i == len(response['snmp_v2_read']) - 1:
                create_credentials(dnac_token, '', '', dcloud_snmp_RO_desc, dcloud_snmp_RO)
                logging.info('SNMP RO Credentials created for ' + dcloud_snmp_RO_desc)
                flag = False
        # Check the site credential snmp RW id
        flag = False
        for i in range(len(response['snmp_v2_write'])):
            if response['snmp_v2_write'][i]['description'] == dcloud_snmp_RW_desc:
                logging.info('SNMP RW Credentials exist')
                flag = True
                break
            elif response['snmp_v2_write'][i]['description'] != dcloud_snmp_RW_desc and flag != True and i == len(response['snmp_v2_write']) - 1:
                create_credentials(dnac_token, '', '', '', '', dcloud_snmp_RW_desc, dcloud_snmp_RW)
                logging.info('SNMP RW Credentials created for ' + dcloud_snmp_RW_desc)
                flag = False
        break

    while True:
        response, status_code = get_credentials(dnac_token)
        # Acquire the site credential cli id
        flag = False
        for i in range(len(response['cli'])):
            if response['cli'][i]['description'] == dcloud_user:
                dcloud_user_id = response['cli'][i]['id']
                logging.info('Acquired CLI Credential ID')
                flag = True
                break
        # Acquire the site credential snmp RO id
        flag = False
        for i in range(len(response['snmp_v2_read'])):
            if response['snmp_v2_read'][i]['description'] == dcloud_snmp_RO_desc:
                dcloud_snmp_RO_id = response['snmp_v2_read'][i]['id']
                logging.info('Acquired SNMP RO Credentials ID')
                flag = True
                break
        # Acquire the site credential snmp RW id
        flag = False
        for i in range(len(response['snmp_v2_write'])):
            if response['snmp_v2_write'][i]['description'] == dcloud_snmp_RW_desc:
                dcloud_snmp_RW_id = response['snmp_v2_write'][i]['id']
                logging.info('Acquired SNMP RW Credentials ID')
                flag = True
                break
        break

    # Set the site credentials
    response, status_code = assign_site_credentials(dnac_token, TargetSiteId, dcloud_user_id, dcloud_snmp_RO_id, dcloud_snmp_RW_id)
    if responsecheck in response['message'] and status_code == 202:
        logging.info('Credentials successfully set')
    else:
        logging.info('Credentials failed to set for')
    time.sleep(15)
    return dcloud_user_id, dcloud_snmp_RO_id, dcloud_snmp_RW_id

# assign_site_credentials
def assign_site_credentials(dnac_token, TargetSiteId, SiteCredentialCli, SiteCredentialSnmpRO, SiteCredentialSnmpRW):
    """
    This function will set the site credentials
    """
    payload = {
        "cliId": SiteCredentialCli,
        "snmpV2ReadId": SiteCredentialSnmpRO,
        "snmpV2WriteId": SiteCredentialSnmpRW
    }
    url = DNAC_URL + f'/dna/intent/api/v1/credential-to-site/{TargetSiteId}'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json, response.status_code

# create_site
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

# get device list of devices in dna center
def get_device_list():
    """
    This function will return the device list
    :param dnac_token: Cisco DNA Center auth token
    :return: response in JSON
    """
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
    # return the device inventory
    return device_inventory, ap_inventory

# device_inventory
def get_device_inventory():
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
    with open('inventory/device_inventory.json', 'w') as f:
        f.write(json.dumps(device_inventory))
    logging.info('  Saved the device inventory to file "device_inventory.json"')

    with open('inventory/device_inventory.yaml', 'w') as f:
        f.write('device_inventory:\n' + yaml.dump(device_inventory, sort_keys=False))
    logging.info('  Saved the device inventory to file "device_inventory.yaml"')

    # save ap inventory to json and yaml formatted files
    with open('inventory/ap_inventory.json', 'w') as f:
        f.write(json.dumps(ap_inventory))
    logging.info('  Saved the device inventory to file "ap_inventory.json"')

    with open('inventory/ap_inventory.yaml', 'w') as f:
        f.write('ap_inventory:\n' + yaml.dump(ap_inventory, sort_keys=False))
    logging.info('  Saved the device inventory to file "ap_inventory.yaml"')

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
    with open('inventory/non_compliant_devices.json', 'w') as f:
        f.write(json.dumps(image_non_compliant_devices))
    logging.info('  Saved the image non-compliant device inventory to file "non_compliant_devices.json"')

    with open('inventory/non_compliant_devices.yaml', 'w') as f:
        f.write('non_compliant:\n' + yaml.dump(image_non_compliant_devices, sort_keys=False))
    logging.info('  Saved the image non-compliant device inventory to file "non_compliant_devices.yaml" ')

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
            repo.delete_file(contents.path, 'remove' + filename, contents.sha)
        except:
            print('File does not exist')

        with open(filename) as f:
            file_content = f.read()
        file_bytes = file_content.encode('ascii')
        base64_bytes = base64.b64encode(file_bytes)
        logging.info('  GitHub push for file: ' + filename)

        # create a file and commit n push
        repo.create_file(filename, "committed by Jenkins - Device Inventory build", file_content)

    date_time = str(datetime.now().replace(microsecond=0))
    logging.info('  App "device_inventory.py" run end: ' + date_time)

    return

# create_discovery
def create_discovery(dnac_token, site_hierarchy, device_list, dcloud_user_id, dcloud_snmp_RO_id, dcloud_snmp_RW_id, dcloud_netconf_id):
    """
    This function will create a discovery for the specified device_ip
    :param dnac_auth: Cisco DNA Center auth token
    :param device_ip: device ip address
    :return: response in JSON
    """
    DiscoveryName = re.sub(r'\s', '', site_hierarchy)
    #device_list_split = device_list.split(',')
    DeviceRange = ""
    if len(device_list) > 1:
        DiscoveryType = 'Multi Range'
        for d in range(len(device_list)):
            if d == 0:
                DeviceRange = DeviceRange + device_list[d] + '-' + device_list[d]
            else:
                DeviceRange = DeviceRange + ',' + device_list[d] + '-' + device_list[d]
    else:
        DiscoveryType = 'Range'
        DeviceRange = DeviceRange + device_list[0] + '-' + device_list[0]

    payload = {
        "name": DiscoveryName,
        "discoveryType": DiscoveryType,
        "ipAddressList": DeviceRange,
        "protocolOrder": "ssh",
        "timeout": 5,
        "retry": 3,
        "globalCredentialIdList": [
            dcloud_user_id,
            dcloud_snmp_RO_id,
            dcloud_snmp_RW_id,
            dcloud_netconf_id
        ]
    }

    url = DNAC_URL + '/dna/intent/api/v1/discovery'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_token}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    response_json = response.json()
    return response_json

# assign_device_to_site
def assign_device(dnac_auth, TargetSiteId, device_list):
    """
    This function will assign the device to the site
    :param dnac_auth: Cisco DNA Center auth token
    :param TargetSiteId: Cisco DNA Center site id
    :param device_list: list of device ip addresses
    :return: response in JSON
    """
    device_list_split = device_list.split(',')
    Devices = []
    for d in range(len(device_list_split)):
        Devices.append({'ip': device_list_split[d]})
    # assign the device to the site
    payload = { 
        "device": Devices 
        }
    payload = json.dumps(payload)
    url = DNAC_URL + f'/dna/system/api/v1/site/{TargetSiteId}/device'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_auth}
    response = requests.post(url, data=payload, headers=header, verify=False)
    response_json = response.json()
    return response_json, response.status_code

# sleep time in seconds
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
