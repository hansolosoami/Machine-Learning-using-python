#!/usr/bin/python3


import cv2
import os
import numpy as np

img_list=os.listdir('/home/kimosabe/imgdata')

x=cv2.imread('/home/kimosabe/imgdata/1.jpg',0)
print(x)

for i in img_list:
	if i=='1.jpg':
		continue
	else:
		print(i)
		y=cv2.imread('/home/kimosabe/imgdata/'+i,0)
		print(y)
		z=np.append(x,y,axis=0)

np.savetxt("trymore.txt", z)
print(z)
print(z.shape)




k = np.loadtxt("trymore.txt")
#cv2.imwrite("trymore","i",".jpg",k)
#print(k.shape)
#print(k[0])
cv2.imwrite('try1.jpg',k)


