#--------------------------3rd party libraries---------------------------------
#numpy
import numpy as np
a = [3, 4, 5, 6]
b = [6, 5, 4, 3]

print(a + b)

a1 = np.array(a) # output is numpy array (an object)
b1 = np.array(b)
print(a1 + b1)

#matplotlib
import matplotlib.pyplot as plt

x = np.linspace(0, 4 * np.pi, 200)
y = np.sin(x)
plt.plot(x, y)
plt.show()

#pandas
# dataframe and series
import pandas as pd
