import cv2 as cv

video = cv.VideoCapture(0)

fps = video.get(cv.CAP_PROP_FPS)
en = video.get(cv.CAP_PROP_FRAME_WIDTH)
boy = video.get(cv.CAP_PROP_FRAME_HEIGHT)

print(fps, en,  boy)

while(video.isOpened()):
    ret, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if ret:
        cv.imshow("kamera", gray)
        if cv.waitKey(1) == ord('q'):
            break

#kameranın fps değerini öğrenme

