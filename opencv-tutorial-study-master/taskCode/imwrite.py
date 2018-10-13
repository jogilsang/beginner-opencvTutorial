# source : opencv-python-tutroals
# modify : jogilsang

import cv2
import pyautogui
import os
import datetime
import numpy as np

os.chdir('C:\\Users\\user\\Desktop\\opencv')

img = cv2.imread('picture.jpg',0)
# 이미지 불러오기 ( 1,0,-1)
# cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

title = "imshow"

cv2.namedWindow(title, cv2.WINDOW_NORMAL)
# 크기 조절 가능
cv2.imshow(title,img)
# 이미지창 타이틀바

k = cv2.waitKey(0)
# 몇초뒤에 사라지는지, 단위 밀리세컨드
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('picture_gray.png',img)
    cv2.destroyAllWindows()
