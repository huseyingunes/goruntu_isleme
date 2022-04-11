import cv2 as cv

video = cv.VideoCapture(0)

while(video.isOpened()):
    ret, frame = video.read()
    if ret:
        nisangah = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # print(nisangah.shape)
        # print(nisangah[0, 0])
        nisangah[239, :] = 0
        nisangah[240, :] = 0
        nisangah[241, :] = 0
        nisangah[:, 319:321] = 0
        cv.imshow("kamera", nisangah)
        if cv.waitKey(33) == ord('q'):
            break