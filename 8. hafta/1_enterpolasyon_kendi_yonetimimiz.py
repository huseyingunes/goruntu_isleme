"""
Pixel Interpolation ile Görüntü Büyütme
========================================
Bu program, bir görüntüyü bilinear interpolasyon yöntemiyle
istenilen boyuta büyütür. Boş pikseller komşu piksel değerlerinden
doğrusal olarak hesaplanır.

Kullanım:
    python pixel_upscale.py --input resim.png --scale 2
    python pixel_upscale.py --input resim.png --width 600 --height 600
    python pixel_upscale.py --input resim.png --scale 3 --output buyuk_resim.png
"""

import argparse
import os
from pathlib import Path

try:
    from PIL import Image
    import numpy as np
except ImportError:
    print("Gerekli kütüphaneler yükleniyor...")
    import subprocess

    subprocess.check_call(["pip", "install", "Pillow", "numpy", "-q"])
    from PIL import Image
    import numpy as np


def bilinear_interpolation(img_array: np.ndarray, new_width: int, new_height: int) -> np.ndarray:
    """
    Bilinear interpolasyon ile görüntüyü yeniden boyutlandırır.

    Verdiğin örnek:
        İlk piksel: [100, 25, 36]   Son piksel: [145, 96, 85]
        Ara değerler:
          Mavi (R): 100 → 115 → 130 → 145
          Yeşil (G): 25 → 48.3 → 71.6 → 96
          Kırmızı (B): 36 → 52.3 → 68.6 → 85

    Bu mantık hem yatay hem dikey yönde uygulanır.

    Args:
        img_array: Orijinal görüntü numpy dizisi (H, W, C)
        new_width:  Hedef genişlik (piksel)
        new_height: Hedef yükseklik (piksel)

    Returns:
        Büyütülmüş görüntü numpy dizisi (new_height, new_width, C)
    """
    old_height, old_width = img_array.shape[:2]
    channels = img_array.shape[2] if img_array.ndim == 3 else 1

    # float32'ye çevir (hassas hesaplama için)
    src = img_array.astype(np.float32)

    # Hedef görüntü için boş dizi
    dst = np.zeros((new_height, new_width, channels), dtype=np.float32)

    # Her hedef piksel için kaynak koordinatı hesapla
    # Köşeden köşeye eşleme (edge-aligned)
    x_scale = (old_width - 1) / (new_width - 1) if new_width > 1 else 0
    y_scale = (old_height - 1) / (new_height - 1) if new_height > 1 else 0

    for y_dst in range(new_height):
        for x_dst in range(new_width):
            # Kaynak koordinatlar (kayan noktalı)
            x_src = x_dst * x_scale
            y_src = y_dst * y_scale

            # Alt-sol köşenin tam koordinatları
            x0 = int(x_src)
            y0 = int(y_src)

            # Üst-sağ köşenin koordinatları (sınır kontrolü ile)
            x1 = min(x0 + 1, old_width - 1)
            y1 = min(y0 + 1, old_height - 1)

            # Ağırlıklar (0.0 ile 1.0 arası)
            wx = x_src - x0  # sağa ağırlık
            wy = y_src - y0  # aşağıya ağırlık

            # 4 komşu pikselden ağırlıklı ortalama (bilinear)
            # Q(x,y) = (1-wx)(1-wy)*P00 + wx*(1-wy)*P10
            #        +  (1-wx)*wy *P01 + wx*wy     *P11
            dst[y_dst, x_dst] = (
                    (1 - wx) * (1 - wy) * src[y0, x0] +
                    wx * (1 - wy) * src[y0, x1] +
                    (1 - wx) * wy * src[y1, x0] +
                    wx * wy * src[y1, x1]
            )

    return np.clip(dst, 0, 255).astype(np.uint8)


def bilinear_interpolation_fast(img_array: np.ndarray, new_width: int, new_height: int) -> np.ndarray:
    """
    Numpy vektörleştirmesi ile hızlandırılmış bilinear interpolasyon.
    Büyük görüntüler için çok daha hızlı çalışır.

    Args:
        img_array: Orijinal görüntü numpy dizisi
        new_width:  Hedef genişlik
        new_height: Hedef yükseklik

    Returns:
        Büyütülmüş görüntü numpy dizisi
    """
    old_height, old_width = img_array.shape[:2]
    is_gray = img_array.ndim == 2
    if is_gray:
        img_array = img_array[:, :, np.newaxis]

    channels = img_array.shape[2]
    src = img_array.astype(np.float32)

    # Hedef piksel koordinat ızgarası
    x_scale = (old_width - 1) / (new_width - 1) if new_width > 1 else 0
    y_scale = (old_height - 1) / (new_height - 1) if new_height > 1 else 0

    x_src = np.linspace(0, old_width - 1, new_width, dtype=np.float32)
    y_src = np.linspace(0, old_height - 1, new_height, dtype=np.float32)

    x0 = np.floor(x_src).astype(np.int32)
    y0 = np.floor(y_src).astype(np.int32)
    x1 = np.minimum(x0 + 1, old_width - 1)
    y1 = np.minimum(y0 + 1, old_height - 1)

    wx = (x_src - x0).reshape(1, -1, 1)  # (1, W, 1)
    wy = (y_src - y0).reshape(-1, 1, 1)  # (H, 1, 1)

    # 4 komşu piksel değerleri  (H, W, C)
    P00 = src[np.ix_(y0, x0)]  # sol-üst
    P10 = src[np.ix_(y0, x1)]  # sağ-üst
    P01 = src[np.ix_(y1, x0)]  # sol-alt
    P11 = src[np.ix_(y1, x1)]  # sağ-alt

    dst = (
            (1 - wx) * (1 - wy) * P00 +
            wx * (1 - wy) * P10 +
            (1 - wx) * wy * P01 +
            wx * wy * P11
    )

    result = np.clip(dst, 0, 255).astype(np.uint8)
    return result[:, :, 0] if is_gray else result


