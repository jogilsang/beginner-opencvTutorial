# source : opencv-python-tutroals
# modify : jogilsang



import cv2
import pyautogui
import os
import datetime
import numpy as np

os.chdir('C:\\Users\\user\\Desktop\\opencv')

img = cv2.imread('picture.jpg',1)
# 이미지 불러오기 ( 1,0,-1)
# cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

title = "imshow"

# b,g,r = cv2.split(img)
# img[:,:,-3] = 255
# img = cv2.merge((b,g,r))

ball = img[0:113, 349:459]
img[100:213, 449:559] = ball

print(img[100,100])

cv2.namedWindow(title, cv2.WINDOW_NORMAL)
# 크기 조절 가능
cv2.imshow(title,img)
# 이미지창 타이틀바
cv2.waitKey(0)
# 몇초뒤에 사라지는지, 단위 밀리세컨드
cv2.destroyAllWindows()
# cv2.destroyWindow() 무슨차이인지 모르겠다
