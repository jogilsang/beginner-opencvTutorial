# source : opencv-python-tutroals
# modify : jogilsang

import cv2
import pyautogui
import os
import datetime
import numpy as np

os.chdir('C:\\Users\\user\\Desktop\\opencv')
# C:\opencv-master\opencv-master\data\haarcascades
# lowerbody_cascade = cv2.CascadeClassifier('C:\\opencv-master\opencv-master\\data\\haarcascades\\haarcascade_lowerbody.xml')
lowerbody_cascade = cv2.CascadeClassifier('C:\\opencv-master\opencv-master\\data\\haarcascades\\haarcascade_smile.xml')

while(True) :
    img = cv2.imread('sul.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # bodys = lowerbody_cascade.detectMultiScale(gray, 1.1, 4)
    bodys = lowerbody_cascade.detectMultiScale(gray, 10, 6)
    # faces = face_cascade.detectMultiScale(gray, 1.3)
    # faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in bodys:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

    cv2.imshow('img',img)
    key = cv2.waitKey(1)
    if key == 27 :
        break

cv2.destroyAllWindows()
