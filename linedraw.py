#!/usr/bin/python2

import cv2

data1=cv2.imread('linux.png')


newd=cv2.line(data1,(200,200),(600,600),(230,120,234),12)
#             img ,  startpoint , endpoint , color , width
cv2.imshow('newin',newd)
cv2.waitKey(0)
cv2.destroyAllWindows()
