#####################################################################
# powershell-CA.ps1
# version 1.0
# This script sets up the windows Certificate Authority
#####################################################################
# Set up the Certificate Authority
#####################################################################
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

Start-Sleep -Seconds 300

#####################################################################
# Install Features for the Certificate Authority
#####################################################################
# Enable the Certificate Authority Web Enrollment service
Install-WindowsFeature -Name ADCS-Web-Enrollment -IncludeManagementTools

# Configure the Certificate Authority Web Enrollment Service
Install-AdcsWebEnrollment 

# Enable the Certificate Authority Online Responder
Add-WindowsFeature Adcs-Online-Cert -IncludeAllSubFeature -IncludeManagementTools

# Configure the Certificate Authority Online Responder Service
Install-AdcsOnlineResponder -Force
