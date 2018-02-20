#!/usr/bin/env python2


import sys,os

list_of_userdir=sys.argv[1:]
exits_dir=os.listdir('.')


for  i   in  list_of_userdir:
	if  i in exits_dir :
		print  i+": already exists "
	else :
                os.mkdir(i)
		print  i+": created !! "



