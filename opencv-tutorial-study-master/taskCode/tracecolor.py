import cv2
import numpy as np
import os

os.chdir('C:\\Users\\user\\Desktop\\opencv')

file = 'torres.mp4'
cap = cv2.VideoCapture(file)

while True:

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    upper_red = np.array([120, 177, 140])
    lower_red = np.array([112, 184, 111])

    # define range of blue color in HSV
    # lower_blue = np.array([110, 50, 50])
    # upper_blue = np.array([130, 255, 255])


    # fail
    # lower_green = np.array([145, 181, 83])
    # upper_green = np.array([96, 134, 35])


    # Threshold the HSV image to get only blue colors
    # mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # 하얀색깔이랑 겹치면 캡처
    # 검은색깔이랑 겹치면 제거

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    # 합성
    k = cv2.waitKey(25) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()