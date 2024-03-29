import numpy as np
import matplotlib.pyplot as plt

# We can create a normal distribution using Numpy's random.normal() function.
# In Numpy terminology, loc is the mean, scale is the standard deviation, and size is the number of values. 
# Ref: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
norm_dist = np.random.normal(loc=5, scale=2, size=1000)

# We can plot this using Matplotlib's hist() function. 
# Ref: https://www.w3schools.com/python/matplotlib_histograms.asp
plt.hist(norm_dist)

# To plot h(x)=x^3 for the range 0 to 10, we'll need to create two arrays. 
# The first will be a series of values from 0 to 10. 
# We'll use Numpy's linspace() function to do this, which returns an evenly spaced array of values between two values. 
# We'll generate 100 values between 0 and 10. 
# Ref: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
x_vals = np.linspace(0, 10, 100)
print(x_vals)

# The second array will contain the cube of each value in our x_vals array. 
# Numpy makes it easy to do this in a number of ways. 
# We'll use the power() function which takes an array and returns an array of its values to a specified power. 
# Ref: https://numpy.org/doc/stable/reference/generated/numpy.power.html
y_vals = np.power(x_vals, 3)
print(y_vals)

# To plot this, we'll use Matplotlib's plot() function, which plots x vs y. 
# We'll plot x_vals agains y_vals.  
# Ref: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot(x_vals, y_vals)

# To display our plot, we'll us show().  
# Ref: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html
plt.show()