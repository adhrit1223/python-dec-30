print("this is a calculator")
a=float(input("enter first number:\t"))
c=(input("enter operator (+, -, /, *, ^): \t"))
b=float(input("enter second number:\t"))
if c=="*":
    print(f"{int(a)} * {int(b)} = {a*b}")
elif c=="/": 
     print(f"{int(a)} / {int(b)} = {a/b}")
elif c=="+":
     print(f"{int(a)} + {int(b)} = {a+b}")
elif c=="-": 
    print(f"{int(a)} - {int(b)} = {a-b}")
elif c=="^": 
     print(f"{int(a)} ^ {int(b)} = {a**b}")
else:
    print("the operator is invalid")
