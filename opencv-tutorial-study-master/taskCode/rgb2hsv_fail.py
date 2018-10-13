import numpy as np
import cv2
import os

os.chdir('C:\\Users\\user\\Desktop\\opencv')

title = "rgb2hsv"

img = cv2.imread('blend.jpg',1)
# lx,ly = -1,-1

def draw_circle(event, x, y, flags, param):
    global lx,ly
    if event == cv2.EVENT_FLAG_LBUTTON:

        b,g,r = img[x,y]
        print('RGB : '+ str(img[x,y]))
        wantedColor = np.uint8([[[b, g, r]]])  # 원하는색깔
        hsv_conversion = cv2.cvtColor(wantedColor, cv2.COLOR_BGR2HSV)
        print('HSV Cpnversion : ' + str(hsv_conversion))




cv2.namedWindow(title, cv2.WINDOW_NORMAL)
# 크기 조절 가능
# 이미지창 타이틀바
cv2.waitKey(0)
# 몇초뒤에 사라지는지, 단위 밀리세컨드

while(1):
    cv2.imshow(title,img)
    k = cv2.waitKey(1) & 0xFF
    cv2.setMouseCallback(title, draw_circle)
    if k == 27:
        break

cv2.destroyAllWindows()
# cv2.destroyWindow() 무슨차이인지 모르겠다


# [출처] HSV와 RGB 색상에 대한 이해(python opencv hsv range)|작성자 바고