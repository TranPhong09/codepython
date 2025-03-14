# Nhập vào 3 cạnh của tam giác
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra xem có phải tam giác hợp lệ không
if a + b > c and a + c > b and b + c > a:
    print("Ba cạnh này tạo thành một tam giác.")

    # Kiểm tra tam giác đều
    if a == b and b == c:
        print("Tam giác đều")
    else:
        # Kiểm tra tam giác vuông
        if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
            # Kiểm tra tam giác vuông cân
            if a == b or a == c or b == c:
                print("Tam giác vuông cân")
            else:
                print("Tam giác vuông nhưng không cân")
        else:
            # Kiểm tra tam giác cân
            if a == b or a == c or b == c:
                print("Tam giác cân nhưng không vuông")
            else:
                print("Tam giác thường")
else:
    print("Ba cạnh này không tạo thành một tam giác hợp lệ.")
