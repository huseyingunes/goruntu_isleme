import cv2 as cv

video = cv.VideoCapture("video/ornek.mp4")


while(video.isOpened()):
    ret, frame = video.read()
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    print(ret)
    if ret:
        cv.imshow("video", frame)
        if cv.waitKey(33) == ord('q'):
            break
