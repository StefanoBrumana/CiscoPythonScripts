# CiscoPythonScripts
Python scripts for Cisco IOS devices

Summary:

## Purpose of scripts
### Usage of logs produced by the script
#### How to run the script ( in Windows command prompt )
#### Example of log obtained after launching the script 

## Purpose of scripts

CiscoMultiTelnet.py: interactive script to telnet multiple Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, enter commands ( listed in the commands.txt file saved in the same folder of this script ) and save the entire log into a .txt file whose name is made by IP address of target device + date/time

CiscoMultiSsh.py: interactive script to ssh multiple Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, enter commands ( listed in commands.txt file that must be manually created in the same folder of this script ) and save the entire log into a .txt file whose name is made by IP address of target device + date/time

CiscoMultiTftpUploadTelnet.py: to access via telnet to a list of Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, export their startup-config to the root folder of a TFTP server ( all these activities are logged in a .txt file created in the same folder of the script )

CiscoMultiTftpUploadSsh.py: to access via ssh to a list of Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, export their startup-config to the root folder of a TFTP server ( all these activities are logged in a .txt file created in the same folder of the script )

### Usage of logs produced by the script

If log file has empty lines, try to use "terminal width 80" command ( if supported by the target Cisco device )
Otherwise you can use the remove empty lines feature integrated in the menus of Notepad++ 
It is a free app to consult log files: it also has a compare plug-in to quickly locate differences

#### How to run the script ( in Windows command prompt )

Open a DOS prompt and change to folder containing the .py script + ip.txt and commands.txt files.

Launch the script ( python was added to the system path of Windows to run it from any folder of this pc ) and answer to the questions appearing on screen
The file "192.168.1.10_Example.txt" in this repository shows an example of what you will see on screen when the script is launched
Some of the details like usernanme/password/IP addresses were edited for privacy: the main purpose here is to explain how to run the script

#### Example of log obtained after launching the script 

A .txt file ( whose name is IP address of the target device + date/time of the script execution - example: 192.168.1.10_04252023-111844.txt ) is created in the same folder of the script
The file "192.168.1.10_04252023-111844.txt" in this repository shows an example of a log produced by the script
Some of the details like usernanme/password/IP addresses were cut or edited for privacy: the main purpose here is to explain what log can be obtained

