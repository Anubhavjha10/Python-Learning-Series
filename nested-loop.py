#nested loop = A loop with in another loop (outter, inner)
#                        outer loop
#                           inner loop

for x in range(3):
    for y in range(1, 10):
        print(y, end = " ")
    print()
