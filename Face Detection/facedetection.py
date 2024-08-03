import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('assets/lol2.jpg')
img=cv2.resize(img,(0,0),fx=.8,fy=.8)

#change to gray (for faster opencv detection) 
grey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5, minSize = (30,30))
#scale - reduces image size by10%, 

for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
#creates a rectangle outside detected image (4=thickness)/green color

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#back to color
 
cv2.imshow('LOL', img)
cv2.waitKey(0)
cv2.destroyAllWindows()  

# The detectMultiScale function is a general function that detects objects. Since we’re calling it on the face cascade, that’s what it detects.
# Everything else is commented.