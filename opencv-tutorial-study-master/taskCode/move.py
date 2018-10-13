import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

os.chdir('C:\\Users\\user\\Desktop\\opencv')

img = cv2.imread('go.jpg')
rows, cols = img.shape[:2]

M = np.float32([[1, 0, 150], [0, 1, 150]])
dst = cv2.warpAffine(img, M, (cols, rows))
# 좌표 150,150 이동
# 출력 이미지의 크기(너비,높이)가 세번쨰인수

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(dst), plt.title('warpAffine')
plt.show()