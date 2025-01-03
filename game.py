import random
print("This game tests your luck")
x = int(input("Pick a number between 1 to 10\n"))
y = random.randint(1, 10)
if 1 <= x <= 10:
        print("The number is:", y)
        if x == y:
            print("You lucky duck, you won!")
        else:
            print("Your bad luck is very bad, you lost!")
else:
        print("You didn't choose a number that is between 1 to 10.")

