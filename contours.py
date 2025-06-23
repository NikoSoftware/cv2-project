import cv2
import numpy as np

def drawShape(src,points):
    i=0
    while i < len(points):
        if i == len(points) - 1:
            cv2.line(src, points[i][0], points[0][0], (0, 0, 255), 2)
        else:
            cv2.line(src, points[i][0], points[i + 1][0], (0, 0, 255), 2)
        i += 1



if __name__ == '__main__':
    #img = cv2.imread('./img/hand.jpeg')

    img = cv2.imread('./img/rhombus.png')

    #单通道
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #二值化
    ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY )

    #轮廓查找
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #绘制轮廓
    #cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

    #轮廓面积
    area = cv2.contourArea(contours[0])
    print(area)

    #轮廓周长
    peri = cv2.arcLength(contours[0], True)

    print(peri)

    # 多边形逼近
    approx = cv2.approxPolyDP(contours[0], 20, True)

    drawShape(img, approx)

    #最小外接矩阵
    rect = cv2.minAreaRect(contours[0])
    box = cv2.boxPoints(rect)
    box = np.intp(box)
    cv2.drawContours(img, [box],0,(0,255,0),2)

    #最大外接矩阵
    x,y,w,h = cv2.boundingRect(contours[0])
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)







    cv2.imshow('img', img)

   # cv2.imshow('binary', binary)


    cv2.waitKey(0)