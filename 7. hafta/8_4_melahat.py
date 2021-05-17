import cv2
import numpy as np

cap = cv2.VideoCapture('video/rat.avi')

lower_blue = np.array([240, 255, 255])
upper_blue = np.array([255, 255, 255])

while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Ekrana çıktı veriliyor
        frame = frame[100:, 200:700]
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('hsv', hsv)
        mask = cv2.inRange(hsv, (15, 0, 0), (25, 255, 255))
        cv2.imshow('mask', mask)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('res', res)
        cv2.imshow('frame', frame)

        # Q ile çıkış yapılıyor
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break
cap.release()
cv2.destroyAllWindows()

# 10