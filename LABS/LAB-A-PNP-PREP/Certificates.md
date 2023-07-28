# Cisco DNA Center and Certificates

## PKI Infrastructure Build

For lab purposes we will utiize a Microsoft Certificate authority to be built on the Active Directory (AD) server with in the lab. Normally this would be built separately with an offline root, and subordinate certificate authority servers, but within the confines of our lab we will make do with the AD server provided.

Within the AD server, we will first set up the Certificate Authority utilizing Powershell. Open a RDP session to the AD server and then the Powershell application and utilize this script:

```ps
# Add domain admin account to IIS_IUSRS group in the domain
Add-ADGroupMember -Identity "IIS_IUSRS" -Members "admin"

# Install the Certificate Authority role
Install-WindowsFeature -Name AD-Certificate -IncludeManagementTools

# Configure the Certificate Authority service
$certConfig = @{
    CACommonName = "CA"
    CAType = "EnterpriseRootCA"
    CryptoProviderName = "RSA#Microsoft Software Key Storage Provider"
    HashAlgorithmName = "SHA256"
    KeyLength = 2048
    ValidityPeriod = "Years"
    ValidityPeriodUnits = 5
    DatabaseDirectory = "C:\Windows\System32\CertLog"
    LogDirectory = "C:\Windows\System32\CertLog"
}
Install-AdcsCertificationAuthority @certConfig
```

Next we need the Certification Enrollment Web Services turned on to get a certificate

```ps
# Enable the Certificate Authority Web Enrollment service
Install-WindowsFeature -Name ADCS-Web-Enrollment -IncludeManagementTools

# Configure the Certificate Authority Web Enrollment Service
Install-AdcsWebEnrollment 

# Enable the Certificate Authority Online Responder
Add-WindowsFeature Adcs-Online-Cert -IncludeAllSubFeature -IncludeManagementTools

# Configure the Certificate Authority Online Responder Service
Install-AdcsOnlineResponder -Force
```

## PKI Certificate Template Build

Once the certificate authority service is operational, we will then add a template which we will utilize for Cisco DNA Center.
This same template may also be used for ISE. For a Template to function correctly we will need to provision a certificate which includes usage for both Client and Server Authentication roles. As it also needs to appear in the Web UI, we will need to duplicate a certificate template. The Web Server built in template will be used for duplication purposes.

1. Follow the following steps on the AD server:

   1. Open a Web RDP session to the AD server and then open the Certificate Authority App by either finding it under Administrative tools or when the start menu is open typing `Certificate Authority` and clicking the App that appears.
   2. When the App is open then click `Certificate Templates`
   3. Then click `Manage` from the menu list.

      ![json](./images/AD-Cert-Template-1.png?raw=true "Import JSON")

2. When the Certificate Template Console is open do the following to duplicate a Certificate Template:

   1. Select the `Web Server` Template towards the bottom of the console
   2. Right click and on the menu select `Duplicate Template`

      ![json](./images/AD-Cert-Template-2.png?raw=true "Import JSON")

3. Within the `Properties of New Template` window complete the following:

   #### General Tab

   1. Select `General` tab and rename the template to `Cisco Server Template`

      ![json](./images/AD-Cert-Template-3.png?raw=true "Import JSON")
   
   #### Extensions Tab

   1. Select `Extensions` tab
   2. Select `Application Policies`
   3. Click `Edit` and `Edit Application Policies Extension` window  opens
   4. Click `Add` to open the `Add Application Policy` window
   5. Select `Client Authentication` from the list 
   6. Click `OK`

      ![json](./images/AD-Cert-Template-4.png?raw=true "Import JSON")

   7. Click `OK` on the `Edit Application Policies Extension` window

      ![json](./images/AD-Cert-Template-5.png?raw=true "Import JSON")

   8. Click `Apply` on the `Extension` tab of `Properties of New Template` window

      ![json](./images/AD-Cert-Template-6.png?raw=true "Import JSON")

   8. Click `OK` to close the `Properties of New Template` window
      
      ![json](./images/AD-Cert-Template-7.png?raw=true "Import JSON")
   
   9. The new `Cisco Server Template` will appear in the list

      ![json](./images/AD-Cert-Template-8.png?raw=true "Import JSON")

4. We will now enable the use of the Newly created Certificate Template by completing the following:

   1. Right click `Certificate Templates` within the `Certificate Authority` app
   2. On the menu select `New` and then `Certificate Template to Issue`

      ![json](./images/AD-Cert-Template-9.png?raw=true "Import JSON")
      
   3. On the `Enable Certificate Templates` window select our new `Cisco Server Template` and click `OK`

      ![json](./images/AD-Cert-Template-10.png?raw=true "Import JSON")

   4. The new `Cisco Server Template` will appear in the list of `Certificate Templates` to be issued. This is the list which is used by the Certificate Web Services.

      ![json](./images/AD-Cert-Template-11.png?raw=true "Import JSON")

   5. To confirm its working in a web browser on the AD server type `http://localhost/certsrv` then log in with the username `admin` and password `C1sco12345`

   6. Navigate to an advanced certificate request and ensure the new `Cisco Server Template` appears in the Web UI.

      ![json](./images/AD-Cert-Template-12.png?raw=true "Import JSON")

