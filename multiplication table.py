b=input("enter number(integer)")
d=b.isnumeric()
c=[1,2,3,4,5,6,7,8,9,10]
if d==True:
    for i in c:
        a=int(b)
        print(f"{a}x{i}={a*i}")
        if i==10:
            break
else:
    print("invalid input")
    
    
