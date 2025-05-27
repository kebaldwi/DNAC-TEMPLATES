# DayN Templates - In Development

![json](../../ASSETS/COMMON/BUILD/underconstruction.png?raw=true "Import JSON")

> [!WARNING]
> The contents of this lab are not ready for public use. Do not use this lab or attempt to use it until this header is removed entirely from the lab.

## Overview

This Module is designed and built to address how to use DayN templates within Cisco Catalyst Center to configure network devices at Day 1 through N. This Lab is designed to be used after first completing the previous modules. 

The purpose of DayN templates is to allow for **ongoing configuration** of features on devices beyond those deployed on the Claiming process. With Cisco Catalyst Center, if devices are not within a fabric, the host onboarding part of the UI will not be available. To that end, templates are an easy way of deploying those types of configuration and much more. Before starting this Lab, please make sure you have finished all the steps in the previous modules.

## Considerations about Templates

* PnP vs. DayN Templates: Cisco recommends using DayN Templates for most configurations, reserving PnP templates for establishing a stable network connection.

* Inventory Database Limitations: The inventory database is inaccessible before the claim process, complicating onboarding. This results in a need for manual input in scripts instead of leveraging known device information.

* Ongoing Modifications: DayN operations templates are stored within a project, while onboarding templates are located in the project Onboarding Configuration. Using onboarding templates post-PnP is impractical due to the absence of **system** and **bind** variables, which could simplify code and reduce repetition.

* Automation Potential: DayN templates facilitate ongoing modifications and automate configurations using data from the inventory database, minimizing manual input.

* Configuration Best Practices: Typical configurations should automatically derive from the Network Settings in Cisco Catalyst Center. Avoid deploying CLI code in templates for tasks already defined by design components, promoting a more UI-centric and maintainable configuration approach.

* Guidance: Utilize design settings for as much configuration as possible, keeping templates streamlined for configurations that may change frequently, enhancing maintainability and troubleshooting.

* **Jinja** vs **Velocity**, choose wisely. My recommendation is to use Jinja simply because it is the defactor template rendering language used in multiple platforms. It is modular, and the logic consrtucts are based on **Python**. 

## Developing a DayN Template

So what should be in the DayN Templates? Well that depends on the situation, but generally speaking we need to build the onboarding capability of the device, and put that which cannot change without disrupting the communication from Device to Catalyst Center.

Additionally, while a more extensive set of settings can be built out for deployment, we will limit the configuration to the **minimum** necessary to perform this step, building off the completed tasks in module 2.

You can create Regular Day N Templates using Jinja2 and Velocity scripting languages within the **Template Hub** within **Cisco Catalyst Center**. There are two basic types of templates we can utilize. **Regular** templates, as well as **Composite** templates. Use a combiination of these templates to adhere to the **DRY** philosophy.

### Regular Templates

**Regular** templates are templates which are typically designed to address a specific use case. Regular templates are written in either Jinja2 or Velocity scripting languages. Each Language has features which may be leveraged to make the script more reusable, allowing the user to not have to repeat themselves. This modular capability allows us to keep a script written to address a specific need small. At the same time each form of scripting language allows for features like variables, conditional logic, and looping constructs. This allows for a small powerful script to be written making it more light weight and easier to fault find and maintain.

### Composite Templates

**Composite** templates are logical templates used for grouping together multiple **Regular** templates. They allow you to use Jinja2 and Velocity **Regular** templates within the same logical template. This allows us to make templates in mutliple languages and to be able to reuse long standing Velocity scripts with newer Jinja2 templates within the same **Composite** Template. This allows for people to code in the language they are more accustomed too, and to continue to support existing scripts.

### Included items:

* System Configuration
  * Hostname
  * System MTU 
  * VTP 
  * Enable Netconf 
* Management Interface Configuration
  * IP address
  * Subnet Mask
  * Source Management Traffic
* Next Hop Configuration
  * Gateway or Routing Protocol

## Exercises

