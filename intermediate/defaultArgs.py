# default arguments = A default value for certrain parameters
# default is used when that argument is omitted
# make yours functions flexible, reduces # of arguments
# 1. positional, 2. default, 3. keyword, 4. arbitrary
def net_price(list_price, discount = 0.2, tax = 0.1):

    return list_price * (1 - discount) * (1 + tax)

print(f"{net_price(500):.2f}")

import time

def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("done")

count(10)