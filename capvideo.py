import cv2


if __name__ == '__main__':

    fourcc = cv2.VideoWriter.fourcc(*'mp4v')

    #cap = cv2.VideoCapture('./img/fengshan.mp4')
    cap = cv2.VideoCapture(0)
    vidf = cv2.VideoWriter.fourcc(*'MP4V')
    cap.set(cv2.CAP_PROP_FOURCC, vidf)  # 应用编码格式
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 宽度
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高度
    print(f"分辨率: {width}x{height}")
    # 摄像头输出格式
    print(f"编码格式: {hex(int(cap.get(cv2.CAP_PROP_FOURCC)))}")

    vw = cv2.VideoWriter('./img/test.mp4', fourcc, 20.0, (int(width), int(height)))



    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame',int(height),int(width))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            cv2.imshow('frame', frame)
            cv2.resizeWindow('frame',int(height),int(width))
            vw.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("帧读取失败，检查USB连接或重启摄像头")
            break
    vw.release()
    cap.release()
    cv2.destroyAllWindows()
