#################################
# project: DNAC-recon
# author: kebaldwi@cisco.com
# use case: Simple recon of DNAC
#################################
import os
import time
import requests
import urllib3
import json
import sys
import logging
import datetime
import maskpass
import warnings

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from dnacentersdk import DNACenterAPI
from datetime import datetime
from pprint import pprint
from requests.auth import HTTPBasicAuth  # for Basic Auth
from http.client import HTTPSConnection
from base64 import b64encode
from getpass import getpass
from tabulate import tabulate

#Define object for hierarchy
class Site:
    def __init__(self,name,type,id,hierarchy,parentid,sitehierarchy):
        self.name = name
        self.type = type
        self.id = id
        self.hierarchy = hierarchy
        self.parentid = parentid
        self.sitehierarchy = sitehierarchy
        pass

#Define object for settings
class Settings:
    def __init__(self,name,id,timezone,dhcpserver,dnsserver,domainname,aaaserver,aaaprotocol):
        self.name = name
        self.id = id
        self.timezone = timezone
        self.dhcpserver = dhcpserver
        self.dnsserver = dnsserver
        self.domainname = domainname
        self.aaaserver = aaaserver
        self.aaaprotocol = aaaprotocol
        pass

#Define object for devices
class Device:
    def __init__(self,hostname,id,platformid,serialnumber,site):
        self.hostname = hostname
        self.id = id
        self.platformid = platformid
        self.serialnumber = serialnumber
        self.site = site
        pass

#Define object for template editor projects
class Project:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        pass

#Define OS settings for display
def os_setup():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
    if not sys.warnoptions:
        warnings.simplefilter("ignore")

#Define pause for keystroke to continue
def pause():
    input("\nPress Enter to continue...\n") 
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

#Define function to create basic auth for DNAC credentials
def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

#Define function to authenticate with DNAC using API credentials
def dnac_authenticate(url, username, password):
    auth = basic_auth(username, password)
    auth_url = f'{url}/dna/system/api/v1/auth/token'
    headers = {
        'content-type': 'application/json',
        'authorization': auth
    }
    response = requests.post(auth_url, headers=headers, verify=False)
    response_json = response.json()
    dnac_token = response_json['Token']
    return dnac_token

#Define various functions for informational gathering data from DNA Center
#Define function for Site Hierarchy Discovery
def dnac_getsite(url, token):
    dnac_url = f'{url}/dna/intent/api/v1/site'
    headers = {
        'content-type': 'application/json',
        'X-Auth-Token': token
    }
    response = requests.get(dnac_url, headers=headers, verify=False)
    response_json = response.json()
    return response_json

#Define function to read Site Hierarchy data
def dnac_readsite(siteResponse):
    json_data = siteResponse['response']
    count = len(json_data)
    array_length = 0
    siteNumber = []
    for i in range(0,count,1):
        name = json_data[i]['name']
        id = json_data[i]['id']
        hierarchy = json_data[i]['siteNameHierarchy']
        sitehierarchy = json_data[i]['siteHierarchy']
        array = json_data[i]['additionalInfo']
        array_length = len(array)
        if (array_length > 1):
            parentid = json_data[i]['parentId']
            for a in range(0,array_length,1):
                if ("Location" in json_data[i]['additionalInfo'][a]['nameSpace']):
                    type = json_data[i]['additionalInfo'][a]['attributes']['type']
        elif (array_length == 1):
            parentid = json_data[i]['parentId']
            if ("Location" in json_data[i]['additionalInfo'][0]['nameSpace']):
                    type = json_data[i]['additionalInfo'][0]['attributes']['type']
        else:
            parentid = ""
            type = "global"                        
        siteNumber.append(Site(name, type, id, hierarchy, parentid, sitehierarchy))
        #print(siteNumber[i].name, siteNumber[i].type, siteNumber[i].id, siteNumber[i].hierarchy, siteNumber[i].parentid, siteNumber[i].sitehierarchy)
    return siteNumber

#Define a function to sort hierarchy for display
def dnac_sortsite(siteNumbers):
    json_data = siteNumbers
    array_length = len(json_data)
    for i in range(array_length):
        for j in range(0, array_length - i - 1):
            if (json_data[j+1].sitehierarchy in json_data[j].sitehierarchy):
                json_data[j+1], json_data[j] = json_data[j], json_data[j+1]
            elif (json_data[j].type == json_data[j+1].type and json_data[j].parentid == json_data[j+1].parentid):
                if (json_data[j].name > json_data[j+1].name):
                    json_data[j+1], json_data[j] = json_data[j], json_data[j+1]
    return json_data

