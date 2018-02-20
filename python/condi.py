import  time
import  webbrowser
import  os
print  "Welcome to python & we are starting with IF & ELSE "

x='''
Press  1  to   check current date and time :  
Press  2  to  open firefox :
Press  3  to reboot system : 
'''

print x

ch=raw_input()


if  ch  ==  '1'  :
	
	print time.ctime()
	

elif  ch  ==  '2'  :

	print  webbrowser.open_new_tab('http://www.google.com')

else :
	

	print  os.system('reboot')

	


