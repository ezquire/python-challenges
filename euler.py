# Created by Tyler Gearing

import numpy as np

def fprime(x):
    return x**x

def euler(x0, y0, x1, step):
    x = np.linspace(x0, x1, int(x1/step)+1)
    y = np.zeros(len(x))
    y[0] = y0
    for i in range (1, len(x)):
        y[i] = y[i-1] + step*fprime(x[i-1])
    return y[-1]

x0 = int(input('Enter an intial value for x: '))
y0 = int(input('Enter an intial value for f(x): '))
x1 = int(input('Enter value to approximate: '))
step = float(input('Enter a step value: '))

print("Approximation:",euler(x0, y0, x1, step))
