import time

my_time = int(input("Enter your Time in second: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = x // 60
    hours = x // 3600
    days = x // 86400
    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times Up!")