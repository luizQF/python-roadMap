temp = 25
is_raining = False

if is_raining: 
    temp = 18
if not is_raining: # you should use 'else', i'm using 'not' here just for notes. 
    temp = 25

if temp >= 19 and temp <= 25: 
    print("It is HOT outside.")
elif temp >= 0 and temp <= 18: 
    print("It is too cold.")
print(temp)