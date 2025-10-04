#logical operators = "or" "and" "not"
#or = at least one condition must be true
#and = both condition must be true
#not = inverts the condition (not False, not True)

#Example of "or"

temp = 20
is_raining = True

if temp >35 or temp < 0 or is_raining:
    print("The Event is Canceled due to inconsistency temprature")
else:
    print("The Event is successfully scheduled")

#Example of "and"

age = 18
is_smoking = False

if age >= 18 and is_smoking:
    print("You are eligible for smoking")
else:
    print("You are not eligible for smoking")

#Example of "not"
umar = 17
has_permission = False

if not (umar < 18 or has_permission):
    print("Access granted!")  # Output: Access granted!
else:
    print("Access denied!")