This section will go through the build and provisioning of **Composite** and **Regular** templates via Cisco Catalyst Center to a Catalyst 9k switch. We will deal with the **Greenfield** scenario only during this module. Remember that a similar approach could be used for **Brownfield**.

### Step 1 - Navigate to Template Hub

Navigate to the CLI Template Hub on Catalyst Center **`Tools > Template Hub`**

![json](../../ASSETS/LABS/CATC/MENU/catc-menu-5.png?raw=true "Import JSON")

### Step 2 - Create a Project

We will create a **Project** for the deployment of these switches within the lab. You may notice that there is a Project which was deployed during the lab preparation module. We will not be utilizing that here, but you could if you desired.

1. Add a new project

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PROJECT/add-project-1.png?raw=true "Import JSON")

1. Add a new project

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PROJECT/add-project-2.png?raw=true "Import JSON")

1. Add a new project

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PROJECT/add-project-3.png?raw=true "Import JSON")

1. Add a new project

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PROJECT/add-project-4.png?raw=true "Import JSON")

1. Add a new project

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PROJECT/add-project-5.png?raw=true "Import JSON")

1. Add a new project

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PROJECT/add-project-6.png?raw=true "Import JSON")

1. Add a new project

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PROJECT/add-project-7.png?raw=true "Import JSON")

1. Add a new project

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PROJECT/add-project-8.png?raw=true "Import JSON")

1. Add a new project

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PROJECT/add-project-9.png?raw=true "Import JSON")

1. Add a new project

   ![json](../../ASSETS/LABS/TEMPLATEEDITOR/PROJECT/add-project-10.png?raw=true "Import JSON")

### Step 3 - Analyze Configuration

Lets now take a look at a sample typical switch configuration from our network. We are going to review this in some detail in the next few sections and build modularized templates. As we do we will disect this configuration showing **how** and **where** specific configuration should be placed for scalability.

<details open>
<summary> Expand to review the complete configuration</summary>

