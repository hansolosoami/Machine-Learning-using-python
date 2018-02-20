#!/usr/bin/python2


import cv2
import  commands,os

img_list=os.listdir('/root/Desktop/dogs')

img=[]
for  i in img_list:
	img.append(cv2.imread('/root/Desktop/dogs/'+i,0))



for  j  in  img:
	f=open('/root/Desktop/imgdogs.txt','w')
	f.write(j)
	f.close()



	

