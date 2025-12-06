n = int(input("Nhập n: "))

fib = [0, 1]

for i in range(2, n):
    fib.append(fib[-1] + fib[-2])

print(fib[:n])
