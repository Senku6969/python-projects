import cv2
import numpy as np 

img=cv2.imread('assets/wp.jpg',-1)
img=cv2.resize(img,(0,0),fx=.5,fy=.5)

# rotating shiz 
# img=cv2.rotate(img, cv2.ROTATE_180) 

px = img[100,100]
print(px)
print(img.size)
print(img.shape)

cv2.imshow('wp', img)
cv2.waitKey(0)
cv2.destroyAllWindows()  