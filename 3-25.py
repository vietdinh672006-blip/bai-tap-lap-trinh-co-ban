s = input("Nhập danh sách số (cách nhau bởi dấu phẩy): ")

nums = [int(x) for x in s.split(',')]

odd = [str(x) for x in nums if x % 2 == 1]

print(",".join(odd))
