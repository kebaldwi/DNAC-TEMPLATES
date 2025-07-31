# ISE Certificate Setup (via GUI)

## Prerequisites and Lab Notes

   1. Completed [**PKI Infrastructure Setup Module**](./Certificates01-PKI-Infrastructure.md)
   2. If you have already done these steps via the API in the [**Certificates03b-ISE-API Module**](./Certificates03a-ISE-API.md), the certificates you generated will need to be deleted first.

>[!NOTE]
>While many of these tasks can be completed with your own device, the screenshots taken (and many of the steps reference) using the Windows Jump Host.  

## Overview

Cisco Identity Services Engine (ISE) uses certificates to provide secure communication and authentication within the network. Certificates identify ISE nodes to endpoints and secure communications between nodes, external servers, and end-user portals such as guest, sponsor, and BYOD portals. ISE manages system certificates for node identification and trusted certificates for establishing trust with users and devices. It supports certificate issuance, key management, and storage through its internal Certificate Authority (CA) service, which can issue and sign certificates for endpoints, enabling secure personal device authentication. Certificates are also used for TLS-based EAP authentication, RADIUS DTLS server authentication, and SAML verification, ensuring secure access control and communication across the network infrastructure.  ISE’s certificate management includes generating Certificate Signing Requests (CSRs), importing CA-signed certificates, and configuring certificate usage for different purposes such as admin communication, portal access, and pxGrid communication -- which is what we will accomplish in this lab.

The process for getting ISE setup with certificates is similar to that of Catalyst Center.  In this lab, we will do most of the work via the ISE GUI - please see the [**Certificates03b-ISE-API**](./Certificates03b-ISE-API.md) module for instructions on how to complete this via API.  For this lab we need to export the Windows root CA certificate and upload it into ISE's Trusted Certificates store first, then generate a CSR, get it signed, and finally upload the signed certificate.

## Exporting the Windows Root CA Certificate
TODO -- See if this will take Base64 format
***Complete the following tasks:***

1. From the Windows Jump Box, open Chrome browser and navigate to http://198.18.133.1/certsrv/ and login with ***username: `admin`*** and ***password: `C1sco12345`*** if prompted

2. From here, click on ***Download a CA Certificate***

   ![json](../../ASSETS/LABS/AD/CERTS/Cert-CSR-10.png?raw=true "Import JSON")

3. Since we only have a single CA in our lab environment, the only one that should show up should be "Current[CA]".  Leave the ***Encoding Method***Í as DER and click ***Download CA certificate***

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-1.png?raw=true "Import JSON")

   You may see a prompt from the browser to ***Keep*** or ***Discard*** this download, choose ***Keep***.  By default, the file will save to the Downloads folder as `certnew.cer`

## Upload the Windows Root CA Certificate to ISE

***Complete the following tasks:***

1. Open a new Chrome browser tab and navigate to the ISE Admin Portal at https://198.18.133.27 (or use the bookmark) and login with ***username: `admin`*** and ***password: `C1sco12345`*** 

2. Using the hamburger menu in the top left, navigate to ***Administration > System > Certificates***

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-2.png?raw=true "Import JSON")

3. In the menu on the left, choose ***Trusted Certificates*** and then ***Import***

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-3.png?raw=true "Import JSON")

4. While in the `Import a new Certificate into the Certificate Store` screen, perform the following:
   
   1. Using the ***Choose File*** button, navigate to the Downloads folder and select the file we exported in the previous section above

   2. For `Friendly Name`, you can enter what you wish, but for the purposes of this lab (and the screenshots below), we will be entering `DCLOUD LAB CA CERTIFICATE`

   3. Check the boxes as detailed below:

         ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-4.png?raw=true "Import JSON")
   
   4. Click the ***Submit*** button.  After the certificate uploads, you will be taken back to the ***Trusted Certificates*** screen

   5. Scroll through the list to locate and validate that your certificate file uploaded.  Here we see that ours was successfull:

         ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-5.png?raw=true "Import JSON")

Now that our Root CA Certificate is part of the Trusted Certificates store, lets generate a Certificate Signing Request.

## Generating a Certificate Signing Request in ISE

***Complete the following tasks:***

1. Assuming you are still logged into ISE and within the ***Administration > System > Certificates*** section from the last task, on the left hand side choose ***Certificate Signing Requests*** and then ***Generate Certificate Signing REquests (CSR)***

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-6.png?raw=true "Import JSON")

