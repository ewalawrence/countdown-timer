# Countdown Timer

import time

myTime = int(input("Enter the time: "))

for x in reversed(range(1, myTime)):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's Up!!!")