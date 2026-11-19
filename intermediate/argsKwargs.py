# *args = means argumentos, it allows you to pass multiple non-key arguments(inside tuples)
# **kwargs = means keyword arguments, it allow you to pass multiple keyword-arguments(inside dictionary)
# * unpacking operator

def add(a, b):
    return a + b # what if i want to pass more than two parameters?

def add2(*args): # it'll pack the arguments inside a touple
    total = 0
    for arg in args:
        total+=arg
    return total

    print(add2(1, 2, 3, 4)) # 10


def print_adress(**kwargs):
    for value in kwargs.values(): # Using dictionary methods to get the values.
        print(value)

print_adress(street="dik", # i'll pack those arguments in a dictionary.
            city="123",
            state="gg")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg)

    print(kwargs.get('city'))
    if "something" in kwargs:
        print("something exists!")
    else:
        print("something doesn't exist!")

shipping_label("luiz", "felipe", city="detroit", something="sidk")