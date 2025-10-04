# duck typing = another way to achieve polymorphysim besides Inheritance
#               object must have the minimum necessary attributes/methods
#               "If it looks a duck and quacks like a duck, it must be a duck"

class animal:
    alive = True

class dog(animal):
    def speak(self):
        print("Bhoo")

class cat(animal):
    def speak(self):
        print("Meow")


animal = [dog(), cat()]

for animal in animal:
    animal.speak()
    print(animal.alive)