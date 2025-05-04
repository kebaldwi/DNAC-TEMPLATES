# DCLOUD LAB Preparation

## DCLOUD VPN Connection

Use AnyConnect VPN to connect to DCLOUD. When connecting, look at the session details and copy the credentials from the session booked into the client to connect.

![json](../ASSETS/COMMON/DCLOUD/VPN-into-DCLOUD.png?raw=true "Import JSON")

## DCLOUD Service Optimization

The DCLOUD environment used in the lab need to be optimized prior to the session, and to do this we need to disable the following:

<p align="center"><img src="../ASSETS/COMMON/DCLOUD/ShutdownUnused.png" width="500" height="690"></p>

In order to accomplish this, use the drop down menu item by each that is shutdown in the image and click the shutdown link.

## DCLOUD Topology

There are two DCLOUD topologies which you will encounter in DCLOUD. One is in the **RTP - EAST DC** and differing one in the **SJC - WEST DC**.

These two topologies eventually will mirror each other but for now the **SJC - WEST DC** is unique.

### Original Topology:

This topology is the same topology we have always used in the lab we will need to make modifications to ensure that the lab will work for these exercises.

![json](../ASSETS/COMMON/DCLOUD/DCLOUD_Topology2.png?raw=true "Import JSON")

When using both the **RTP - EAST DC** and **SJC - WEST DC** you will need to ensure the topology is logically aligned to the above. To do that we will hide Catalyst 9300-3 in the diagram below using **802.1q Tunneling** which is a service provider type fix.  

### SJC - WEST DC:

This topology has been altered from the original topology we have always used in the lab and requires small modifications.

