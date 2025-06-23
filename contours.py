import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('./img/star.jpeg')


#单通道
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #二值化
    ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY )

    #轮廓查找
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #绘制轮廓
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

    #轮廓面积
    area = cv2.contourArea(contours[0])
    print(area)

    #轮廓周长
    peri = cv2.arcLength(contours[0], True)

    print(peri)


    #print(contours)





    cv2.imshow('img', img)

    cv2.imshow('binary', binary)


    cv2.waitKey(0)