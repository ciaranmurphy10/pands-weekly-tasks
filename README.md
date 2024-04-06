# 23-24: 8632 -- PROGRAMMING AND SCRIPTING. 

# Weekly Tasks

## Bank
### Task
>When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 
>
>Write a program called bank.py 
>
>The program should:
>
>Prompt the user and read in two money amounts (in cent)
>Add the two amounts
>Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
>
>`$ python bank.py`
>
>`Enter amount1(in cent): 65`
>
>`Enter amount2(in cent): 180`
>
>`The sum of these is €2.45`

### Discussion
This task requires the code to do a number of different things:
* Accept inputs from the user.
* Save them in the correct format. 
* Convert cent to euro. 
* Print a disriptive sentence. 

The trickiest part of this is the conversion from cent to euro. It may be tempting to simply divide the cent amount by 100, but this would lead to our amount being stored as a float since the output of division in Python is always a float. Due to how floating points are stored as binary in Python, this can lead rounding errors and other issues so it's best to avoid this. 

A safer way to do this calculation is to use floor division to divide our cent amount by 100, which discards the remainder and returns the result as an integer. This tells us how many times 100 fits into our cent amount (which could be 0 times). This is our euro amount. To get our cent amount, we use the modulo operator to find the remainder when dividing our original cent amount by 100. This gives us our cent amount. When we put these together, we get our original cent amount in euro and cent. 

An issue that you run into as a result of calculating the euro and cent amounts in this way is that if the cent amount is less than 10, it will natuarally display as a single digit. Since the standard format for displaying a euro and cent amount is to insert a leading 0 in front of the cent part in this situation, we can use string formatting to deal with this. 

