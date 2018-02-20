#!/usr/bin/env python2

import  sys

y=sys.argv[1]
def  ok():

	print  "i am the one !!"
	print   "#################"
	print   "#################"
	print   "#################"
	print    "ok google"


def   motd(x):

	print  "great day here with Windows ",x

def  dont():
	print  "out of planet !!"


if  sys.platform  ==  'linux2' or   sys.platform == 'POSIX' :
	ok()

elif  sys.platform ==  'win32'  :
	motd(y)
else :
	dont() 



