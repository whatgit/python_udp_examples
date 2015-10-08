#!/usr/bin/python

################################################################
#Creates a UDP socket and send "hello" to destination_ip 
#then close the socket
################################################################

from socket import *

destination_ip = "192.168.30.29"
port = 10000

sock = socket(AF_INET, SOCK_DGRAM)
sock.sendto("hello", (destination_ip, port))
sock.close()
