a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))
c = int(input("Nhap so thu ba: "))
d = int(input("Nhap so thu tu: "))

# Tìm số lớn nhất
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
if d > max_val:
    max_val = d

# Tìm số nhỏ nhất
min_val = a
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
if d < min_val:
    min_val = d

# Sắp xếp theo thứ tự tăng dần (dùng if-else)
if a > b:
    a, b = b, a  # Đổi chỗ nếu a > b
if a > c:
    a, c = c, a  # Đổi chỗ nếu a > c
if a > d:
    a, d = d, a  # Đổi chỗ nếu a > d
if b > c:
    b, c = c, b  # Đổi chỗ nếu b > c
if b > d:
    b, d = d, b  # Đổi chỗ nếu b > d
if c > d:
    c, d = d, c  # Đổi chỗ nếu c > d

# In kết quả
print("So lon nhat:", max_val)
print("So nho nhat:", min_val)
print("Thu tu tang dan:", a, b, c, d)
