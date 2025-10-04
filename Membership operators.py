# Membership Oprerators = used to test wheather a value or variable is found in a sequence
# (string, list, tuple, set or dictionary)
#                   1. in
#                   2. not in

#word = "Apple"
#letter = input("Guess a letter in the secret word: ")
#if letter in word:
#    print(f"There is a {letter} in the secret word.")
#else:
#    print(f"There is no {letter} in the secret word.")

# for not in example
word = "Apple"
letter = input("Guess a letter in the secret word: ")
if letter not in word:
    print(f"There is no {letter} in the secret word.")
else:
    print(f"There is a {letter} in the secret word.")


email = input("Enter your email: ")

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")