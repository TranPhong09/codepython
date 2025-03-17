# Nhập năm sinh của từng người
nam_sinh_bac = int(input("Nhap nam sinh cua Bac: "))
nam_sinh_trung = int(input("Nhap nam sinh cua Trung: "))
nam_sinh_nam = int(input("Nhap nam sinh cua Nam: "))

# Tính tuổi tính đến năm 2025
tuoi_bac = 2025 - nam_sinh_bac
tuoi_trung = 2025 - nam_sinh_trung
tuoi_nam = 2025 - nam_sinh_nam

# Sắp xếp theo thứ tự tuổi giảm dần
if tuoi_bac >= tuoi_trung and tuoi_bac >= tuoi_nam:
    if tuoi_trung >= tuoi_nam:
        print("Thu tu tuoi giam dan:", "Bac Trung Nam")
    else:
        print("Thu tu tuoi giam dan:", "Bac Nam Trung")
else:
    if tuoi_trung >= tuoi_bac and tuoi_trung >= tuoi_nam:
        if tuoi_bac >= tuoi_nam:
            print("Thu tu tuoi giam dan:", "Trung Bac Nam")
        else:
            print("Thu tu tuoi giam dan:", "Trung Nam Bac")
    else:
        if tuoi_bac >= tuoi_trung:
            print("Thu tu tuoi giam dan:", "Nam Bac Trung")
        else:
            print("Thu tu tuoi giam dan:", "Nam Trung Bac")
