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
import time
import requests
import urllib3
import os

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth  # for Basic Auth
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings


# Cisco DNA Center
DNAC_URL = 'https://Cisco DNA Center'
DNAC_USER = 'username'
DNAC_PASS = 'password'

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings


def get_dnac_jwt_token(dnac_auth):
    """
    Create the authorization token required to access DNA C
    Call to Cisco DNA Center - /api/system/v1/auth/login
    :param dnac_auth - Cisco DNA Center Basic Auth string
    :return: Cisco DNA Center JWT token
    """

    url = DNAC_URL + '/dna/system/api/v1/auth/token'
    header = {'content-type': 'application/json'}
    response = requests.post(url, auth=dnac_auth, headers=header, verify=False)
    dnac_jwt_token = response.json()['Token']
    return dnac_jwt_token


def get_device_info(device_id, dnac_jwt_token):
    """
    This function will retrieve all the information for the device with the Cisco DNA Center device id
    :param device_id: Cisco DNA Center device_id
    :param dnac_jwt_token: Cisco DNA Center token
    :return: device info
    """
    url = DNAC_URL + '/dna/intent/api/v1/network-device?id=' + device_id
    header = {'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    device_response = requests.get(url, headers=header, verify=False)
    device_info = device_response.json()
    return device_info['response'][0]


def get_client_info(ip_address, dnac_jwt_token):
    """
    This function will check if the host with the {ip_address} is connected to the network
    The function will create a path trace between the host with the {ip_address} and the Cisco DNA Center IP address
    :param ip_address: host (client) IPv4 address
    :param dnac_jwt_token: Cisco DNA Center token
    :return: Access Switch, Switchport, or None
    """
    path_trace_id = create_path_trace(ip_address, '', DNAC_IP, '', '', dnac_jwt_token)
    path_trace_result = get_path_trace_info(path_trace_id, dnac_jwt_token)
    if path_trace_result[0] == 'COMPLETED':
        access_switch = path_trace_result[1][2]
        switchport = path_trace_result[1][1]
        return access_switch, switchport
    if path_trace_result[0] == 'FAILED' and 'Not able to locate unique interface or host for source ip address' in \
            path_trace_result[1][0]:
        return None
    return 'Something went wrong'


def get_device_info_ip(ip_address, dnac_jwt_token):
    """
    This function will retrieve the device information for the device with the management IPv4 address {ip_address}
    :param ip_address: device management ip address
    :param dnac_jwt_token: Cisco DNA Center token
    :return: device information, or None
    """
    url = DNAC_URL + '/dna/intent/api/v1/network-device/ip-address/' + ip_address
    header = {'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    response = requests.get(url, headers=header, verify=False)
    response_json = response.json()
    device_info = response_json['response']
    if 'errorCode' == 'Not found':
        return None
    else:
        return device_info


def get_physical_topology(dnac_jwt_token):
    """
    This function will retrieve the physical topology all devices
    :param dnac_jwt_token: Cisco DNA C token
    :return: topology links - all the layer 2 topology
    """
    url = DNAC_URL + '/dna/intent/api/v1/topology/physical-topology'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    response = requests.get(url, headers=header, verify=False)
    topology_json = response.json()['response']
    topology_links = topology_json['links']
    return topology_links


def get_device_id_name(device_name, dnac_jwt_token):
    """
    This function will find the DNA C device id for the device with the name {device_name}
    :param device_name: device hostname
    :param dnac_jwt_token: DNA C token
    :return:
    """
    device_id = None
    device_list = get_all_device_info(dnac_jwt_token)
    for device in device_list:
        if device['hostname'] == device_name:
            device_id = device['id']
    return device_id


def sync_device(device_name, dnac_jwt_token):
    """
    This function will sync the device configuration from the device with the name {device_name}
    :param device_name: device hostname
    :param dnac_jwt_token: DNA C token
    :return: the response status code, 202 if sync initiated, and the task id
    """
    device_id = get_device_id_name(device_name, dnac_jwt_token)
    param = [device_id]
    url = DNAC_URL + '/dna/intent/api/v1/network-device/sync?forceSync=true'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    sync_response = requests.put(url, data=json.dumps(param), headers=header, verify=False)
    task = sync_response.json()['response']['taskId']
    return sync_response.status_code, task


def get_all_device_info(dnac_jwt_token):
    """
    The function will return all network devices info
    :param dnac_jwt_token: DNA C token
    :return: DNA C device inventory info
    """
    url = DNAC_URL + '/dna/intent/api/v1/network-device'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    all_device_response = requests.get(url, headers=header, verify=False)
    all_device_info = all_device_response.json()
    return all_device_info['response']


def get_device_info_family(family, dnac_jwt_token):
    """
    The function will return all network devices info, matching the device family {family}
    :param family: device family
    :param dnac_jwt_token: DNA C token
    :return: DNA C device inventory info
    """
    url = DNAC_URL + '/dna/intent/api/v1/network-device?family=' + family
    header = {'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    all_device_response = requests.get(url, headers=header, verify=False)
    all_device_info = all_device_response.json()
    return all_device_info['response']


def update_interface_admin(interface_id, admin_status, dnac_jwt_token):
    """
    This function will update the admin status of an interface
    :param interface_id: device interface uuid
    :param admin_status: interface admin status: 'DOWN', 'UP'
    :param dnac_jwt_token: Cisco DNA C token
    :return: task_id: the task id for the update port operation
    """
    url = DNAC_URL + '/dna/intent/api/v1/interface/' + interface_id
    param = {'adminStatus': admin_status}
    header = {'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    response = requests.put(url, data=json.dumps(param), headers=header, verify=False)
    response_json = response.json()['response']
    task_id = response_json['response']['taskId']
    return task_id

