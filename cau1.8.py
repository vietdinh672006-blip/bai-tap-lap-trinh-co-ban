print("sinh vien : ho van viet")

print("ma so sv :245751030110099")

print("#############################")
a, b = 1, 2
total = 0
print(a,end=" ")
while (a <=4000000-1):
    if a % 2 == 0:
        total += a
    a, b = b, a+b
    print(a,end=" ")
print("\n sum of prime numbers term in fibonacci series: ",total)