def upscale_image(
        input_path: str,
        output_path: str = None,
        scale: float = None,
        new_width: int = None,
        new_height: int = None,
        fast: bool = True
) -> str:
    """
    Görüntüyü büyütür ve kaydeder.

    Args:
        input_path:  Kaynak görüntü dosyası
        output_path: Çıktı dosyası (None ise otomatik isimlendirilir)
        scale:       Büyütme katsayısı (örn: 2 → 2x büyütme)
        new_width:   Hedef genişlik (piksel)
        new_height:  Hedef yükseklik (piksel)
        fast:        True → hızlı numpy modu, False → adım adım döngü modu

    Returns:
        Kaydedilen dosyanın yolu
    """
    # Görüntüyü yükle
    img = Image.open(input_path)
    mode = img.mode
    img_array = np.array(img)

    old_h, old_w = img_array.shape[:2]
    print(f"Orijinal görüntü: {old_w} x {old_h} piksel  |  Mod: {mode}")

    # Hedef boyutları hesapla
    if scale is not None:
        new_width = int(old_w * scale)
        new_height = int(old_h * scale)
    elif new_width is None or new_height is None:
        raise ValueError("Lütfen --scale VEYA hem --width hem --height parametrelerini belirtin.")

    print(f"Hedef boyut: {new_width} x {new_height} piksel  (x{new_width / old_w:.2f})")

    # Interpolasyon
    print("Bilinear interpolasyon uygulanıyor...")
    if fast:
        result = bilinear_interpolation_fast(img_array, new_width, new_height)
    else:
        result = bilinear_interpolation(img_array, new_width, new_height)

    # Çıktı yolunu belirle
    if output_path is None:
        p = Path(input_path)
        suffix = f"_x{scale:.1f}" if scale else f"_{new_width}x{new_height}"
        output_path = str(p.parent / f"{p.stem}{suffix}{p.suffix}")

    # Kaydet
    out_img = Image.fromarray(result, mode=mode)
    out_img.save(output_path)
    print(f"✓ Kaydedildi: {output_path}")
    return output_path


def demo_excel_example():
    """
    Excel'deki örnek pikselleri kullanarak interpolasyonu gösterir.
    Satır 1: [100,25,36]  ·  ·  [145,96,85]
    """
    print("\n" + "=" * 55)
    print("  EXCEL ÖRNEĞİ: Eksik Piksel Değerlerini Hesapla")
    print("=" * 55)

    # 1x4 boyutlu küçük 'görüntü': sadece ilk ve son piksel dolu
    row1 = np.array([[[100, 25, 36], [0, 0, 0], [0, 0, 0], [145, 96, 85]]], dtype=np.uint8)

    # Şimdi sadece köşe piksellerini biliyoruz; aralarını hesapla
    known = np.array([[[100, 25, 36], [145, 96, 85]]], dtype=np.uint8)  # 1x2
    interpolated = bilinear_interpolation_fast(known, new_width=4, new_height=1)

    print("\nOrijinal (bilinen) değerler:")
    print(f"  Piksel 1: R={known[0, 0, 0]}  G={known[0, 0, 1]}  B={known[0, 0, 2]}")
    print(f"  Piksel 4: R={known[0, 1, 0]}  G={known[0, 1, 1]}  B={known[0, 1, 2]}")

    print("\nHesaplanan (interpolasyon sonrası) değerler:")
    for i in range(4):
        p = interpolated[0, i]
        print(f"  Piksel {i + 1}: R={p[0]}  G={p[1]}  B={p[2]}")

    # İkinci satır örneği
    print("\n" + "-" * 40)
    known2 = np.array([[[100, 25, 36], [145, 96, 85]],
                       [[200, 12, 96], [0, 5, 6]]], dtype=np.uint8)  # 2x2
    interpolated2 = bilinear_interpolation_fast(known2, new_width=4, new_height=4)

    print("2x2 grid → 4x4 interpolasyon sonucu:")
    for y in range(4):
        row_str = "  "
        for x in range(4):
            p = interpolated2[y, x]
            row_str += f"[{p[0]:3},{p[1]:3},{p[2]:3}]  "
        print(row_str)
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Bilinear interpolasyon ile görüntü büyütme",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Örnekler:
  python pixel_upscale.py --input foto.png --scale 2
  python pixel_upscale.py --input foto.jpg --width 1200 --height 800
  python pixel_upscale.py --input foto.png --scale 3 --output sonuc.png
  python pixel_upscale.py --demo
        """
    )
    parser.add_argument("--input", "-i", help="Kaynak görüntü dosyası")
    parser.add_argument("--output", "-o", help="Çıktı dosyası (opsiyonel)")
    parser.add_argument("--scale", "-s", type=float, help="Büyütme katsayısı (örn: 2)")
    parser.add_argument("--width", "-W", type=int, help="Hedef genişlik (piksel)")
    parser.add_argument("--height", "-H", type=int, help="Hedef yükseklik (piksel)")
    parser.add_argument("--slow", action="store_true", help="Yavaş ama adım adım döngü modunu kullan")
    parser.add_argument("--demo", action="store_true", help="Excel örneğini çalıştır")

    args = parser.parse_args()

    if args.demo:
        demo_excel_example()
        return

    if not args.input:
        parser.print_help()
        print("\n[!] En az --input ve (--scale VEYA --width + --height) gereklidir.")
        return

    upscale_image(
        input_path=args.input,
        output_path=args.output,
        scale=args.scale,
        new_width=args.width,
        new_height=args.height,
        fast=not args.slow
    )


if __name__ == "__main__":
    main()