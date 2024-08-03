import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)

	
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    frame = cv2.flip(frame,1)
    cv2.setWindowTitle( 'video', 'WebCam' ) 

    # Convert the frame to grayscale for faster face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

	#creates a rectangle outside detected image (4=thickness)/green color
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow('Video', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == 32: #exits window on spacebar
        break

video_capture.release()
cv2.destroyAllWindows()


# frame = cv2.flip(frame,0)
# In cv2.flip() argument try using 0 if you want to flip in y axis, 1 if you want to flip in x axis and -1 if want to flip in both axes.