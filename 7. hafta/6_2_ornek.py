"""
fare ile tıklanılan pikselin sahip olduğu rengin 10 yaklaşığını
şeffaf yaparak png olarak kaydeden programı yazınız.
"""

# calude cevabı
"""
Kameradan canlı görüntü alır.
BOŞLUK  → anlık kareyi dondurur, fare ile tıklanan rengi şeffaf yapıp PNG kaydeder.
R       → canlı yayına geri döner.
Q / ESC → çıkış.
"""

import cv2
import numpy as np

# Tolerans değeri (0-255 arası, renk yakınlık eşiği)
TOLERANS = 30
KAMERA_ID = 0  # Birden fazla kamera varsa 1, 2 ... deneyin

CANLI_PENCERE  = "Kamera - BOŞLUK: Dondur | Q: Çıkış"
DONUK_PENCERE  = "Dondurulmuş Kare - Tıklayarak Renk Seç | R: Geri Dön"

donuk_kare      = None   # Dondurulmuş BGR kare
mod             = "canli"  # "canli" | "donuk"


# ── Yardımcı fonksiyonlar ────────────────────────────────────────────────────

def rengi_seffaf_yap(goruntu_bgr, b, g, r, tolerans):
    """Verilen BGR rengine yakın pikselleri şeffaf yapar, BGRA döndürür."""
    bgra = cv2.cvtColor(goruntu_bgr, cv2.COLOR_BGR2BGRA)

    alt = np.array([max(0,   b - tolerans),
                    max(0,   g - tolerans),
                    max(0,   r - tolerans), 0],   dtype=np.uint8)
    ust = np.array([min(255, b + tolerans),
                    min(255, g + tolerans),
                    min(255, r + tolerans), 255], dtype=np.uint8)

    maske = cv2.inRange(bgra, alt, ust)
    bgra[maske > 0, 3] = 0

    etkilenen = int(np.count_nonzero(maske))
    toplam    = goruntu_bgr.shape[0] * goruntu_bgr.shape[1]
    print(f"[Bilgi] Şeffaf piksel: {etkilenen}/{toplam} "
          f"(%{etkilenen / toplam * 100:.1f})")
    return bgra


def onizleme_olustur(bgra):
    """Şeffaf alanları damalı desen üzerine harmanlayarak BGR önizleme üretir."""
    y, x  = bgra.shape[:2]
    d     = 10
    zemin = np.zeros((y, x, 3), dtype=np.uint8)
    for i in range(0, y, d):
        for j in range(0, x, d):
            renk = 200 if (i // d + j // d) % 2 == 0 else 255
            zemin[i:i+d, j:j+d] = renk

    alfa   = bgra[:, :, 3:4].astype(float) / 255.0
    bgr_f  = bgra[:, :, :3].astype(float)
    zemin_f = zemin.astype(float)
    return (bgr_f * alfa + zemin_f * (1 - alfa)).astype(np.uint8)


# ── Fare geri çağrımı (sadece donuk modda aktif) ─────────────────────────────

def fare_callback(event, x, y, flags, param):
    global donuk_kare

    if event != cv2.EVENT_LBUTTONDOWN or donuk_kare is None:
        return

    bgr_piksel = donuk_kare[y, x]
    b, g, r    = int(bgr_piksel[0]), int(bgr_piksel[1]), int(bgr_piksel[2])
    print(f"\n[Tıklanan] ({x},{y})  BGR:({b},{g},{r})  RGB:({r},{g},{b})")

    sonuc    = rengi_seffaf_yap(donuk_kare, b, g, r, TOLERANS)
    onizleme = onizleme_olustur(sonuc)

    cv2.imshow(DONUK_PENCERE, onizleme)

    dosya = "seffaf_cikti.png"
    cv2.imwrite(dosya, sonuc)
    print(f"[Kaydedildi] '{dosya}'  (Tolerans: ±{TOLERANS})")


# ── Ana döngü ────────────────────────────────────────────────────────────────

def main():
    global donuk_kare, mod

    kamera = cv2.VideoCapture(KAMERA_ID)
    if not kamera.isOpened():
        print(f"Hata: Kamera (id={KAMERA_ID}) açılamadı.")
        return

    print("=" * 55)
    print("  Kameradan Renk Şeffaflaştırıcı")
    print("=" * 55)
    print(f"  Tolerans : ±{TOLERANS}")
    print("  BOŞLUK   : Kareyi dondur")
    print("  Sol tık  : Donuk karede renk seç → PNG kaydet")
    print("  R        : Canlı yayına dön")
    print("  Q / ESC  : Çıkış")
    print("=" * 55)

    cv2.namedWindow(CANLI_PENCERE, cv2.WINDOW_NORMAL)

    while True:
        if mod == "canli":
            ret, kare = kamera.read()
            if not ret:
                print("Hata: Kameradan kare alınamadı.")
                break

            # Canlı pencereye bilgi yazısı ekle
            bilgi = kare.copy()
            cv2.putText(bilgi, "BOSLUK: Dondur  |  Q: Cikis",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.imshow(CANLI_PENCERE, bilgi)

        tus = cv2.waitKey(1) & 0xFF

        if tus in (ord('q'), ord('Q'), 27):
            break

        elif tus == ord(' ') and mod == "canli":
            # Kareyi dondur
            ret, donuk_kare = kamera.read()
            if ret:
                mod = "donuk"
                cv2.namedWindow(DONUK_PENCERE, cv2.WINDOW_NORMAL)
                cv2.setMouseCallback(DONUK_PENCERE, fare_callback)

                onizleme = donuk_kare.copy()
                cv2.putText(onizleme, "Renk secmek icin tiklayin  |  R: Geri don",
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0, 200, 255), 2, cv2.LINE_AA)
                cv2.imshow(DONUK_PENCERE, onizleme)
                print("\n[Kare donduruldu] Şeffaf yapmak istediğiniz renge tıklayın.")

        elif tus in (ord('r'), ord('R')) and mod == "donuk":
            # Canlı yayına dön
            mod = "donuk"  # geçici; pencere kapat
            cv2.destroyWindow(DONUK_PENCERE)
            donuk_kare = None
            mod = "canli"
            print("[Canlı yayın] Kameraya geri dönüldü.")

    kamera.release()
    cv2.destroyAllWindows()
    print("\nProgram kapatıldı.")


if __name__ == "__main__":
    main()