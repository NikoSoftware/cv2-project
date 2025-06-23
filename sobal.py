
import cv2

if __name__ == '__main__':

    img = cv2.imread('./img/person.jpeg')

    distx = cv2.Sobel(img, cv2.CV_64F, 1, 0,ksize=5)
    disty = cv2.Sobel(img, cv2.CV_64F, 0, 1,ksize=5)
    mix = cv2.addWeighted(distx, 0.5, disty, 0.5, 0)

    lab = cv2.Laplacian(img, cv2.CV_64F,ksize=5)

    cv2.imshow('img', img)
    # cv2.imshow('img1', distx)
    # cv2.imshow('img2', disty)
    cv2.imshow('img3', mix)
    cv2.imshow('img4', lab)


    key = cv2.waitKey(0)
