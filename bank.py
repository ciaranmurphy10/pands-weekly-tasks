# Request the user to enter an amount in cent and save it to the variable amount1. 
# This variable will be of type string, even if the user types an integer.
amount1 = input("Enter amount1(in cent): ") 

# Try to convert the amount to type int and save it to the variable amount1_int. 
amount1_int = int(amount1)

# Request the user to enter an amount in cent and save it to the variable amount2. 
# This variable will be of type string, even if the user types an integer.
amount2 = input("Enter amount2(in cent): ")

# Try to convert the amount to type int and save it to the variable amount2_int. 
amount2_int = int(amount2)

# Add the two integer amounts together and save the sum to the variable sum.
sum = amount1_int + amount2_int 

# Use floor division to find the euro amount of the cent amount. 
sum_euro_part = sum // 100

# Use modulo to find the cent amount of the cent amount.
sum_cent_part = sum % 100

# Use f strings to print the euro and cent amount in a human readable format. 
# :02d needs to be added to the cent part so that if the cent amount is a single digit, a leading 0 will be added. 
print(f"The sum of these is €{sum_euro_part}.{sum_cent_part:02d}")