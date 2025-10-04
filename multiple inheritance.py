# multiple inheritence = inherit from more than one parent class
#                        C(A,B)

#multilevel inheritance = inherit from a parent which inherits from another parent
#                         C(B) <- A
class animal:
    pass
class Prey(animal):
    pass
    def flee(self):
        print("I'm flee")

class predator(animal):
    def hunt(self):
        print("I'm hunt")

class rabbit(Prey):
    pass

class hawk(predator):
    pass

class fish(Prey, predator):
    pass

rabbit = rabbit()
hawk = hawk()
fish = fish()

rabbit.flee()