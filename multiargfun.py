#!/usr/bin/python

import  os
import sys
t=sys.argv[1:]
y=tuple(t)
def  install(*x):
	for  i  in x:
		os.system('yum  install -y  '+i)



def  add(*x):
	sum=0	
	for  i in x:
		sum=sum+i


	print  sum

install(y)
