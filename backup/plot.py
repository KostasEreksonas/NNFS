#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x**2

p2_delta = 0.0001

x1 = 1
x2 = x1+p2_delta

y1 = f(x1)
y2 = f(x2)

approximate_derivative = (y2-y1) / (x2-x1)
print(approximate_derivative)

x = np.arange(0, 50, 0.001)
y = f(x)

plt.plot(x, y)
plt.show()
