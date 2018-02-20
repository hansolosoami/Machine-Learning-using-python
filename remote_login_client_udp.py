#!/usr/bin/python

import  socket
import  time
import  commands
import  os
import  sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip=sys.argv[1]
s_port=sys.argv[2]

user=raw_input("enter user name : ")
password=raw_input("enter password  : ")

s.sendto(user,(s_ip,int(s_port)))
s.sendto(password,(s_ip,int(s_port)))
response=s.recvfrom(10)[0]

if  response  ==  'notallowed' :
	print  "wrong user or password plz try again.."
	s.close()

elif  s.recvfrom(2)[0] == 'ok' :

	cmd=raw_input("enter your command :  ")
	s.sendto(cmd,(s_ip,int(s_port)))
	print  s.recvfrom(100000)[0]

else :
	print  "something went wrong plz contact to system admin"





