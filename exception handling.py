# exception handling = A event that interrupts the flow of a program
#                      (ZeroDivisionError, TypeError, ValueError)
#                      1. try,  2. except,  3. finally
try:
    numbers = int(input("Enter the number: "))
    print(1/numbers)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("You can't divide by word Motherfucker!")
except Exception:
    print("Something went wrong")
finally:
    print("The program is done")