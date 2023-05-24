import cv2 as cv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

mp_drawing = mp.solutions.drawing_utils

base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

video = cv.VideoCapture(0)

while(video.isOpened()):
    ret, frame = video.read()
    if ret:
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        detection_result = detector.detect(image)
        print(detection_result)
        if not detection_result:
            annotated_image = mp_drawing.draw_landmarks(image.numpy_view(), detection_result)
        else:
            annotated_image = frame
        #cv.imshow("kamera", frame)
        cv.imshow("sdfsdf", cv.cvtColor(annotated_image, cv.COLOR_RGB2BGR))
        if cv.waitKey(300) == ord('q'):
            break

