import cv2


if __name__ == '__main__':
    cv2.namedWindow('test', cv2.WINDOW_NORMAL)

    img =cv2.imread('img/74a5ec12ddc39c17910b6e235836fdf.png', cv2.IMREAD_COLOR)

    cv2.imshow( 'test', img)

    cv2.imwrite('./img/test.jpg', img)

    key = cv2.waitKey(0)

    if key & 0xFF ==  ord('q'):
        exit(0)

    cv2.destroyAllWindows()



