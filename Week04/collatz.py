# This program asks the user to input any positive integer and outputs the successive values of the following
# calculation: # At each step calculate the next value by taking the current value and, if it is even, 
# divide it by two, but if it is odd, multiply it by three and add one.
# The program ends if the current value is one.
# Author: Orla Woods

# Ask the user to input a positive integer

number = int(input("Please enter a positive integer: ")) 
# I got this on my own from lectures and labs # (looking back at the code)

# I knew I had to: check if the number is odd or even. First I tried to do this as standalone code but that
# was overcomplicating things and didnt work.  I wrote the general correct code (i.e., using while it's not 1, 
# if it's even divide by 2, if it's odd multiply by 3 and add 1) but I had overcomplicated it by definining 
# a new number.   It is confusing me that you use the same variable name throughout and dont have to redesignate
# a new variable. But also it does make sense as you need to use it in a loop so can't keep using new variable
# names at each itteration. 
# In the end, I copied the code I had written into chatgpt and it showed me my errors. I had absolutely
# overcomplicated it but was pleased to see that I had the general idea correct and i'm getting better at the 
# syntax as the weeks go on. 

while number != 1:
    if number % 2 == 0:
         number = number // 2
         print(number)
    else:
         number = number * 3 + 1
         print(number)

print("Got there in the end!")
