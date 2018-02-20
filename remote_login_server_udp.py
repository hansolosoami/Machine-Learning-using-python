#!/usr/bin/python

import  socket
import  time
import  commands
import  os
import  sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",1111))

user=s.recvfrom(10)[0]
password=s.recvfrom(10)

if  user == 'root' and  password[0] == 'redhat' :
	while True:
		s.sendto("ok",password[1])
		data=s.recvfrom(50)
		if  data[0]  == 'quit' or data[0] == 'exit' :
			s.sendto("closing server ..",data[1])
			s.close()
		else :
			result=commands.getoutput(data[0])
			s.sendto(result,data[1])

else :

	s.sendto("notallowed",password[1])



