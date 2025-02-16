# accounts.py
# This program reads a 10 character account number and outputs the last 4 digits with Xs
# author: Orla Woods

'''
accountnumber = input("Please enter a 10 digit account number: ")
lastfourdigits = accountnumber[-4:]
securityaccountnumber = (f"Your account number is: XXXXXX{lastfourdigits}")
print(securityaccountnumber)
'''


# I have done the datacamp first few modules on python which teach about 
# how to name the place of an item in a list of things i.e. digit 7 in 10 or -4 for the same one.                          
# I am also getting help here as I code and I think that's co-pilot running
# I'm not taking all suggestions but trying to think myself and using co-pilot
# when i encounter a syntax error. trying to get to grips with when to use f string


accountnumber = input("Please enter an account number of any length: ")
lastfourdigits = accountnumber[-4:]

# i need to assign the last 4 digits as integers. using place assignment
# counting back from the end of the account number allows me to 
# use -4 position in any length of # account number. This will work for 
# all a/c numners >= 4 digits. the struggle is how to replace n amount 
# of numbers from the start of the # a/c number to position -4 with the 
# same number of Xs as digits in that part of the a/c no. i want to define the 
# range from 0 position to -4 as a string (I think?) of n numberrs and replace 
# this string with another string of n number of Xs, allowing n to vary per a/c
# no.
# action 1: I checked the type: the output of firstdigits is a string
# action 2: I checked the length of the string firstdigits: 7 in an 
# 11 digit number so I am happy I have identified the first digits which are
# not the last 4 digits.
# action 3: I am going to try to replace the string in the range [:-4] with Xs.
# This did not work. Lots of reading around the w3schools python tutorials to 
# try to understand how to replace a varying range of string with Xs. 
# I tried this replace and it gave a sytax error. i asked co-pilot and it 
# said i can't replace using a range, to use the length (I was on the right track
# checking this earlier). This worked for a/c numbers of >= 4 digits. Co-pilot 
# helped me write the code as I was tying. I uesd a "+"" for the print, between
# the n amount of Xs and the 4 end digits but took this out as a plus appeared
# in the output. 
# That was a great fun! Tough but so satisfying to finally get it. I feel like
# I'm properly coding and love it!  

firstdigits = accountnumber[:-4]
firstdigitsx = firstdigits.replace(firstdigits, "X" * len(firstdigits))

securityaccountnumber = (f"Your account number is: {firstdigitsx}{lastfourdigits}")
print(securityaccountnumber)

