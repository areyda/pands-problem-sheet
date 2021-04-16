# collatz.py
# Weekly Task 04 - collatz.py
# Author: Amy Reynolds

# References
# Ln 9-21 - https://en.wikipedia.org/wiki/Collatz_conjecture - defining function

# Define the collatz function 
def f(number):
    # Using the modulo operator with a modulus of 2, to determine if the number is even
    # Return and divide the number by 2 (// is used to ensure that an integer value is outputted instead of a floating value)
    if (number%2) ==0:
        return (number//2)
    
    # Otherwise (in this case if the number is odd), return and multiply the number by 3 and add 1.
    else:
        return (3*number) +1   

def collatz(number):
    # Continue looping until the number = 1
    # Output the current value of the number 
    while number!=1:
        # Output current value of the number (inputted number)
        print (number)
        # Apply function to number as defined above
        number = f(number)
        # return number  or return 1 (in this case the value is 1 - outside of while loop) - avoids the return of None as an output 
    return (number)

# Request the user to input a positive integer
number = int(input("Enter a positive integer: "))
# Output values after function applied 
print (collatz(number)) 