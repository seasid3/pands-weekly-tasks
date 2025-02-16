# accounts.py
# This program reads a 10 character account number and outputs the last 4 digits
# with Xs. It also does the same for an account number of n digits length 
# (where n>= 4)
# author: Orla Woods

'''
accountnumber = input("Please enter a 10 digit account number: ")
lastfourdigits = accountnumber[-4:]
securityaccountnumber = (f"Your account number is: XXXXXX{lastfourdigits}")
print(securityaccountnumber)

# I did the datacamp first few modules on python which teach about 
# how to name the place of an item in a list of things i.e. digit 7 in 10 or -4 for the same one.                          
# I am also getting help here as I code and I think that's co-pilot running
# I'm not taking all suggestions but trying to think myself and using co-pilot
# when i encounter a syntax error. trying to get to grips with when to use f 
# string
'''
# Extra task:

accountnumber = input("Please enter an account number of any length: ")
lastfourdigits = accountnumber[-4:]
firstdigits = accountnumber[:-4]

# i need to assign the last 4 digits as integers. using place assignment
# counting back from the end of the account number allows me to 
# use -4 position in any length of account number >= 4 digits long. the 
# struggle is how to replace n amount of numbers from the start of the a/c 
# number to position -4 with the same number of Xs as digits in that part of
# the a/c no. 
# i want to define the # range from 0 position to -4 as a string (I think?) 
# of n numberrs and replace this string with another string of n number of Xs.

'''
# action 1: I checked the type. The output of firstdigits is a string

print(type(firstdigits))

# action 2: I checked the length of the string firstdigits: 7 in an 
# 11 digit number so I am happy I have identified the first digits which are
# not the last 4 digits.

print(len(firstdigits))

# action 3: I am going to try to replace the string in the range [:-4] with Xs.
# function from w3schools

firstdigitsx = string.replace(firstdigits, "X", [0:-4])

# This did not work, it gave a sytax error. 
'''

# i asked co-pilot about the syntax error and it said i can't replace using 
# a range, to use the length (glad to realise I was on the right track with 
# length earlier). Everything I could find on W3schools was working with
# defined variables but not varying variable. 
# The approach of replacing for the length worked for a/c numbers of >= 4 digits
# Co-pilot helped write the # code as I was typing. I uesd a "+"" for the print
# between the n amount of Xs and the 4 end digits but took this out as a 
# plus appeared in # the output.

firstdigitsx = firstdigits.replace(firstdigits, "X" * len(firstdigits))
securityaccountnumber = (f"Your account number is: {firstdigitsx}{lastfourdigits}")
print(securityaccountnumber)
 
# That was a great fun! Tough but so satisfying to finally get it. Love the
# problem solving aspect of it and I am delighted to feel like I'm 
# properly coding! Thank you!


