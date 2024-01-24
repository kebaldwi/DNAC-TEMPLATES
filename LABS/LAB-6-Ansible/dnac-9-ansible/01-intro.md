# Ansible and Cisco DNA Center

In this module, we will use *Ansible* to run REST API tasks in playbooks against Cisco DNA Center manages. 

Ansible can be used as an orchestrator for managing complex deployments and workflows. It allows you to define the entire infrastructure as code, including the relationships between different components, and then deploy and manage it with ease. Ansible can also be integrated with other tools in your DevOps toolchain, such as Jenkins or GitLab, to create a fully automated deployment pipeline. With Ansible, you can easily manage the entire lifecycle of your infrastructure, from provisioning and configuration to deployment and scaling.

Ansible can be used to automate the management of Cisco DNA Center, which is a software-based network automation and assurance platform. Cisco provides an Ansible collection for DNA Center that includes modules for managing a wide range of network devices, including switches, routers, and wireless access points.

## Ansible Background

To help DevOps engineers, Cisco has created a rich collection of libraries to accelerate the development of API-based workflows and integrations. Currently, Cisco DNA Center supports a northbound Python Software Development Kit (SDK), RedHat and **Community certified Ansible modules**, a Go SDK and a Terraform provider. All these libraries are very easy to install and update, requiring only few commands. They allow the DevOps engineers to focus on rendering the data to and from the API rather than writing functions for each API call, eliminating development cycles.

Ansible is an open-source automation tool that allows you to manage your infrastructure as code. It works by using SSH to connect to remote machines and executing tasks defined in YAML files called playbooks. Ansible is agentless, which means it doesn't require any software to be installed on the remote machines. Instead, it uses SSH to connect to them and run the necessary tasks. This makes it easy to manage large, complex infrastructures from a single control machine.

Ansible is written in Python and uses Python as its primary language for writing modules and plugins. However, you don't need to know Python to use Ansible. You can write playbooks using YAML, which is a simple, human-readable language. Ansible also provides a large number of pre-built modules that you can use to automate common tasks, such as managing packages, users, and files.

Within this section you will use and review prewritten code to see how various tasks can be orchestrated via Ansible in Cisco DNA Center.

> **Prerequisites**: **Completed** the previous section **Python Applications**

> [**Next Section**](02-scriptserver.md)
