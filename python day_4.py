#Problem Statement: Write a program that takes user input for their age and 
# prints different messages based on the following conditions:

#If the age is less than 18, print "You are a minor."
# If the age is between 18 and 65 (inclusive), print "You are an adult."
# If the age is greater than 65, print "You are a senior citizen."

age = int(input("your age?"))

if age < 18:
    print("You are a minor.")
elif 18 < age <65:
    print("You are an adult.")
if age > 65 :
    print("You are a senior citizen.")
