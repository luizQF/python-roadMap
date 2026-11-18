# nested loop = A loop within another loop. The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
        #print(x,y, end=" ")  # This will print the values of x and y on the same line, separated by a space

# It's often used for working with 2D data structures, such as lists of lists (a list of rows, where each row is a list of columns). For example, you can use nested loops to iterate through a 2D list and print its elements.