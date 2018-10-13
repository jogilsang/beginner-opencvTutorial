# source : opencv-python-tutroals
# modify : jogilsang

import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

os.chdir('C:\\Users\\user\\Desktop\\opencv')

img = cv2.imread('picture.jpg',0)
# 이미지 불러오기 ( 1,0,-1)
# cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

title = "imshow"

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
#  to hide tick values on X and Y axis
plt.show()







