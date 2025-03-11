import cv2 as cv

video = cv.VideoCapture(0)

asagi_filtreli_taraf = None
ret, frame = video.read()
asagi_filtreli_taraf = frame[240:, :]

while True:
    ret, frame = video.read()
    asagi = frame[240:,:]

    for s in range(239, 0, -1):
        asagi_filtreli_taraf[s] = asagi_filtreli_taraf[s-1]
    asagi_filtreli_taraf[0, :] = frame[240, :]

    frame[240:, :] = asagi_filtreli_taraf

    cv.imshow("Filtre", frame)

    if cv.waitKey(5) == ord('q'):
        break

video.release()