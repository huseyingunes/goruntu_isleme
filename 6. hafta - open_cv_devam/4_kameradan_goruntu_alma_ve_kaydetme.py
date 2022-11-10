import cv2 as cv

video = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("video/kayit.avi", fourcc, 20.0, (640, 480), 0)

while(video.isOpened()):
    ret, frame = video.read()
    nisangah = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #print(nisangah.shape)
    #print(nisangah[0, 0])
    if ret:
        nisangah[239, :] = 0
        nisangah[240, :] = 0
        nisangah[241, :] = 0
        nisangah[:, 319:321] = 0
        out.write(nisangah)
        cv.imshow("kamera", nisangah)
        if cv.waitKey(33) == ord('q'):
            break

out.release()
video.release()
