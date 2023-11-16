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
import datetime

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

# logging, debug level, to file {application_run.log}
logging.basicConfig(level=logging.INFO)
current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
date_time_str = str(datetime.now().strftime('%m-%d-%Y_%H-%M-%S'))
logging.info('App "deploy_settings.py" Start, ' + current_time)

# project path
project_details_path = Path(__file__).parent/'../DEVWKS-2176/project_details.yml'
with open(project_details_path, 'r') as file:
    project_data = yaml.safe_load(file)
DNAC_URL = 'https://' + project_data['dna_center']['ip_address']
DNAC_USER = project_data['dna_center']['username']
DNAC_PASS = project_data['dna_center']['password']

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)

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

            # get Cisco DNA Center Auth token
            dnac_auth = get_dnac_token(DNAC_AUTH)

            # Get the target site id 
            TargetSiteId = get_target_site_id(dnac_auth, parent_name, area_name, building_name, floor_name)
            
            # Create the site settings
            response, status_code = create_site_settings(dnac_auth, TargetSiteId, domain_name, dns_server_primary, dns_server_secondary, dhcp_server_primary, dhcp_server_secondary, snmp_server, snmp_boolean, syslog_server, syslog_boolean, netflow_server, netflow_port, netflow_boolean, ntp_server_primary, ntp_server_secondary, timezone, banner_message, banner_boolean, aaa_server, aaa_address, aaa_protocol, aaa_secret)
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
                for i in range(len(response['cli'])):
                    if response['cli'][i]['description'] == dcloud_user:
                        dcloud_user_id = response['cli'][i]['id']
                        #print(f"cli id: {dcloud_user_id}")
                        logging.info('CLI Credentials exist for ' + site_hierarchy)
                        flag = True
                        break
                    elif response['cli'][i]['description'] != dcloud_user and flag != True and i == len(response['cli']) - 1:
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
                    elif response['snmp_v2_read'][i]['description'] != dcloud_snmp_RO_desc and flag != True and i == len(response['snmp_v2_read']) - 1:
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
                    elif response['snmp_v2_write'][i]['description'] != dcloud_snmp_RW_desc and flag != True and i == len(response['snmp_v2_write']) - 1:
                        create_credentials(dnac_auth, '', '', '', '', dcloud_snmp_RW_desc, dcloud_snmp_RW)
                        logging.info('SNMP RW Credentials created for ' + site_hierarchy)
                        flag = False
                break
            # Set the site credentials
            response, status_code = assign_site_credentials(dnac_auth, TargetSiteId, dcloud_user_id, dcloud_snmp_RO_id, dcloud_snmp_RW_id)
            if responsecheck in response['message'] and status_code == 202:
                logging.info('Credentials successfully set for ' + site_hierarchy)
            else:
                logging.info('Credentials failed to set for ' + site_hierarchy)
            time.sleep(15)
            address = ''      
     
    date_time = str(datetime.now().replace(microsecond=0))
    logging.info('  App "deploy_settings.py" end, : ' + date_time)

if __name__ == '__main__':
    sys.exit(main())

