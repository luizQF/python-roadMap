# module = a file containing code you want to incluse in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files.

#print(help("modules"))

#import math
#import math as m
from math import pi

a, b, c ,d = 1, 2, 3, 4

print(pi ** a)

import modules.ex_module as math2

result = math2.pi
result = math2.square(3)
print(result) 

