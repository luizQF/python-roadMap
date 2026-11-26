import datetime
import time

def display_program():
    print("-------------------------------")
    print("          ALARM CLOCK          ")
    print("-------------------------------")
    print("OPTIONS:\n")
    print("  1- TIMER")
    print("  2- ALARM\n")
    print("-------------------------------")

def timer():
    count = int(input("Set the timer in seconds: "))
    try:
        
        if count > 0:
            for i in range(count, 0, -1):
                seconds = i % 60
                minutes = (i // 60) % 60
                hours = (i // 3600) % 24
                print(f"{hours:02}:{minutes:02}:{seconds:02}")
                time.sleep(1)
            print("WAKE UP!!!")
        else:
            print("The number must be higher than 0.")
    except ValueError:
        print("Please enter a valid number")
    except KeyboardInterrupt:
        print("\nProgram Interrupt")

def alarm(target_time):
    current_time = datetime.datetime.now().strftime("%H:%M:%S") # convert to a string format
    target_time = input("Enter the time you wanna wake up [xx:xx:xx]: ")

    while(target_time >= current_time):
        print(current_time)
    if(target_time <= current_time):
        print("WAKE UP!!!")
 
