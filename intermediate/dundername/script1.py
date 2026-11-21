# this script can be imported or run standalone functions and classes in this module can be reused without the main block of code executing


def favorite_food(food):
    print(f"favorite food: {food}")
    
def mainAlt():
    print("This is script1")

if __name__ == '__main__':
    mainAlt()
else:
    print(f"imported script: {__name__}")
