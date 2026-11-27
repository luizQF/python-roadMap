import datetime
import time
import pygame
def display_program():
    print("-------------------------------")
    print("          ALARM CLOCK          ")
    print("-------------------------------")
    print("OPTIONS:\n")
    print("  1- TIMER")
    print("  2- ALARM")
    print("  3- EXIT\n")
    print("-------------------------------")
    return input("Option: ")

def timer():
  
    try:
        count = int(input("Set the timer in seconds: "))
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

def alarm():
    try:
        target_time = input("Enter the time you wanna wake up [xx:xx:xx]: ")
        current_time = datetime.datetime.now().strftime("%H:%M:%S") # convert to a string format
        
        while(target_time > current_time):
            current_time = datetime.datetime.now().strftime("%H:%M:%S") # convert to a string format
            print(current_time)
            time.sleep(1)
        print("WAKE UP!!!")
        time.sleep(4)
        #pygame.mixer.init()
        #pygame.mixer.music.load(sound_file)
        #pygame.mixer.music.play()
    except ValueError:
        print("Please enter a valid number")
    except KeyboardInterrupt:
        print("\nProgram Interrupt")

 
if __name__ == "__main__":
    is_running = True
    while(is_running):
        match display_program():
            case "1":
                timer()
            case "2": 
                alarm()
            case "3":
                is_running = False
                print("Program Finished")