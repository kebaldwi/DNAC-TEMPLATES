# Hierarchy Build Deployment

## Python Deployment

In the previous step we pasted a **Groovy Script** into the **Pipeline Configuration**. This script tells Jenkins what to do when the **Pipeline** is initiated.


## Hierarchy Deployment

We will now **build** the **Hierarchy** using the **CSV** answer file and the **Python Program** previously discussed.

Complete the following:

1. If not already open: 

    1. If not already open, open the `mRemoteNG application from the desktop using the icons shown.

       ![json](./assets/remoteng-connect.png?raw=true "Import JSON")

    2. Within the mRemoteNG application double click on the Script Server and an SSH connection will open to the Ubuntu Server.

       ![json](./assets/remoteng-ssh.png?raw=true "Import JSON")

2. In the script server shell type the following:

   `python3 /root/PYTHON-LAB/deploy_hierarchy.py`

3. The following should be displayed:

4. Try running the script again and see what happens:

5. The following should be displayed:

> [**Next Section**](./06-verify.md)
