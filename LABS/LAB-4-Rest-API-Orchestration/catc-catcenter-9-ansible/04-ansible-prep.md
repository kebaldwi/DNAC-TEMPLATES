# Preparing the Ansible Collection

## Cisco DNA Center Python SDK

To prepare you will install the [**Cisco DNA Center Python SDK**](https://dnacentersdk.readthedocs.io/en/latest/) using pip or by downloading the source code and running a setup script. This can be accomplished within a virtual environment or within the global Python installation on a host. 

The Cisco DNA Center Python SDK and Cisco DNA Center Ansible collection should be preinstalled in your Lab, but we can review the install process.

To install the Cisco DNA Center Python SDK using pip, run the following as we need SDK version 2.5.5:

```SHELL
pip3 install dnacentersdk==2.5.5 
```

![json](./images/ansible-dnacentersdk.png?raw=true "Import JSON")

This command installs the latest dnacentersdk package and any missing dependencies. If you are running an older version of Cisco DNA Center, ensure you match the version of the SDK and Ansible collection that is compatible with your version of Cisco DNA Center.

## Ansible Collection

You will now install the Ansible collection. If you have the full Ansible package installed, a version of the **cisco.dnac** Ansible collection should already be present on your system. 

>**Note**: You can verify the install by running on versions of ansible on newer versions of Ansible as of `2.13.10`.

```SHELL
ansible-galaxy collection list
```

What you should see:

![json](./images/collections.png?raw=true "Import JSON")

> **Note**: If the preceding command results in a syntax error, your version of Ansible is too **old**. Please upgrade Ansible at the top of the lab.

For our lab we need **cisco.dnac** collection at **6.6.4**.

If the Cisco DNA Center Ansible collection is not present, or you receive an error on the previous command we can atttempt an install using:

```SHELL
ansible-galaxy collection install cisco.dnac:6.6.4 --force
```

![json](./images/ansible-collectioninstall.png?raw=true "Import JSON")

## Git Pull of Lab Content

We will use a clone of a specific subfolder from `DNAC-Templates` for this section of the lab.

In preparation from the working home directory folder `cd ~` issue the following command:

```SHELL
pip install github-clone
```

![json](./images/gitclone.png?raw=true "IMPORT JSON")

Once the package has installed issue the following command to clone the specific subfolder to make things easier in the lab:

```SHELL
 ghclone https://github.com/kebaldwi/DNAC-TEMPLATES/tree/master/LABS/LAB-I-Rest-API-Orchestration/dnac
 ```

![json](./images/cloning.png?raw=true "IMPORT JSON")

To ensure all the required files are there issue an `ls -lR ./dnac` and confirm:

![json](./images/clone-dir.png?raw=true "IMPORT JSON")

> [**Next Section**](05-dnac-vars.md)