```
service tcp-keepalives-in
service tcp-keepalives-out
service timestamps debug datetime msec localtime show-timezone
service timestamps log datetime msec show-timezone year
service password-encryption
service sequence-numbers
service call-home
no platform punt-keepalive disable-kernel-core
!
hostname ASW-9300-ACCESS
!
vrf definition Mgmt-vrf
 address-family ipv4
 exit-address-family
 address-family ipv6
 exit-address-family
!
logging buffered 16384 informational
no logging console
aaa new-model
!
aaa group server radius CON-VTY
 server-private 198.18.133.1 key 7 <redacted>
 ip radius source-interface Vlan5
 deadtime 6
!
aaa authentication login default local
aaa authentication login CON-LAB local-case
aaa authorization console
aaa authorization exec default local 
aaa authorization exec CON-LAB local 
aaa authorization network default group dnac-client-radius-group 
aaa accounting network default start-stop group radius
aaa session-id common
!
clock timezone EST -5 0
clock summer-time EDT recurring
switch 1 provision c9300-48u
!
ip routing
!
ip name-server 198.18.133.1
ip domain lookup source-interface Vlan5
ip domain name base2hq.com
!
udld enable
lldp run
!
vtp domain base2hq.com
vtp mode transparent
vtp version 1
!
port-channel load-balance src-dst-ip
!
spanning-tree mode rapid-pvst
spanning-tree portfast default
spanning-tree portfast bpduguard default
spanning-tree extend system-id
!
enable secret 9 <redacted>
username admin privilege 15 secret 9 <redacted>
!
redundancy
 mode sso
!
vlan 5
 name mgmtvlan
vlan 10
 name apvlan
vlan 20
 name datavlan
vlan 30
 name voicevlan
vlan 40
 name guestvlan
!
interface Port-channel1
 switchport trunk native vlan 5
 switchport trunk allowed vlan 5,10,20,30,40
 switchport mode trunk
!
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 no ip address
 shutdown
 negotiation auto
!
interface range GigabitEthernet1/0/1-48
 switchport access vlan 20
 switchport voice vlan 30
 spanning-tree portfast
!
interface TenGigabitEthernet1/1/1, TenGigabitEthernet1/1/2 
 switchport trunk allowed vlan 1,5,10,20,30,40
 switchport mode trunk
 channel-group 1 mode active
 channel-protocol lacp 
!
interface Vlan5
 description MgmtVlan
 ip address 192.168.5.3 255.255.255.0
 no ip redirects
 no ip proxy-arp
!
ip forward-protocol nd
ip http server
ip http authentication local
ip http secure-server
ip http secure-trustpoint <redacted>
ip http client source-interface Vlan5
ip ssh time-out 60
ip ssh source-interface Vlan5
ip ssh version 2
!
ip radius source-interface Vlan5 
ip sla enable reaction-alerts
logging origin-id ip
logging source-interface Vlan5
logging host 10.10.0.20
logging host 198.18.133.27 transport udp port 20514
!
snmp-server community private RW
snmp-server community public RO
snmp-server trap-source Vlan5
snmp-server enable traps all
snmp-server host 10.10.0.20 version 2c private 
snmp-server host 198.18.133.27 version 2c private 
snmp-server host 10.10.0.20 version 2c public 
snmp-server host 198.18.133.27 version 2c public 
!
radius-server attribute 6 on-for-login-auth
radius-server attribute 6 support-multiple
radius-server attribute 8 include-in-access-req
radius-server attribute 25 access-request include
radius-server attribute 31 mac format ietf upper-case
radius-server attribute 31 send nas-port-detail mac-only
radius-server dead-criteria time 5 tries 3
radius-server retransmit 2
radius-server deadtime 3
!
radius server dnac-radius_198.18.133.27
 address ipv4 198.18.133.27 auth-port 1812 acct-port 1813
 timeout 4
 retransmit 3
 automate-tester username dummy ignore-acct-port probe-on
 pac key 7 <redacted>
!
banner login ^
  Session On $(hostname) Is Monitored!!!
  *****************************LEGAL WARNING************************************
  * This device is part of a Demonstration computer network and is provided for*
  * official use by authorized users ONLY. Any information, documents, or      *
  * materials in the network are the property of this firm. Unauthorized use,  *
  * duplication, or disclosure of information or systems in this network is    *
  * strictly prohibited by Federal Law (18 USC 10130). Use of this network     *
  * constitutes consent to monitoring which may be released to firm management *
  * and/or law enforcement agencies and may result in disciplinary action,     *
  * civil action, and/or criminal prosecution.                                 *
  ****************************LEGAL WARNING*************************************
^
!
line con 0
 exec-timeout 0 0
 privilege level 15
 authorization exec CON-LAB
 logging synchronous
 login authentication CON-LAB
 stopbits 1
line vty 0 31
 exec-timeout 0 0
 authorization exec CON-LAB
 logging synchronous
 login authentication CON-LAB
 terminal-type mon
 length 0
 transport input ssh
!
ntp source Vlan5
ntp server 198.18.133.1
!
end
```

</details>

