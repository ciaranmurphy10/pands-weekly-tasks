import datetime

# Using the datetime library, we can work out which day of the week it is today. 
# https://docs.python.org/3/library/datetime.html

# We'll use method chaining. 
# First we'll create a date object from the datetime library. 
# Then we'll use the today() method to find today's date. 
# Then we'll use the weekday() method to find the day of the week from today's date. 
# This will asign an integer to the today variable ranging from 0 to 6 where 0 represents Monday, etc.
today = datetime.date.today().weekday()

# Next we'll create a simple if statement to check if it's a weekday based on the day of the week. 
if today in range(0,5):
  weekday = True
else:
  weekday = False

# Finally, we'll use another if statement to print a string to print based on whether it's a weekday or not. 
if weekday:
  print("Back to work, it's a weekday!")
else:
  print("Take a hike, it's the weekend!")