# ISE Certificate Setup (via API)

## Prerequisites and Lab Notes

   1. Completed [**PKI Infrastructure Setup Module**](./Certificates01-PKI-Infrastructure.md)
   2. If you have already done these steps via the GUI in the [**Certificates03a-ISE-GUI Module**](./Certificates03a-ISE-GUI.md), the certificates you generated will need to be deleted first.

>[!NOTE]
>While many of these tasks can be completed with your own device, the screenshots taken (and many of the steps reference) using the Windows Jump Host.  

## Overview

Cisco Identity Services Engine (ISE) uses certificates to provide secure communication and authentication within the network. Certificates identify ISE nodes to endpoints and secure communications between nodes, external servers, and end-user portals such as guest, sponsor, and BYOD portals. ISE manages system certificates for node identification and trusted certificates for establishing trust with users and devices. It supports certificate issuance, key management, and storage through its internal Certificate Authority (CA) service, which can issue and sign certificates for endpoints, enabling secure personal device authentication. Certificates are also used for TLS-based EAP authentication, RADIUS DTLS server authentication, and SAML verification, ensuring secure access control and communication across the network infrastructure.  ISE’s certificate management includes generating Certificate Signing Requests (CSRs), importing CA-signed certificates, and configuring certificate usage for different purposes such as admin communication, portal access, and pxGrid communication -- which is what we will accomplish in this lab.
The process for getting ISE setup with certificates is similar to that of Catalyst Center.  In this lab, we will do most of the work via the ISE API using Postman.  As a reminder, if you do not have Postman installed on your machine (or cannot install it for this lab), you may use the Windows Jump Host within the lab as it already has Postman pre-installed.  Should you prefer to setup the ISE certificates via GUI - please see the [**Certificates03b-ISE-GUI**](./Certificates03b-ISE-GUI.md) module for instructions on how to do that.  For this lab we need to export the Windows root CA certificate and upload it into ISE's Trusted Certificates store first, then generate a CSR, get it signed, and finally upload the signed certificate.

## Postman Setup

For this lab, we have prebuilt the Postman environment and collection you will need to complete the lab.  Of course, in your production environment, you would be able to implement these APIs in a more programatic way (Python, Ansible, etc.) - but the goal here is to introduce you to the APIs and how they work.  The assumption with this lab is that you are familiar with using Postman, but if not - please reach out to your lab proctor for assistance.

The download links for the collections are below:

   <p><a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/POSTMAN/lab-0-ise-certificate-automation-collection.json">⬇︎COLLECTION⬇︎</a></p>
   <p><a href="https://git-link.vercel.app/api/download?url=https://github.com/kebaldwi/DNAC-TEMPLATES/blob/master/CODE/POSTMAN/lab-0-ise-certificate-automation-environment.json">⬇︎ENVIRONMENT⬇︎</a></p>

<p><a href="https://learning.postman.com/docs/getting-started/importing-and-exporting/importing-data/">Instructions for importing Collection/Environment into Postman</a></p>

>[!NOTE]
>You will need to disable SSL certificate verification in Postman Settings for this lab

Now that your Postman application is setup, lets move on to setting up ISE with a Trusted Root Certificate

## Enabling APIs on ISE

Unfortunately, by default, when and ISE instance is first spun up (as it is in this lab) - it has its API access disabled.  We must enable this via the GUI before we can use APIs.

***Complete the following tasks:***

1. From the Windows Jump Box, open a Chrome browser and navigate to ISE using https://198.18.133.27 (or using the bookmark) and login with ***username: `admin`*** and ***password: `C1sco12345`***

2. From the hamburger menu in the top left hand corner, choose ***Administration > System > Settings***

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-9.png?raw=true "Import JSON")

3. On the left, choose ***API Settings*** then ***API Service Settings*** - enable both ERS (Read/Write) and Open API (Read/Write) and then ***Save***

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-10.png?raw=true "Import JSON")


Now ISE should be ready for API calls, but before we can get to that...lets get our certificate ready!

