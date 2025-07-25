import time

def count(end, start = 1):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(5)