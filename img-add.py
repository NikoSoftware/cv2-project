import cv2
import numpy as np




if __name__ == '__main__':

    img = np.zeros((460, 640), np.uint8)

    img2 = img.copy()

    img[50:150,50:200] = 255

    img2[100:250,150:300] = 255





    ofImg = cv2.bitwise_not(img)

    #并集才会显示
    addImg = cv2.bitwise_and(img, img2)

    #或
    yuImg = cv2.bitwise_or(img, img2)
    #异或
    yiImg = cv2.bitwise_xor(img, img2)


    cv2.imshow('img', img)

    cv2.imshow('img2', ofImg)

    cv2.imshow('img3', addImg)

    cv2.imshow('img4', yuImg)

    cv2.imshow('img5', yiImg)

    cv2.waitKey(0)
