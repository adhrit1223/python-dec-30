a=float(input("enter ur mrk:\t"))
if 0<=a and a<=100:
    if 80<=a and a<=100:
        print("distinction")
    elif 60<=a and a<=79:
        print("first division")
    else:
        print("fail")
else:
    print("wrong range")
