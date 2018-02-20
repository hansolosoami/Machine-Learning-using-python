#!/usr/bin/python3
import cv2

#image read of messi
img_read=cv2.imread('b.jpg')

#dimensions of the image
print(img_read.shape)

#fitting cropped part into new one
new_image=cv2.imread('b.jpg')

for i in range(200,500):
	for j in range(350,650):
			new_image[i][j+300]=img_read[i][j]


#writing the image
cv2.imwrite('new_b.jpg',new_image)

#cv2.imshow('roi window',new_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

