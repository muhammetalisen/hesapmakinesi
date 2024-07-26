def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y != 0:
        return x / y
    else:
        return "Bölme hatası: 0'a bölme yapılamaz."

def hesap_makinesi():
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    secim = input("Seçiminizi yapın (1/2/3/4): ")

    if secim in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Birinci sayıyı girin: "))
            num2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            return

        if secim == '1':
            print(f"Sonuç: {toplama(num1, num2)}")
        elif secim == '2':
            print(f"Sonuç: {cikarma(num1, num2)}")
        elif secim == '3':
            print(f"Sonuç: {carpma(num1, num2)}")
        elif secim == '4':
            print(f"Sonuç: {bolme(num1, num2)}")
    else:
        print("Geçersiz seçim")

hesap_makinesi()
