nam_sinh = int(input("Nhập năm sinh: "))
ma_ghe = input("Nhập mã loại ghế (R, V, A, S): ").upper()

# Tính tuổi
tuoi = 2025 - nam_sinh

# Xác định giá vé
if tuoi < 12:
    gia_ve = 50000
if tuoi < 60:
    gia_ve = 100000
else:
    gia_ve = 80000

# Xác định phụ thu
if ma_ghe == "R":
    phu_thu = 0
if ma_ghe == "V":
    phu_thu = 10000
if ma_ghe == "A":
    phu_thu = 20000
else:
    phu_thu = 30000

# Tính tổng tiền
tong_tien = gia_ve + phu_thu

print("Tổng số tiền phải trả:", tong_tien, "đ")
