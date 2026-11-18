import time

my_time = int(input("Enter the countdown time in seconds: "))
# i did a counter instead of a countdown because it is easier to calculate the time remaining by subtracting the counter from the total time
for i in range(0, my_time, +1):
    seconds = i % 60
    minutes = (i // 60) % 60 # // -> int result which means the division result must be a integer (you could use type casting to int as well)
    hours = (i // 3600) % 24  # // -> int result which means the division result must be a integer (you could use type casting to int as well)
    print(f"{hours:02}:{minutes:02}:{seconds:02} -> {my_time - i} seconds remaining")
    time.sleep(1)  # Wait for 1 second
    


time.sleep(3)  # Wait for 3 seconds before starting the countdown

print("TIME'S UP!")