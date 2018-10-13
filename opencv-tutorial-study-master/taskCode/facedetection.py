# source : opencv-python-tutroals
# modify : jogilsang

import cv2
import pyautogui
import os
import datetime
import numpy as np

os.chdir('C:\\Users\\user\\Desktop\\opencv')
# C:\opencv-master\opencv-master\data\haarcascades
face_cascade = cv2.CascadeClassifier('C:\\opencv-master\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\opencv-master\opencv-master\\data\\haarcascades\\haarcascade_eye.xml')
# fullbody_cascade = cv2.CascadeClassifier('C:\\opencv-master\opencv-master\\data\\haarcascades\\haarcascade_smile.xml')

img = cv2.imread('sul.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# bodys = fullbody_cascade.detectMultiScale(gray, 1.3, 5)
# faces = face_cascade.detectMultiScale(gray, 1.3)
# faces = face_cascade.detectMultiScale(gray)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
