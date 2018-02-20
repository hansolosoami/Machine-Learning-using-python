#!/usr/bin/Python

import cv2

img=cv2.imread('football.jpg')
img1= img[0:600, 200:]

cv2.imshow("original image ",img1)

img2=img1[344:406,414:482]
#cv2.imshow("ball image ",img2)

height,width,channel=img2.shape

#print height
#print width

for i in range(0,height):
         for j in range(0,width):
             
             img1[264+i,373+j]=img2[i,j]


cv2.imshow("updated image ",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''x1=404
y1=344

x2 =482
y2=406


394 213'''