### References
[https://www.w3schools.com/python/ref_func_input.asp](https://www.w3schools.com/python/ref_func_input.asp)

[https://www.geeksforgeeks.org/floating-point-error-in-python/](https://www.geeksforgeeks.org/floating-point-error-in-python/)

[https://www.geeksforgeeks.org/floor-division-in-python/](https://www.geeksforgeeks.org/floor-division-in-python/)

[https://realpython.com/python-modulo-operator/](https://realpython.com/python-modulo-operator/)

[https://www.w3docs.com/snippets/python/display-number-with-leading-zeros.html#google_vignette](https://www.w3docs.com/snippets/python/display-number-with-leading-zeros.html#google_vignette)

[https://realpython.com/python-f-strings/](https://realpython.com/python-f-strings/)

## Accounts
### Task
>Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
>
>Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
>
>`$ python accounts.py`
>
>`Please enter an 10 digit account number: 1234567890`
>
>`XXXXXX7890`

>Extra:
>Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

## Discussion
When the use enters their account number it will initially be stored as a string, but since strings are immutable and cannot be changed once they're created, we'll need to convert it to another type so that we can edit the last four digits. Lists are an ideal data type for manipulation, so we'll use the `list()` method to convert our string to a list. 

The `len()` function an then be used to determine the number of digits in the account number. We can then use a for loop to cycle through the digits of the account number, replacing each with an X up until the last four digit.

We can then convert our list back into a string using the `.join()` method.

## References
[https://python-forum.io/thread-15056.html](https://python-forum.io/thread-15056.html)

[https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/](https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/)

[https://www.w3schools.com/python/ref_func_list.asp](https://www.w3schools.com/python/ref_func_list.asp)

[https://realpython.com/len-python-function/](https://realpython.com/len-python-function/)

[https://www.w3schools.com/python/ref_string_join.asp](https://www.w3schools.com/python/ref_string_join.asp)

## Collatz

### Task
>Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
>
>At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
>
>Have the program end if the current value is one.
>
>Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).
>
>Example of it running:
>
>`$ python collatz.py`
>
>`Please enter a positive integer: 10`
>
>`10 5 16 8 4 2 1`

### Discussion
When this program is run, it will request the user to enter a positive integer. This will be stored as a string type so we'll convert it to an int type. We can then print it, as this will be the first value in the sequence.

We'll then use a while loop with nested if statement. The while loop checks if a condition is true (in this case, whether x is not equal to 1) and continually performs a task if this condition is met. As long as x is not 1, we use an if statement with the modulo operator to check if x is even or odd. Based on this, it is either divided by two or multiplied by 3. 

Once x becomes equal to 1, the while loop condition will not be satisfied anymore and the program will stop running.  

### References

[https://en.wikipedia.org/wiki/Collatz_conjecture#:~:text=The%20Collatz%20conjecture%20states%20that,years%20after%20receiving%20his%20doctorate.](https://en.wikipedia.org/wiki/Collatz_conjecture#:~:text=The%20Collatz%20conjecture%20states%20that,years%20after%20receiving%20his%20doctorate.)

[https://codereview.stackexchange.com/questions/285429/automate-the-boring-stuff-with-python-the-collatz-sequence#:~:text=Write%20a%20function%20named%20collatz,return%203%20*%20number%20%2B%201%20.](https://codereview.stackexchange.com/questions/285429/automate-the-boring-stuff-with-python-the-collatz-sequence#:~:text=Write%20a%20function%20named%20collatz,return%203%20*%20number%20%2B%201%20.)

[https://www.w3schools.com/python/python_while_loops.asp](https://www.w3schools.com/python/python_while_loops.asp)

[https://realpython.com/python-modulo-operator/](https://realpython.com/python-modulo-operator/)

## Weekdays

### Task
>Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
>
>You will need to search the web to find how you work out what day it is.
>
>An example of running this program on a Thursday is given below.
>
>$ python weekday.py
>Yes, unfortunately today is a weekday.
>
>
>An example of running it on a Saturday is as follows:
>
>`$ python weekday.py`
>
>`It is the weekend, yay!`

### Discussion

To work out what day of the week it is, we'll use the datetime module which can be imported at the start of our code. We'll chain together a number of methods operating on the date class from the datetime library to find out the current day of the week. 

Since the day of the week will be represented as an integer from 0 to 7, we'll use an if statement to check if it's a weekday (0, 1, 2, 3, or 4) or a weekend (5 or 6). 
 

### References
[https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/](https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/)

[https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)

[https://www.w3schools.com/python/ref_func_range.asp](https://www.w3schools.com/python/ref_func_range.asp)

## Square Root

### Task
>Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
>
>You should create a function called <tt>sqrt</tt> that does this.
>
>I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
>
>This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 
>
>This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.
>
>
`$ python squareroot.py`
>
>`Please enter a positive number: 14.5`
>
>`The square root of 14.5 is approx. 3.8.`

### Discussion
This program uses the Newton Raphson method for determining the square root of a number. This method uses a brute force iterative method for repeatedly approximating the square root of a number. It starts by using an initial guess (in our case, 1) and then iterating over a numerical method to get closer and closer to the square root until a desired level of accuracy is reached. 

To do this I've written a funciton which is a little bit more complicated than it needs to be for our purposes, since we won't be using custom errors or guesses when running the program. 

### References
[https://www.geeksforgeeks.org/newton-raphson-method/](https://www.geeksforgeeks.org/newton-raphson-method/)

[https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html](https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html)

[https://www.w3schools.com/python/python_functions.asp](https://www.w3schools.com/python/python_functions.asp)

## Counts e's
### Task
>Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
>
>The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
>
>Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.
>
>`$ python es.py moby-dick.txt`
>
>`116960`

### Discussion
This program opens a text file, reads the contents, and then counts how many e's there are in the text by iterating through each letter and checking if it's an e. 

The sys library can be used to read arguments which are given when running the program. 
 

### References
[https://www.w3schools.com/python/python_file_open.asp](https://www.w3schools.com/python/python_file_open.asp)

[https://www.geeksforgeeks.org/command-line-arguments-in-python/](https://www.geeksforgeeks.org/command-line-arguments-in-python/)

[https://stackoverflow.com/questions/43120555/for-loop-to-count-letters-in-a-word](https://stackoverflow.com/questions/43120555/for-loop-to-count-letters-in-a-word)

## Plot Task

### Task


### Discussion
 

### References