#Define a function to display the Hierarchy
def dnac_displaysite(dnac_url, dnac_token):
    siteResponse = dnac_getsite(dnac_url, dnac_token)
    #print('\nThis is the raw site data from DNA Center:\n\n',siteResponse)
    siteNumbers = dnac_readsite(siteResponse)
    #print('\nThis is formatted hierarchial data for each site extrapolated from DNA Center\n')
    #for rowdata in siteNumbers:
        #print(rowdata.name, rowdata.type, rowdata.hierarchy, rowdata.id)
    siteSorted = dnac_sortsite(siteNumbers)
    print('\nThis is sorted hierarchial site data extrapolated from DNA Center\n')
    table = [['Site Hierarchy', 'Type', 'Site Name']]
    for rowdata in siteSorted:
        tableData = [rowdata.hierarchy, rowdata.type, rowdata.name]
        table.append(tableData)
    print(tabulate(table, headers='firstrow', tablefmt='simple_outline'))
    return siteSorted

#Define function for Site Settings Discovery
def dnac_getsettings(url, token, siteId=""):
    if (siteId):
        dnac_url = f'{url}/dna/intent/api/v1/network?siteId={siteId}'
    else:
        dnac_url = f'{url}/dna/intent/api/v1/network'
    headers = {
        'content-type': 'application/json',
        'X-Auth-Token': token
    }
    response = requests.get(dnac_url, headers=headers, verify=False)
    response_json = response.json()
    return response_json

#Define function to read Site Settings data
def dnac_readsettings(dnac_url, dnac_token, siteInfo):
    count = len(siteInfo)
    siteSettings = []
    for i in range(0,count,1):
        name = siteInfo[i].name
        id = siteInfo[i].id
        siteResponse = dnac_getsettings(dnac_url, dnac_token, id)
        json_data = siteResponse['response']
        timezone = ""
        dhcpserver = ""
        dnsserver = ""
        domainname = ""
        aaaserver = ""
        aaaprotocol = ""
        for setting in json_data:
            if (setting['instanceType'] == 'timezone'):
                timezone = setting['value'][0]
            if (setting['instanceType'] == 'ip'):
                dhcpserver = setting['value'][0]
            if (setting['instanceType'] == 'dns'):
                dnsserver = setting['value'][0]['primaryIpAddress'] 
                if (setting['value'][0]['secondaryIpAddress']): 
                    dnsserver.append(',' + setting['value'][0]['secondaryIpAddress'])
                domainname = setting['value'][0]['domainName']
            if (setting['instanceType'] == 'aaa' and setting['value'][0]['ipAddress']):
                aaaserver = setting['value'][0]['ipAddress']
                aaaprotocol = setting['value'][0]['protocol']
        siteSettings.append(Settings(name, id, timezone, dhcpserver, dnsserver, domainname, aaaserver, aaaprotocol))
        #print(name, timezone, dhcpserver, dnsserver, domainname, aaaserver, aaaprotocol)
    return siteSettings

#Define a function to display the Settings
def dnac_displaysettings(dnac_url, dnac_token, siteSorted):
    siteSettings = dnac_readsettings(dnac_url, dnac_token, siteSorted)
    print('\nThis table is the settings for each site extrapolated from DNA Center\n')
    table = [['Site Name', 'TimeZone', 'DHCP Server', 'DNS Server', 'DNS Suffix', 'DNS Server', 'AAA Server', 'AAA Protocol']]
    for rowdata in siteSettings:
        tableData = [rowdata.name, rowdata.timezone, rowdata.dhcpserver, rowdata.dnsserver, rowdata.domainname, rowdata.aaaserver, rowdata.aaaprotocol]
        table.append(tableData)
    print(tabulate(table, headers='firstrow', tablefmt='simple_outline'))

#Define a function to get the Network Devices
def dnac_getdevices(url, token, DeviceId=""):
    if (DeviceId):
        dnac_url = f'{url}/dna/intent/api/v1/network-device/{DeviceId}'
    else:
        dnac_url = f'{url}/dna/intent/api/v1/network-device/'
    headers = {
        'content-type': 'application/json',
        'X-Auth-Token': token
    }
    response = requests.get(dnac_url, headers=headers, verify=False)
    response_json = response.json()
    return response_json

