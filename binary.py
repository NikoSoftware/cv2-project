import cv2


if __name__ == '__main__':
    img = cv2.imread('./img/person.jpeg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret,dist = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)


    cv2.imshow('img', img)

    cv2.imshow('gray', gray)

    cv2.imshow('dist', dist)




    cv2.waitKey(0)