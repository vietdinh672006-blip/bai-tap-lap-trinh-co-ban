ds = input("Nhập danh sách: ").split()

ds.remove('123')      # xóa phần tử có giá trị '123'

for ch in ds:
    print(ch)
