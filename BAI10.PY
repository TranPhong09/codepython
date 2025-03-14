so_kwh = int(input("Nhập số kWh điện tiêu thụ: "))

# Tính tiền điện theo mức giá lũy kế
if so_kwh <= 50:
    tien_dien = so_kwh * 2000
elif so_kwh <= 100:
    tien_dien = (50 * 2000) + ((so_kwh - 50) * 2500)
else:
    tien_dien = (50 * 2000) + (50 * 2500) + ((so_kwh - 100) * 3000)

print("Số tiền phải trả:", tien_dien, "đ")
