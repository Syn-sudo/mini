print('''
Beden Kitle İndeksi (BKİ), şu formülle hesaplanır:
BKİ = Kilo / (Boy * Boy)

BKİ Değerleri ve Anlamları:
---------------------------
BKİ 18.5'in altındaysa       ---> Zayıf
BKİ 18.5 - 24.9 arasındaysa  ---> Normal
BKİ 25 - 29.9 arasındaysa    ---> Fazla Kilolu
BKİ 30 ve üzerindeyse        ---> Obez
''')

boy = float(input("Boyunuzu (metre cinsinden) giriniz: "))
kilo = float(input("Kilonuzu (kg cinsinden) giriniz: "))

bki = kilo / (boy ** 2)

print(f"Beden Kitle İndeksiniz (BKİ): {bki:.2f}")

if bki < 18.5:
    print("Durum: Zayıf")
elif 18.5 <= bki < 25:
    print("Durum: Normal")
elif 25 <= bki < 30:
    print("Durum: Fazla Kilolu")
else:
    print("Durum: Obez")
