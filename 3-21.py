s = input("Nhập chuỗi số nhị phân: ")
lst = s.split(',')

result = []

for b in lst:
    if int(b, 2) % 5 == 0:     # đổi sang thập phân và kiểm tra
        result.append(b)

print(",".join(result))