[Cisco Enterprise Networks Hardware Sandbox East DC](https://dcloud2-rtp.cisco.com/content/catalogue?search=Enterprise%20Networks%20Hardware%20Sandbox&screenCommand=openFilterScreen)

[Cisco Enterprise Networks Hardware Sandbox West DC](https://dcloud2-sjc.cisco.com/content/catalogue?search=Enterprise%20Networks%20Hardware%20Sandbox&screenCommand=openFilterScreen)

![json](../ASSETS/COMMON/DCLOUD/DCLOUD_Topology3.png?raw=true "Import JSON")

When using the **SJC - WEST DC** you need to proceed with the following mitigating steps which we will detail below:

1. Open a connection to the console on the **Catalyst 9300 - 3**
2. Log into the switch with the following credentials:

   - username: netadmin
   - password: C1sco12345
   - enable:   C1sco12345

3. Paste the following into the terminal 

```
term length 0
tclsh                            
puts [open "flash:base9300-3.cfg" w+] {
version 17.9
service timestamps debug datetime msec
service timestamps log datetime msec
no platform punt-keepalive disable-kernel-core
hostname c9300-3
vrf definition Mgmt-vrf
 address-family ipv4
 exit-address-family
 address-family ipv6
 exit-address-family
no logging console
enable password C1sco12345
aaa new-model
aaa authentication login default local
aaa authentication login CONSOLE none
aaa authorization exec default local 
aaa session-id common
ip routing
ip domain name dcloud.cisco.com
username admin privilege 15 password 0 C1sco12345
username netadmin privilege 15 password 0 C1sco12345
vlan 123
name dot1qtunnel
interface GigabitEthernet0/0
 vrf forwarding Mgmt-vrf
 ip address 198.18.128.24 255.255.255.0
 negotiation auto
int gi 1/0/1
 shut
interface range GigabitEthernet1/0/2, GigabitEthernet1/0/48
 switchport access vlan 123
 switchport mode dot1q-tunnel
 no cdp enable
 l2protocol-tunnel cdp
 l2protocol-tunnel stp
 l2protocol-tunnel vtp
 l2protocol-tunnel lldp
 l2protocol-tunnel point-to-point pagp
 l2protocol-tunnel point-to-point lacp
 l2protocol-tunnel point-to-point udld
interface Vlan1
 no ip address
ip http server
ip http authentication local
ip http secure-server
ip http client source-interface GigabitEthernet0/0
ip route vrf Mgmt-vrf 0.0.0.0 0.0.0.0 198.18.128.1
ip ssh version 2
snmp-server community public RO
snmp-server community private RW
line con 0
 login authentication CONSOLE
 stopbits 1
line vty 0 4
 password C1sco12345
iox
end
}
tclquit
!
copy base9300-3.cfg run
!
!
```

4. Ensure the following configuration appears on ports Gi 1/0/2 and Gi 1/0/48 and that Gi 1/0/1 is shutdown.

```
 switchport access vlan 123
 switchport mode dot1q-tunnel
 no cdp enable
 l2protocol-tunnel cdp
 l2protocol-tunnel stp
 l2protocol-tunnel vtp
 l2protocol-tunnel lldp
 l2protocol-tunnel point-to-point pagp
 l2protocol-tunnel point-to-point lacp
 l2protocol-tunnel point-to-point udld
```

5. After 5 minutes check the CDP relationship on all devices except the C9300-3 to verify that the lab is set up logically like this:

![json](../ASSETS/COMMON/DCLOUD/DCLOUD_Topology2.png?raw=true "Import JSON")

## DCLOUD LAB Readiness Checks and Troubleshooting

Open a connection to the console for the following:

- **[ISR 4331](#isr-4331-readiness)**
- **[Catalyst 9300 - 1](#catalyst-9300---1-readiness)**
- **[Catalyst 9300 - 2](#catalyst-9300---2-readiness)**
- **Catalyst 9300 - 3**
- **[AP 1](#ap-1-and-ap-2-readiness)**
- **[AP 2](#ap-1-and-ap-2-readiness)**

### **ISR 4331** Readiness

1. Log into the **ISR 4331** router with the following credentials:

   - username: netadmin
   - password: C1sco12345
   - enable:   C1sco12345

2. Paste the following into the terminals for the router and switches:

   ```
   
   sh cdp neigh
   sh ip ospf ne
   sh run | s username|snmp|netconf

   ```

4. You should see on the **ISR 4331** the following:

### **Catalyst 9300 - 1** Readiness

1. Log into the **Catalyst 9300 - 1** switch with the following credentials:

   - username: netadmin
   - password: C1sco12345
   - enable:   C1sco12345

2. Paste the following into the terminals for the router and switches:

   ```
   
   sh cdp neigh
   sh ip ospf ne
   sh run | s username|snmp|netconf

   ```

5. You should see on the **Catalyst 9300 - 1** the following:

### **Catalyst 9300 - 2** Readiness

1. Log into the **Catalyst 9300 - 2** switch with the following credentials:

   - username: netadmin
   - password: C1sco12345
   - enable:   C1sco12345

2. Paste the following into the terminals for the router and switches:

   ```
   
   sh cdp neigh
   sh ip ospf ne
   sh run | s username|snmp|netconf

   ```

6. You should see on the **Catalyst 9300 - 2** the following:

### **AP 1** and **AP 2** Readiness

> [!CAUTION]
> During this section wait until the Catalyst 9300 - 1 and Catalyst 9300 - 2 are both in an up state and not in a reboot of some kind.

1. Log into the **AP 1** and **AP 2** access points with the following credentials:

   - username: Cisco
   - password: Cisco
   - enable:   Cisco

2. You should be able to log in. If you cannot then complete the following:

   1. Try to log in using the following credentials:

      - username: admin
      - password: Cisco12345
      - enable:   Cisco12345
   
   2. If successful enter the following command and say **Yes** or **Enter** at any prompt to begin the reset sequence.

      ```
      capwap ap erase all
      ```
   
   3. The Access Point will reset and should at this point be ready for the lab.

> [!IMPORTANT]
> **Feedback:** If you found this set of **labs** or **content** helpful, please fill in comments on this feedback form [give feedback](https://github.com/kebaldwi/DNAC-TEMPLATES/discussions/new?category=feedback-and-ideas).</br></br>
**Content Problems and Issues:** If you found an **issue** on the **lab** or **content** please fill in an [issue](https://github.com/kebaldwi/DNAC-TEMPLATES/issues/new) include what file, along with the issue you ran into. 

> [**Return to Lab Menu**](./README.md)