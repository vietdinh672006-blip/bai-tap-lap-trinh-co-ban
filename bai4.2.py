a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

print(f"Nghịch đảo của các số tự nhiên trong khoảng ({a}, {b}):")

for i in range(a + 1, b):
    if i > 0:
        reciprocal = 1 / i
        print(f"1/{i} = {reciprocal:.6f}")