## Exporting the Windows Root CA Certificate (as Base 64)

>[!NOTE]
>If you have completed the certificate export as part of the [***Certificates02-Catalyst-Center-GUI module***](./Certificates02-Catatlyst-Center-GUI.md) (as part of this same lab slot)- you do not need to export the CA cert again as long as it is in Base 64 format.

***Complete the following tasks:***

1. From the Windows Jump Box, open Chrome browser and navigate to http://198.18.133.1/certsrv/ and login with ***username: `admin`*** and ***password: `C1sco12345`*** if prompted

2. From here, click on ***Download a CA Certificate***

   ![json](../../ASSETS/LABS/AD/CERTS/Cert-CSR-10.png?raw=true "Import JSON")

3. Since we only have a single CA in our lab environment, the only one that should show up should be "Current[CA]".  Leave the ***Encoding Method***Í as DER and click ***Download CA certificate***

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-1.png?raw=true "Import JSON")

   You may see a prompt from the browser to ***Keep*** or ***Discard*** this download, choose ***Keep***.  By default, the file will save to the Downloads folder as `certnew.cer`

## Cleaning Up the Windows Root CA Certificate

Because text editors tend to add either carriage returns or line feeds (or both) to certificate files, we need to modify the text of the Root CA file a bit so that we can use it within our Postman API call.  To do so, we will utilize Notepad++ for this example.  Similar ways of cleaning up certificate files exist either in PowerShell (for Windows) or the ***awk*** utility on MacOS/Linux - but these are outside the scope of this lab.

***Complete the following tasks:***

1. Locate the Root CA file in the Downloads folder of the Windows Jump Host (or wherever you saved it - reminder that by default it is named `certnew.cer`)

2. Right click and choose ***Edit with Notepad++***

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-1.png?raw=true "Import JSON")

3. Here, we are going to use the ***Replace*** tool to perform several tasks.

   1. Select all text with either ***Ctrl+A*** or by highlighting all text with your mouse cursor

   2. In the menu bar, click ***Search > Replace*** this opens the Replace window.

   3. In the bottom left of the Replace window, change the "Search Mode" from Normal to ***Extended***

         ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-2.png?raw=true "Import JSON")

   3. In the ***Find what:*** field, enter "\n" (without quotes), leave the ***Replace with:*** field blank, and click ***Replace All***.

         ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-3.png?raw=true "Import JSON")

   4. Next, in the ***Find what:*** field, enter "\r" (without quotes), and in the ***Replace with:*** field enter "\\\n" without quotes.  
   
         >[!IMPORTANT] 
         >Pay close attention that this is a DOUBLE back slash before the n!
         
         Again click ***Replace All***

         ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-4.png?raw=true "Import JSON")

   6. What we should now be left with is a very long string with several "\n" where line breaks used to be.

         ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-5.png?raw=true "Import JSON")

   7. Close out of the Replace window and copy the entirety of the line of text to the clipboard.

## Installing the Root CA in ISE using Postman

At this point, it is assumed that you have successfully opened Postman application and imported the Collection and Environment above.  Note that the screenshots are with the Postman application in dark mode.  Ensure that your Environment is selected in the top right of the Postman screen as "lab-0-ise-certificate-automation-environment".

***Complete the following tasks:***

1. Under ***Collections > lab-0-ise-certificate-automation-collection***, expand the "CERTIFICATES" folder and look for ***POST - Import Trusted Certificate***

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-6.png?raw=true "Import JSON")

2. When the request opens, click on the ***Body*** field and note that all of the entries have been prefilled with the exception of the "data" key:

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-7.png?raw=true "Import JSON")

3. Paste the long string that we copied from the previous task (modifying the Certificate file) in between the double quotes of the "data" key.  Ensure that there are no errors (red squiggly lines or changes in color of the string of text would indicate something did not paste correctly).  Then click ***Send***

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-8.png?raw=true "Import JSON")

4. In the bottom section of the window, we should see a JSON response indicating a Success:

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-11.png?raw=true "Import JSON")

