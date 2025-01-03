import random
a= "rock","paper","scissors"  
i=1
b=[] 
c=[]
d=[] 
while i !=0:
    b=input("enter ur answer(rock paper or scissors)\n")
    c=random.choice(a)
    print(f"I choose {c}")
    if b==c:
        print("its a draw")
    if c=="scissors":
        if b== "paper"  :
            print("I win")
        elif b== "rock"  :
            print("you win")
    if c== "rock"  :
        if b== "scissor"  :
            print("I win")
        elif b== "paper"  :
            print("you win")
    if c== "paper"  :
        if b== "rock"  :
            print("I win")
        elif b== "scissors"  :
            print("you win")
    d=input("wanna continue?reply in y or n for yes or no\n")
    if d== "y"  :
        i=1
    else:
        i=i-1
 



      
