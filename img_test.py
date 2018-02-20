#!/usr/bin/Python

import cv2

img=cv2.imread('OpenCV.jpg')
height,width,channel=img.shape

print "Choices :"
print "Press 1 for Centre of image"
print "Press 2 for contrast of image"
print "Press 3 for image crop"
i=raw_input("Enter you choice : ")


if i == 1 :

     print "height = ",height
     print "width = ",width
     centre = [height/2,width/2]
     print "Centre = ",centre

if i == 2 :
#change pixel value
     for i in range(200,height):
         for j in range(400,width):
             a,b,c=img[i,j]
             img[i,j]=[a+50,b+50,c+50]

if i==3 :
#image crop
     x1=200
     y1=300
     x2=500
     y2=600
     img1=img[x1:x2 , y1:y2]
     cv2.imshow('Cropped Image',img1)

cv2.imshow('image window1',img)
cv2.waitKey(0)
