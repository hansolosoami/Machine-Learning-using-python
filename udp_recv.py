#!/usr/bin/env python2

import  socket
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#                    ip_type(ipv4) ,  proto_type (UDP)

x.bind(("",9999))
#  default ip is binded with port 9999 

while True:

	data=x.recvfrom(1000)
	print  "data receive from  CLIENT is   ",data[0]
	print  "CLIENT IP ADDRESS  ",data[1][0]
	print  "####################################"
	print  "#                                  #"
	print  "#                                  #"
	print  "####################################"
	reply=raw_input("type your reply :   ")
	x.sendto(reply,data[1])




x.close()



