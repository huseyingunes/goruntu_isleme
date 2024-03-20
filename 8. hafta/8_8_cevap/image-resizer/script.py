import sys
import cv2 


first_param = sys.argv[1]


image = cv2.imread("./public/" + first_param)

new_image = cv2.resize(image, (int(sys.argv[3]), int(sys.argv[4])))

file_path = "/" + sys.argv[2]

cv2.imwrite("./public" + file_path, new_image)

print(file_path)




