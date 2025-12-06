print("sinh vien : ho van viet")

print("ma so sv :245751030110099")

print("#############################")
chuoi = input('Nhap chuoi: ')
ket_qua = ''                       

for ch in chuoi:
    if not ch.isdigit():          
        ket_qua += ch             

print('Chuoi sau khi loai bo chu so:', ket_qua)

