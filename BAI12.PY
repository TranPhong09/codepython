nam_sinh = int(input("Nhập năm sinh: "))

# Xác định Thiên Can
can = nam_sinh % 10
if can == 0:
    can_str = "Canh"
if can == 1:
    can_str = "Tân"
if can == 2:
    can_str = "Nhâm"
if can == 3:
    can_str = "Quý"
if can == 4:
    can_str = "Giáp"
if can == 5:
    can_str = "Ất"
if can == 6:
    can_str = "Bính"
if can == 7:
    can_str = "Đinh"
if can == 8:
    can_str = "Mậu"
if can == 9:
    can_str = "Kỷ"

# Xác định Địa Chi
chi = nam_sinh % 12
if chi == 0:
    chi_str = "Thân"
if chi == 1:
    chi_str = "Dậu"
if chi == 2:
    chi_str = "Tuất"
if chi == 3:
    chi_str = "Hợi"
if chi == 4:
    chi_str = "Tý"
if chi == 5:
    chi_str = "Sửu"
if chi == 6:
    chi_str = "Dần"
if chi == 7:
    chi_str = "Mão"
if chi == 8:
    chi_str = "Thìn"
if chi == 9:
    chi_str = "Tỵ"
if chi == 10:
    chi_str = "Ngọ"
if chi == 11:
    chi_str = "Mùi"

print("Năm", nam_sinh, "là năm", can_str, chi_str)
