import time
import sys
import telnetlib
#Other is same as VBS example. 
HOST = "192.168.1.78" #Emulator IP

tn = telnetlib.Telnet(HOST)

print tn.read_eager()
tn.write("admin\r\n") #the user name is admin
time.sleep(2)    
tn.write("\r\n") #there is no password - just return - now logged in
print tn.read_eager()
time.sleep(2)    
tn.write("\r\n")
print tn.read_very_lazy()
tn.write("\r\n")
tn.write("GI\r\n")          #hey camera tell me more about you
print tn.read_very_lazy() #read output
sess_op = tn.read_all()
print sess_op
tn.close()
