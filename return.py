#return = statement used to end a function
#         and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def div(x, y):
    z = x / y
    return z

print(div(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("anubhav", "jha")
print(full_name)