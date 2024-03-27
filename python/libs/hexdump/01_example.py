import hexdump

packet = b'y\x00\x00\x00\x00\x00H\x1e\xbcs\x02\x01X\x03A\x00\x08\x00\x00\x00qcmap_nl_decode_nlmsg(): Delneigh on other iface\x00qcmap_netlink.cpp\x00\x9c\xbb'

decoded = hexdump.hexdump(packet)
print(decoded)