Now that we have successfully enabled the Certificate Authority and templates lets go ahead and build the Cisco DNA Center certificate.

## Cisco DNA Center Certificate Installation

### Building the Certificate Signing Request 

To build the Certificate Signing Request we will utilize openssl and use a config file. This process can be completed on any platform with openssl installed. It does not necessarily need to be Cisco DNA Center. 

Open an RDP session to the `Jump Host` and from within the desktop session open the mRemoteNG application for SSH sessions.

**Complete the following tasks:**

1. Double click on the DNA Center link to open a session

2. Log in to Cisco DNA Center with the following credentials **username: `maglev`** and **password: `C1sco12345`**

3. Within Cisco DNA Center issue the `pwd` command and ensure we are in the path `/home/maglev`

4. Create and then change directory to `/home/maglev/certs` by issuing the command `mkdir certs && cd certs`

5. create the openssl.cnf file used for configuration using the command `touch ./openssl.cnf`

6. Open the VI terminal with the **openssl.cnf** file using `vi ./openssl.cnf` then paste the following into the window by right click.

```
req_extensions = v3_req
distinguished_name = req_distinguished_name
default_bits = 4096
default_md = sha512
prompt = no
[req_distinguished_name]
C = US
ST = NC
L = RTP
O = CISCO
OU = DCLOUD
CN = dnac-vip.dcloud.cisco.com
emailAddress = kebaldwi@cisco.com

[ v3_req ]
basicConstraints = CA:FALSE
keyUsage = digitalSignature, keyEncipherment
extendedKeyUsage=serverAuth,clientAuth
subjectAltName = @alt_names
[alt_names]
DNS.1 = dnac-vip.dcloud.cisco.com
DNS.2 = dnac.dcloud.cisco.com
DNS.3 = pnpserver.dcloud.cisco.com
DNS.4 = pnpserver.pnp.dcloud.cisco.com
IP.1 = 198.18.129.100
```
7. Write and Close the file by typing `:` then `wq!`

8. Create a **CSR Key** using the command `openssl genrsa -out csr.key 4096`

9. Using the premade **csr.key** we will now create the **CSR** to be submitted to Cisco DNA Center. Use the command `openssl req -config openssl.cnf -new -key csr.key -out DNAC.csr`

10. We will then display the file and copy and paste it within Certificate Authority Web Server Application. To display the file use the command `more ./DNAC.csr`

### Submitting the Certificate Signing Request

1. Open Chrome and enter the URL `http://198.18.133.1/certsrv` and log in with the credentials **username: `admin`** and **password: `C1sco12345`**

2. Within the Certificate Authority Web Site navigate the following:

   1. Click Request a Certificate
   2. Click advanced certificate request
   3. To submit the Certificate Request paste the CSR as shown
   4. **Important** Select `Cisco Server Template` for the Certificate Template
   5. Click submit
   6. On the Certificate Issued page:
      1. **Important** select **DER encoded**
      2. **Important** download from the link **Download Certificate Chain** and save it as `dnac-chain.p7b`
   7. Open the windows command prompt `CMD` application and do the following:
      1. Change directory to the Downloads directory `cd Downloads`
      2. Check the directory to ensure the file `dnac-chain.p7b` exists via the command `dir`
      3. Copy the file to Cisco DNA Center using scp usint the following command `scp -P 2222 ./dnac-chain.p7b maglev@198.18.129.100:/home/maglev/certs` and when prompted the **username: `maglev`** and the **password: `C1sco12345`**
   8. On Cisco DNA Center via the mRemoteNG SSH session we now will take the certificate chain and create a Privacy Enhanced Mail (PEM) file for import into Cisco DNA Centers GUI. Use the command `openssl pkcs7 -in dnac-chain.p7b -inform DER -out dnac-chain.pem -print_certs`

Congratulations the Certificate is prepared, now we will import it into Cisco DNA Center.

### Installing Cisco DNA Centers Certificate

1. First lets download the **Certificate** to our workstation using the scp command `scp -P 2222 maglev@198.18.129.100:/home/maglev/certs/dnac-chain.pem ./` and when prompted the **username: `maglev`** and the **password: `C1sco12345`**
2. Second lets download the **CSR KEY** to our workstation using the scp command `scp -P 2222 maglev@198.18.129.100:/home/maglev/certs/csr.key ./` and when prompted the **username: `maglev`** and the **password: `C1sco12345`**
3. Log into Cisco DNA Center with the credentials **username: `admin`** and **password: `C1sco12345`**
4. Navigate to the Menu and then Select **System > Settings**
5. On the Settings page scroll on the left down to and select **Certificates**
6. On the System tab click the **Replace Certificate** button
7. On the **Certificates** page select **PEM** then click the link to choose the file `dnac-chain.pem` from the Downloads directory. When opened into the UI click the **Upload** button
8. Scroll down the page to the Private Key section. Then click the link to choose the file `csr.key` from the Downloads directory. When opened into the UI click the **Upload** button
9. Scroll down to the Encryption question and select **No** as we did not encrypt the certificate. Then click **Save**.

Cisco DNA Center will now log out. After a few minutes refresh the GUI from the browser then display the certificate within the Browser and it should look like this.

Congratulations you have changed the certificate and are now ready to use DNS for discovery purposes.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Return to Lab**](./README.md)