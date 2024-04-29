import numpy as np
import matplotlib.pyplot as plt

# We can create a normal distribution using Numpy's random.normal() function.
# In Numpy terminology, loc is the mean, scale is the standard deviation, and size is the number of values. 
norm_dist = np.random.normal(loc=5, scale=2, size=1000)

# We can plot this using Matplotlib's hist() function. 
plt.hist(norm_dist, 
	alpha = 0.6, # Make our histogram slightly transparent. 
	color = "cornflowerblue", # Choose the fill colour of the bins
	edgecolor = "black", # Choose the edge colour of the bins
	linewidth = 0.5, # Choose the width of the edges of the bins
	label = "Normal Distribution, $N=1000$, $μ=5$, $σ=2$") # Choose the label text for the legend, using TeX to format the parameters. 

# To plot h(x)=x^3 for the range 0 to 10, we'll need to create two arrays. 
# The first will be a series of values from 0 to 10. 
# We'll use Numpy's linspace() function to do this, which returns an evenly spaced array of values between two values. 
# We'll generate 1000 values between 0 and 10. 
x_vals = np.linspace(0, 10, 1000)

# The second array will contain the cube of each value in our x_vals array. 
# Numpy makes it easy to do this in a number of ways. 
# We'll use the power() function which takes an array and returns an array of its values raised to a specified power. 
y_vals = np.power(x_vals, 3)

# To plot this, we'll use Matplotlib's plot() function, which plots x vs y. 
# We'll plot x_vals against y_vals.  
plt.plot(x_vals, y_vals,
	color = "darkslategray", # Choose the colour of the line.
	label = "$h(x) = x^3$.", # Use TeX to render our cubed equation for use in the legend. 
	linewidth = 0.8 # Choose the width of the line (or rather curve in our case). 
	)

plt.title("Histogram and Curve Plot") # Add a title.
plt.xlabel("X axis") # Add text to the x axis. 
plt.ylabel("Y axis") # Add text to the y axis. 
plt.legend() # Add a legend. Values will be taken from labels which we've already defined. 

# To display our plot, we'll us show().  
plt.show()