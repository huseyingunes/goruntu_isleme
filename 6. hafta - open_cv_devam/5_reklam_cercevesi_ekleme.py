import cv2 as cv

video = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("video/kayit.avi", fourcc, 20.0, (640, 480))

resim = cv.imread("resim/ad_soyad.jpg")

i = 0
while(video.isOpened()):
    i += 1
    ret, frame = video.read()
    if i % 10 == 0:
        frame = resim
        i = 0
    #print(nisangah.shape)
    #print(nisangah[0, 0])
    if ret:

        out.write(frame)
        cv.imshow("kamera", frame)
        if cv.waitKey(33) == ord('q'):
            break

out.release()
video.release()