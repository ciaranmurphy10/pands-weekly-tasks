amount1 = input("Enter amount1(in cent): ")
amount2 = input("Enter amount2(in cent): ")

amount1_int = int(amount1)
amount1_int = int(amount1)

sum_in_cent = amount1_int + amount1_int 

sum_euro_part = sum_in_cent // 100
sum_cent_part = sum_in_cent % 100

print(f"The sum of these is €{sum_euro_part}.{sum_cent_part}")