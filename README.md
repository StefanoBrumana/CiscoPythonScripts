# CiscoPythonScripts
Python scripts for Cisco IOS devices

## Purpose of scripts

CiscoMultiTelnet.py: interactive script to telnet multiple Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, enter commands ( listed in the commands.txt file saved in the same folder of this script ) and save the entire log into a .txt file whose name is made by IP address of target device + date/time

CiscoMultiSsh.py: interactive script to ssh multiple Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, enter commands ( listed in commands.txt file that must be manually created in the same folder of this script ) and save the entire log into a .txt file whose name is made by IP address of target device + date/time

CiscoMultiTftpUploadTelnet.py: to access via telnet to a list of Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, export their startup-config to the root folder of a TFTP server ( all these activities are logged in a .txt file created in the same folder of the script )

CiscoMultiTftpUploadSsh.py: to access via ssh to a list of Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, export their startup-config to the root folder of a TFTP server ( all these activities are logged in a .txt file created in the same folder of the script )

### Usage of logs produced by the script

If log file has empty lines, try to use "terminal width 80" command ( if supported by the target Cisco device ): otherwise you can use the remove empty lines feature integrated in the menus of Notepad++ ( my favourite free app to consult log files: it also has a compare plug-in to quickly locate differences )

#### How to run the script ( in Windows command prompt )

Open a DOS prompt and change to folder containing the .py script + ip.txt and commands.txt files.
Launch the script ( python was added to the system path of Windows to run it from any folder of this pc ) and answer to the questions appearing on screen.
Some of the below details like usernanme/password/IP addresses were edited for privacy: the main purpose here is to explain how to run the script.

C:\Temp\PythonScripts>python CiscoMultiTelnet.py
##############################
Python telnet script for Cisco
##############################
Has target device an username required for telnet access (Y/N)?y
Enter Username: cisco123
Password: **********
Has target device an enable password (Y/N)?y
Enter enable password: ************
Working on device 192.168.1.10
Executing and logging these commands:
terminal length 0

terminal width 80

show clock

show version

show run

############# end of python script #############
End of operations on device 192.168.1.10
All logged into file 192.168.1.10_04252023-111844.txt
Wait conclusion of the entire process before opening any log file
##############################################
##############################################
##############################################
All operations logged into your present folder

C:\Temp\PythonScripts>

#### Example of log obtained after launching the script 

A .txt file ( whose name is IP address of the target device + date/time of the script execution - example: 192.168.1.10_04252023-111844.txt ) is created in the same folder of the script.
Some of the below details like usernanme/password/IP addresses were cut or edited for privacy: the main purpose here is to explain what log can be produced.

Switch>enable
Password: 
Switch#terminal length 0
Switch#
Switch#terminal width 80
Switch#
Switch#show clock
11:18:32.632 CCT Tue Apr 25 2023
Switch#
Switch#show version
Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(55)SE5, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2012 by Cisco Systems, Inc.
Compiled Thu 09-Feb-12 18:14 by prod_rel_team
Image text-base: 0x00003000, data-base: 0x02800000
ROM: Bootstrap program is C3750E boot loader
BOOTLDR: C3750E Boot Loader (C3750X-HBOOT-M) Version 12.2(53r)SE1, RELEASE SOFTWARE (fc1)
Switch uptime is 1 year, 9 weeks, 2 days, 1 hour, 14 minutes
System returned to ROM by power-on
System restarted at 10:23:12 CCT Sat Feb 19 2022
System image file is "flash:/c3750e-universalk9-mz.122-55.SE5/c3750e-universalk9-mz.122-55.SE5.bin"
This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.
A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html
If you require further assistance please contact us by sending email to
export@cisco.com.
License Level: ipbase
License Type: Permanent
Next reload license Level: ipbase
cisco WS-C3750X-48 (PowerPC405) processor (revision A0) with 262144K bytes of memory.
Processor board ID FDOxxxxxxxx
Last reset from power-on
3 Virtual Ethernet interfaces
1 FastEthernet interface
52 Gigabit Ethernet interfaces
2 Ten Gigabit Ethernet interfaces
The password-recovery mechanism is enabled.
512K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : 44:03:A7:xx:xx:xx
Motherboard assembly number     : 73-xxxxx-xx
Motherboard serial number       : FDOxxxxxxxx
Model revision number           : A0
Motherboard revision number     : A0
Model number                    : WS-C3750X-48T-S
Daughterboard assembly number   : 800-xxxxx-xx
Daughterboard serial number     : FDOxxxxxxxx
System serial number            : FDOxxxxxxxx
Top Assembly Part Number        : 800-xxxxx-xx
Top Assembly Revision Number    : A0
Version ID                      : V03
CLEI Code Number                : COMxxxxxxx
Hardware Board Revision Number  : 0x04
Switch Ports Model              SW Version            SW Image                 
------ ----- -----              ----------            ----------               
*    1 54    WS-C3750X-48       12.2(55)SE5           C3750E-UNIVERSALK9-M     
Configuration register is 0xF
Switch#
Switch#show run
Building configuration...
Current configuration : 7422 bytes
!
! Last configuration change at 18:29:39 CCT Wed Apr 12 2023 by cisc0sw2
! NVRAM config last updated at 19:18:17 CCT Tue Sep 20 2022 by cisc0sw2
!
version 12.2
no service pad
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname Switch
!
boot-start-marker
boot-end-marker
!
enable secret 5 **********************
enable password **********
!
username cisco123 password 0 **********
!
!
no aaa new-model
clock timezone CCT 2
switch 1 provision ws-c3750x-48
system mtu routing 1500
ip routing
!
!
no ip domain-lookup
ip domain-name test.it
vtp mode off
!
....
spanning-tree mode mst
spanning-tree extend system-id
!
!
!
no errdisable detect cause gbic-invalid
!
vlan internal allocation policy ascending
!
vlan 100
 name data
!
vlan 200
 name data-2
!
lldp run
!
!
interface FastEthernet0
 no ip address
 no ip route-cache cef
 no ip route-cache
 shutdown
!
interface GigabitEthernet1/0/1
 switchport access vlan 100
 switchport mode access
....
interface TenGigabitEthernet1/1/2
 speed nonegotiate
!
interface Vlan1
 no ip address
 shutdown
!
interface Vlan100
 description vlan-data
 ip address 192.168.1.10 255.255.255.0
!
....
ntp clock-period 36027235
ntp server 192.168.1.50
end
Switch#
Switch############## end of python script #############
Switch#exit
                                                                                                                                                                       Log closed on 04252023-111844
