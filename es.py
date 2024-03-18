import sys

def count_es(file_name):
  """
  This function will take a text file and count the number of e's in it. 

  Args:
    file_name (str): The name of the text file. It is assumed that this file will be in the same folder as the script. 

  Returns:
    int: The count of the number of e's in the text file. 
  """

  # Open the file and assign it to the variable file. 
  # Ref: https://www.w3schools.com/python/python_file_open.asp
  with open(file_name, "r") as file:

    # Read the text in the file, and assign it to the variable file_text. 
    # This will be a string. 
    file_text = file.read()

    # We don't know yet if there is an e in the file, so we start our count of e's at 0. 
    num_es = 0

    # Using a for loop we cycle through each letter in file_text.
    for letter in file_text:
      # If a letter is an e (lower or upper) we add 1 to our count of e's.
      if letter.lower() == "e":
        num_es += 1

    # Return the number of e's. 
    return num_es

# The sys module can be used to pass arguments when running a script. 
# Ref: https://www.geeksforgeeks.org/command-line-arguments-in-python/
  
# We will assume that only two arguments are passed when running this script, the python script name and the text file name in that order. 
# sys.argv will contain a list of arguments passed. 
# We'll use sys.argv[1] to index the second item in the list, which is our text file name. 
file_name = sys.argv[1]

# Run the count_es() function, taking the supplied file as an argument and print the result. 
print(count_es(file_name))
