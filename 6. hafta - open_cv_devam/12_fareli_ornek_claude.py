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
import numpy as np
import os

# Seçim değişkenleri
secim_basladi = False
baslangic_nokta = (-1, -1)
bitis_nokta = (-1, -1)
secim_yapiliyor = False
dondurulmus_frame = None
bolge_sayaci = 1  # Kaydedilen bölge numarası

# Kayıt klasörü
kayit_klasoru = "resim"
os.makedirs(kayit_klasoru, exist_ok=True)

def mouse_callback(event, x, y, flags, param):
    global secim_basladi, baslangic_nokta, bitis_nokta, secim_yapiliyor, bolge_sayaci, dondurulmus_frame

    if event == cv.EVENT_LBUTTONDOWN:
        secim_basladi = True
        secim_yapiliyor = True
        baslangic_nokta = (x, y)
        bitis_nokta = (x, y)

    elif event == cv.EVENT_MOUSEMOVE:
        if secim_yapiliyor:
            bitis_nokta = (x, y)

    elif event == cv.EVENT_LBUTTONUP:
        secim_yapiliyor = False
        bitis_nokta = (x, y)

        # Geçerli bir seçim yapıldı mı kontrol et
        x1, y1 = min(baslangic_nokta[0], bitis_nokta[0]), min(baslangic_nokta[1], bitis_nokta[1])
        x2, y2 = max(baslangic_nokta[0], bitis_nokta[0]), max(baslangic_nokta[1], bitis_nokta[1])

        if (x2 - x1) > 5 and (y2 - y1) > 5 and dondurulmus_frame is not None:
            bolge = dondurulmus_frame[y1:y2, x1:x2]
            dosya_adi = os.path.join(kayit_klasoru, f"bolge_{bolge_sayaci}.png")
            cv.imwrite(dosya_adi, bolge)
            print(f"[✓] Bölge {bolge_sayaci} kaydedildi → {dosya_adi}")
            bolge_sayaci += 1

video = cv.VideoCapture(0)
cv.namedWindow("kamera")
cv.setMouseCallback("kamera", mouse_callback)

donduruldu = False  # Görüntü donduruldu mu?

while video.isOpened():

    if not donduruldu:
        ret, frame = video.read()
        if not ret:
            break

        # Renk kanallarını al
        kirmizi = frame[:, :, 2].copy()
        yesil   = frame[:, :, 1].copy()

        # Kırmızı ↔ Yeşil değerlerini değiştir
        frame[:, :, 2] = yesil
        frame[:, :, 1] = kirmizi

        # Mavi kanalı yarıya düşür
        frame[:, :, 0] = (frame[:, :, 0] / 2).astype(np.uint8)

        dondurulmus_frame = frame.copy()
        gosterim = frame.copy()
    else:
        # Dondurulmuş karede seçim dikdörtgenini çiz
        gosterim = dondurulmus_frame.copy()

        if secim_yapiliyor or baslangic_nokta != (-1, -1):
            x1 = min(baslangic_nokta[0], bitis_nokta[0])
            y1 = min(baslangic_nokta[1], bitis_nokta[1])
            x2 = max(baslangic_nokta[0], bitis_nokta[0])
            y2 = max(baslangic_nokta[1], bitis_nokta[1])
            cv.rectangle(gosterim, (x1, y1), (x2, y2), (0, 255, 255), 2)

        # Durum bilgisi
        cv.putText(gosterim, "DONDURULDU | Bolge sec | [D] devam | [ESC] cikis",
                   (10, 25), cv.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 1)

    cv.imshow("kamera", gosterim)

    tus = cv.waitKey(2) & 0xFF

    if tus == ord('s') and not donduruldu:
        donduruldu = True
        # Seçimi sıfırla
        baslangic_nokta = (-1, -1)
        bitis_nokta     = (-1, -1)
        secim_basladi   = False
        print("[S] Görüntü donduruldu. Fare ile bölge seçebilirsiniz.")

    elif tus == ord('d') and donduruldu:
        donduruldu = False
        baslangic_nokta = (-1, -1)
        bitis_nokta     = (-1, -1)
        secim_basladi   = False
        print("[D] Görüntü akışı devam ediyor.")

    elif tus == 27:  # ESC
        print("[ESC] Çıkılıyor...")
        break

video.release()
cv.destroyAllWindows()