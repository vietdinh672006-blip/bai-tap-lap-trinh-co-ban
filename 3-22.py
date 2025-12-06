output = []

for num in range(1000, 3001):
    s = str(num)
    if all(int(c) % 2 == 0 for c in s):
        output.append(s)

print(",".join(output))
