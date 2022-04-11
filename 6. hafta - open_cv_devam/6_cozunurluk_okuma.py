import cv2 as cv

resim = cv.imread("resim/ad_soyad.jpg")

print(resim.shape)

print("Resmin yüksekliği :", resim.shape[0])
print("Resmin genişliği :", resim.shape[1])
###########################################
h, w, d = resim.shape

print("Resmin yüksekliği :", h)
print("Resmin genişliği :", w)
print("Resmin renk derinliği :", d)