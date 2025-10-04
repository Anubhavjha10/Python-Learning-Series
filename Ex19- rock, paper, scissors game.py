import random

options = ("rock","paper","scissor")


while True:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice(Rock, Paper, Scissor): ").lower()

    print(f"You: {player}.")
    print(f"Computer: {computer}.")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("You win!")
    elif player == "paper" and computer == "scissor":
        print("You win!")
    elif player == "scissor" and computer == "rock":
        print("You win!")
    else:
        print("You lose! Computer wins!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if not play_again == "y":
        break

print("Thank you for playing!")