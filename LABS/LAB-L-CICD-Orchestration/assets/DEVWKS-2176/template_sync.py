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


import json
import logging
import os
import time
import yaml
import base64
import requests
import datetime

from pprint import pprint
from github import *
from pathlib import Path  # used for relative path to "templates_jenkins" folder
from datetime import datetime
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

# pull all files from GitHub repo
def github_pull():

    os.chdir('templates')
    files_list = os.listdir()
    permissions = 0o755

    # authenticate to github
    g = Github(GITHUB_USERNAME, GITHUB_TOKEN)

    # searching for my repository
    repo = g.search_repositories(GITHUB_REPO)[0]

    # update inventory files
    for filename in repo.get_contents('templates/git_pull'):
        file_content = base64.b64decode(filename.content)
        with open(filename.name, 'wb') as f:
            f.write(file_content)
        logging.info('  GitHub pull for file: ' + filename.name)

    # Change the permissions of the folder
    os.chdir('../')
    os.chmod('../DEVWKS-2176/templates', permissions)
    return

# push all files to GitHub repo
def github_push():
    
    os.chdir('templates')
    files_list = os.listdir()

    # authenticate to github
    g = Github(GITHUB_USERNAME, GITHUB_TOKEN)

    # searching for my repository
    repo = g.search_repositories(GITHUB_REPO)[0]
    repo_tgt = repo.get_contents('templates/git_push')

    # update inventory files
    for filename in files_list:
        try:
            contents = repo.get_contents(f'templates/git_push/{filename}')
            repo.delete_file(contents.path, 'remove' + filename, contents.sha)
            logging.info('  Deleting existing file: ' + filename)
        except:
            logging.info('  File does not exist: ' + filename)

        with open(filename) as f:
            file_content = f.read()
        file_bytes = file_content.encode('ascii')
        base64_bytes = base64.b64encode(file_bytes)

        # create a file and commit n push
        repo.create_file(f'templates/git_push/{filename}', "committed by Jenkins - Device Inventory build", file_content)
        logging.info('  GitHub push for file: ' + filename)
    return

def main():
    """
    This script will sync the templates from the GitHub repo to the Cisco DNA Center and back again.
    """

    # logging basic
    logging.basicConfig(level=logging.INFO)

    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    date_time_str = str(datetime.now().strftime('%m-%d-%Y_%H-%M-%S'))
    logging.info('  App "template_synch.py" run start, ' + current_time)

    github_pull() # working
    #github_push() # working

    date_time = str(datetime.now().replace(microsecond=0))
    logging.info('  App "template_synch.py" run end: ' + date_time)

    return

if __name__ == '__main__':
    main()
