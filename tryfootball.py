#!/usr/bin/python3

#import of modules for the program
import cv2
import os
import numpy as np
#storing images in a list of images
img_list=os.listdir('/root/Desktop/a/football_players')
print(img_list)

#storing first image in the numpy array x
x=cv2.imread('/root/Desktop/a/football_players/8.jpg',0)

#loop to store all the images in numpy array x
for i in img_list:
	#skiping first image as it is stored earlier
	if i=='8.jpg':
		continue
	#loading the lest over images in the numpy array
	else:
		print(i)
		y=cv2.imread('/root/Desktop/a/football_players/'+i,0)
		print(y)
		#appending the other images data in numpy array x
		z=np.concatenate((x,y))
		x=z

#storing the numpy array data of images in text file using savetxt method
np.savetxt("tryfootball.txt",x)
print("The numpy array data:\n")
print(x)
print("The shape of the numpy array data:",x.shape)
#reading numpy array data from a text file using loadtxt method
k = np.loadtxt("tryfootball.txt")

#decompressing of text file into images
length=len(img_list)

#loop to store images
for i in range(1,length+1):
	imgdata=k[400*(i-1):400*i,0:400]
	cv2.imwrite("output/"+str(i)+".jpg",imgdata)

