import time 

while True:
 print("İlk sayinizi seçiniz:")
 ilksayi = int(input())

 print("İşlem türünü seçiniz:")

 time.sleep(1)
 print("Toplama için: + ")
 time.sleep(0.3)
 print("Çarpma için: * ")
 time.sleep(0.3)
 print("çikarma için: - ")
 time.sleep(0.3)
 print("bölme için: / ")
 time.sleep(0.3)

 işlem = input()

 print("İkinci Sayinizi seçiniz:")
 ilk2sayi = int(input())

 if işlem == "*":
    print("Sonuç: ", ilksayi * ilk2sayi )
 elif işlem == "+":
    print("Sonuç: ", ilksayi + ilk2sayi )
 elif işlem == "-":
    print("Sonuç: ", ilksayi - ilk2sayi )
 elif işlem == "/":
    print("Sonuç: ", ilksayi / ilk2sayi )
 else:
    print("geçersiz işlem seçtiniz")

 devam = input("Tekrar işlem yapmak ister misiniz? (e/h): ")
 time.sleep(0.4)

 if devam.lower() != "e":
        print("Hesap makinesi kapatiliyor...")
        break



