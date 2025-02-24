# Connecting to the Script Server

You have two options for connectivity to the DCLOUD Lab script server. I recommend that you use a local SSH application like putty to connect to the script server. The alternate is to use the jumphost which we depict below. The username and password for the script server are:

- username: root
- password: C1sco12345

```sh
ssh root@198.18.134.28
```

Within the lab environment we will use the SSH application on the windows jumphost `mRemoteNG` located on the desktop on the `Jump Host` to connect to the `Script Server`. The script server is an Ubuntu 20.04.3 Server with all the software loaded to complete this section.

Complete the following:

1. Open the `mRemoteNG application from the desktop using the icons shown.

   ![json](./assets/remoteng-connect.png?raw=true "Import JSON")

2. Within the mRemoteNG application double click on the Script Server and an SSH connection will open to the Ubuntu Server.

   ![json](./assets/remoteng-ssh.png?raw=true "Import JSON")

> [**Next Section**](./04-verify.md)
