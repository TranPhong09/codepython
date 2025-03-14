# Nhập năm từ bàn phím
nam = int(input("Nhập một năm dương lịch: "))

# Kiểm tra năm nhuận
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(nam, "là năm nhuận.")
else:
    print(nam, "không phải là năm nhuận.")
