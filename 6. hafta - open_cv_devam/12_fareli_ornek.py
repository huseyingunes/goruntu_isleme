"""
kameradan görüntüyü alın
görüntüdeki kırmızı  yeşil renklerin değerlerini değiştirin.
görüntüdeki mavi rengin değerini yarı yarıya düşürün
s tuşuna basılınca kamera görüntüsü dursun
    kamera görüntüsü durunca kullanıcı fare ile istediği bir bölgeyi seçsin
        seçilen bölge otomatik olarak numaralandırılarak kaydedilsin
d tuşuna basınca görüntü tekrar akmaya devam etsin
esc tuşuna basılınca çıkılsın
"""

import cv2 as cv
video = cv.VideoCapture(0)
while(video.isOpened()):
    ret, frame = video.read()
    kirmizi = frame[:, :, 2]
    yesil = frame[:, :, 1]
    frame[:, :, 2] = yesil
    frame[:, :, 1] = kirmizi
    frame[:, :, 0] = frame[:, :, 0] / 2

    if ret:
        cv.imshow("kamera", frame)
        if cv.waitKey(2) == ord('s'):
            break
