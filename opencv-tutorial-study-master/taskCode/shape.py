import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir('C:\\Users\\user\\Desktop\\opencv')

img = cv2.imread('shape.jpg')
kernel = np.ones((5, 5), np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


cv2.imshow('gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()