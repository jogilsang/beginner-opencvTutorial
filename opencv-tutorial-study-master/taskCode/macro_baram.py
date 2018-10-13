import cv2
import pyautogui
import os
import datetime

os.chdir('C:\\Users\\user\\Desktop\\s')

# 바람의나라 클라이언트 위치 : 우상단밀착
# 바람의나라 안내창 위치좌표 : 1730,500
# 바람의나라 안내창 크기 : 185, 160

titleNum = 1
title = str(titleNum) + '.jpg'
im = pyautogui.screenshot(title, region=(1730,500, 185, 160))
# 안내창 스크린샷 찍기 그리고 저장하기
# 파일명은 순번이다.

img = cv2.imread(title, 0)
# 스크린샷 찍힌 소스사진 가져오기
img2 = img.copy()
template = cv2.imread('template.jpg',0)
# 제일핵심 : 찾을 대상인 Template 이미지 파일을 가져온다.
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF']

# CV_TM_SQDIFF ... 각 픽셀의 차이의 합
# CV_TM_SQDIFF_NORMED ... CV_TM_SQDIFF / sqrt(각 픽셀의 제곱의 곱)
# CV_TM_CCORR ... 각 픽셀의 곱의 합
# CV_TM_CCORR_NORMED ... CV_TM_CCORR / sqrt(각 픽셀의 제곱의 곱)
# CV_TM_CCOEFF
# CV_TM_CCOEFF_NORMED ... CV_TM_CCOEFF / sqrt(각 픽셀의 제곱의 곱)

dt = datetime.datetime.now()

if dt.minute == 30 :

else

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 범위 밖에 다른거 인식함
    if bottom_right[0] > 125 :
        continue
    # 범위 안에 인식함
    else :
        pyautogui.press('down')
        pyautogui.press('down')
        # 두번 눌러서 내려가기

    cv2.rectangle(img,top_left, bottom_right, 255, 2)
    # 사각형 그리기

    # 창고
    # location = pyautogui.locateOnScreen('catch.jpg', grayscale=True)