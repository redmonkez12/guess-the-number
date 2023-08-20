import random


player_name = input("What's your name?\n")

print(f"Hello {player_name}, let's get ready for the game. I am thinking a number between 1 and 20")

number = random.randint(1, 20)

MAX_TRIES = 3

while True:
    guesses_taken = 0

    while guesses_taken < MAX_TRIES:
        try:
            guess = input(f"Try to guess. Guess number: {guesses_taken + 1}\n")
            guess = int(guess)

            if guess < 0 or guess > 20:
                print("Choose the number in the range. Try it again!")
                continue
        except ValueError:
            print("Invalid number. Try it again!")
        else:
            guesses_taken += 1

            if guess < number:
                print("Your guess is small")

            if guess > number:
                print("Your guess is big")

            if guess == number:
                break

    if guess == number:
        print(f"Perfect, {player_name}. You won and you needed {guesses_taken} guess(es)")

    if guess != number:
        print(f"Don't worry, you can try it again! My number was: {number}")

    if not input("Do you want to play again?\n").lower().startswith("y"):
        break


# What's your name?
# Tomas
# Hello Tomas, let's get ready for the game. I am thinking a number between 1 and 20
# Try to guess. Guess number: 1
# 10
# Try to guess. Guess number: 2
# 22
# Try to guess. Guess number: 3
# 33
# Do you want to play again?
# n