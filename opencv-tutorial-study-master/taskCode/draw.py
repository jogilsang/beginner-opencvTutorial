# source : opencv-python-tutroals
# modify : jogilsang

import cv2
import pyautogui
import os
import datetime
import numpy as np

os.chdir('C:\\Users\\user\\Desktop\\opencv')

# Create a black image
img = cv2.imread('picture.jpg',0)

width, height = img.shape[::-1] # 내 캐릭터의 width, height 값

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,511),(width,511),(255,0,0),5)
# 시작좌표, 끝좌표, 칼라, 두께

img = cv2.rectangle(img,(0,511),(width,height),(255,0,0),-1)
# 시작좌표, 끝좌표, 칼라, 두께
# 두께 -1 이면 꽉 채움

# img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
# 중심좌표, 반지름,컬러,두께

pts = np.array([[0,0],[20,30],[70,20],[width,height]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],False,(255,255,255))
# 배경, 좌표들, 닫힘여부, 컬러


font = cv2.FONT_HERSHEY_SIMPLEX
# 폰트 종류
cv2.putText(img,'Image and Video Handling Tool : OpenCV',(30,575), font, 1,(0,0,0),2,cv2.LINE_AA)
# 그림, 문구, 시작좌표, 폰트종류, 폰트크기, 색상, 사이즈, 선 유형



cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
