import cv2, time

video=cv2.VideoCapture(0)
while True:
    check, frame = video.read()

    print(check)
    print(frame)

    time.sleep(3)
    cv2.imshow("capturing",frame)

    key=cv2.waitKey(2000)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows
