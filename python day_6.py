# Write a program that takes two numbers as input from the user and performs division.
# Handle the potential division by zero error.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

try:
    division = num1 / num2
    print(f"{num1} divided by {num2} is {division}")  # if num2 is 0, this will raise an exception
except ZeroDivisionError:
    print("Cannot divide by zero") # this will only execute if the exception is raised
    