#!/usr/bin/python

########################################################################################
#
# Running this script will send a "very important message" to the multicast_group
# After that, it will wait for any response it might get for 0.2s
# Then it will close the socket
#
########################################################################################

import socket
import struct
import sys

port = 10000
message = "very important message"
multicast_group = ("224.0.0.251", port)

#create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#set a time out
sock.settimeout(0.2)

#set time-to-live
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
	#send data to the multicast group
	print >> sys.stderr, 'sending "%s"' %  message
	sent = sock.sendto(message, multicast_group)
	
	#Look for response from all recipeints
	while True:
		print >> sys.stderr, 'waiting to receive'
		try:
			data, server = sock.recvfrom(16)
		except socket.timeout:
			print >> sys.stderr, 'timed out, no more responses'
			break
		else:
			print >> sys.stderr, 'receive "%s" from %s' % (data, server)
finally:
	print >> sys.stderr, 'closing socket'
	sock.close()
		
