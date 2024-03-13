# First, well create a function which takes in two arguments. 
# The first argument is the number which you want to find the square root of. 
# The second is the acceptable error. 

def sqrt(number, error, guess = 1):
  """
  """

  # First, we need to guess what the square root may be. 
  # If a guess is not supplied, the default value of 1 will be used. 

  sqrt_est = guess

  while number - (sqrt_est ** 2) > error:
    sqrt_est = 0.5 * (sqrt_est + (number / sqrt_est)))

