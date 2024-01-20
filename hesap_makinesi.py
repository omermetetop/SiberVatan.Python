def hesap_makinesi():
    print("Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

  
    secim = input("Yapmak istediğiniz işlem:(1/2/3/4): ")
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    
    if secim == '1':
        sonuc = sayi1 + sayi2
    elif secim == '2':
        sonuc = sayi1 - sayi2
    elif secim == '3':
        sonuc = sayi1 * sayi2
    elif secim == '4':
        if sayi2 != 0:
            sonuc = sayi1 / sayi2
        else:
            print("Hata")
            return

   
    print(f"Sonuç: {sonuc}")


hesap_makinesi()
