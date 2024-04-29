# Request the user to enter a positive integer (which will be saved as a string) and convert it to an integer. 
x = int(input("Please enter a positive integer: "))

# Check if x is a negative integer or 0. 
if isinstance(x, int) and x < 1:
  # Raise a ValueError if so. 
  raise ValueError("The inputted value must be a positive integer.")

# Print the first integer in the sequence.
print(x)

# Use a while loop to continually check if x is 1. Once x is equal to 1, the while loop will end.  
while x != 1:
  # First, check if x is even by checking if it is divisible by 2 using the modulo operator. 
  if x % 2 == 0:
    # If it is even, update x by dividing it by 2. 
    # This will convert it to a float, so we use int() to convert it back to an integer. 
    x = int(x / 2)
    # Print the new value of x.
    print(x)
  # If it is not even, we can assume that it is odd.
  else:
    # If it is odd, update x by multiplying it by 3 and adding 1. 
    x = (3 * x) + 1
    # Print the new value of x. 
    print(x)