# Cisco DNA Center and Certificates

## PKI Infrastructure

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
```

Once the certificate authority service is operational, we will then add a template which we will utilize for Cisco DNA Center.
This same template may also be used for ISE.

```ps
Add-CATemplate -Name "RASandIASServer" -Force
```

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Return to Lab**](./README.md)