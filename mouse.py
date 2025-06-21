import cv2


def mouse_callback(event, x, y, flags, param):
    print(event, x, y, flags, param)


if __name__ == '__main__':

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 640, 480)
    img =cv2.imread('./img/test.jpg')
    cv2.setMouseCallback('frame', mouse_callback)
    while True:
        cv2.imshow('frame', img)
        cv2.resizeWindow('frame', 640, 480)
        key = cv2.waitKey(0)
        if key == ord('q'):
            break


    cv2.destroyAllWindows()

