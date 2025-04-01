# This program will read in a text file (moby-dick.txt) and outputs the number of 'e's it contains. 
# Author: Orla Woods

# I found this very confusing. To start with, I took the messingwithfiles (txt files) code from week 
# 7 lecures (that I type as I listen to the lectures to make it go in!) and adapted it to
# create a file called moby-dick.txt. It did this but then I had no idea what to do (I used brown cow etc
# to make sure it was working and it was, the file was created. code commented out below)

'''
with open("moby-dick.txt", "w+") as f: # open in write mode and in text mode
      f.write("what the hell\n") # moby-dick.txt file doesnt exist yet but if i run es.py, it will
      f.write("brown cow\n")  # create the moby-dick.txt file. 
      f.seek(0) # i was at the end of the program so it didnt print higher info. so need this to go back to the 
      # beginning and print from there
      data = f.read()
      print(data)'

      # i had the file with the brown cow text but then i deleted this code as i didnt know where to go
      # from here
'''
# I asked chat GPT how to code what you were looking for, reading in the text in the weekly task in chatGPT. 
# The code provided seemed to work (although I used FILENAME instead of their filename as you had been using
# this) but was still reading in the how now brown cow text from the maby-dick.txt file I created above. 
# So I asked chatGPT "how do i get all the text from moby dick into moby-dick.txt" and it said i could do 
# this by saving a txt file directly from here: https://www.gutenberg.org/files/2701/2701-h/2701-h.htm
# or I could do it manually. As I had created the txt file already, I decided to do it manually. This didnt look
# great so then I went to https://www.gutenberg.org/ebooks/2701 and saved the plain text file to my 
# pands-weekly-tasks Week7 desktop folder and replaced the moby-dick.txt file I had created earlier.
# I got this message from both the manual and saving a txt file from the website when i ran
# "python es.py moby-dick.txt":
# "Error: An unexpected error occurred while processing the file: 'charmap' codec can't decode byte 0x9d 
#  in position 6742: character maps to <undefined>""
# I asked ChatGPT what was this error. It told me that this "indicates that there's an issue with character 
# encoding. This happens because the file you're trying to read contains characters that are not compatible
# with the default encoding used by Python on your system". It tole me to make sure this following text
# was included my code when reading the file (utf-8 is most common encoding for text files):
# "(encoding = 'utf-8' , errors ='ignore')"
# I removed the translator notes, notes from the publisher, etc. from the moby-dick.txt file to make it as 
# clean as possible  


import sys # allows access to some variables and functions that interact directly with the Python runtime 
# environment. Used to handle command-line arguments
import os # to use functions to interact with the operating system

def count_e_in_file(FILENAME): # defining the function count 'e' in file, taking an arg which is the name 
    # of a file (as a string). i.e. takes a filename as an input.
    try: # allows you to write code to handle errors. 
        if not os.path.exists(FILENAME): # make sure the file exists. function is from os module 
                       # and checks if a file exists at the specified path (FILENAME). 
                       # os.path.exists is True if the file exists. If "False" the following code executes:
             print("Error: The file does not exist.") # file cannot be found
             sys.exit(1) # terminates the program with an exit status code of 1. an exit status code of 
             # 0 indicates success but a non-zero code means an error occurred and the program exits. The
             # program won't continue running when a critical error (e.g. missing file) occurrs.
             
        # Open and read the file with explicit encoding
        with open(FILENAME, 'r', encoding = 'utf-8' , errors ='ignore') as f: # The first argument is the 
            # name (path)  of the file, read-only, using utf-8 to decode the moby-dick.txt file, ignore = any 
            # characters which can't be decoded are skipped instead of causing an error). File oject name is 
            # assigned to the variable f, which can be used in the with block.
            # when the with block is exited, the file is automatically closed. 
            total_e_count = 0 # initialising the count, starting at 0. It holds the running total of number of 
            # 'e's (lower and upper case) in the moby-dick.txt file
            for line in f: # iterate over "f", the file object. loops through the .txt file line-by-line until
                # all lines in the file have been processed.
                # count "e" and "E" in the current line
                total_e_count += line.lower().count('e') # "lower" converts all text to lower case, then 'e'
                # is counted. use of += means the count of 'e' from the current line is added to the running
                # total (total_e_count)
            
        #print the total of 'e' characters
        print(total_e_count)

    except Exception as e: # catches errors/exceptions during the execution of the code inside the try block.
        # if an error occurs in the try block, the program jumpts to the except block to handle the error.
        # "Exception" included all built-in exceptios in Python. Therefore, it handles unexpected errors.
        # "as e" allows you to access the details about the error.
         print(f"Error: An unexpected error occurred while processing the file: {e}")
         sys.exit(1)

def main(): # defining the main program
     # checking for command line arguments
     if len(sys.argv) != 2: # sys.argv is a list provided by the sys module that contains the
          # command-line arguments passed when running the Python script. sys.argv[0] is the script name (i.e. 
          # es.py). sys.argv[1] and beyond are additional args passed to the script (we expect the file
          # name). checking if the length is not equal to 2, check is the user did or didnt provide 
          # exactly one file name.
          print("Usage: python es.py <FILENAME>") # if exactly one argument isn't provided (the filename), the
          # usage message lets them know how to run the script properly
          sys.exit(1) #  if the number of args is incorrect, the line exits the program (as above) with an status
          # code of 1, indicating an error occurred. The programe stops running.
    
     FILENAME = sys.argv[1] # if the number of arguments is correct (exactly 2) the line takes the 
     # second arg (sys.arg[1] whihc is expected to be the name of the file "moby-dick.txt") and 
     # assigns it to the variable FILENAME
     
     # Check if the file ends with a .txt extension
     if not FILENAME.lower().endswith('.txt'):  
          print("Error: The file must have a .txt extension") # error if not a .txt gile
          sys.exit(1)

     # call the function to count 'e's
     count_e_in_file(FILENAME) # passes the FILENAME as an arg to the function.

# call the main function to start the program
main()

# to run this i need to enter the following in the terminal: python es.py moby-dick.txt

# This code:
# - checks if only one argument (the filename is provided)
# - if the argument count is wrong, displays useage message and exits
# - if the argument count is correct, assigns the filename to FILENAME and calls
# the count_e_in_file(FILENAME) function to process the file.

# To be totally clear again, I was absolutely stumped with this. I relied on chatGPT for all of the help
# as when I went to read the pyton files it was very complicated and I needed it explained explicitly to me.
# When I got the code working, I asked chatGPT to explain each line of code to me and that is where I got the
# notes. While I am able to type "python es.py moby-dick-txt" in the terminal and return a count on the 'e's 
# in the moby-dick.txt file I created (I am not sure which extra text I erased that you have in yours and
# I no longer have, but I don't think the actual number is what's important?), I really want to be upfront
# that I may never have been able to complete this task without chatGPT and I am on that knife edge of
# understanding/not understanding it