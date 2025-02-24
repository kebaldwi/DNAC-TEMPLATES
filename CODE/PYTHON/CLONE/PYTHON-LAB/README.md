# PYTHON-LAB

## Overview

This Repository is to be used in the Python LAB in DCLOUD only. The code is a set of example use cases and is not considered a whole solution. This Repository is only to show the art of the possible.

The repository will include scripts and examples with the following:

1. Template Scripting
2. CSV files for settings
3. YAML files for settings
4. Python Automation Examples

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
