nam_sinh_nam = int(input("Nhập năm sinh của người con trai: "))
nam_sinh_nu = int(input("Nhập năm sinh của người con gái: "))

# Tính tuổi vào năm 2025
tuoi_nam = 2025 - nam_sinh_nam
tuoi_nu = 2025 - nam_sinh_nu

# Kiểm tra điều kiện
dieu_kien_1 = (tuoi_nu > tuoi_nam + 1) or (tuoi_nam > tuoi_nu + 1)
dieu_kien_2 = (tuoi_nu >= 18) and (tuoi_nam >= 20)
dieu_kien_3 = (tuoi_nam + tuoi_nu) % 5 == 0

# Kết quả
if dieu_kien_1 and dieu_kien_2 and dieu_kien_3:
    print("Họ có thể kết hôn vào năm 2025.")
else:
    print("Họ KHÔNG thể kết hôn vào năm 2025.")
