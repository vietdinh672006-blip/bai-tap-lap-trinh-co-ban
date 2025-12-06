print("sinh vien : ho van viet")

print("ma so sv :245751030110099")

print("#############################")

s = input("Nhập chuỗi: ")
kq = ""

for ch in s:
    if not ch.isdigit():   # nếu KHÔNG phải là số
        kq += ch

print(kq)

