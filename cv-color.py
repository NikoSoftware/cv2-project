import cv2

def callback(pos):
    pass


if __name__ == '__main__':
    cv2.namedWindow('colorBar')

    colorList = [cv2.COLOR_BGR2RGBA,cv2.COLOR_BGR2BGRA,cv2.COLOR_BGR2GRAY,cv2.COLOR_BGR2HLS,cv2.COLOR_BGR2HLS]

    cv2.createTrackbar('color', 'colorBar', 0, len(colorList)-1, callback)
    img =cv2.imread('./img/test.jpg')

    while True:

        index = cv2.getTrackbarPos('color', 'colorBar')

        cv_img = cv2.cvtColor(img, colorList[index])

        cv2.imshow('colorBar', cv_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
