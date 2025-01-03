import random
a = random.randint(1, 100)
chances = 10
print("guess a number between 1 and 100")
print("You have 10 chances to guess it")
while chances > 0:
    guess = int(input("guess: \n"))
    chances -= 1
    if guess < a:
        print("guss higher You have {chances} chances left")
    elif guess > a:
        print("guess lower You have {chances} chances left")
    else:
        print("Congratulations! You guessed the number in {10 - chances} attempts")
        break
else:
        print("Sorry, you've run out of chances. The number was {a}")

  
