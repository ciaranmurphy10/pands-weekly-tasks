# Request a 10 digit account number from the user..
acc_no = input("Please enter a 10 digit account number: ")

# Since strings are an immutable data type, we'll convert the account number into a list of characters using the list() function. 
acc_no_list = list(acc_no)

# Next we'll use a for loop to cycle through the first 6 elements of the list and replace them with "X"
for i in range(0,6): 
    acc_no_list[i] = "X"

# We can use the .join() method to convert the list back into a string.
acc_no_censored = "".join(acc_no_list)

# Finally, we'll print the censored account number.
print(acc_no_censored)

