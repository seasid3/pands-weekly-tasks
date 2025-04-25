# accounts.py
# This program reads in a 10 character account number and outputs the first 6 digits with Xs and shows the 
# last 4 digits. 
# Extra: It also does the same for an account number of n digits in length (where n >= 4)
# author: Orla Woods



# Task: ask the user to input a 10 digit account number.
# Revising this task at the end of the module, I have decided to use a while loop to ensure the
# user only inputs a 10 digit number, using the length function. 
# https://www.datacamp.com/tutorial/elif-statements-python
# https://www.w3schools.com/python/ref_func_len.asp
# I had to ask chatGPT to check my code and correct it: 
# https://chatgpt.com/share/68064053-6b28-800d-b835-e32d53e0e69b
# The task is commented out so that I can run the extra task below:
'''''
account_number = input("Please enter a 10 digit account number: ")
while len(account_number) != 10 or not account_number.isdigit():
    account_number = input("Invalid input. Please enter a 10 digit account number: ")
   
last_four_digits = account_number[-4:] 
security_account_number = (f"Your account number is: XXXXXX{last_four_digits}")
print(security_account_number)
'''

# Extra task: Adjust the code to work for an account number of any length >= 4 digits.
# I think I need to assign the last 4 digits as integers. Using place assignment, counting back from the end of 
# the # account number allows me to use -4 position in any length of account number >= 4 digits long. The 
# struggle is how to replace n amount of numbers from the start of the a/c number to position -4 with the same 
# number of Xs as digits in that part of the a/c number. I want to define the range from 0 position to -4 as a 
# string (I think?) # of n numberrs and replace this string with another string of n number of Xs.

account_number = input("Please enter an account number of any length: ")
last_four_digits = account_number[-4:]
first_digits = account_number[:-4]

# Action 1: I checked the type. 
# print(type(first_digits))
# The output of firstdigits is a string. 

# Action 2: I checked the length of the string first_digits: 7 in an 11 digit number so I am happy I have 
# identified the first digits which are not the last 4 digits.
# print(len(first_digits))

# Action 3: I am going to try to replace the string in the range [:-4] with Xs.
# first_digits_x = string.replace(first_digits, "X", [0:-4])
# https://www.w3schools.com/python/ref_string_replace.asp
# This did not work, it gave a sytax error (invalid syntax). 

# Asking ChatGPT, I sae I was on the right track using length:
# https://chatgpt.com/share/68063d6c-ea8c-800d-9793-676a87799fc5

first_digits_x = 'X' * len(account_number[:-4])
secure_account = first_digits_x + last_four_digits
print(secure_account)


