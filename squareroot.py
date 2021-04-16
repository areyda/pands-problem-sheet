# squareroot.py
# Weekly Task 06 - squareroot.py
# Author: Amy Reynolds
# Purpose: Computing the square root for an inputted value using various functions


# Function 2 - Defining sqrt function 
# References 
# Ln #21 - Iterations - https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
# Ln #23 - Newton's Method Formula - https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# Ln #27 - Round to 2 decimal places - bmi.py weekly task 02

# Request the user to input a positive number
number = float(input("Enter a positive number : "))

# Defining the sqrt function and number of iterations applied, the more iterations, the more accurate the result output.
def sqrt(number, number_iters = 1000):
    # Inputted number to be square rooted 
    x = float(number)
    # loop through for number of iterations
    for i in range(number_iters): 
        # Newton's method - to determine square root of an number
        number = 0.5 * (number + (x / number))
    return number

# Output the square root of the inputted value, rounded to 2 decimal places
print ("The square root of",number, "is approx",(round(sqrt(number), 2)))


# Function - 1 - import math 
# Reference
# Ln #43 - Round to 2 decimal places - bmi.py weekly task 02

# Request the user to input a positive number
number = float(input("Please enter a positive number: "))

# Using the import math function
# Output the square root of the inputted value
import math
print("The square root of",number, "is approx", math.sqrt(number))

# Output the square root of the inputted value, rounded to 2 decimal places
print ("The square root of",number, "is approx",(round(sqrt(number), 2)))