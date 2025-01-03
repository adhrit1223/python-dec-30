b=input("enter number(integer):\t")
d=b.isnumeric()
if d==True:
    a=input("enter the times:\t")
    f=a.isnumeric()
    if f==True:
        x= int(b)
        y=int(a)
        for i in range(1,x+1,1):
            for j in range(1,y+1,1):
                print(f"{i}x{j}={i*j}")
                if j==y:
                    print("\n")
                
    else:
           print("invalid input")
else:
    print("invalid input")
    
    
