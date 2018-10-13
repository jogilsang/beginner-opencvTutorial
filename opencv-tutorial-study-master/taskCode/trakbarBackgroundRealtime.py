import cv2
import numpy as np
import os

def nothing(x):
    pass

# Create a black image, a window
# img = np.zeros((300,512,3), np.uint8)


os.chdir('C:\\Users\\user\\Desktop\\opencv')
img = cv2.imread('picture.jpg',1)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('RGB','image',0,2,nothing)
cv2.createTrackbar('control','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    rgb = cv2.getTrackbarPos('RGB','image')
    c = cv2.getTrackbarPos('control','image')
    s = cv2.getTrackbarPos(switch,'image')

    img[:, :, -3] = 255

    if s != 0:
        img[:, :, rgb] = c



cv2.destroyAllWindows()