# stealth port scanner
# threeway hdsh concept based

# origin
# 1111111111111
# client ->syn+port-> server
# 2222222222222
# client <-syn+ack<-  server
# 3333333333333
# client ->ack->      server

# using modified:
# 1111111111111
# client ->syn+port-> server
# 2222222222222
# client <-syn+ack<-  server
# 3333333333333
# client ->rst->      server

from logging import getLogger, ERROR        #1
getLogger("scapy.runtime").setLevel(ERROR)  #2
from scapy.all import *                     #3
import sys                                  #4
from datetime import datetime               #5
from time import strftime                   #6

#1
# import from logging
#2
# this will remove the
# "No Route Found for IPv6 Destination" error
# when importing scapy

# getting user input
try:
    target = raw_input("[*] Enter Target IP Address: ")
    min_port = raw_input("[*] Enter Minimum Port Number: ")
    max_port = raw_input("[*] Enter Maximum Port Number: ")
    try:
        if int(min_port) >= 0 and int(max_port) >= 0:
            pass
        else:
            print("\n[!] Invalid Range of Ports")
            print("[!] Exiting...")
            sys.exit(1)
    except Exception:
        print("\n[!] Invalid Range of Ports")
        print("[!] Exiting...")
        sys.exit(1)
except KeyboardInterrupt:
    print("\n[!] Shutdown Requested...")
    print("[!] Exiting...")
    sys.exit(1)

# setting values
ports = range(int(min_port),int(max_port)+1)
start_clock = datetime.now()
SYNACK = 0x12
RSTACK = 0x14

# check the target is up
# create the IP packet and if there is no error
# target is up
def checkhost(ip):
    conf.verb = 0
    try:
        ping = sr1(IP(dst = ip)/ICMP())
        print("\n[*] Target is Up, Beginning Scan...")
        pass
    except Exception:
        print("\n[!] Couldn't Resolve Target")
        print("[!] Exiting...")
        sys.exit(1)
        pass
    pass


# scanning a given port
# conf.verb=0 prevents sended packets from being printe on the screen
def scanport(port):
    srcport = RandShort()
    conf.verb = 0
    SYNACKpkt = sr1(IP(dst = target)/TCP(sport = srcport, dport = port, flags = "S"))
    pktflags = SYNACKpkt.getlayer(TCP).flags
    if pktflags == SYNACK:
        return True
    else:
        return False
    RSTpkt = IP(dst = target)/TCP(sport = srcport, dport = port, flag = "R")
    send(RSTpkt)
