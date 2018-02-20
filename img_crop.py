#!/usr/bin/python2

import cv2

data=cv2.imread('blu1.jpg')

print data.size
print data.shape
print '------------SEE THIS---------------'

x1=input('the starting of the row you want to crop!!!!')
x2=input('the endinig of the row you want to crop!!!!')
y1=input('the starting of the column you want to crop!!!!')
y2=input('the ending of the column you want to crop!!!!')

image=data[x1:x2 , y1:y2]

cv2.imshow('windowwssss',image)
cv2.waitKey(0)

cv2.destroyAllWindows()





