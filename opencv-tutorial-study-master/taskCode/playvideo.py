# source : opencv-python-tutroals
# modify : jogilsang

import cv2
import pyautogui
import os
import datetime
import numpy as np

os.chdir('C:\\Users\\user\\Desktop\\opencv')

cap = cv2.VideoCapture('torres.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
        # 25 가 default, 1 개빠름, 0 멈춤, empyty 멈춤

cap.release()
cv2.destroyAllWindows()