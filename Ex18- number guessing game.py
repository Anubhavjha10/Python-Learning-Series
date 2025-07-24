# Python Number Guessing Game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)

guesses = 0
is_running = True

print("----Python Number GUessing Game----")
print(f"Select a number between {lowest_num} and {highest_num}.")

while is_running:
    guess = input("Guess a number =  ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That is not a number.")
            print(f"Please Select a number between {lowest_num} and {highest_num}.")
        elif guess < answer:
            print(f"Your guess is too low.")
        elif guess > answer:
            print(f"Your guess is too high.")
        else:
            print(f"Your guess is correct! The answer is {answer}.")
            print(f"You have {guesses} guesses left.")
            is_running = False
    else:
        print("That is an out of range number.")
        print(f"Please Select a number between {lowest_num} and {highest_num}.")

