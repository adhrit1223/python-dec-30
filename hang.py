import random
a = ["dog", "cat", "bat"]
b = random.choice(a)
tukka = []
lives = 6
while lives > 0:
    d = []
    for c in b:
        if c in tukka:
            d.append(c)  
        else:
            d.append("_")
    print("Word:", " ".join(d))
    if "_" not in d:
        print("You win!")
        break
    guess = input("Enter a letter: ").lower()

    if guess in tukka:
        print("You already guessed that letter.")
    elif guess in b:
        print("Good guess!")
        tukka.append(guess)  
    else:
        print("Wrong guess!")
        tukka.append(guess) 
        lives -= 1 
        print(f"Wrong, {lives} lives remaining.")
if lives == 0:
    print("You win in your dreams, but not here. Victory chases you, but you have always outrun it.")
