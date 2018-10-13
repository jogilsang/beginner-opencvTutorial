# source : opencv-python-tutroals
# modify : jogilsang

import cv2
import pyautogui
import os
import datetime
import numpy as np

os.chdir('C:\\Users\\user\\Desktop\\opencv')

CAM = 0
FILE ='Halloween-12720.mp4'
# FILE ='Snatch-12844-tacofleur.mp4'
# FILE ='Kettlebell Flip-12842-tacofleur.mp4'

cap = cv2.VideoCapture(FILE)
# 0 => 현재카메라
# -1 => 아무것도안뜸
# 1 -> 두번쨰카메라

if cap.isOpened() == False: #카메라 생성 확인
    print('Can\'t open the CAM')
    exit()

face_cascade = cv2.CascadeClassifier('C:\\opencv-master\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\opencv-master\opencv-master\\data\\haarcascades\\haarcascade_eye.xml')



while(True):
# Capture frame-by-frame
    ret, frame = cap.read()
# returns a bool (True/False). If frame is read correctly, it will be True.
# Our operations on the frame come here
# Display the resulting frame

    # ret = cap.set(3,365)
    # ret = cap.set(4,365)

    frameValueX = str(cap.get(3))
    frameValueY = str(cap.get(4))
    frameValueTotal = frameValueX + " X " + frameValueY
    # default 640 x 480

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # faces = face_cascade.detectMultiScale(gray, 1.3, 2,0,(30,30))

    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # cv2.imshow('frame',gray)
    cv2.imshow(frameValueTotal,frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('videocapture_gray.png', gray)
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
