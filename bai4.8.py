ds = input('Nhap day tu: ').split()  
max_len = max(len(tu) for tu in ds)
tu_dai_nhat = [tu for tu in ds if len(tu) == max_len]

print('Cac tu dai nhat:')
for tu in tu_dai_nhat:
    print(tu)
