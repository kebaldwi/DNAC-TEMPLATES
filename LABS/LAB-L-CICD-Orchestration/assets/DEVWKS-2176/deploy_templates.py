#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Cisco DNA Center Jinja2 Configuration Templates

Copyright (c) 2021 Cisco and/or its affiliates.

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
import sys
import time
import requests
import urllib3
import json
import datetime
import yaml
import logging
from template_sync import github_pull

from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from dnacentersdk import DNACenterAPI   
from pprint import pprint
from pathlib import Path  # used for relative path to "templates_jenkins" folder
urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

os.environ['TZ'] = 'America/Los_Angeles'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

# directory search for files
def search_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

#main function
def main():
    """
    This script will load the file with the name {file_info}
    The file includes the information required to deploy the template. The network device hostname, the Cisco DNA Center
    project name, the configuration template file name.
    The application will:
     - verify if the project exists and create a new project if does not
     - update or upload the configuration template
     - commit the template
     - verify the device hostname is valid
     - deploy the template
     - verify completion and status of the template deployment
    """

    # logging, debug level, to file {application_run.log}
    logging.basicConfig(level=logging.INFO)

    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    date_time_str = str(datetime.now().strftime('%m-%d-%Y_%H-%M-%S'))
    logging.info('App "deploy_templates.py" Start, ' + current_time)

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

    # operational information path
    project_details_path = Path(__file__).parent/'../DEVWKS-2176/site_operations.yml'
    with open(project_details_path, 'r') as file:
        project_data = yaml.safe_load(file)
    PROJECT_NAME = project_data['project']['name']
    POD_NAME = project_data['project']['pod']
    logging.info('Project Name: ' + PROJECT_NAME)
    logging.info('Pod Name: ' + POD_NAME)

    # Create a DNACenterAPI "Connection Object"
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.2.2.3', verify=False)

    # creating unique project name based on the pod name
    TEMPLATE_PROJECT_NAME = PROJECT_NAME + '-' + POD_NAME
    logging.info('Template Project Name: ' + TEMPLATE_PROJECT_NAME)

    # check if existing project, if not create a new project
    response = dnac_api.configuration_templates.get_projects(name=TEMPLATE_PROJECT_NAME)
    if response == []:
        # project does not exist, create project
        payload_data = {'name': TEMPLATE_PROJECT_NAME}
        response = dnac_api.configuration_templates.create_project(payload=payload_data)
        logging.info('  Template Project Name: ' + TEMPLATE_PROJECT_NAME + ' created')
        time.sleep(15)
        response = dnac_api.configuration_templates.get_projects(name=TEMPLATE_PROJECT_NAME)
    else:
        logging.info('  Template Project Name: ' + TEMPLATE_PROJECT_NAME + ' already exists')
    project_id = response[0]['id']
    logging.info('    Template Project Name: ' + TEMPLATE_PROJECT_NAME)
    logging.info('    Template Project ID : ' + project_id)

    # verify if template exist, delete if it does
    response = dnac_api.configuration_templates.get_projects(name=TEMPLATE_PROJECT_NAME)
    templates_list = response[0]['templates']
    template_id = None

    # get the template information
    #border_templates_list = project_data['template_info']['border']['templates']
    #edge_templates_list = project_data['template_info']['edge']['templates']

    # get the device information
    border_devices_list = project_data['border_devices']['ip']
    border_templates_list = project_data['border_devices']['templates']
    edge_devices_list = project_data['edge_devices']['ip']
    edge_templates_list = project_data['edge_devices']['templates']
    logging.info('  Devices and Templates for: ' + TEMPLATE_PROJECT_NAME)
    logging.info('    Border Devices: ' + str(border_devices_list))
    logging.info('    Border Templates: ' + str(border_templates_list))
    logging.info('    Edge Devices: ' + str(edge_devices_list))
    logging.info('    Edge Templates: ' + str(edge_templates_list))

    # get the template file names
    border_template_file_names = border_templates_list.split(',')
    edge_template_file_names = edge_templates_list.split(',')
    template_name_list = border_template_file_names + edge_template_file_names
    
    for template in templates_list:
        for template_name in template_name_list:
            if template['name'] == template_name:
                template_id = template['id']
                response = dnac_api.configuration_templates.deletes_the_template(template_id=template_id)
                logging.info('Template found on DNA Center and deleted')
                time.sleep(15)
            #elif template_id is not None:
                #response = dnac_api.configuration_templates.deletes_the_template(template_id=template_id)
                #logging.info('Template found and deleted')
                #time.sleep(15)

    # sync templates from GitHub repo to local folder if not already done
    directory = '../DEVWKS-2176/templates'
    found_files = search_files(directory)
    flag_file_not_found = False
    if found_files:
        logging.info('Found files in directory: ' + directory)
        if len(found_files) == (len(template_name_list) + 1):
            for file in found_files:
                for template_name in template_name_list:            
                    if template_name in file:
                        logging.info('    Found file: ' + template_name)
                        flag_file_not_found = False
            if flag_file_not_found is False:
                logging.info('All files found in directory: ' + directory)
            else:
                logging.info('Not all files found in directory: ' + directory)
                github_pull()
        else:
            logging.info('Not all files found in directory: ' + directory)
            github_pull()
    else:
        logging.info('No files found in directory: ' + directory)
        github_pull()
    
    # create the new CLI templates
    logging.info('Creating Templates on DNA Center in Project: ' + TEMPLATE_PROJECT_NAME)
    deployment_cli_config_commands = []

    for template_name in template_name_list:
        template_file_path = Path(__file__).parent/f'../DEVWKS-2176/templates/{template_name}'
        cli_file = open(template_file_path, 'r') # open the file
        cli_config_commands = cli_file.read()  # read the file
        deployment_cli_config_commands.append(cli_config_commands)

        payload_template = {
            "name": template_name,
            "tags": [],
            "author": "Jenkins",
            "deviceTypes": [
                {
                    "productFamily": "Routers"
                },
                {
                    "productFamily": "Switches and Hubs"
                }
            ],
            "softwareType": "IOS-XE",
            "softwareVariant": "XE",
            "softwareVersion": "",
            "templateContent": cli_config_commands,
            "rollbackTemplateContent": "",
            "rollbackTemplateParams": [],
            "parentTemplateId": project_id,
            "templateParams": []
        }
        response = dnac_api.configuration_templates.create_template(project_id=project_id,payload=payload_template)
        task_id = response['response']['taskId']
        logging.info('    Created template: ' + template_name + ' in project: ' + TEMPLATE_PROJECT_NAME)
        time.sleep(15)

        # check the task result
        response = dnac_api.configuration_templates.get_projects(name=TEMPLATE_PROJECT_NAME)
        templates_list = response[0]['templates']
        template_id = None
        for template in templates_list:
            if template['name'] == template_name:
                template_id = template['id']
        
        # commit the template
        commit_payload = {
            'comments': 'Jenkins committed',
            'templateId': template_id
        }
        response = dnac_api.configuration_templates.version_template(payload=commit_payload)
        logging.info('      Template committed')
        time.sleep(5)

    # deploy the templates
    logging.info('Deploying templates from project: ' + TEMPLATE_PROJECT_NAME)
    response = dnac_api.configuration_templates.get_projects(name=TEMPLATE_PROJECT_NAME)
    templates_list = response[0]['templates']
    template_id = []
    device_ip = []
    
    # Gathering the template IDs
    logging.info('  Acquiring template IDs from project')
    for template_name in template_name_list:
        for template in templates_list:
            if template['name'] == template_name:
                template_id.append(template['id'])
                break
    logging.info('  Acquired template IDs from project')

    # Gathering the device targets IDs
    logging.info('  Acquiring device IDs from targets')
    for template_name in template_name_list:        
        # check if template is a border template
        if template_name in border_template_file_names:
            if template_name == border_templates_list:
                tgt_device = border_devices_list[0]
                device_ip.append(tgt_device)
                logging.info('    Acquired device ' + str(tgt_device) + ' target for template: ' + template_name)
            else:
                for i in range(len(border_template_file_names)):
                    if template_name == border_template_file_names[i]:
                        tgt_device = border_devices_list[i]
                        device_ip.append(tgt_device)
                        logging.info('    Acquired device ' + str(tgt_device) + ' target for template: ' + template_name)
        elif template_name in edge_template_file_names:
            # check if template is an edge template
            if template_name == edge_templates_list:
                tgt_device = edge_devices_list[0]
                device_ip.append(tgt_device)
                logging.info('    Acquired device ' + str(tgt_device) + ' target for template: ' + template_name)
            else:
                for i in range(len(edge_template_file_names)):
                    if template_name == edge_template_file_names[i]:
                        tgt_device = edge_devices_list[i]
                        device_ip.append(tgt_device)
                        logging.info('    Acquired device ' + str(tgt_device) + ' target for template: ' + template_name)

    # Deploying templates to device targets IDs
    logging.info('  Deploying templates to device IDs')
    
    for i in range(len(device_ip)):
        deploy_payload = {
                "forcePushTemplate": True,
                "targetInfo": [
                    {
                        "id": device_ip[i],
                        "type": "MANAGED_DEVICE_IP"
                    }
                ],
                "templateId": template_id[i]
            }
        response = dnac_api.configuration_templates.deploy_template_v2(payload=deploy_payload)
        task_id = response['response']['taskId']
        logging.info('    Deployed template to device: ' + device_ip[i])
        time.sleep(15)
        
        # retrieve the deployment status
        response = dnac_api.task.get_task_by_id(task_id=task_id)
        deployment_status = response['response']['isError']
        if deployment_status is False:
            logging.info('      Deployment successful')
        else:
            logging.info('      Deployment not successful')
            
        # save deployment report to file
        deployment_report = {
            'timestamp': current_time,
            'template_content': deployment_cli_config_commands[i],
            'report': deployment_status}
        report_file_path = Path(__file__).parent/f'../DEVWKS-2176/reports/{device_ip[i]}_{date_time_str}_deployment_report.json'
        with open(report_file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(deployment_report))
        
        logging.info(f'Deployment Report Created for {device_ip[i]}:')
        logging.info(json.dumps(deployment_report))
    
    date_time = str(datetime.now().replace(microsecond=0))
    logging.info('End of Application "deploy_templates.py" Run: ' + date_time)
    return

if __name__ == "__main__":
    main()
