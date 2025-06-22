import cv2


if __name__ == '__main__':
    img = cv2.imread('./img/test.jpg')

    cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),2,4)



    cv2.imshow('img', img)

    key = cv2.waitKey(0)
    if key == 27:
        exit(0)
    cv2.destroyAllWindows()