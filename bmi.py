# bmi.py
# Weekly Task 02 - BMI Calculation 
# Author: Amy Reynolds 

# request person's height in centrimeters 
# int - converts string that inputted into to an integer
height = int(input ("enter your height (cm):? "))
print ("your height (cm) is {} " .format (height))

# request person's weight in kg         
weight = int(input ("enter your weight (kg):?"))
print ("your weight (kg) is {} " .format (weight))  

# BMI Calculation (kg/m^2)
BMI = weight / (height/100)**2

# BMI Calculation Result Output (weight / height)
print ("your BMI is {} " .format (BMI)) 


# References
# LN 15 - https://www.includehelp.com/python/bmi-body-mass-index-calculator.aspx - BMI Calculation 