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
import os

video = cv.VideoCapture(0)

# Kayıt klasörü
kayit_klasoru = "resim"
os.makedirs(kayit_klasoru, exist_ok=True)

sayac = 1
durdu_mu = False
donmus_kare = None

while video.isOpened():
    if not durdu_mu:
        ret, frame = video.read()

        if not ret:
            print("Kameradan görüntü alınamadı.")
            break

        # Kırmızı ve yeşil kanalları değiştir
        kirmizi = frame[:, :, 2].copy()
        yesil = frame[:, :, 1].copy()

        frame[:, :, 2] = yesil
        frame[:, :, 1] = kirmizi

        # Mavi kanalı yarıya düşür
        frame[:, :, 0] = (frame[:, :, 0] // 2)

        # Ekranda göster
        cv.imshow("kamera", frame)

        tus = cv.waitKey(20) & 0xFF

        if tus == ord('s'):
            durdu_mu = True
            donmus_kare = frame.copy()

        elif tus == 27:  # ESC
            break

    else:
        # Duran görüntüyü göster
        cv.imshow("kamera", donmus_kare)

        # Fare ile bölge seç
        roi = cv.selectROI("kamera", donmus_kare, showCrosshair=True, fromCenter=False)
        x, y, w, h = roi

        # Geçerli bir seçim yapıldıysa kaydet
        if w > 0 and h > 0:
            secilen_bolge = donmus_kare[y:y+h, x:x+w]
            dosya_adi = os.path.join(kayit_klasoru, f"bolge_{sayac}.png")
            cv.imwrite(dosya_adi, secilen_bolge)
            print(f"Kaydedildi: {dosya_adi}")
            sayac += 1
        else:
            print("Herhangi bir bölge seçilmedi.")

        # Kullanıcı d basana kadar görüntü akmasın
        while True:
            cv.imshow("kamera", donmus_kare)
            tus = cv.waitKey(20) & 0xFF

            if tus == ord('d'):
                durdu_mu = False
                break
            elif tus == 27:  # ESC
                video.release()
                cv.destroyAllWindows()
                exit()

video.release()
cv.destroyAllWindows()