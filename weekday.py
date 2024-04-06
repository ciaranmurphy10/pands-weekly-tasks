import datetime

# Using the datetime library, we can work out which day of the week it is today. 

# We'll use method chaining. 
# First we'll create a date object from the datetime library. 
# Then we'll use the today() method to find today's date. 
# Then we'll use the weekday() method to find the day of the week from today's date. 
# This will asign an integer to the today variable ranging from 0 to 6 where 0 represents Monday, etc.
today = datetime.date.today().weekday()

# Next we'll create an if statement to check if it's a weekday based on the day of the week, and print a string based on whether it's a weekday or not. 
# Since the range function is not inclusive of the upper bound, we'll use range(0,5) to check if it's 0 to 4 (a weekday).
# If not, we can assume that it's either 6 or 7 (weekend). 
if today in range(0,5):
  print("Back to work, it's a weekday!")
else:
  print("Take a hike, it's the weekend!")