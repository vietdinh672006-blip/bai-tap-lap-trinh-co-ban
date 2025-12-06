print("Sinh vien: LE TRONG TRUNG")
print("Ma so SV : 245751030110070")
print("#############################")

str=input("Enter a String:")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print (dict)
