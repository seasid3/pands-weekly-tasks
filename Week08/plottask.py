# plottask.py
# This program will display a histogram of a normal distribution of 1000 values with a mean of 5 and a 
# standard deviation (SD) of 2. It will also define the function h(x)=x**3 in the range 0 to 10 
# and will plot both plots on the same set of axes.
# Author: Orla Woods

# Step 1: Import modules
import numpy as np
import matplotlib.pyplot as plt

# Step 2: 
# ask numpy to generate 1000 values which are normally distributed, have a mean of 5 and a SD of 2
# looking at Week 8 lactures, and https://realpython.com/numpy-random-normal/ and 
# https://numpy.org/doc/2.1/reference/random/generated/numpy.random.normal.html as well as
# https://pynative.com/python-get-random-float-numbers/#:~:text=Use%20the%20round()%20function,precision%20to%20two%20decimal%20places.
# to look at defining decimal places when randomly generating numbers (I had the 2 outside the round function
# but this cleared it up), I write:

# Randomly generate numbers for use in the histogram
np.random.seed(1) # from Week 8 lectures, use a seed so the numbers generated are the same each time 
# the program is run.
numbers = np.random.normal(loc=5, scale=2, size=1000) # random generation of 1000 numbers with
# mean (loc) of 5, SD (scale) of 2.

# Santiy check:
# print(numbers) # When it worked, plot the histogram:

# Step 3: write a function h(x)=X**3 in the range 0,10

# Define x as an array of numbers 1-10, inclusive
# https://numpy.org/doc/2.1/reference/generated/numpy.arange.html#numpy-arange
x = np.arange(1, 11) # starting at 1 but not including 11
# print(x) sanity check

# Step 4: define the function for the second plot
hx = x**3 
# print(hx) sanity check

# Step 5: Plot the histogram of random numbers
# Looking at https://numpy.org/doc/2.2/reference/generated/numpy.histogram.html to edit plot features.
plt.hist(numbers, bins = 50, color = "lime", edgecolor = "blue", linewidth = 1, linestyle = "-", label = "1000 random numbers") 
# large number of bins makes a smoother histogram

# Step 6: Plot the function h(x)=x**3 on the same plot
plt.plot(x, hx, linewidth = 2, color = "red", label = "$h(x) = x^3$") # $ is LaTex to get superscript 
# cubed (I knew I could do this from Ian's lectures)

# Step 7: define the plot features to make it look nice
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/shared_axis_demo.html#sphx-glr-gallery-subplots-axes-and-figures-shared-axis-demo-py
plt.xlim(-2.5, 15)
plt.ylim(0, 1000)
plt.title("Week 8 Task Plot")
plt.xlabel("x")
plt.ylabel("y = h(x)")
plt.legend()

# Step 8: Show
plt.show() # comment this out to save, and then comment save below out and show again.

# Save figure to file
# plt.savefig("plottask.png")

# I really enjoyed this task and was much more comfortable with it than the moby-dick task. The python script
# required to run this task seems much more intuitive to me