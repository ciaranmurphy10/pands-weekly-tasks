# Request an account number from the user. The account number could be of any length.
# We'll assume that only the account number is entered, and no other text such as spaces or "My account number is...", etc.
acc_no = input("Please enter your account number: ")

# Since strings are an immutable data type, we'll convert the account number into a list of characters using the list() function. 
acc_no_list = list(acc_no)

# Since account numbers of varying lengths may be entered, we'll use the len() function to check the how many elements are in the list.
acc_no_len = len(acc_no_list) 

# Next we'll use a for loop to cycle through the elements of the list, stopping four elements short of the end, and replace them with "X".
for i in range(0, acc_no_len-4): 
    acc_no_list[i] = "X"

# We can use the .join() method to convert the list back into a string.
acc_no_censored = "".join(acc_no_list)

# Finally, we'll print the censored account number.
print(acc_no_censored)

