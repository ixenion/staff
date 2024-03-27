from scapy.all import *

# create IP packet with ttl = 64
x = IP(ttl=64)
# and send it by:
send(x)

# IP packet has source and destination
# so then define them
x.scr="192.168.1.1"
x.dst="192.168.1.2"
send(x)

# see all commands by "lsc()" into scapy prompt
#>>> lsc()


# confusing situation (sends 2000 packets)
# send 2000 to the router while pretending to e a router
# send(IP(src="192.168.1.1",dst="192.168.1.1")/TCP(sport=135,dport=135), count=2000)

# hide real self mac
# sendp(Ether(src="11:22:33:44:55:66")/IP(src="192.168.1.1",dst="192.168.1.1")/TCP(sport=135,dport=135), count=2000)



# to deauth: pretend to be the router which intended to kick other devise off
# to network scan: again pretend to be a router and send arp request & and listen replies in wireshark
