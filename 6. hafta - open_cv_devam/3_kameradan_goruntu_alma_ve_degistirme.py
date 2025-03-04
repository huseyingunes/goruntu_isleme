import cv2 as cv

video = cv.VideoCapture(0)

while(video.isOpened()):
    ret, frame = video.read()
    nisangah = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #print(nisangah.shape)
    #print(nisangah[0, 0])q
    if ret:
        nisangah[239, :] = 0
        nisangah[240, :] = 0
        nisangah[241, :] = 0
        nisangah[:, 319:322] = 0
        cv.imshow("kamera", nisangah)
        if cv.waitKey(33) == 27:
            break

