# question 1
from turtle import width


def greet(name):
    print("Hello, " + name + "!")

# question 2
def personalized_greet(name, greeting):
    print(greeting + ", " + name + "!")
personalized_greet("Alice", "Good morning")

# question 3 
def square(num):
    return num ** 2
result = square(5)
print("The square of 5 is:", result)

# question 4
def rectangle_area(length, width):
    return length * width
result = rectangle_area(4, 5)
print("The area of the rectangle is:", result)

# question 5 
def apply_operation(function, number):
    return function(number)
def double(num):
    return num * 2 
result1 = apply_operation(double, 7)
print("The double of 7 is:", result1)
result2 = apply_operation(square, 3)
print("The square of 3 is:", result2)