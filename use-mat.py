
import cv2
import numpy as np


if __name__ == '__main__':
    img = cv2.imread('./img/test.jpg')

    print(img.shape)
    print(img.size)

    b,g,r = cv2.split(img)

    img2 = cv2.merge([b,g,r])



    cv2.imshow('frame',g)
    cv2.imshow('frame2',img2)
    cv2.waitKey(0)