2. Fill out the Certificate Signing Request as follows:

   ```
   Usage = Multi-Use
   Allow Wildcard Certificates = leave unchecked
   Nodes = since this is a single-node deployment in our lab, select the only node available
   Subject:
      Common Name = leave at $FQDN$
      Organizational Unit = DCLOUD
      Organization = CISCO
      City = SJC
      State = CA
      Country = US
      Subject Alternative Name (SAN) - PLEASE SEE NOTE BELOW
      Key Type = RSA
      Key Length = 4096
      Digest to Sign With = SHA-512
   ```

      >[!NOTE]
      >While this form has the common name as $FQDN$, we also want to include the Fully Qualified Domain Name as a Subject Alternative Name as well, so the SAN fields should be filled out as follows:

   ```
   First Field Drop Down = select DNS and in the text field enter "ise.dcloud.cisco.com"
   Second Field Drop Down = select IP Address and in the text field enter 198.18.133.27
   ```
   So the filled out form should look like below:

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-9.png?raw=true "Import JSON")

   At the bottom right, click ***Generate***

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-8.png?raw=true "Import JSON")

3. This will save an `iseMultiUse.pem` file to the Downloads folder on the Windows Jump Host


## Signing the ISE CSR with Certificate Authority

***Complete the following tasks:***

1. From the same Windows Jump Host as the previous tasks, navigate to the "Downloads" folder, right click on the .pem file that was just downloaded from ISE, and choose "Edit with Notepad++"

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-10.png?raw=true "Import JSON")

>[!NOTE]
>If prompted to download update packages for Notepad++, just click "No"

2. Copy the entire contents of the Notepad++ file 


3. Open a new Chrome browser tab and enter the URL `http://198.18.133.1/certsrv` and log in with the credentials **username: `admin`** and **password: `C1sco12345`**

   ![json](../../ASSETS/LABS/AD/CERTS/Cert-CSR-9.png?raw=true "Import JSON")

4. Within the Certificate Authority Web Site navigate the following:

   1. Click Request a Certificate

      ![json](../../ASSETS/LABS/AD/CERTS/Cert-CSR-10.png?raw=true "Import JSON")

   2. Click advanced certificate request

      ![json](../../ASSETS/LABS/AD/CERTS/Cert-CSR-11.png?raw=true "Import JSON")

   3. To submit the Certificate Request paste the CSR as shown

      ![json](../../ASSETS/LABS/AD/CERTS/Cert-CSR-12.png?raw=true "Import JSON")

   4. **Important** Select `Cisco Server Template` for the Certificate Template and click submit

      ![json](../../ASSETS/LABS/AD/CERTS/Cert-CSR-13.png?raw=true "Import JSON")

   5. **Important** This time we'll actually select **Base 64 encoded** and then download the certificate

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-11.png?raw=true "Import JSON")

5. The certificate file should now be downloaded to the Downloads folder, by default it will be named `certnet.csr`

### Installing ISE Certificate

***Complete the following tasks:***

1. Open a Chrome browser tab back to ISE (if you don't have one open already) by navigating to https://198.18.133.27 (or using the bookmark) and login with ***username: `admin`*** and ***password: `C1sco12345`*** 

2. Using the hamburger menu in the top left, navigate to ***Administration > System > Certificates***

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-2.png?raw=true "Import JSON")

3. On the left choose **Certificate Signing Requests** - then place a check next to the existing CSR (should only be one option) and choose **Bind Certificate**

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-12.png?raw=true "Import JSON")

4. Select **Choose File** and navigate to/select the `certnet.csr` file we exported earlier.

5. Choose a **Friendly Name** - for the purposes of this lab we will use `DCLOUD ISE CERTIFICATE`

6. Put checks next to **Admin, EAP Authentication, RADIUS DTLS, and pxGrid**.  Note that you may receive popups like the below when you check each of these.  Choose **OK** for each.

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-12.png?raw=true "Import JSON")

7. Your screen should look like this, choose **Submit**

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-13.png?raw=true "Import JSON")

8. You will get a couple of [!Warning] messages.  Oneabout Enabling Admin role, and another about certificate validity being longer than 398 days.  Choose **YES** to both of these.  At this point the ISE application will reboot.  Wait approximately 5 minutes and log back into ISE.

Congrats, your ISE instance is now ...CERTIFIED!


> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 


> [**Return to Lab**](./README.md)