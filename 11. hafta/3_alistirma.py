"""
Fare tıklanılan 4 noktayı bir dikdörtgen ile birleştiren program
Fare ile her tıklandığında o bölgeye ufak yeşil bir yuvarlak çizecek
4. Noktaya tıklandığında bu 4 noktayı mazi çizgiler ile birleştirecek
"""














import cv2

kose = []


def fare_tiklama(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Sol tıklama olayı
        # Tıklanan yere yuvarlak çiz
        cv2.circle(resim, (x, y), 10, (0, 255, 0), -1)
        kose.append((x, y))
        cv2.imshow('Resim', resim)
        if len(kose) == 4:
            dortgen()


def dortgen():
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = kose
    # Dörtgeni çiz
    cv2.line(resim, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv2.line(resim, (x2, y2), (x3, y3), (255, 0, 0), 2)
    cv2.line(resim, (x3, y3), (x4, y4), (255, 0, 0), 2)
    cv2.line(resim, (x4, y4), (x1, y1), (255, 0, 0), 2)

    del kose[:]
    cv2.imshow('Resim', resim)


resim = cv2.imread('resim/dosya.jpg')
cv2.imshow('Resim', resim)
cv2.setMouseCallback('Resim', fare_tiklama)

# 'q' tuşuna basılana kadar beklet
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Pencereleri kapat
cv2.destroyAllWindows()