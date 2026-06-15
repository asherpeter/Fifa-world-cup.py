#exercise 1 function that takes in input and calculates area of a rectangle
def area_of_rectangle(length, width):
    area = length * width
    return area

print(area_of_rectangle(5, 3)) 

#exercise 2 function that takes in input and calculates area of a circle
import math
def area_of_circle(radius):
    area = math.pi * radius ** 2
    return area
print(area_of_circle(4))


#exercise write a program demonstrating between a local and global variable
global_variable = "I am a global variable"
def demonstrate_variables():
    local_variable = "I am a local variable"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable

demonstrate_variables()