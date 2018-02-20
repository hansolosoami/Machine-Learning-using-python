#!/usr/bin/env python2

import  sys
def  ok():

	print  "i am the one !!"
	print   "#################"
	print   "#################"
	print   "#################"
	print    "ok google"


def   motd():

	print  "great day here"

def  dont():
	print  "out of planet !!"


if  sys.platform  ==  'linux2' or   sys.platform == 'POSIX' :
	ok()

elif  sys.platform ==  'win32'  :
	motd()
else :
	dont() 



