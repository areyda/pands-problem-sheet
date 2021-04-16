# collatz.py
# Weekly Task 04 - collatz.py
# Author: Amy Reynolds

# References
# Ln 13-25 - https://www.reddit.com/r/Python/comments/57r6bf/collatz_conjecture_program/

# Request the user to input a positive integer
number = int(input ("Please enter a positive integer: "))

# Continue looping until the number = 1
    # Output the current value of the number 
while number!=1:
    print (number)
    # Using the modulo operator with a modulus of 2, to determine if the number is even
    # Divide the number by 2 (// is used to ensure that an integer value is outputted instead of a float)
    if (number%2) == 0:
        number = (number//2)
    # Otherwise (in this case if the number is odd), multiply the number by 3 and add 1.
    else:
        number= ((number*3)+1)
# Output number (in this case the value is 1 - outside of while loop)
print(number)