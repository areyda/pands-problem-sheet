# es.py
# Weekly Task 07 - es.py
# Author: Amy Reynolds
# Purpose: To display the number of "e" characters in that are being read from the modydick.txt.

# Reference: 
# Ln 13-16 - https://stackoverflow.com/questions/48885930/counting-specific-characters-in-a-file-python


with open ("mobydick.txt", "r") as f:
    data = f.read ()

    count = 0
    for i in data:
        if i.endswith("e"):
            count +=1
print (count)