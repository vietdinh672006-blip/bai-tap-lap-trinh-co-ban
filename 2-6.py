print("sinh vien : ho van viet")

print("ma so sv :245751030110099")

print("#############################")

def get_sum(*num):
    tmp=0
    #duyet cac tham so
    for i in num:
        tmp+=i
    return tmp
result=get_sum(1,2,3,4,5)
print(result)

