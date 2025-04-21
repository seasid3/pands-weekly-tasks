# bank.py
# This program asks the user to input two amounts in cent, adds them together and outputs the result in euro (with
# a decimal point).
# Author: Orla Woods

# ask the user to input two amounts in cent.
amount_1 = input("Enter amount 1 (in cent): ")
amount_2 = input("Enter amount 2 (in cent): ") 

# Add amount1 and amount2, converting them to integers from strings (I was getting this error before that: 
# TypeError: unsupported operand type(s) for /: 'str' and 'int'). 
answer = int(amount_1) + int(amount_2) 
# reference: https://www.datacamp.com/tutorial/how-to-convert-a-string-into-an-integer-in-python
  
# Divide the answer by 100 to convert it from cent to euro and round to 2 decimal places.
round_answer = round((answer / 100), 2)
# reference: https://stackoverflow.com/questions/70080676/how-do-i-print-cents-as-decimals
# reference: https://www.datacamp.com/tutorial/python-round-to-two-decimal-places

print(f"The sum of these is €{round_answer}") # using an f string to print the answer.

   