# This program asks the user to input any positive integer and outputs the successive values of the following
# calculation: # At each step calculate the next value by taking the current value and, if it is even, 
# divide it by two, but if it is odd, multiply it by three and add one.
# The program ends if the current value is one.
# Author: Orla Woods

# Ask the user to input a positive integer, converting the inputted string to an integer.
number = int(input("Please enter a positive integer: ")) 
# I got this on my own from lectures and labs (looking back at the code)

# https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-23.php#google_vignette
# https://en.wikipedia.org/wiki/Collatz_conjecture
# https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence

# Coming back at this at the end of the lectures, using knowledge from later lectures, I wanted to insert a 
# loop to ensure that the program wouldn't run if the user entered an integer less than 1. 
# https://stackoverflow.com/questions/26748083/creating-a-loop-to-check-a-variable-to-make-sure-it-is-a-positive-integer
# https://www.reddit.com/r/learnpython/comments/yq7vkk/write_a_program_that_prompts_the_user_to_enter_an/?rdt=37874

# Use a while loop to ensure the user inputs a positive integer
# https://www.w3schools.com/python/python_while_loops.asp
while number <= 0:
    number = int(input("The input must be a positive integer. Please enter a positive integer: "))

# Doing the Collatz Conjecture, using a while loop
# My code wasn't working so I asked chatGPT: 
# https://chatgpt.com/share/68069acd-eba4-800d-a0e7-f3b55e95547a

while number != 1:
     if number % 2 == 0:
         number = number // 2
     else:
         number = number * 3 + 1
print(number)

print("Got there in the end!")
