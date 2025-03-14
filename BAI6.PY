# Nhập điểm thi từ bàn phím
diem = float(input("Nhập điểm thi môn Tin: "))

# Xếp loại giải thưởng chỉ với if else
if diem >= 18:
    print("Giải Nhất")
else:
    if diem >= 16:
        print("Giải Nhì")
    else:
        if diem >= 14:
            print("Giải Ba")
        else:
            if diem >= 10:
                print("Giải Khuyến khích")
            else:
                print("Không đạt giải")
