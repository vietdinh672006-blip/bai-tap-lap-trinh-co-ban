s = input("Nhập chuỗi: ")
kq = ""

for ch in s:
    if not ch.isdigit():   # nếu KHÔNG phải là số
        kq += ch

print(kq)
