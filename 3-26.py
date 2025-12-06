total = 0

while True:
    s = input()
    if not s:
        break
    
    action, value = s.split()
    value = int(value)

    if action == 'D':
        total += value
    elif action == 'W':
        total -= value

print("Số dư cuối:", total)
