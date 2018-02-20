#!/usr/bin/python2

import time
import  thread
def  ok():
	while True:
		print  "let me start...plz.."
		time.sleep(1)

def  nook():
	while True:
		print  "first priority first.."
		time.sleep(2)


thread.start_new_thread(ok,())
thread.start_new_thread(nook,())

while True:
	pass

