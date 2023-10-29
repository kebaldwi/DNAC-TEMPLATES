#####################################################################
# powershell.ps1
# version 1.0
# This script sets up the windows environment
#####################################################################
#Set up DHCP scopes on DHCP Server for IPV4
#####################################################################
#PnP Scope for mgmtvlan
Add-DhcpServerv4Scope -Name "DCLOUD-pnp-mgmtvlan" -StartRange 192.168.5.1 -EndRange 192.168.5.254 -SubnetMask 255.255.255.0 -LeaseDuration 6.00:00:00 -SuperScope "DCLOUD-Lab"
Set-DhcpServerv4OptionValue -ScopeId 192.168.5.0 -Router 192.168.5.1 
Add-Dhcpserverv4ExclusionRange -ScopeId 192.168.5.0 -StartRange 192.168.5.1 -EndRange 192.168.5.9
Set-DhcpServerv4OptionValue -ScopeId 192.168.5.0 -OptionId 43 -Value ([System.Text.Encoding]::ASCII.GetBytes("5A1N;B2;K4;I198.18.129.100;J80"))
Set-DhcpServerv4OptionValue -ScopeId 192.168.5.0 -DnsServer 198.18.133.1 -DnsDomain "dcloud.cisco.com"
#Scope for apvlan
Add-DhcpServerv4Scope -Name "DCLOUD-apvlan" -StartRange 192.168.10.1 -EndRange 192.168.10.254 -SubnetMask 255.255.255.0 -LeaseDuration 6.00:00:00 -SuperScope "DCLOUD-Lab"
Set-DhcpServerv4OptionValue -ScopeId 192.168.10.0 -Router 192.168.10.1 
Add-Dhcpserverv4ExclusionRange -ScopeId 192.168.10.0 -StartRange 192.168.10.1 -EndRange 192.168.10.9
Set-DhcpServerv4OptionValue -ScopeId 192.168.10.0 -OptionId 43 -Value ([System.Text.Encoding]::ASCII.GetBytes("5A1N;B2;K4;I198.18.129.100;J80"))
Set-DhcpServerv4OptionValue -ScopeId 192.168.10.0 -DnsServer 198.18.133.1 -DnsDomain "dcloud.cisco.com"
#Scope for datavlan
Add-DhcpServerv4Scope -Name "DCLOUD-datavlan" -StartRange 192.168.20.1 -EndRange 192.168.20.254 -SubnetMask 255.255.255.0 -LeaseDuration 6.00:00:00 -SuperScope "DCLOUD-Lab"
Set-DhcpServerv4OptionValue -ScopeId 192.168.20.0 -Router 192.168.20.1 
Add-Dhcpserverv4ExclusionRange -ScopeId 192.168.20.0 -StartRange 192.168.20.1 -EndRange 192.168.20.9
Set-DhcpServerv4OptionValue -ScopeId 192.168.20.0 -DnsServer 198.18.133.1 -DnsDomain "dcloud.cisco.com"
#Scope for voicevlan
Add-DhcpServerv4Scope -Name "DCLOUD-voicevlan" -StartRange 192.168.30.1 -EndRange 192.168.30.254 -SubnetMask 255.255.255.0 -LeaseDuration 6.00:00:00 -SuperScope "DCLOUD-Lab"
Set-DhcpServerv4OptionValue -ScopeId 192.168.30.0 -Router 192.168.30.1 
Add-Dhcpserverv4ExclusionRange -ScopeId 192.168.30.0 -StartRange 192.168.30.1 -EndRange 192.168.30.9
Set-DhcpServerv4OptionValue -ScopeId 192.168.30.0 -DnsServer 198.18.133.1 -DnsDomain "dcloud.cisco.com"
#Scope for guestvlan
Add-DhcpServerv4Scope -Name "DCLOUD-guestvlan" -StartRange 192.168.40.1 -EndRange 192.168.40.254 -SubnetMask 255.255.255.0 -LeaseDuration 6.00:00:00 -SuperScope "DCLOUD-Lab"
Set-DhcpServerv4OptionValue -ScopeId 192.168.40.0 -Router 192.168.40.1 
Add-Dhcpserverv4ExclusionRange -ScopeId 192.168.40.0 -StartRange 192.168.40.1 -EndRange 192.168.40.9
Set-DhcpServerv4OptionValue -ScopeId 192.168.40.0 -DnsServer 198.18.133.1 -DnsDomain "dcloud.cisco.com"
#Sope for disabledvlan
Add-DhcpServerv4Scope -Name "DCLOUD-disabledvlan" -StartRange 192.168.99.1 -EndRange 192.168.99.254 -SubnetMask 255.255.255.0 -LeaseDuration 6.00:00:00 -SuperScope "DCLOUD-Lab"
Set-DhcpServerv4OptionValue -ScopeId 192.168.99.0 -Router 192.168.99.1 
Add-Dhcpserverv4ExclusionRange -ScopeId 192.168.99.0 -StartRange 192.168.99.1 -EndRange 192.168.99.9
Set-DhcpServerv4OptionValue -ScopeId 192.168.99.0 -DnsServer 198.18.133.1 -DnsDomain "dcloud.cisco.com"
Set-DhcpServerv4OptionValue -ScopeId 192.168.99.0 -OptionId 43 -Value ([System.Text.Encoding]::ASCII.GetBytes("5A1N;B2;K4;I198.18.129.100;J80"))

Start-Sleep -Seconds 60

#####################################################################
#Set up DNS Entries for DNA Center
#####################################################################
Add-DnsServerResourceRecordA -Name "dnac-vip" -ZoneName "dcloud.cisco.com" -AllowUpdateAny -IPv4Address "198.18.129.100" -TimeToLive 01:00:00
Add-DnsServerResourceRecordCName -Name "dnac" -HostNameAlias "dnac-vip.dcloud.cisco.com" -ZoneName "dcloud.cisco.com"
#Additional line for pnpserver DNS Discovery for dcloud.com - to use remove leading HASH from next line
#Add-DnsServerResourceRecordCName -Name "pnpserver" -HostNameAlias "dnac-vip.dcloud.cisco.com" -ZoneName "dcloud.cisco.com"
Add-DnsServerResourceRecordA -Name "ise" -ZoneName "dcloud.cisco.com" -AllowUpdateAny -IPv4Address "198.18.133.27" -TimeToLive 01:00:00
Add-DnsServerResourceRecordCName -Name "guest" -HostNameAlias "ise.dcloud.cisco.com" -ZoneName "dcloud.cisco.com"
Add-DnsServerResourceRecordCName -Name "mydevice" -HostNameAlias "ise.dcloud.cisco.com" -ZoneName "dcloud.cisco.com"
Add-DnsServerResourceRecordCName -Name "sponsor" -HostNameAlias "ise.dcloud.cisco.com" -ZoneName "dcloud.cisco.com"
Add-DnsServerResourceRecordA -Name "wlc" -ZoneName "dcloud.cisco.com" -AllowUpdateAny -IPv4Address "198.18.134.100" -TimeToLive 01:00:00

Start-Sleep -Seconds 60

#####################################################################
#Set up DNS Entries for PnP Subdomain DNA Center
#####################################################################
Add-DnsServerPrimaryZone -Name "pnp.dcloud.cisco.com" -ReplicationScope "Forest" -PassThru

#Pause required to allow Zone to be created prior to CNAME Entry
Start-Sleep -Seconds 300

Add-DnsServerResourceRecordCName -Name "pnpserver" -HostNameAlias "dnac-vip.dcloud.cisco.com" -ZoneName "pnp.dcloud.cisco.com"
