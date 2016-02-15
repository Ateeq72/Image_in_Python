import cv2
import subprocess as sb
import os

from twisted.mail.imap4 import modified_unbase64

os.system('pwd')

#sb.call(["convert","koala_ears.png","-virtual-pixel Black"," -distort Shepards", "'30,11 20,11  48,29 58,29'","koala_ear_pull.png"])

#os.system("convert koala_ears.png -virtual-pixel Black -distort Shepards '30,11 20,11  48,29 58,29'  koala_ear_pull.png ")

face_cascade = cv2.CascadeClassifier('/home/aristocrat/face-reg/opencv-2.4.11/data/haarcascades/haarcascade_frontalface_alt2.xml')
cascPath = '/home/aristocrat/face-reg/opencv-2.4.11/data/haarcascades/haarcascade_frontalface_default.xml'


eye_cascade = cv2.CascadeClassifier('/home/aristocrat/face-reg/opencv-2.4.11/data/haarcascades/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('/home/aristocrat/face-reg/opencv-2.4.11/data/haarcascades/haarcascade_smile.xml')


infile = '/home/aristocrat/IdeaProjects/Image_Processing_in_Python/images/download.jpg'
outfile = '/home/aristocrat/IdeaProjects/Image_Processing_in_Python/images/out.jpg'
img = cv2.imread(infile,1)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.equalizeHist(gray)

faceCascade = cv2.CascadeClassifier(cascPath)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.5,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)


#faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]

    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray )
    mouth = mouth_cascade.detectMultiScale(roi_gray )
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        print "Face  : ", ex, ey, ew, eh
        eyespoint = (ex,ey,ex+ew,ey+eh)
        eyesnew = (ex+5,ey+5,ex+ew+5,ey+eh+5)
        print eyesnew
       # os.system("convert %s -virtual-pixel Black -distort Shepards '%s %s' %s " % ( infile,eyespoint,eyesnew,outfile))
    for (ex,ey,ew,eh) in mouth:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        print "Mouth  : ", ex, ey, ew, eh
        mouthmidx = (ex + ew/2)
        mouthmidy = (ey+eh/2)
        print mouthmidx,mouthmidy
        msmix = mouthmidx+18
        msmiy = mouthmidy+18
        print eyespoint
        eyesnew = (ex,ey)
        print eyesnew
        os.system("convert  %s  -distort Shepards '%s,%s  %s,%s'   %s " % ( infile,mouthmidx,mouthmidy,msmix,msmiy,outfile))


imge = cv2.imread(outfile,1)
cv2.imshow('Old',img)
cv2.imshow('New',imge)
cv2.waitKey(0)
cv2.destroyAllWindows()
