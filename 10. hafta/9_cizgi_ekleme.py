import cv2 as cv

resim = cv.imread("resim/kirpilmis_manzara.jpg")

cv.line(resim, (0, 0), (256, 256), (255, 0, 0), 50, lineType=cv.LINE_AA)
## https://www.oreilly.com/library/view/mastering-opencv-4/9781789344912/5c4150d2-b550-40be-8b18-f2e71e20d9be.xhtml
cv.imshow("a", resim)
cv.waitKey(0)
