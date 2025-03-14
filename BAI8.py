loai_phong = input("Nhập loại phòng (A, B, C): ").upper()
so_ngay = int(input("Nhập số ngày thuê: "))

if loai_phong == "A":
    don_gia = 300000
elif loai_phong == "B":
    don_gia = 250000
elif loai_phong == "C":
    don_gia = 200000

    print("Số tiền phải trả:", so_ngay * don_gia, "đ")
