# weekday.py
# This program will output if today is a weekday or not.
# Author: Orla Woods

# Googling how to determine what day of the week it is without user input in python:
# https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python
# https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/
# Help from ChatGPT: https://chatgpt.com/share/680b862a-a638-800d-9c13-7ad88168ca38

# Import datetime module
import datetime

# Get the current date and time:
current_date = datetime.datetime.today()

# Sanity check
# print(current_date) # reverted to a comment when sanity check worked

# Get the day of the week (0 = Monday, 6 = Sunday):
day_of_week = current_date.weekday()

# Sanity check: 
# print(day_of_week) # reverted to a comment when sanity check worked

# Use an if/else statement to give an output depending on if the current day of the week is a weekday or a 
# weekend day. 
if day_of_week <5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It's the weekend, yay!")

# Fist, I wanted to write if dayOfWeek[:5] for the weekday output but this returned an
# error about not being able to slice integers [dayOfWeek = # currentDate.weekday() returns integers]. 
# I was also trying to assign a day name to the day_of_week but I didnt need to do this as the integer values 
# were all that were required.
# Asking ChatGPT (link above) why I need datetime.datetime.today() to get the current date and time, and 
#n not just datetime.today(), it explained that the I need to state the module name (datetime) as well as the
# class name (datetime) in the module, which allows me to access the today() function. Without both datetimes, 
# python wouldn't know if I was trying to reference the module or the class. I did try datetime.(today) and
# it returned an error "AttributeError: module 'datetime' has no attribute 'today'". This makes total sense
# to me now. 
