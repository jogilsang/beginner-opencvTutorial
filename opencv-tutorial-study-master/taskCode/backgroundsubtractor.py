import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

os.chdir('C:\\Users\\user\\Desktop\\opencv')

# cap = cv2.VideoCapture('realtime_cam.avi')
cap = cv2.VideoCapture('torres.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2()
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
