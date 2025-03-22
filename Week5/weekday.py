# This program will output if today is a weekday or not.
# Author: Orla Woods

# I had no idea where to start with this so I asked chatGPT how python can
# determine what day of the week it is without user input. It told me to 
# import the datetime module which allows you to work with dates and times

# import datetime module
import datetime

# It then told me to get the current date and time as follows:
currentDate = datetime.datetime.now()

# sanity check
# print(currentDate) - reverted to a comment when sanity check worked

# It then told me to get the day of the week as an integer 
# (0 = Monday, 6 = Sunday):
dayOfWeek = currentDate.weekday()

# sanity check
# print(dayOfWeek) - reverted to a comment when sanity check worked

# The chatGPT told me to define a list of weekday names
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# sanity check, using code proposed by chatgpt:
# print out day of the week
# print("Today is:", weekdays[dayOfWeek]) - reverted to 
# a comment when sanity check worked

# now I am going to insert a loop: this is going to output 
# "Yes, unfortunately today is a weekday." where an item from the 
# list weekdays[:5] is produced. It will say "It's the weekend, yay!" for
# the list weekdays[5:]. Again used chatGPT for help.

if dayOfWeek <5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It's the weekend, yay!")

# I wanted to write if dayOfWeek[:5] for the weekday output but I have learned 
# that you can't slice integers [dayOfWeek = currentDate.weekday() returns 
# integers] so you have to use a function "<5" that you can use for integers
# (days of weeks as 0 to 6 are not index positions but actual integers 
# - confusing but I can feel the penny dropping!)