import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir('C:\\Users\\user\\Desktop\\opencv')

img = cv2.imread('canny.jpg',1)

titles = ['orginal', 'level1', 'level2', 'level3']

images = []
images.append(img)

for i in range(3):
    img = cv2.pyrDown(img)
    images.append(img)

for i in range(4):
    cv2.imshow(titles[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()