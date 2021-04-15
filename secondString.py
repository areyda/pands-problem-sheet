# secondString.py
# Weekly Task 03 - secondString
# Author: Amy Reynolds

# References
# Ln 10 - https://www.w3schools.com/python/python_howto_reverse_string.asp - Reverse String [::-1]
# Ln 10 - https://stackoverflow.com/questions/58886774/python-how-do-i-reverse-every-other-string-in-a-list Reverse [::2]

# input string and reverse backwards as -1 to include every 2nd character
string = input("Please enter a sentence: ") [::-1][::2]
print (string)