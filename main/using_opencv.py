import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('/home/aristocrat/face-reg/opencv-2.4.11/data/haarcascades/haarcascade_frontalface_default.xml')
cascPath = '/home/aristocrat/face-reg/opencv-2.4.11/data/haarcascades/haarcascade_frontalface_default.xml'


eye_cascade = cv2.CascadeClassifier('/home/aristocrat/face-reg/opencv-2.4.11/data/haarcascades/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('/home/aristocrat/face-reg/opencv-2.4.11/data/haarcascades/haarcascade_smile.xml')
img = cv2.imread('/home/aristocrat/IdeaProjects/Image_Processing_in_Python/images/download.jpg',1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cascPath)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)


#faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
     roi_gray = gray[y:y+h, x:x+w]
     roi_color = img[y:y+h, x:x+w]
     eyes = eye_cascade.detectMultiScale(roi_gray)
     mouth = mouth_cascade.detectMultiScale(roi_gray)
     for (ex,ey,ew,eh) in eyes:
         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
         print "Face  : ", ex, ey, ew, eh
     for (ex,ey,ew,eh) in mouth:
         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
         print "Mouth  : ", ex, ey, ew, eh

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()