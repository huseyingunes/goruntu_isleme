import cv2 as cv

resim = cv.imread("resim/kirpilmis_manzara.jpg")

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(resim, 'metin', (10, 200), font, 4, (255, 0, 0), 5, lineType=cv.LINE_AA)


cv.imshow("a", resim)
cv.waitKey(0)
