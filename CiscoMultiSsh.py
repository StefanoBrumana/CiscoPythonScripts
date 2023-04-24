#python script version 0.3 January 2021 to ssh multiple Cisco devices  all
#with same username, password and ( optional enable password ) with unique credentials,
#enter commands and save the entire log into a .txt file
#whose name is made by IP address of target device + date/time
#tested in python 3.8.5 on windows 7 pro 64 bit + pip version 20.1.1
#ssh libraries: paramiko version 2.7.2, netmiko version 3.3.2
#import required python libraries to execute this script
import paramiko
import time
import getpass
import sys
import time
import os
from datetime import datetime

print ("###########################")
print ("Python ssh script for Cisco")
print ("#########FaAndàIMan########")
username=input("Enter Login: ")
password=getpass.getpass()
#ask if the target device has a privileged password to get privileged access
while ( answer:= input ("Has target device an enable password (Y/N)?").upper() ) not in {"Y", "N"}: pass
if answer == "Y":
 enable=input("Enter enable password: ")
 #open file ip.txt to retrieve addresses of target devices
 #this ip.txt file must be in same folder of this python script
iplist=open("ip.txt")

for line in iplist:
 #open file commands.txt to retrieve commands to be executed on target devices
 #this commands.txt file must be in same folder of this python script
 #commands.txt must begin with terminal pagination disable in order to collect
 #entire outputs of certain long show commands
 commands=open("commands.txt")
 Host=line.strip("\n")
 print ("Working on device",Host )
 ip = Host
 #ssh performed on default TCP port 22
 try: 
  SESSION = paramiko.SSHClient()
  SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  SESSION.connect(ip,port=22,
                 username=username,
                 password=password,
                 look_for_keys=False,
                 allow_agent=False)
  time.sleep(2)
  DEVICE_ACCESS = SESSION.invoke_shell()
  if answer == "Y":
   DEVICE_ACCESS.send("enable\n")
   DEVICE_ACCESS.send(enable + "\n")
   time.sleep(2)
  print ("Executing and logging these commands:")
  for line in commands:
   DEVICE_ACCESS.send(line + "\n")
   print (line)
   time.sleep(3)
   #each ssh command is executed every 3 seconds: increase it if some output is missing
  #ssh session MUST be closed properly with an exit command otherwise log files will not be 
  #created or the ssh session will not work reliably
  DEVICE_ACCESS.send("exit\n")
  #Max size of log file that can be recorded is 1 Mbyte: it can be increased up to 2 Mbytes
  output = DEVICE_ACCESS.recv(1024000)
  str_all = output.decode('ascii')
  timestr = datetime.now().strftime("%m%d%Y-%H%M%S")
  log_file = Host + "_" + timestr + ".txt"
  f = open (log_file,"w")
  f.write(str_all)
  confirmation = "Log closed on "
  f.writelines(confirmation)
  f.writelines(timestr)
  print ("End of operations on device",Host)
  print ("All logged into file ", Host, "_", timestr, ".txt", sep="" )
  print ("Wait conclusion of the entire process before opening any log file")
  #all operations are logged in a file with name: IP-address_Date-Time.txt
  #this file is created in the same folder of this script
  SESSION.close
  commands.close()

 except paramiko.AuthenticationException:
  timestr = datetime.now().strftime("%m%d%Y-%H%M%S")
  log_file = Host + "_ERROR_" + timestr + ".txt"
  with open(log_file, "a") as f:
   print("Ssh authentication failed: verify your credentials", file=f)
  time.sleep(2)
 except paramiko.SSHException as sshException:
  timestr = datetime.now().strftime("%m%d%Y-%H%M%S")
  log_file = Host + "_ERROR_" + timestr + ".txt"
  with open(log_file, "a") as f:
   print("Check if ssh is properly enabled on target device", file=f)
   print(sshException.args, file=f)
  time.sleep(2)
 except paramiko.BadHostKeyException as badHostKeyException:
  timestr = datetime.now().strftime("%m%d%Y-%H%M%S")
  log_file = Host + "_ERROR_" + timestr + ".txt"
  with open(log_file, "a") as f:
   print("Check if ssh key is properly set on target device", file=f)
   print (badHostKeyException.args, file=f)
  time.sleep(2)
 except Exception:
  timestr = datetime.now().strftime("%m%d%Y-%H%M%S")
  log_file = Host + "_ERROR_" + timestr + ".txt"
  with open(log_file, "a") as f:
   print("Unable to reach via ssh target device", file=f)
   print("Check if IP address", Host, "is connected", file=f)  
  time.sleep(2)

print ("##############################################")
print ("##################FaAndàIMan##################")
print ("##############################################")
print ("All operations logged into your present folder")
iplist.close()

#remove empty lines from log ( file with name: IP-address_Date-Time.txt )
#this file is created in the same folder of this script
filename = log_file
def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)

remove_empty_lines(filename)
f.close()