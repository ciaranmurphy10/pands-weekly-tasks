# First, well create a function which takes in two arguments. 
# The first argument is the number which you want to find the square root of. 
# The second is the acceptable error. 

def sqrt(number, error = 0.01, guess = 1):
  """
  """

  # First, we need to guess what the square root may be. 
  # If a guess is not supplied, the default value of 1 will be used. 

  sqrt_est = guess
  print(f"First guess: {sqrt_est}")
  print(f"First error: {(number - (sqrt_est ** 2))}")

  while abs(number - (sqrt_est ** 2)) > error:
    sqrt_est = 0.5 * (sqrt_est + (number / sqrt_est))

    print(f"Next guess: {sqrt_est}")
    print(f"Next error: {(number - (sqrt_est ** 2))}")

  print(f"Final guess: {sqrt_est}")

  return sqrt_est

x = sqrt(9, guess = 2.9)