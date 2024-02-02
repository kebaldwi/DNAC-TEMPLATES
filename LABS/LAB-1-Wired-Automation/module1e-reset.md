# PnP Preparation Continued

## Step 6 - Reset EEM Script or PnP Service Reset

When testing, you will frequently need to start again on the switch to test the whole flow. To accomplish this, paste this small script into the 9300 target switch, which will create a file on flash which you may load into the running-configuration at any time to reset the device to factory settings:

There are now two methods for this The first and simplest method is to make use of the **`pnp service reset`** command as advised by Matthew Bishop. This command was introduced in a recent Train of XE code. This command may not erase all information on the device. I strongly recommend using the EEM Script.

Failing that we have an EEM script which you may use iterated below.

```tcl
tclsh                            
puts [open "flash:prep4dnac" w+] {
!
! Remove any confirmation dialogs when accessing flash
file prompt quiet
!
no event manager applet prep4dnac
event manager applet prep4dnac
 event none sync yes
 action a1010 syslog msg "Starting: 'prep4dnac'  EEM applet."
 action a1020 puts "Preparing device to be discovered by device automation - This script will reboot the device."
 action b1010 cli command "enable"
 action b1020 puts "Saving config to update BOOT param."
 action b1030 cli command "write"
 action c1010 puts "Erasing startup-config."
 action c1020 cli command "wr er" pattern "confirm"
 action c1030 cli command "y"
 action d1010 puts "Clearing crypto keys."
 action d1020 cli command "config t"
 action d1030 cli command "crypto key zeroize" pattern "yes/no"
 action d1040 cli command "y"
 action e1010 puts "Clearing crypto PKI stuff."
 action e1020 cli command "no crypto pki cert pool" pattern "yes/no"
 action e1030 cli command "y"
 action e1040 cli command "exit"
 action f1010 puts "Deleting vlan.dat file."
 action f1020 cli command "delete /force vlan.dat"
 action g1010 puts "Deleting certificate files in NVRAM."
 action g1020 cli command "delete /force nvram:*.cer"
 action h0001 puts "Deleting PnP files"
 action h0010 cli command "delete /force flash:pnp*"
 action h0020 cli command "delete /force nvram:pnp*"
 action i0001 puts "Reseting Stack Priority"
 action i0010 cli command "switch 1 priority 1"
 action z1010 puts "Device is prepared for being discovered by device automation.  Rebooting."
 action z1020 syslog msg "Stopping: 'prep4dnac' EEM applet."
 action z1030 reload
exit
!
alias exec prep4dnac event manager run prep4dnac
!
end
}
tclquit
```

Additionally, for help with troubleshooting, install this helpful EEM script in the directory in the same manner as above. This will help to see which lines were sent to the switch and helps deduce where a template may be failing.

```tcl
tclsh
puts [open "flash:dnacts" w+] {
!
event manager applet CLI_COMMANDS-->
event cli pattern ".*" sync no skip no
action 1 syslog msg "$_cli_msg"
!
}
tclquit
```

#### Step 6.1 - ***Reset Switch and Test Discovery***

Finally, we want to test the routing, connectivity, DHCP, DNS services, and discovery mechanism. Reset the ***c9300-1*** Target switch by pasting the following sequence into the console. We will watch the switch come up but not intercede or type anything into the console after the reboot has started.

```vtl
!
copy prep4dnac running-config
!
prep4dnac
!
```

The Switch should reboot and display this eventually in the console which acknowledges that the 9300 has discovered the Cisco Catalyst Center.

![json](./images/DNAC-IPV4-DISCOVERY.png?raw=true "Import JSON")

Additionally, within Cisco Catalyst Center on the Plug and Play window, the device should show as unclaimed.

![json](./images/DNAC-9300-Discovery.png?raw=true "Import JSON")

## Summary

The next step will be to build the PnP Onboarding settings and template on Cisco Catalyst Center, which we will cover in the next lab entitled [**Onboarding Templates**](../LAB-B-Onboarding-Template/README.md#Day0) - The next lab explains in-depth and how to deploy Day 0 templates.

> **Feedback:** If you found this repository please fill in comments and [**give feedback**](https://app.smartsheet.com/b/form/f75ce15c2053435283a025b1872257fe) on how it could be improved.

> [**Continue to PnP and Discovery Lab**](./module2-pnp.md)

> [**Return to LAB Menu**](./README.md)