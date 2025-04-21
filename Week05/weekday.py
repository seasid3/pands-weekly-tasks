# This program will output if today is a weekday or not.
# Author: Orla Woods

# Googling how to determine what day of the week it is without user input in python:
# https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python
# https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/
# Help from ChatGPT: https://chatgpt.com/c/68069f62-4914-800d-8a49-3694d5b79891

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

# Define a list of weekday names
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Sanity check: print out day of the week
# print("Today is:", weekdays[day_of_week]) # reverted to # a comment when sanity check worked

# Use an if/else statement to give an output depending on if the current day of the week is a weekday or a 
# weekend day. 
if day_of_week <5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It's the weekend, yay!")

# Fist, I wanted to write if dayOfWeek[:5] for the weekday output but this returned an
# error about not being able to slice integers [dayOfWeek = # currentDate.weekday() returns integers]. 