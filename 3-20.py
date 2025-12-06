print("sinh vien : ho van viet")

print("ma so sv :245751030110099")

print("#############################")

n = int(input("Nhập n: "))

for i in range(n):
    row = [1] * (i+1)
    for j in range(1, i):
        row[j] = prev[j-1] + prev[j]
    print(row)
    prev = row

