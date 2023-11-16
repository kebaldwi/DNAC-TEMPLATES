# DEVWKS-2176 
## Overview

This Repository is to be used in the DEVWKS-2176 workshop. The code is a set of example use cases and is not considered a whole solution. This Repository is only to show the art of the possible.

The repository will include scripts and examples with the following:

1. Template Scripting
2. CSV files for settings
3. YAML files for settings
4. Python Automation Examples
5. Jenkins Pipeline Examples

## Included

## Cisco Catalyst (DNA) Center Templates

Simple examples to program automation on two 9300 in DCLOUD using Autoconf. This allows the automated configuration of switchports based on interface templates logically assigned by device classification.

## CSV Settings File

A simple CSV forms the data for the DNA Center deployment and is updated on Cisco DNA Center via three Python programs:

1. **deploy_hierarchy.py** - which builds the hierarrchy based on the rows in the CSV.
2. **deploy_settings.py** - which deploys the settings and credentials based on the hierarchy in the CSV.
3. **device_discovery.py** - which discovers new devices associated to the hierarchy in the CSV.

## YAML Settings Files

A set of YAML files are used here. One for project settings like user information and another for site operations.

1. **site_operations.yml** - has all the operational information about the campus environment
2. **project_details.yml** - has user information for Git and DNA Center

## Python Automation Programs

Semi elaborate automation programs have been made out of Python to automate Cisco DNA Center. These automation programs are developed to be automated via Jenkins or automnomously. Jenkins will track changes in files, and automate accordingly.

1. **deploy_hierarchy.py** - which builds the hierarrchy based on the rows in the CSV.
2. **deploy_settings.py**  - which deploys the settings and credentials based on the hierarchy in the CSV.
3. **device_discovery.py** - which discovers new devices associated to the hierarchy in the CSV.
4. **deploy_templates.py** - which deploys templates from local files to Cisco DNA Center and onto devices
5. **device_inventory.py** - which gets inventory information from Cisco DNA Center and writes it to a GitHub Repo
6. **template_sync.py**    - which synchronizes GitHub templates with local store.

## Cisco Catalyst (DNA) Center Jenkins Automations

This repo includes the files for four Cisco DNA Center Jenkins automations pipelines.

- Pull from GitHub CLI templates and the devices that we need to configure in the lab and production - "jenkinsfile_templates"
Automate the process of deploying CLI templates to devices. This build may run every evening during maintenance hours or on-demand.

- Collect the device inventory and push to GitHub - "jenkinsfile_inventory"
The always up-to-date inventory may be used by other automations tools and platforms

- Create a new campus with a Border, and Edge node device - "jenkinsfile_campus"
Automate the process to create new fabrics using GitHub repos with the fabric configuration saved as YAML files
