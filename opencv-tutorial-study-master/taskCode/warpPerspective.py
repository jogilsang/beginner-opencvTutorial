import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir('C:\\Users\\user\\Desktop\\opencv')

img = cv2.imread('go.jpg')
rows, cols, ch = img.shape[:3]

# pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts1 = np.float32([[74, 43], [246, 40], [13, 237], [298, 232]])
# 좌상,우상,좌하,우하 Z모양으로 값 대입해야됨
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
# 구현할사이즈

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (300, 300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()