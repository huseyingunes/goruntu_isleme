import cv2 as cv

video = cv.VideoCapture("video\ornek.mp4")

fps = video.get(cv.CAP_PROP_FPS)
en = video.get(cv.CAP_PROP_FRAME_WIDTH)
boy = video.get(cv.CAP_PROP_FRAME_HEIGHT)
print(fps, en,  boy)

while(video.isOpened()):
    ret, frame = video.read()
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    print(ret)
    if ret:
        cv.imshow("video", frame)
        if cv.waitKey(33) == 27:
            break
