import cv2
import numpy as np


if __name__ == '__main__':

    img = cv2.imread('./img/city.jpeg')

    print(img.shape)


    #reimg = cv2.resize(img, (1080, 720))

    saimg = cv2.resize(img,None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)

    img6 = cv2.resize(img,(640,640))

    cv2.imshow('img1', img)

    cv2.imshow('img6', img6)


    cv2.imshow('img3', saimg)

    key = cv2.waitKey(0)
    if key == 27:
        exit(0)
    cv2.destroyAllWindows()

