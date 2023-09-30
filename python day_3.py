#Problem Statement: Write a program that takes two numbers from the user and performs the following operations:

#Requirements:

#1. Add the two numbers and print the result.
# 2. Subtract the second number from the first number and print the result.
# 3. Multiply the two numbers and print the result.
# 4. Divide the first number by the second number and print the result.

x = int(input("enter first no."))
y = int(input("enter second no."))

add = x+y
sub = y-x
multiply = x*y
div = x/y

print(f"addition = {add}\n subtraction = {sub}\n multiply = {multiply}\n division = {div} ")


