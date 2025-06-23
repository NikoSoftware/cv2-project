import cv2
import numpy as  np

#腐蚀
if __name__ == '__main__':
    img = cv2.imread('./img/bird.jpeg')

    #kernel = np.ones((3, 3), np.uint8)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    dst = cv2.erode(img, kernel, iterations=1)

    dis = cv2.dilate(img, kernel, iterations=1)

    # 开运算
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    # 闭运算
    close =  cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    # 形态学梯度
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)




    cv2.imshow('img', img)

    cv2.imshow('dst', dst)
    cv2.imshow('dis', dis)
    cv2.imshow('open', open)

    cv2.imshow('gradient', gradient)
    cv2.waitKey(0)

