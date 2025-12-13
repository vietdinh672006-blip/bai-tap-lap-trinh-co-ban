     print("sinh vien : ho van viet")

     print("ma so sv :245751030110099")
  
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


