 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         ICE 10.3

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)
y = np.sin(x)

plt.stem(x,y)
plt.show()
