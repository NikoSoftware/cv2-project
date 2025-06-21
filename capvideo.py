import cv2


if __name__ == '__main__':

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')


    #cap = cv2.VideoCapture('./img/fengshan.mp4')
    cap = cv2.VideoCapture(0)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 宽度
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高度
    print(f"分辨率: {width}x{height}")
    # 摄像头输出格式
    fourcc_code = int(cap.get(cv2.CAP_PROP_FOURCC))
    fourcc_str = "".join([chr((fourcc_code >> 8 * i) & 0xFF) for i in range(4)])
    print(f"输出格式: {fourcc_str}")

    vw = cv2.VideoWriter('./img/test.mp4', fourcc, 20.0, (int(width), int(height)))



    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 640, 480)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
            cv2.resizeWindow('frame', 640, 480)
            vw.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    vw.release()
    cap.release()
    cv2.destroyAllWindows()
