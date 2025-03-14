a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))
c = int(input("Nhap so thu ba: "))

# Kiểm tra và sắp xếp theo thứ tự tăng dần
if a > b:
    a, b = b, a  # Đổi chỗ nếu a lớn hơn b
if a > c:
    a, c = c, a  # Đổi chỗ nếu a lớn hơn c
if b > c:
    b, c = c, b  # Đổi chỗ nếu b lớn hơn c

# In kết quả
print(a, b, c)
