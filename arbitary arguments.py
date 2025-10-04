# *arg = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-argument
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. Arbitrary

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2,3,4,5,6))

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123",
              city="gharoli",
              state="delhi",
              zip="110096",
              country="India")