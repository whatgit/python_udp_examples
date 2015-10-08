#!/usr/bin/python

########################################################
#
# Running this script will join the multicast_group
# then it listens to all udp packets sent to that group
# as well as packets sent directly at its own IP address
# 
# After receiving any message, it will send "ack" back
# to the sender
########################################################

import socket
import struct
import sys

port = 10000
multicast_group = "224.0.0.251"
server_address = ('',port)

#create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind to the server address
sock.bind(server_address)

#tell the operating system to add the socket to the multicast group on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack("4sL", group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

#receive/respond loop
while True:
        print >> sys.stderr, '\nwaiting to receive message'
        data, address = sock.recvfrom(1024)

        print >> sys.stderr, 'received %s bytes from %s' % (len(data), address)
        print >> sys.stderr, data

        print >> sys.stderr, 'sending acknowledgement to', address
        sock.sendto('ack', address)
