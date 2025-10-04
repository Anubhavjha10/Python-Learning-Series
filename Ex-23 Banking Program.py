# Banking Program

def show_balance(balance):
    print(f"your balance is ${balance:.2f}")

def deposit():
    amount = float(input("enter amount to deposit: "))

    if amount < 0:
        print("you cannot deposit negative amount")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("you cannot withdraw more than your balance")
        return 0
    elif amount < 0:
        print("Enter an valid Number")
        return 0
    else:
        return amount

def main():

    balance = 0
    is_running = True

    while is_running:
        print("*********************************")
        print("---------Banking Program---------")
        print("*********************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice")
    print("*********************************")
    print("    Thank You! Have a Nice Day   ")
    print("*********************************")

if __name__ == "__main__":
    main()