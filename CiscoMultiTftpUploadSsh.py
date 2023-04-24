#python script version 0.3 January 2021 to access via ssh
#and export via tftp the startup-config from a list of Cisco
#devices all with same username, password and optional enable password
#enter commands and send their startup-config to the root folder of a TFTP server
#tested in python 3.8.5 on windows 7 pro 64 bit with 3cDaemon TFTP server
#pip version 20.1.1
#ssh libraries: paramiko version 2.7.2, netmiko version 3.3.2
#import required python libraries to execute this script
import paramiko
import time
import getpass
import sys
import time
import re 
from datetime import datetime

#user is prompted to insert unique username and password of all the target devices
print ("#############################################################")
print ("Python script to export startup-config via TFTP from Cisco")
print ("##########FaAndàIMan#########################################")
username=input("Enter Login: ")
password=getpass.getpass()
#ask if the target device has a privileged password to get privileged access
while ( answer:= input ("Has target device an enable password (Y/N)?").upper() ) not in {"Y", "N"}: pass
if answer == "Y":
 enable=input("Enter enable password: ")
#enter the ip address of the tftp server where startup-configs will be exported
tftp_server= input ("Type IP address of TFTP server: ")

#check that ip address of the tftp_server is properly typed by the end user
#in case of error the script will be immediately terminated
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
  25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
  25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
  25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
       
def check(tftp_server):
 if(re.search(regex, tftp_server)):  
  print("###############################################################")
  print("You entered a valid IP address")
  print("TFTP server MUST be running on such host")
  print("Its firewall or anti-virus should not discard any incoming file") 
  print("###############################################################")
 else:  
  print("###################################################################")
  print("ERROR: you entered an invalid IP address: script will be terminated") 
  print("Re-launch the script and type a correct IP address")  
  print("###################################################################")
  time.sleep(5)
  quit()
check(tftp_server)

print ("All operations logged into tftp-log.txt of your present folder")
time.sleep(2)
#all activities on screen will be saved into tftp-log.txt file created in
#the same folder of this script: any previous copy of tftp-log will be overwritten
stdout_fileno = sys.stdout
sys.stdout = open("tftp-log.txt","w")

#open file ip.txt to retrieve addresses of target devices
#this ip.txt file must be in same folder of this python script
iplist=open("ip.txt")

for line in iplist:
 Host=line.strip("\n")
 sys.stdout.write ("Working on device " + Host + "\n" )
 stdout_fileno.write ("Working on device " + Host + "\n" )
 ip = Host
 #ssh performed on default TCP port 22
 try:  
  client = paramiko.SSHClient()  
  # create an SSH client
  # Set the policy to auto-connect to hosts not in known-hosts file
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
  time.sleep(2)
  channel = client.invoke_shell()
  time.sleep(1)    
  if answer == "Y":
   channel.send("enable\n")
   channel.send(enable + "\n")
   time.sleep(2)
  #activities will be displayed both on screen and saved into tftp-log.txt file
  #created in the same folder of this script
  sys.stdout.write ("Exporting the startup-config..." + "\n")
  stdout_fileno.write ("Exporting the startup-config..." + "\n")
  #startup-config exported from the target device will be saved into the root
  #folder of the tftp server with an unique name startup-config_IPaddress_date/time
  #IP adddress is from the target device
  timestr = datetime.now().strftime("%m%d%Y-%H%M%S")
  channel.send("copy startup-config tftp:\n")
  channel.send(tftp_server + "\n")
  config_file = "startup-config_" + Host + "_" + timestr
  channel.send(config_file + "\n")
  time.sleep(5)  
  #ssh session MUST be closed properly with an exit command otherwise log files will not be 
  #created or the ssh session will not work reliably
  channel.send("exit\n")  
  sys.stdout.write ("End of operations on device " + Host + "\n")
  stdout_fileno.write ("End of operations on device " + Host + "\n")
  sys.stdout.write ("File is in root folder of TFTP server " + tftp_server + "\n") 
  stdout_fileno.write ("File is in root folder of TFTP server " + tftp_server + "\n")
  sys.stdout.write ("It is called startup-config_" + Host + "_" + timestr + "\n")
  stdout_fileno.write ("It is called startup-config_" + Host + "_" + timestr + "\n")
  client.close()
  #SESSION.close
 
 except paramiko.AuthenticationException:
  sys.stdout.write ("Ssh authentication failed: verify your credentials" + "\n")
  stdout_fileno.write ("Ssh authentication failed: verify your credentials" + "\n")
  time.sleep(2)
 except paramiko.SSHException as sshException:
  sys.stdout.write (str(sshException) + "\n")
  stdout_fileno.write (str(sshException) + "\n")  
  sys.stdout.write ("Check if ssh is properly enabled on target device\n")
  stdout_fileno.write ("Check if ssh is properly enabled on target device\n")
  time.sleep(2)
 except paramiko.BadHostKeyException as badHostKeyException:
  sys.stdout.write (str(badHostKeyException) + "\n")
  stdout_fileno.write (str(badHostKeyException) + "\n")  
  sys.stdout.write ("Check if ssh key is properly set on target device\n")
  stdout_fileno.write ("Check if ssh key is properly set on target device\n")
  time.sleep(2)
 except Exception:
  sys.stdout.write ("Unable to reach via ssh target device " + Host + "\n")
  stdout_fileno.write ("Unable to reach via ssh target device " + Host + "\n")
  sys.stdout.write ("Check if IP address " + Host + " is connected" + "\n")
  stdout_fileno.write ("Check if IP address " + Host + " is connected" + "\n")
  time.sleep(2)

iplist.close()

sys.stdout.write ("############# end of python script #############\n")
stdout_fileno.write ("############# end of python script #############\n")
sys.stdout.write ("All operations logged into tftp-log.txt of your present folder\n")
stdout_fileno.write ("All operations logged into tftp-log.txt of your present folder\n")
sys.stdout.write ("Log closed on " + timestr + "\n")
stdout_fileno.write ("Log closed on " + timestr + "\n")


sys.stdout.close()
sys.stdout = stdout_fileno
