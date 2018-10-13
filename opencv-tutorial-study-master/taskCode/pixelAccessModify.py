# source : opencv-python-tutroals
# modify : jogilsang

import cv2
import pyautogui
import os
import datetime
import numpy as np

os.chdir('C:\\Users\\user\\Desktop\\opencv')

# Create a black image
img = np.zeros((512,512,3), np.uint8)

px = img[100,100]
print(px)

# white square
img[100,100] = [255,255,255]
print(img[100,100])
img[100,200] = [255,255,255]
print(img[100,100])
img[150,150] = [255,255,255]
print(img[100,100])
img[200,100] = [255,255,255]
print(img[100,100])
img[200,200] = [255,255,255]
print(img[100,100])

font = cv2.FONT_HERSHEY_SIMPLEX


cv2.putText(img,'size : '+str(img.size) ,(100,250), font, 1,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img,'shape : '+str(img.shape),(100,350), font, 1,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img,'dtype : '+str(img.dtype),(100,450), font, 1,(255,255,255),2,cv2.LINE_AA)
# shape의 행,열,채널수 다곱하면 size(총 픽셀)
# 그림, 문구, 시작좌표, 폰트종류, 폰트크기, 색상, 사이즈, 선 유형

# img.itemset((10,10,2),100)
# img.item(10,10,2)

img2 = cv2.imread('picture.jpg',1)





# 폰트 종류
cv2.putText(img2,'size : '+str(img2.size) ,(30,575), font, 1,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img2,'shape : '+str(img2.shape),(30,475), font, 1,(255,255,255),2,cv2.LINE_AA)
# 행,열,채널수 다곱하면 size(총 픽셀)
cv2.putText(img2,'dtype : '+str(img2.dtype),(30,375), font, 1,(255,255,255),2,cv2.LINE_AA)
# 그림, 문구, 시작좌표, 폰트종류, 폰트크기, 색상, 사이즈, 선 유형


# 100,100 좌표의 픽셀값
# Draw a diagonal blue line with thickness of 5 px

cv2.imshow('image', img)
cv2.imshow('image2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
