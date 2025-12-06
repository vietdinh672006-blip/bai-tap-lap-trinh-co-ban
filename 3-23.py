s = input("Nhập câu: ")

so_chu_cai = 0
so_chu_so = 0

for ch in s:
    if ch.isalpha():
        so_chu_cai += 1
    elif ch.isdigit():
        so_chu_so += 1

print("Số chữ cái là:", so_chu_cai)
print("Số chữ số là:", so_chu_so)
