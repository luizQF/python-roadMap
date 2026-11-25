# Decorator = A function that extends the behavior of another function
# w/o modifying the base function
# pass the base function as an argumento to the decorator

def add_sprinkles(func):
    def wrapper(*args, **kwargs): # without the wrapper the program automatically call the function when apply a decorator
        print("Sprinkless added")
        func(*args, **kwargs)
    return wrapper

def add_flavor(func):
    def wrapper(*args, **kwargs): # it allow you to pass atributtes to the function.
        if args or kwargs:
            print("flavor added") 
        func(*args, **kwargs)
    return wrapper


@add_sprinkles 
@add_flavor
def get_ice_cream(flavor=None):
    print(f"Here is your {flavor + " " if not flavor == None else ""}icecream!")

get_ice_cream("Banana")
