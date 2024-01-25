# DHCP Discovery using Windows DHCP Service

As you may recall, for a device to discover Cisco Catalyst Center, the device uses a discovery method to help it find Cisco Catalyst Center. 

The PnP components are as follows:

![json](../../ASSETS/pnp-workflows.png?raw=true "Import JSON")

There are three automated methods to make that occur:

1. **DHCP with option 43** - ***requires the DHCP server to offer a PnP string via option 43***
2. **DNS lookup** 
    - *requires the DHCP server to offer a domain suffix and a name server to resolve the **pnpserver** address*
    - *requires the **pnpserver** entry to appear in the Subject Alternative Name of the GUI Certificate*
3. **Cloud re-direction** via *https://devicehelper.cisco.com/device-helper* - *requires the DHCP server to offer a name server to make DNS resolutions*

#### Step 1.2b - ***Windows Server Configuration***

If we want to use the Windows DHCP service, connect to the windows ***AD1*** server. On the windows server, you have two options to deploy DHCP scopes the UI or PowerShell. We will deploy the scope via PowerShell. Paste the following into PowerShell to create the required DHCP scope:

```ps
Add-DhcpServerv4Scope -Name "DNAC-Templates-Lab" -StartRange 192.168.5.1 -EndRange 192.168.5.254 -SubnetMask 255.255.255.0 -LeaseDuration 6.00:00:00 -SuperScope "PnP Onboarding"
Set-DhcpServerv4OptionValue -ScopeId 192.168.5.0 -Router 192.168.5.1 
Add-Dhcpserverv4ExclusionRange -ScopeId 192.168.5.0 -StartRange 192.168.5.1 -EndRange 192.168.5.1
```

The DHCP scope will look like this in Windows DHCP Administrative tool:

![json](./images/WindowsDHCPscoperouteronly.png?raw=true "Import JSON")

Next, we will introduce the helper address statement on the management VLAN's SVI to point to the Windows DHCP server. Connect to switch ***c9300-2*** and paste the following configuration:

```vtl
!
conf t
!
  interface Vlan 5                         
     ip helper-address 198.18.133.1                  
     end
!
wr
!
```

#### Step 2.1b - ***Option 43 with Windows DHCP Configuration***

If using the Windows DHCP Server and the desire is to use Option 43 discovery method, then paste the following configuration into PowerShell:

```ps
Set-DhcpServerv4OptionValue -ScopeId 192.168.5.0 -OptionId 43 -Value ([System.Text.Encoding]::ASCII.GetBytes("5A1N;B2;K4;I198.18.129.100;J80"))
```

The DHCP scope modification will resemble the following image of the Windows DHCP Administrative tool:

![json](./images/DNACDHCPoption43.png?raw=true "Import JSON")
