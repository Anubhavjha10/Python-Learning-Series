# Sloat Machine
import random

def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("***********")
    print("|".join(row))
    print("***********")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 8
        elif row[0] == '⭐':
            return bet * 15
    return 0




def main():
    balance = 100

    print("*********************************")
    print("    Welcome to Python Slots's    ")
    print("    Symbols: 🍒🍉🍋🔔⭐         ")
    print("*********************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance.")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning.....\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You Won ${payout}")
        else:
            print(f"You Lost ${payout}")

        balance += payout

        play_again = input("Would you like to play again? (Y/N): ").upper()

        if play_again != 'Y':
            break
    print("**************************************")
    print(f"Game Over. Your balance is ${balance}")
    print("**************************************")

if __name__ == "__main__":
    main()
