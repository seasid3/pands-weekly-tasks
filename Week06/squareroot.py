# squareroot.py
# This program will take a positive floating-point number as an input and will output and approximation
# of its square root using Newton's method.
# Author: Orla Woods

# Theory of Newton's Method:
# looking at https://en.wikipedia.org/wiki/Newton%27s_method and TCD source: 
# https://calculus.domains.trincoll.edu/wp-content/uploads/2019/10/F19_131_Newton_s_Method_final.pdf  
# I understood that Newtowns method uses the formula to make sequential iterations which more closely 
# approximate the square root of a number as the number of iterations increase. 

# How to code Newton's Method in python:
# looking at https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/  and 
# https://math.stackexchange.com/questions/3524205/square-roots-by-newton-s-method
# to see how to do this in practice. In practice, the interations continue until the absolute value 
# of the root is less than the tolerance. 

# I copied the code from above (https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/) 
# into VS Code and ran it through Chatgpt, asking it to check the code. ChatGPT suggested several changes to
# the code, mainly how to define the tolerance and to better define the variables. 

# When I ran the code it gave 15 decimal places in the output, so I used the round() function
# https://www.w3schools.com/python/ref_func_round.asp
# After writing the code, I ran it through ChatGPT to check for errors and it suggested several changes 
# to improve readability and precision of the code: 
# https://chatgpt.com/share/6806aab8-4c48-800d-bd96-cdd0a3bacafc

a_number = float(input("Please enter a positive number: ")) # ask the user to provide the number

# Define a function sqrt to return the square root of a number using Newton's method:
def sqrt(a_number: float, tolerance: float = 1e-5) -> float: # function returns a float 

     # Adding a value error to make sure the user inputs a positive number:
     if a_number <= 0:
          raise ValueError("Please input a positive number.")

     # Define the initial guess for the square root
     x = a_number / 2    

     # Initialise the iteration count. Use 0 as a value to allow the iterations to start
     count = 0

     while True:
         count += 1 # keep iterating with the calculation..

          # Calculate a new approximation for the square root
         root = 0.5 * (x + (a_number/x))

         # check for closeness (based on the tolerance level). define when to stop the calculation
         if abs(root - x) < tolerance:
             break
         
         # Update guess for the next iteration
         x = root

     # Return the square root value rounded to 2 decimal places
     return round(root, 2) 

# Print the result 
print(f"The square root of {a_number} is approx. {sqrt(a_number)}")