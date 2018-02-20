#!/usr/bin/env python2


import sys,os

list_of_userdir=sys.argv[1:]
exits_dir=os.listdir('.')


for  i   in  list_of_userdir:
	if  i in exits_dir :
		os.rmdir(i)
		print  i+": removed "
	else :
		print  i+": does not exist "