#Define a function to display the Network Devices
def dnac_readdevices(dnac_url, dnac_token):
    siteResponse = dnac_getdevices(dnac_url, dnac_token)
    json_data = siteResponse['response']
    siteDevices = []
    for device in json_data:
        hostname = ""
        id = ""
        platformid = ""
        serialnumber = ""
        site = ""
        hostname = device['hostname']
        id = device['id']
        platformid = device['platformId']
        serialnumber = device['serialNumber']
        site = device['snmpLocation']
        siteDevices.append(Device(hostname, id, platformid, serialnumber, site))
        #print(hostname, platformid, serialnumber, id, site)
    return siteDevices

#Define a function to display the Network Devices
def dnac_displaydevices(dnac_url, dnac_token, siteSorted=""):
    print('\nThis table is the devices for each site extrapolated from DNA Center\n')
    table = [['Hostname', 'Platform', 'Serial Number', 'Device ID', 'Site Name']]
    devices = dnac_readdevices(dnac_url, dnac_token)
    for rowdata in devices:
        tableData = [rowdata.hostname, rowdata.platformid, rowdata.serialnumber, rowdata.id, rowdata.site]
        table.append(tableData)
    print(tabulate(table, headers='firstrow', tablefmt='simple_outline'))

#Define function for listing projects with templates
def dnac_listprojects(url, token):
    dnac_url = f'{url}/dna/intent/api/v1/template-programmer/project'
    headers = {
        'content-type': 'application/json',
        'X-Auth-Token': token
    }
    response = requests.get(dnac_url, headers=headers, verify=False)
    response_json = response.json()
    print('\nThis table is the list projects of templates from DNA Center\n')
    #print(response_json)
    table = [['Projects', 'Project Id']]
    projectList = []
    for project in response_json:
        projectname = project['name']
        projectid = project['id']
        projectList.append(Project(projectname,projectid))
        tableData = [projectname, projectid]
        table.append(tableData)
    print(tabulate(table, headers='firstrow', tablefmt='simple_outline'))
    return projectList

#Define function for exporting projects with templates
def dnac_exportprojects(url, token, projectList):
    for project in projectList:
        projectName = project.name
        project = f'["{projectName}"]'
        dnac_url = f'{url}/dna/intent/api/v1/template-programmer/project/name/exportprojects'
        headers = {
            'content-type': 'application/json',
            'X-Auth-Token': token
        }
        payload = project
        response = requests.post(dnac_url, headers=headers, data=payload, verify=False)
        response_json = response.json()
        taskId = response_json['response']['taskId']
        print(f'Downloading {projectName}.....')
        dnac_url = f'{url}/dna/intent/api/v1/task/{taskId}'
        time.sleep(3)
        responseExport = requests.get(dnac_url, headers=headers, verify=False)
        responseExport_json = responseExport.json()
        if (responseExport_json['response']['isError'] == False):
            json_file = responseExport_json['response']['data']
            with open('%s.json' % projectName,'w') as outputFile:
                json.dump(json_file, outputFile)
        else:
            print(f'\nThere was a problem in downloading the Project named: {projectName}')
            print('Please check the log messages and dependancies on other projects.\n')
    return 

# Define main function
def main():
    os_setup()
    print("DNA Center Recon:\n")
    print("We are going to collect information to connect to your DNA Center\n")
    dnac_ipaddress = input("Enter the IP address of DNA Center: ")
    dnac_user = input("Enter the administrative username: ")
    dnac_pwd = maskpass.askpass("Enter the administrative password: ")
    dnac_url = f'https://{dnac_ipaddress}'
    dnac_token = dnac_authenticate(dnac_url, dnac_user, dnac_pwd) 
    print("\n\nThis is the Token we will use for Authentication:")
    print('\nReceived Token: \n', dnac_token)
    pause()   
    print('\n\nWe will now work to discover site data from DNA Center:')
    siteSorted = dnac_displaysite(dnac_url, dnac_token)
    pause()
    print('\n\nWe will now work to discover site settings from DNA Center:')
    dnac_displaysettings(dnac_url, dnac_token, siteSorted)
    pause()
    print('\n\nWe will now work to list all devices managed by DNA Center:')
    dnac_displaydevices(dnac_url, dnac_token)
    pause()
    print('\n\nWe will now work to export all templates from DNA Center:')
    projectList = dnac_listprojects(dnac_url, dnac_token)
    pause()
    print('\n\nExporting all project templates from DNA Center to local folder:\n\n')
    dnac_exportprojects(dnac_url, dnac_token, projectList)
    print('\n\nRecon of DNA Center is complete')

if __name__ == "__main__":
    main()   
