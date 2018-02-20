#!usr/bin/env python

import cv2

data=cv2.imread('index.jpg')

#print data.shape
#print data.size

cv2.imshow('windowssss',data)
#cv2.waitkey(0)
cv2.destroyAllWindows()


