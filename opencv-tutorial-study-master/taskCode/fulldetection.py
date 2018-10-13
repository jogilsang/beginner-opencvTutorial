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
fullbody_cascade = cv2.CascadeClassifier('C:\\opencv-master\opencv-master\\data\\haarcascades\\haarcascade_fullbody.xml')

img = cv2.imread('sul.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
bodys = fullbody_cascade.detectMultiScale(gray, 5000, 5000)
# faces = face_cascade.detectMultiScale(gray, 1.3)
# faces = face_cascade.detectMultiScale(gray)
for (tx,ty,tw,th) in bodys:
    img = cv2.rectangle(img,(tx,ty),(tx+tw,ty+th),(0,0,255),2)
    troi_gray = gray[ty:ty+th, tx:tx+tw]
    troi_color = img[ty:ty+th, tx:tx+tw]



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
