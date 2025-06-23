import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('./img/person.jpeg')

    dist = cv2.Canny(img, 100, 200)


    cv2.imshow('img', img)

    cv2.imshow('img2', dist)

    cv2.waitKey(0)