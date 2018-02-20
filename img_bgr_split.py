#!/usr/bin/python2


import  cv2
img=cv2.imread('blu1.jpg')

#  spliting img into all 3  colors

b,g,r=cv2.split(img)

print b 
print g
print r

cv2.imshow('blue window',b) 
cv2.imshow('green window',g) 
cv2.imshow('Red window',r) 
cv2.waitKey(0)
cv2.destroyAllWindows()


