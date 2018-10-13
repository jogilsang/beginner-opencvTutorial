# source : opencv-python-tutroals
# modify : jogilsang

import cv2
import pyautogui
import os
import datetime
import numpy as np

# FourCC code is passed as cv2.VideoWriter_fourcc('M','J','P','G') or cv2.
# VideoWriter_fourcc(*'MJPG) for MJPG.

os.chdir('C:\\Users\\user\\Desktop\\opencv')

cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('realtime_cam.avi',fourcc, 20.0, (640,480))
while(cap.isOpened()) :

        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,0)
            # write the flipped frame
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break


cap.release()
# Release everything if job is finished
out.release()
cv2.destroyAllWindows()