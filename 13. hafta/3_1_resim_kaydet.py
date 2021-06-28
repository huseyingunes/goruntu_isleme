import cv2

video_capture = cv2.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    cv2.imshow("a", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("hg.jpg", frame)
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
