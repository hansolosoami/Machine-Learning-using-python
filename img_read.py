#!/usr/bin/python3

import cv2,time
img_data=cv2.imread('blu1.jpg',1)
img_data1=cv2.imread('blu1.jpg',0)
img_data2=cv2.imread('blu1.jpg',-1)
#  grayscale image 


cv2.imshow('adhoc window',img_data)
cv2.imshow('adhoc window1',img_data1)
cv2.imshow('adhoc window2',img_data2)
cv2.waitKey(0)
cv2.destroyAllWindows()
