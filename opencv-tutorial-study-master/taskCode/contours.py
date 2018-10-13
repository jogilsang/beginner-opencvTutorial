import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir('C:\\Users\\user\\Desktop\\opencv')

title = "contours"

img = cv2.imread('canny.jpg')

imgray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.CHAIN_APPROX_NONE : 외곽 점 일일이 다찍음


# draw contours
cnt = contours[4]
image = cv2.drawContours(image, [cnt], 0, (0,255,0), 3)


# cv2.namedWindow(title, cv2.WINDOW_NORMAL)
# 크기 조절 가능
cv2.imshow(title,image)
# 이미지창 타이틀바
cv2.waitKey(0)
# 몇초뒤에 사라지는지, 단위 밀리세컨드
cv2.destroyAllWindows()
# cv2.destroyWindow() 무슨차이인지 모르겠다