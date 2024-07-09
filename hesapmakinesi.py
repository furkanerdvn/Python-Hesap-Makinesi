def hesapla(islem, sayi1, sayi2):
    if islem == 1:
        return sayi1 + sayi2
    elif islem == 2:
        return sayi1 - sayi2
    elif islem == 3:
        return sayi1 * sayi2
    elif islem == 4:
        if sayi2 != 0:
            return sayi1 / sayi2
        else:
            return "Hata: sıfıra bölme!"

print("---Hesap Makinesi Programına Hoş Geldiniz!---")
print()
print("Yapabileceğiniz işlemler:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

while True:
    print()
    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4) veya çıkmak için 'q' tuşuna basın: ")

    if secim == 'q':
        print("---Hesap Makinesi Programı Kapatılıyor...---")
        break

    try:
        secim = int(secim)
        if secim in (1, 2, 3, 4):
            sayi1 = float(input("Birinci sayıyı girin: "))
            print()
            sayi2 = float(input("İkinci sayıyı girin: "))
            print()

            sonuc = hesapla(secim, sayi1, sayi2)
            if isinstance(sonuc, str):
                print(sonuc)
            else:
                print(f"Sonuç: {sonuc}")
        else:
            print("Geçersiz giriş. Lütfen 1 ile 4 arasında bir sayı seçin veya 'q' tuşuna basarak çıkın.")
            print()
    except ValueError:
        print("Geçersiz giriş. Lütfen geçerli bir sayı veya 'q' tuşuna basın.")
        print()
