import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir('C:\\Users\\user\\Desktop\\opencv')

# hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]
# • points are the contours we pass into.
# • hull is the output, normally we avoid it.
# • clockwise : Orientation flag. If it is True, the output convex hull is oriented clockwise. Otherwise, it is oriented
# counter-clockwise.
# • returnPoints : By default, True. Then it returns the coordinates of the hull points. If False, it returns the
# indices of contour points corresponding to the hull points.

title = "contours"

img = cv2.imread('bird.jpg')

imgray = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[4]
# x,y,w,h = cv2.boundingRect(cnt)
# img = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(image,[box],0,(0,0,255),2)

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)


# cv2.namedWindow(title, cv2.WINDOW_NORMAL)
# 크기 조절 가능
# cv2.imshow(title,img)
cv2.imshow(title,im)
# 이미지창 타이틀바
cv2.waitKey(0)
# 몇초뒤에 사라지는지, 단위 밀리세컨드
cv2.destroyAllWindows()
# cv2.destroyWindow() 무슨차이인지 모르겠다