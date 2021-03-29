# collatz.py
# Weekly Task 04 - collatz.py
# Author: Amy Reynolds

numbers = []

number= int(input ("Please enter a number: "))

if (number%2) == 0:
    print(int(number/2),(numbers))

else:print(int(number*3+1),(numbers))

print(numbers)