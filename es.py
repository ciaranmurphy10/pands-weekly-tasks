import sys

# Define a function called count_es() which accepts one argument.
def count_es(file_path):
  """
  This function will take a path to a text file and count the number of e's in it. 

  Args:
    file_path (str): The path to the text file. 

  Returns:
    int: The count of the number of e's in the text file. 
  """

  # Open the file and assign it to the variable file. 
  with open(file_path, "r") as file:

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
# We will assume that only two arguments are passed when running this script, the python script name and the path to a text file in that order. 
# sys.argv will contain a list of arguments passed. 
# We'll use sys.argv[1] to index the second item in the list, which is our text file path. 
file_path = sys.argv[1]

# Run the count_es() function, taking the supplied user path as an argument and print the result. 
print(count_es(file_path))
