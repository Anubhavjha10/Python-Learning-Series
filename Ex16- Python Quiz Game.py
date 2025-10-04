# Python Quiz Game

questions = ("1. The image formed in a compound microscope is ",
             "2. The lens used in a simple microscope is ",
             "3. The elimination of toxic nitrogenous waste and excess water in man is by ",
             "4. The S. I. unit of refractive index is ",
             "5. The liquid metal is ")

options = (("A. erect","B. inverted","C. sometimes erect, sometimes inverted","D. None"),
          ("A. Concave","B. Convex","C. Cylindrical","D. None"),
          ("A. Excretion","B. Circulation","C. Reproduction","D. Pollution"),
          ("A. Meter","B. CM","C. Watt","D. No unit"),
          ("A. Bismuth","B. Magnesium","C. Mercury","D. Sodium"))

answers = ("B","B","A","D","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter the correct answer(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("-----------------")
print("      Result     ")
print("-----------------")

print ("answers: ", end = " ")
for answer in answers:
    print(answer, end = " ")
print()

print ("guesses: ", end = " ")
for guess in guesses:
    print(guess, end = " ")
print()

score = (score / len(questions) * 100)
print(f"Your Score is:{score}% ")