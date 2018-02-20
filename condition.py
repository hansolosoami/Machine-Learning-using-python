#!/usr/bin/python

import  commands
import  webbrowser

# webbrowesr library will open defalut browser of OS
# print  normal message   

print "Okey Python getting started with COnditional "
print  "                                         "
print  "                                         "
print  "                                         "
'''

print "Okey Python getting started with COnditional "

print "Okey Python getting started with COnditional "


'''
#  taking input from user 
#  raw_input always give you string type data
"""
user_input=raw_input("plz enter your name :   ")

print  "welcome to Python INput Method  "+user_input

print  "type of data you entered is  ",type(user_input)
"""

x=raw_input("type any number :  ")

if  int(x)  > 20 and int(x) < 30  :

	print  commands.getoutput('date')

elif  int(x)  > 30 :

	print  commands.getoutput('gnome-terminal')
	
else  :

	print  "Plz wait YouTube is about to Open...."
	
	webbrowser.open_new_tab('https://www.youtube.com')
        






