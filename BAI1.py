a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))

# Tinh tong 
tong = a + b 
print("tong giua 2 so ", a, " va ", b, " la : ", tong)  

# Kiem tra tong co am khong 
if tong < 0: 
    print("Tong cua 2 so", a, "va", b, "la so am.")
else:
    if tong > 0:
        print("Tong cua 2 so", a, "va", b, "la so duong")
    else: 
        print("Tong cua 2 so", a, "va", b, "bang khong")


# Kiem tra xem 2 so do cung dau khong 
if a > 0 and b > 0:
    print(a, "va", b, "la 2 so cung duong")
else:
    if a < 0 and b < 0:
        print(a, "va", b, "la 2 so cung am")
    else: 
        print(a, "va", b, "la 2 so khac dau")


# Kiem tra xem 2 so cung chan, cung le hay khac loai 
if a % 2 == 0 and b % 2 == 0:
    print(a, "va", b, "la 2 so cung chan")
else: 
    if a % 2 != 0 and b % 2 != 0:
        print(a, "va", b, "la 2 so cung le")
    else:
        print(a, "va", b, "la 2 so khac loai")
