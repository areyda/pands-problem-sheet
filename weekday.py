# weekday.py
# Weekly Task 05 - weekday.py
# Author: Amy Reynolds
# Purpose: To determine if today is a weekday or if it's the weekend. 

# Reference: 
# Ln 13, 17:
# https://www.codegrepper.com/code-examples/python/python+get+current+week+day
# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
# https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday

# Import the datetime module for date objects 
import datetime

# If the weekday is greater or equal to 5 ((Saturday (int 5) or Sunday (int 6)))
# Display the following string 
if (datetime.datetime.today().weekday()) >=5:
    print ("It is the weekend, yay!")

# Otherwise, display the string below
else:
    print("Yes, unfortunately today is a weekday.")

