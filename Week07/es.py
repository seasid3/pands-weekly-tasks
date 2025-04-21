# es.py
# This program will read in a text file (moby-dick.txt) and outputs the number of 'e's it contains. 
# Author: Orla Woods

# I found this very confusing. 
# To start with, I took the messingwithfiles (txt files) code from week 7 lecures (that I type as I listen to 
# the lectures) and adapted it to create a file called moby-dick.txt. It did this but then I had no idea what 
# to do (I used brown cow etc. to make sure it was working and it was, the file was created. Code commented
# out below)

'''
with open("moby-dick.txt", "w+") as f: # open in write mode and in text mode
      f.write("what the hell\n") # moby-dick.txt file doesnt exist yet but if i run es.py, it will
      f.write("brown cow\n")  # create the moby-dick.txt file. 
      f.seek(0) # I was at the end of the program so it didnt print higher info. so need this to go back to the 
      # beginning and print from there
      data = f.read()
      print(data)'

      # I had the file with the brown cow text but then i deleted this code as i didnt know where to go
      # from here
'''

# I asked chat GPT how to code what you were looking for reading in the text in the weekly task to chatGPT. 
# (https://chatgpt.com/share/6806c0a1-e9ec-800d-adf1-0d56fb4b211a), the code provided seemed to work but was 
# still reading in the how now brown cow text from the maby-dick.txt file I created above. 
# I then asked chatGPT "how do i get all the text from moby dick into moby-dick.txt" 
# (https://chatgpt.com/c/6806c0e2-a80c-800d-b843-1983716ec034) and it said i could do 
# this by saving a txt file directly from here: https://www.gutenberg.org/files/2701/2701-h/2701-h.htm
# As I had created the txt file already, I decided to do it manually. This didnt look
# great so I went to https://www.gutenberg.org/ebooks/2701 and saved the plain text file to my 
# pands-weekly-tasks Week7 desktop folder and replaced the moby-dick.txt file I had created earlier.
# I got this message from both the manual and saving a txt file from the website when I ran
# "python es.py moby-dick.txt":
# "Error: An unexpected error occurred while processing the file: 'charmap' codec can't decode byte 0x9d 
#  in position 6742: character maps to <undefined>""
# I asked ChatGPT what this error was. It told me that this "indicates that there's an issue with character 
# encoding. This happens because the file you're trying to read contains characters that are not compatible
# with the default encoding used by Python on your system". It tole me to make sure this following text
# was included my code when reading the file (utf-8 is most common encoding for text files):
# "(encoding = 'utf-8' , errors ='ignore')"
# I removed the translator notes, notes from the publisher, etc. from the moby-dick.txt file to make it as 
# clean as possible  

# Import sys module
import sys # Allows access to some variables and functions that interact directly with the Python runtime 
# environment. Used to handle command-line arguments
# Import the os module 
import os # To use functions to interact with the operating system

def count_e_in_file(filename): # Defining the function count 'e' in file, taking one argument (filename)
       # (as a string) and representing the path to a text file.
    try: # Allows you to write code to handle errors. 
        with open(filename, 'r', encoding = 'utf-8' , errors ='ignore') as f: # Attempts to open the file 
        # located at dilename in read only mode. File is read using UTF-8. Any characters which can't be 
        # decoded are skipped instead of causing an error. File oject name is assigned the variable f, 
        # which can be used in the with block. The with statenebt ebsures that the file is automatically closed
        # after the block is executed, even if the an error occurs.  
            contents = f.read() # Read entire content of the file into a variable (string) called contents.            # Count both lower and uppercase 'e'
            total_e_count = contents.lower().count('e') # Converts the contents to lowercase and counts the "e's"
            return total_e_count # returns the final count to the calling function (main())
    except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist.") # For when the file cannot be found.
            # The error message is printed and the program exits with a status code of 1 (error).
            sys.exit(1)
    except UnicodeDecodeError:
            print(f"Error: the file '{filename}' is not a valid UTF-8 text file.") # Catches errors that occur
            # if the file cannot be decoded using UTF-8. This can happen if the file is not a plain text file.
            sys.exit(1)
    except Exception as e: # Catches all other unexpected errors/exceptions during the execution of the code 
    # inside the try block. If an error occurs in the try block, the program jumps to the except block to 
    # handle the error (with a non-zero status code, indicating an error). "as e" allows you to access the 
    # details about the error.
            print(f"Unexpected error while reading the file: {e}")
            sys.exit(1)

# Define the main fuvtion to execute the script
def main(): 
     # Checking for command line arguments
     if len(sys.argv) != 2: # sys.argv is a list provided by the sys module that contains the
          # command-line arguments passed when running the Python script. sys.argv[0] is the script name (i.e. 
          # es.py). sys.argv[1] and beyond are additional args passed to the script (we expect the file
          # name). checking if the length is not equal to 2, checks if the user did or didnt provide 
          # exactly one file name (sys.argv[0] is the script name and sys.argv[1] is the filename).
          print("Usage: python es.py <filename>") # If exactly one argument isn't provided (the filename), the
          # usage message is displayed. This message tells the user how to run the script correctly.
          sys.exit(1) #  If the number of args is incorrect, the line exits the program (as above) with an status
          # code of 1, indicating an error occurred. The programe stops running.
            
     filename = sys.argv[1] # If the number of arguments is correct (exactly 2) the line takes the 
     # second arg (sys.arg[1] whihc is expected to be the name of the file "moby-dick.txt") and 
     # assigns it to the variable 'filename'           
            
     if not os.path.isfile(filename): # Make sure the file exists. function is from os module 
            # and checks if a file exists at the specified path (filename). 
            # os.path.exists is True if the file exists. If "False" the following code executes:
        print("Error: '{filename}' is not a valid file.") # File is not valid
        sys.exit(1) # Terminates the program with an exit status code of 1. An exit status code of 
             # 0 indicates success but a non-zero code means an error occurred and the program exits. The
             # program won't continue running when a critical error (e.g. missing file) occurrs.       
     
     # Count "e" and "E" in the current line using the counting function
     total_e_count = count_e_in_file(filename) 
            
     # Print the total of 'e' characters
     print(total_e_count)

# The script should only run main() when executed directly, not when imported as a module.
if __name__ == "__main__":
# Call the main function to start the program
    main()

# To run this I need to enter the following in the terminal: python es.py moby-dick.txt

# To be totally upfront again, I was absolutely lost with this. I relied on chatGPT for all of the help
# as when I went to read the python documentation it was very complicated and I needed it explained explicitly 
# to me. When I got the code working, I asked chatGPT to explain each line of code to me 
# (https://chatgpt.com/share/6806c0a1-e9ec-800d-adf1-0d56fb4b211a) and that is where I got 
# the comments from. While I am able to type "python es.py moby-dick-txt" in the terminal and return a count on 
# the 'e's in the moby-dick.txt file I created (I am not sure which extra text I erased that you have in yours 
# and # I no longer have, but I don't think the actual number is what's important?), I really want to be upfront
# that I may never have been able to complete this task without ChatGPT and I am on that knife edge of
# understanding/not understanding it.
