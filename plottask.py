# plottask.py
# Weekly Task 08 - plottask.py
# Author: Amy Reynolds
# Purpose: To display a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

# Reference: 
# https://www.w3schools.com/python/matplotlib_intro.asp
# Ln 21 -23 https://www.w3schools.com/python/matplotlib_labels.asp

import matplotlib.pyplot as plt 
import numpy as np

x = np.array(range(0,4))
y = x * x
z = x * x * x

plt.plot (x, x, label = "linear")
plt.plot(x, y, label = "xsquared")
plt.plot (x, z, label = "xcubed")
plt.legend ()
plt.title ("plottask.py (Weekly Task 8)")
plt.xlabel ("x-axis")
plt.ylabel ("y-axis")
plt.grid()
plt.show()