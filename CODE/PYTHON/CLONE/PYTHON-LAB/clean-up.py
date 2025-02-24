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

# DNA Center credentials
DNAC_URL = 'https://' + "198.18.129.100"
DNAC_USER = "admin"
DNAC_PASS = "C1sco12345"

def delete_managed_devices():
   # create a DNACenterAPI "Connection Object" to use the Python SDK
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.2.3.3',
                            verify=False)
    # Get all managed devices
    devices = dnac_api.devices.get_device_list()
    # Delete managed switches and routers
    for device in devices.response:
        if device.family in ["Switches and Hubs", "Routers"]:
            dnac_api.devices.delete_device_by_id(device.id)
    print("Managed switches and routers deleted successfully!")

# remove hierarchy
def remove_hierarchy():
    # Create DNACenterAPI instance
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.2.3.3',
                            verify=False)
    # Remove floors
    while True:
        hierarchy = dnac_api.sites.get_site()
        for site in hierarchy.response:
            if "parentId" in site and "additionalInfo" in site:
                if any(info["nameSpace"] == "Location" and info["attributes"]["type"] == "floor" for info in site.additionalInfo):
                    dnac_api.sites.delete_site(site_id=site.id)
                elif any(info["nameSpace"] == "Location" and info["attributes"]["type"] == "building" for info in site.additionalInfo):
                    dnac_api.sites.delete_site(site_id=site.id)
                elif any(info["nameSpace"] == "Location" and info["attributes"]["type"] == "area" for info in site.additionalInfo):
                    if site.name != "Global":
                        dnac_api.sites.delete_site(site_id=site.id)
        hierarchy = dnac_api.sites.get_site()
        if len(hierarchy.response) == 1:
            print("Floors, buildings, and areas removed except global successfully!")
            break

# clear global settings
def clear_global_network_settings():
    # Create DNACenterAPI instance
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.2.3.3',
                            verify=False)
    # Get Global site ID
    global_site = dnac_api.sites.get_site(name='Global')
    global_site_id = global_site.response[0].id
    # Define the payload with the updated settings
    payload = {
        "settings": {
            "dhcpServer": [""],
            "dnsServer": {
                "domainName": "",
                "primaryIpAddress": ""
            },
            "syslogServer": {
                "ipAddresses": [""],
                "configureDnacIP": True
            },
            "snmpServer": {
                "ipAddresses": [""],
                "configureDnacIP": True
            },
            "netflowcollector": {
                "configureDnacIP": True
            },
            "ntpServer": [""],
            "timezone": "US/Pacific",
            "messageOfTheday": {
                "retainExistingBanner": "False",
                "bannerMessage": "",
                "retainExistingBanner": "True"
            }
        }
    }
    # Update the Global site network settings
    dnac_api.network_settings.update_network(site_id=global_site_id, payload=payload)
    print("Global site network settings cleared successfully!")

# remove device credentials
def remove_device_credentials():
    # Create DNACenterAPI instance
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.2.3.3',
                            verify=False)
    # Remove the site credentials
    while True:
        response = dnac_api.network_settings.get_device_credential_details()
        # Get the site credential cli id
        flag = False
        if response['cli'] == [] and response['snmp_v2_read'] == [] and response['snmp_v2_write'] == []:
            break
        elif response['cli'] != []:
            for i in range(len(response['cli'])):
                if response['cli'][i]['id'] != "":
                    user_id = response['cli'][i]['id']
                    dnac_api.network_settings.delete_device_credential(id=user_id)
        elif response['snmp_v2_read'] != []:
            for i in range(len(response['snmp_v2_read'])):
                if response['snmp_v2_read'][i]['id'] != "":
                    user_id = response['snmp_v2_read'][i]['id']
                    dnac_api.network_settings.delete_device_credential(id=user_id)
        elif response['snmp_v2_write'] != []:
            for i in range(len(response['snmp_v2_write'])):
                if response['snmp_v2_write'][i]['id'] != "":
                    user_id = response['snmp_v2_write'][i]['id']
                    dnac_api.network_settings.delete_device_credential(id=user_id)
    print("Device credentials removed successfully!")

# remove template projects
def remove_template_projects():
    # Create DNACenterAPI instance
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.2.3.3',
                            verify=False)
    # Get all template projects
    template_projects = dnac_api.configuration_templates.get_projects() #template_projects = dnac_api.template_programmer.get_projects()
    # Iterate over each template project and delete if the name matches "RemoveMe"
    for project in template_projects:
        if project.name != "Cloud DayN Templates" and project.name != "Onboarding Configuration" and project.name != "Sample Jinja Templates" and project.name != "Sample Velocity Templates":
            project_id = project.id
            dnac_api.configuration_templates.deletes_the_project(project_id)
    print("Template projects removed successfully!")

# main
def main():
    try:
        # Delete managed devices
        delete_managed_devices()
        # Get hierarchy data
        remove_hierarchy()
        # Clear global settings
        clear_global_network_settings()
        # Remove device credentials
        remove_device_credentials()
        # Remove template projects
        remove_template_projects()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
