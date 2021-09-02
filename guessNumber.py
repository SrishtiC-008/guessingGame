import random
print("Number Guessing Game")
chances = 0
number = random.randint(1,9)
guess = int(input("Guess a number between 1 and 9: "))

while chances < 5:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations, you won")
        break
    elif guess < number:
        print("You are too low guess a higher number",guess)
    else:
        print("You are to high you need to guess lower",guess)

    chances += 1

if not chances < 5:
    print("You loose!!, the number is ",number)
     