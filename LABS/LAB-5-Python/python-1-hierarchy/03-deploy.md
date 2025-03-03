# Hierarchy Deployment

We will now **build** the **Hierarchy** using the **CSV** answer file and the **Python Program** previously discussed.

Complete the following:

1. If not already open: 

    1. If not already open, open the `mRemoteNG application from the desktop using the icons shown.

       ![json](../assets/remoteng-connect.png?raw=true "Import JSON")

    2. Within the mRemoteNG application double click on the Script Server and an SSH connection will open to the Ubuntu Server.

       ![json](../assets/remoteng-ssh.png?raw=true "Import JSON")

2. In the script server shell type the following:

   ```sh
   python3 /root/PYTHON-LAB/deploy_hierarchy.py
   ```

3. The following should be displayed:

   ![json](../assets/hierarchy-build.png?raw=true "Import JSON")

4. Try running the script again and see what happens:

   ```sh
   python3 /root/PYTHON-LAB/deploy_hierarchy.py
   ```

5. The following should be displayed:

   ![json](../assets/hierarchy-rebuild.png?raw=true "Import JSON")

6. Because the script is developed to determine what exists prior to adding configuration it skips over the sections pretty quickly. In this way it is **partially** **IDEMPOTENT**. To be **fully** **IDEMPOTENT** it would also remove configuration which could be added but for safety reasons is not within the code samples provided.

> [**Next Section**](./04-verify.md)
