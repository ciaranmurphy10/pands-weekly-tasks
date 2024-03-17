def sqrt(number, error = 0.01, guess = 1):
  """
  This function calculates the square root of a number to a desired level of accuracy. 

  Args:
    number (int, float): The positive number which you would like to find the square root of. 
    error: (float): The acceptable absolute difference between the square of our square root estimate and the original number. The default value is 0.01. 
    guess (int, float): The initial guess that the algorithm will use. This will default to 1 but if you have a better guess it may decrease computation time.

  Output:
    float: The estimated square root of the original number. 
  """

  # First, we need to guess what the square root may be. 
  # If a guess is not supplied, the default value of 1 will be used. 
  sqrt_est = guess

  # Next we'll use a while loop to continuously test whether our acceptable error has been met. 
  # If a desired error level has not been supplied, the default value of 0.01 will be used. 
  while abs(number - (sqrt_est ** 2)) > error:
    # If the acceptable error has not been met, we'll apply an iteration of the Newton-Raphson method.
    sqrt_est = 0.5 * (sqrt_est + (number / sqrt_est))
    # The square root estimate has now been updated so we will loop back around and test the error condition again. 

  # Once the error condition has been met, we'll return our square root estimate. 
  return sqrt_est

# Request the user for a positive number, convert it to a float, and save it to the variable number. 
number = float(input("Please enter a positive number: "))

# Calculate the square root using sqrt() and print a descriptive string. 
print(f"The square root of {number} is approx. {sqrt(number)}.")