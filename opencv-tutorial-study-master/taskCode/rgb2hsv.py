import numpy as np
import cv2
import os

os.chdir('C:\\Users\\user\\Desktop\\opencv')

title = "rgb2hsv"

# lx,ly = -1,-1

wantedColor = np.uint8([[[111,53,31]]])
hsv_green = cv2.cvtColor(wantedColor,cv2.COLOR_BGR2HSV)

print(hsv_green)