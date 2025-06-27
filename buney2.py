print('''
Not Hesaplama Sistemi:
-----------------------
- Vize1: Toplam notun %30'u
- Vize2: Toplam notun %30'u
- Final: Toplam notun %40'ı

Harf Notu Karşılıkları:
------------------------
90 ve üzeri      --> AA
85 - 89 arası     --> BA
80 - 84 arası     --> BB
75 - 79 arası     --> CB
70 - 74 arası     --> CC
65 - 69 arası     --> DC
60 - 64 arası     --> DD
55 - 59 arası     --> FD
0  - 54 arası     --> FF
''')

vize1 = float(input("1. Vize Notunuzu Giriniz: "))
vize2 = float(input("2. Vize Notunuzu Giriniz: "))
final = float(input("Final Notunuzu Giriniz: "))

toplam_not = (vize1 * 0.30) + (vize2 * 0.30) + (final * 0.40)

print(f"Toplam Notunuz: {toplam_not:.2f}")

# Harf notu belirlenir
if toplam_not >= 90:
    print("Harf Notu: AA")
elif toplam_not >= 85:
    print("Harf Notu: BA")
elif toplam_not >= 80:
    print("Harf Notu: BB")
elif toplam_not >= 75:
    print("Harf Notu: CB")
elif toplam_not >= 70:
    print("Harf Notu: CC")
elif toplam_not >= 65:
    print("Harf Notu: DC")
elif toplam_not >= 60:
    print("Harf Notu: DD")
elif toplam_not >= 55:
    print("Harf Notu: FD")
else:
    print("Harf Notu: FF")
