# What is function?
# A function is a block of code that runs only when it is called.

# Why use functions?
# 1. Avoid repeating code.
# 2. Make program clean and organized.
# 3. easy to debug and reuse.

# syntax of function
# def function_name(parameters):
#     code to execute

# Example
# def greet():
#     print("Hello students")
# greet()  # calling the function

# ---------------------------------------------------------------------------------------

# Function with parameters
# def greet(name):
# def greet(name="Shruti"): # default parameter
#     print(f"Hello {name}")
# greet() # function call without argument, it will use default parameter value
# greet("naiya")

# ---------------------------------------------------------------------------------------
# Function with return value
# Used when we want to send result back

# def add(a, b):
#     return a + b

# result = add(2, 3)
# print(result)  

# ---------------------------------------------------------------------------------------

# Task 1 : create a function to calculate and return result
num1 = float(input("enter the number1"))
num2 = float(input("enter the number2"))
op = (input("enter the operator(+,-,*,/)"))
def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2 
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    result = calculate(num1,num2,op)
    print(f"result is {result}") 




# Task 2 : Create a function to check if a number is even or odd

# num = int(input("Enter a number: "))
# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# result = even_odd(num)
# print(result)

# Task 3 : Create a function to calculate the factorial of a number using for loop
# num = int(input("Enter a number: "))
# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     return fact
# result = factorial(num)
# print(result)

# second way using recursion
#num = int(input("Enter a number: "))
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)   
# result = factorial(num)
# print(result)
#
# Task 4 : create a function to find maximum of three numbers
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))        
# def find_max(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# result = find_max(num1, num2, num3)
# print(f"The maximum number is: {result}")

# Task 5 : create a function to check if a string is palindrome or not using join and reverse methods
# text = input("Enter a string: ")
# def is_palindrome(text):
#     reversed_text = ''.join(str(reversed(text)))
#     if text == reversed_text:
#         return "Palindrome"
#     else:
#         return "Not Palindrome"
# result = is_palindrome(text)
# print(result)

# Task 6 : create a function to calculate the area of a circle 

# radius = float(input("Enter the radius of the circle: "))
# def area_of_circle(radius):
#     area = 3.14 * radius * radius
#     return area
# result = area_of_circle(radius)
# print(f"The area of the circle is: {result}")