#for loops = execute a block of code a fixed number of times.
# You can inerate over a range, string, sequence, etc...

for x in range(1, 11):
    if x % 2 == 0:
        continue
    else:
        print(x)