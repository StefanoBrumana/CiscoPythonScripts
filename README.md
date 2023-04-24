# CiscoPythonScripts
Python scripts for Cisco IOS devices

CiscoMultiTelnet.py: interactive script to telnet multiple Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, enter commands ( listed in the commands.txt file saved in the same folder of this script ) and save the entire log into a .txt file whose name is made by IP address of target device + date/time

CiscoMultiSsh.py: interactive script to ssh multiple Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, enter commands ( listed in commands.txt file that must be manually created in the same folder of this script ) and save the entire log into a .txt file whose name is made by IP address of target device + date/time

CiscoMultiTftpUploadTelnet.py: to access via telnet to a list of Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, export their startup-config to the root folder of a TFTP server ( all these activities are logged in a .txt file created in the same folder of the script )

CiscoMultiTftpUploadSsh.py: to access via ssh to a list of Cisco devices ( listed in ip.txt file that must be manually created in the same folder of this script ) all with same username, password and (optional) enable password, export their startup-config to the root folder of a TFTP server ( all these activities are logged in a .txt file created in the same folder of the script )

If log file has empty lines, try to use "terminal width 80" command ( if supported by the target Cisco device ): otherwise you can use the remove empty lines feature integrated in the menus of Notepad++ ( my favourite free app to consult log files: it also has a compare plug-in to quickly locate differences )





