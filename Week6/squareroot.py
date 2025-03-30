# This program will take a positive floating-point number as an input and will output and approximation
# of its square root using Newton's method.
# Author: Orla Woods


# Theory of Newton's Method:
# looking at https://en.wikipedia.org/wiki/Newton%27s_method and TCD source 
# here https://calculus.domains.trincoll.edu/wp-content/uploads/2019/10/F19_131_Newton_s_Method_final.pdf  
# I understood that Newtowns method uses the formula to make sequential iterations which more closely 
# approximate the square root of a number as the number of iterations increase. 

# How to code Newton's Method in python:
# looking at https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ 
# to see how to do this in practice. In practice, the interations continue 
# until the absolute value of the root is less than the tolerance. 

# I copied the code from above (https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/) 
# into VS Code and ran it through Chatgpt, asking it to check the code. ChatGPT suggested several changes to
# the code, mainly how to define the tolerance and to better define the variables. 

# When I ran the code it gave 15 decimal places in the output, so I asked chatgpt how to make sure the 
# output was one decimal place. This gave me the round function which we used before but I couldn't 
# remember how to define the number of decimal places. The following code was what I finished with.



# Using a function to return the square root of a number using Newton's method:

def sqrt(number, tolerance=1e-5):
    
    # define the initial guess for the square root
    x = number

    # to count the number of iterations. need a value to allow the iterations to start, use 0
    count = 0

    while True:
         count += 1 # keep iterating with the calculation..

         # Calculate the approximation for the square root
         
         root = 0.5 * (x + (number/x))

         # check for closeness (based on the tolerance level). define when to stop the calculation
         if (abs(root - x) < tolerance):
              break
         
         # Update root
         x = root
    
    return round(root, 1) # return the answer to 1 decimal place

number = float(input("Please enter a positive number: ")) # ask the user to provide the number
print(f"The square root of {number} is approx. {sqrt(number)}")