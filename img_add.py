#!/usr/bin/python2

import cv2

data1=cv2.imread('linux.png')
data2=cv2.imread('hai.png')

newd=cv2.add(data2,data1)

cv2.imshow('newin',newd)
cv2.waitKey(0)
cv2.destroyAllWindows()