5. We can further validate this by:

   1. Opening a web browser and navigating to ISE using https://198.18.133.27 (or using the bookmark) and login with ***username: `admin`*** and ***password: `C1sco12345`***

   2. Using the hamburger menu to navigate to ***Administration > System > Certificates***

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-12.png?raw=true "Import JSON")

   3. On the left, choose ***Trusted Certificates***

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-13.png?raw=true "Import JSON")

   4. From there, we should be able to scroll and see the certificate we uploaded

      ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-14.png?raw=true "Import JSON")

Now let's move on to generating a Certificate Signing Request

## Generating a Certificate Signing Request (CSR) via API (and Downloading it!)

***Complete the following tasks:***

1. Open up your Postman application again, and this time under ***Collections > lab-0-ise-certificate-automation-collection*** > ***Certificates*** select ***POST - Generate CSR***.  Notice in the ***Body*** section all keys/fields are already filled out for you here, with appropriate SanDNS name, SanIP, Subject, State, etc.  We simply need to click ***Send***

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-15.png?raw=true "Import JSON")

2. Here we receive our response success message:

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-16.png?raw=true "Import JSON")

3. Back in the ISE GUI, under ***Administration > System > Certificates*** on the left hand side choose ***Certificate Signing Requests***.  Place a check next to the CSR in the table (should only be the one), and choose ***Export***

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-17.png?raw=true "Import JSON")

4. Save the file in the Downloads folder, by default it will be named `iseMultiUse.pem`


## Signing the ISE CSR with Certificate Authority

***Complete the following tasks:***

1. Open the "Downloads" folder, right click on the .pem file that was just downloaded from ISE, and choose "Edit with Notepad++".  Thankfully, because Windows CertSrv can correctly parse carriage returns/line feeds, we do not need to modify this file.

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-GUI-CSR-10.png?raw=true "Import JSON")

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

5. The certificate file should now be downloaded to the Downloads folder, by default it will be named `certnet.csr`, but you can save it as you wish.

## Cleaning Up the Signed ISE Certificate

Now that we have our signed ISE certificate, to use it within an API we have to do the same cleanup that we did previously.  Follow the steps in the [Cleaning Up The Windows Root CA Certificate](#cleaning-up-the-windows-root-ca-certificate) section, just using this newly downloaded file.

>[!NOTE]
>Keep this file open, we'll be using the text string from this in a couple tasks!

## Getting the CSR "ID"

In order to be able to "bind" the signed certificate we just downloaded to the appropriate Certificate Signing Request in ISE, we need to get the "id" of the CSR.  Thankfully, since we only have a single CSR, this should be pretty easy!

***Complete the following tasks:***

1. In your Postman app, under ***Collections > lab-0-ise-certificate-automation-collection*** > ***Certificates*** select ***GET - CSR Listing***.  This GET request has an empty body (although you can use filters if you have multiple CSRs).  Simply press ***Send***

2. The return results should have the "id" that we need.  Copy this value from your Postman output.

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-19.png?raw=true "Import JSON")

## Binding the CSR with the Certificate

***Complete the following tasks:***

1. Open your Postman app, and now under ***Collections > lab-0-ise-certificate-automation-collection*** > ***Certificates*** select ***POST - Bind CSR***.  You will see that everything in the Body has been populated for you ***except*** the "id" value (which we just found in the previous task), and the "data" value (that we generated in the task before that).

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-18.png?raw=true "Import JSON")

2. For the "id" key, paste the id value that you copied from the previous task.  And for the "data" key, as before, paste the entire certificate file string from the above task - looking out for any errors in the formatting (red squiggly lines, changes in text color, etc).  Then click ***Send***

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-20.png?raw=true "Import JSON")

3. And now we get a successful response.  ISE will now reboot - so wait ~5 minutes or so before attempting to login to the admin portal again.

   ![json](../../ASSETS/LABS/AD/CERTS/ISE-API-CSR-21.png?raw=true "Import JSON")


Congrats, your ISE instance is now ...CERTIFIED!



> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 


> [**Return to Lab**](./README.md)