import cv2
import numpy as np


if __name__ == '__main__':
    image = cv2.imread('./img/test.jpg')
    # 垂直翻转（沿X轴）
    vertical_flip = cv2.flip(image, 0)

    # 水平翻转（沿Y轴）
    horizontal_flip = cv2.flip(image, 1)

    # 双向翻转
    both_flip = cv2.flip(image, -1)

    # 显示结果
    cv2.imshow("Original", image)
    cv2.imshow("Vertical Flip", vertical_flip)
    cv2.imshow("Horizontal Flip", horizontal_flip)
    cv2.imshow("Both Flip", both_flip)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
