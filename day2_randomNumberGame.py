import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)

attempts = 0
guess = 0

while guess != secret_number: 
    guess = int(input("Make a guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else: 
        print(f"Correct! the number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts.")
