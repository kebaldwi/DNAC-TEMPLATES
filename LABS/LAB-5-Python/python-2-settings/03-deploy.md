# Settings and Credntials Deployment

We will now **deploy** the **Settings** and **Credentials** using the **CSV** answer file and the **Python Program** previously discussed.

Complete the following:

1. If not already open: 

    1. If not already open, open the `mRemoteNG application from the desktop using the icons shown.

       ![json](../assets/remoteng-connect.png?raw=true "Import JSON")

    2. Within the mRemoteNG application double click on the Script Server and an SSH connection will open to the Ubuntu Server.

       ![json](../assets/remoteng-ssh.png?raw=true "Import JSON")

2. In the script server shell type the following:

   ```sh
   python3 /root/PYTHON-LAB/deploy_settings.py
   ```

3. The following should be displayed:

   ![json](../assets/settings-build.png?raw=true "Import JSON")

4. Because the script is developed to determine always push the configuration in the **CSV** it applies the settings and credentials to the hierarchy.

> [**Next Section**](./04-verify.md)
