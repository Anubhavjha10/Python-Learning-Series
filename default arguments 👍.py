#default arguments = A default value for certain parameters
#                    default is udes when that argument is omitted
#                    make your functions more flexible, reduces # of arguments
#                    1. positional, 2. Default, 3. keywords, 4. arbitrary

def net_price(list_price, discount, tax):
    return list_price * (1-discount) + (1 + tax)

print(net_price(500, 0, 0.05))
