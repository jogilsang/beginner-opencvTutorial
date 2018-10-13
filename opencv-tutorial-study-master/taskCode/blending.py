import cv2
import pyautogui
import os
import datetime
import numpy as np

os.chdir('C:\\Users\\user\\Desktop\\opencv')

img1 = cv2.imread('picture.jpg')
img2 = cv2.imread('blend.jpg')
# 사이즈 똑같아야함

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
# dst=α⋅img1+β⋅img2+γ
# 알파는 0~1 사이

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()