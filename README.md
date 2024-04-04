## Description
This repository contains the weekly tasks for the module 23-24: 8632 -- PROGRAMMING AND SCRIPTING. 

## Weekly Tasks
### Week 1 
Week 1 did not contain a programming task.

### Week 2
#### Task
>When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 
>
>Write a program called bank.py 
>
>The program should:
>
>Prompt the user and read in two money amounts (in cent)
>Add the two amounts
>Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
>$ python bank.py
>Enter amount1(in cent): 65
>Enter amount2(in cent): 180
>The sum of these is €2.45

#### Discussion
This task requires the code to do a number of different things:
* Accept inputs from the user.
* Save them in the correct format. 
* Convert cent to euro. 
* Print a disriptive sentence. 

The trickiest part of this is the conversion from cent to euro. It may be tempting to simply divide the cent amount by 100, but this would lead to our amount being stored as a float since the output of division in Python is always a float. Due to how floating points are stored as binary in Python, it's best to avoid this. 

A safer way to do this calculation is to use floor division to divide our cent amount by 100, which discards the remainder and returns the result as an integer. This tells us how many times 100 fits into our cent amount (which could be 0 times). This is our euro amount. To get our cent amount, we use the modulo operator to find the remainder when dividing our original cent amount by 100. This gives us our cent amount. When we put these together, we get our original cent amount in euro and cent. 

An issue that you run into as a result of calculating the euro and cent amounts in this way is that if the cent amount is less than 10, it will natuarally display as a single digit. Since the standard format for displaying a euro and cent amount is to insert a leading 0 in this situation, we can use string formatting to deal with this. 

#### References
[https://www.w3schools.com/python/ref_func_input.asp](https://www.w3schools.com/python/ref_func_input.asp)
[https://www.geeksforgeeks.org/floating-point-error-in-python/](https://www.geeksforgeeks.org/floating-point-error-in-python/)
[https://www.w3docs.com/snippets/python/display-number-with-leading-zeros.html#google_vignette](https://www.w3docs.com/snippets/python/display-number-with-leading-zeros.html#google_vignette)
[https://realpython.com/python-f-strings/](https://realpython.com/python-f-strings/)