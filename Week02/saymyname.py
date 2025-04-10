# saymyname.py
# This program is messing with inputs
# Author: Orla Woods

# ask the user to input their name and print "hello" with their name. Code from lectures.
name = input("Say your name: ")
print("Hello " + name)

# ask the user to input any number, turn it into an integer and multiply by 4. Oytput is the answer. 
# Code from lectures.
number= int(input("Enter a number:"))
answer = number * 4
print(f"The answer is {answer}") # in week 11 I have gone back and used am f string to insert a string  
# into the answer so it doesn't just print out the number alone.