1. Lets discount any config that is automated by default from Catalyst Center claim process. This config that is **deployed automatically**. Along with this we will discount any configuration which is **default configuration** on the switch as that will already be there. Thus they do not need a place in our template.

   <details open>
   <summary> Expand to review the complete configuration</summary>
   
   ```
   archive
    log config
     logging enable
     logging size 500
     hidekeys
     !
    !
   !
   service timestamps debug datetime msec
   service timestamps log datetime msec
   service password-encryption
   service sequence-numbers
   !
   ! Disable external HTTP(S) access
   ! Disable external Telnet access
   ! Enable external SSHv2 access
   !
   no ip http server
   !
   no ip http secure-server
   !
   crypto key generate rsa label dnac-sda modulus 2048
   ip ssh version 2
   !
   ip scp server enable
   !
   line vty 0 15
    ! maybe redundant
   login xxxxxx
    transport input ssh
    ! maybe redundant
    transport preferred none
   !
   ! Set VTP mode to transparent (no auto VLAN propagation)
   ! Set STP mode to Rapid PVST+ (prefer for non-Fabric compatibility)
   ! Enable extended STP system ID
   ! Set Fabric Node to be STP Root for all local VLANs
   ! Enable STP Root Guard to prevent non-Fabric nodes from becoming Root
   ! Confirm whether vtp mode transparent below is needed
   vtp mode transparent
   !
   spanning-tree mode rapid-pvst
   !
   spanning-tree extend system-id
   ! spanning-tree bridge priority 0
   ! spanning-tree rootguard
   ! spanning-tree portfast bpduguard default
   no udld enable
   !
   errdisable recovery cause all
   !
   errdisable recovery interval 300
   !
   ! Enable SNMP and RW access
   !
   snmp-server xxxxxxxx
   !
   username xxxxxx
   !
   enable algorithm-type scrypt secret xxxxxxxx
   !
   hostname Switch
   ! DNS settings
   !
   ip domain name base2hq.com
   !
   ip name-server 10.10.0.250
   !
   ```
   </details>

1. Lets also discount any configurations which will be in the **Design** section or have been deployed via the **PnP Claiming Process**. These are the number of lines **REMOVED** at this point.

   <details open>
   <summary> Expand to review the removed configuration</summary>
   
   ```
   service password-encryption
   service sequence-numbers
   service call-home
   no platform punt-keepalive disable-kernel-core
   !
   hostname ASW-9300-ACCESS
   !
   vrf definition Mgmt-vrf
    address-family ipv4
    exit-address-family
    address-family ipv6
    exit-address-family
   !
   switch 1 provision c9300-48u
   !
   ip name-server 198.18.133.1
   ip domain lookup source-interface Vlan5
   ip domain name base2hq.com
   !
   vtp domain base2hq.com
   vtp mode transparent
   vtp version 1
   !
   spanning-tree mode rapid-pvst
   spanning-tree extend system-id
   !
   enable secret 9 <redacted>
   username admin privilege 15 secret 9 <redacted>
   !
   vlan 5
    name mgmtvlan
   !
   interface Port-channel1
    switchport trunk native vlan 5
    switchport trunk allowed vlan 5
    switchport mode trunk
   !
   interface GigabitEthernet0/0
    vrf forwarding Mgmt-vrf
    no ip address
    negotiation auto
   !
   interface TenGigabitEthernet1/1/1, TenGigabitEthernet1/1/2 
    switchport trunk allowed vlan 1,5
    switchport mode trunk
    channel-group 1 mode active
    channel-protocol lacp 
   !
   interface Vlan5
    description MgmtVlan
    ip address 192.168.5.3 255.255.255.0
    no ip redirects
    no ip proxy-arp
   !
   ip ssh source-interface Vlan5
   ip ssh version 2
   !
   ip radius source-interface Vlan5 
   logging source-interface Vlan5
   logging host 10.10.0.20
   logging host 198.18.133.27 transport udp port 20514
   !
   snmp-server community private RW
   snmp-server community public RO
   snmp-server trap-source Vlan5
   snmp-server enable traps all
   snmp-server host 10.10.0.20 version 2c private 
   snmp-server host 198.18.133.27 version 2c private 
   snmp-server host 10.10.0.20 version 2c public 
   snmp-server host 198.18.133.27 version 2c public 
   !
   ntp source Vlan5
   ntp server 198.18.133.1
   !
   end
   ```
   
   </details>

