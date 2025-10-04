#keyword arguments = an argumnet preceded by an identifier
#                    helps with readability
#                    order of argument dosen't matter
#                    1. positional, 2. Default, 3. keywords, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", "Mr.","Anubhav", "Jha")

for x in range(1,11):
    print(x, end=" ")

print("1","2","3","4","5","6","7","8","9", sep ="-")