1. The remaining configuration shown here can be modularized to simplify it. Here is what is left which we will use templates to build.

   <details open>
   <summary> Expand to review the complete configuration</summary>
   
   ```
   service tcp-keepalives-in
   service tcp-keepalives-out
   service timestamps debug datetime msec localtime show-timezone
   service timestamps log datetime msec show-timezone year
   !
   logging buffered 16384 informational
   no logging console
   !
   aaa new-model
   aaa group server radius CON-VTY
    server-private 198.18.133.1 key 7 <redacted>
    deadtime 6
   aaa authentication login default local
   aaa authentication login CON-LAB local-case
   aaa authorization console
   aaa authorization exec default local 
   aaa authorization exec CON-LAB local 
   aaa authorization network default group dnac-client-radius-group 
   aaa accounting network default start-stop group radius
   aaa session-id common
   !
   clock timezone EST -5 0
   clock summer-time EDT recurring
   !
   ip routing
   !
   udld enable
   lldp run
   !
   port-channel load-balance src-dst-ip
   !
   spanning-tree portfast default
   spanning-tree portfast bpduguard default
   !
   redundancy
    mode sso
   !
   vlan 5
    name mgmtvlan
   vlan 10
    name apvlan
   vlan 20
    name datavlan
   vlan 30
    name voicevlan
   vlan 40
    name guestvlan
   !
   interface Port-channel1
    switchport trunk allowed vlan 5,10,20,30,40
   !
   interface GigabitEthernet0/0
    shutdown
   !
   interface range GigabitEthernet1/0/1-48
    switchport access vlan 20
    switchport voice vlan 30
    spanning-tree portfast
   !
   interface TenGigabitEthernet1/1/1, TenGigabitEthernet1/1/2 
    switchport trunk allowed vlan 1,5,10,20,30,40
   !
   ip forward-protocol nd
   ip http server
   ip http authentication local
   ip http secure-server
   ip http secure-trustpoint <redacted>
   ip ssh time-out 60
   ip ssh source-interface Vlan5
   ip ssh version 2
   !
   ip sla enable reaction-alerts
   logging origin-id ip
   logging host 10.10.0.20
   logging host 198.18.133.27 transport udp port 20514
   !
   radius-server attribute 6 on-for-login-auth
   radius-server attribute 6 support-multiple
   radius-server attribute 8 include-in-access-req
   radius-server attribute 25 access-request include
   radius-server attribute 31 mac format ietf upper-case
   radius-server attribute 31 send nas-port-detail mac-only
   radius-server dead-criteria time 5 tries 3
   radius-server retransmit 2
   radius-server deadtime 3
   !
   radius server dnac-radius_198.18.133.27
    address ipv4 198.18.133.27 auth-port 1812 acct-port 1813
    timeout 4
    retransmit 3
    automate-tester username dummy ignore-acct-port probe-on
    pac key 7 <redacted>
   !
   banner login ^
     Session On $(hostname) Is Monitored!!!
     *****************************LEGAL WARNING************************************
     * This device is part of a Demonstration computer network and is provided for*
     * official use by authorized users ONLY. Any information, documents, or      *
     * materials in the network are the property of this firm. Unauthorized use,  *
     * duplication, or disclosure of information or systems in this network is    *
     * strictly prohibited by Federal Law (18 USC 10130). Use of this network     *
     * constitutes consent to monitoring which may be released to firm management *
     * and/or law enforcement agencies and may result in disciplinary action,     *
     * civil action, and/or criminal prosecution.                                 *
     ****************************LEGAL WARNING*************************************
   ^
   !
   line con 0
    exec-timeout 0 0
    privilege level 15
    authorization exec CON-LAB
    logging synchronous
    login authentication CON-LAB
    stopbits 1
   line vty 0 31
    exec-timeout 0 0
    authorization exec CON-LAB
    logging synchronous
    login authentication CON-LAB
    terminal-type mon
    length 0
    transport input ssh
   !
   end
   ```
   
   </details>

1. The first thing
1. The first thing
1. The first thing
1. The first thing
1. The first thing


## Summary

Congratulations you have completed xxx

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Continue to DayN Provisioning Module**](../LAB-3-Advanced-Automation/module5-dayn.md)

> [**Return to Lab Menu**](./README.md)