import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x**2

x = np.arange(0,5,0.001)
y = f(x)

plt.plot(x,y)

p2_delta = 0.0001
x1 = 1
x2 = x1+p2_delta

y1 = f(x1)
y2 = f(x2)


print((x1,y1), (x2,y2))
apx_derivative = (y2-y1)/(x2-x1)
print(f"Aproximate derivative for f(x) where x = {x1} is {apx_derivative}")
b = y2 - (apx_derivative*x2)

def tang_line(x):
    return (apx_derivative*x)+b

to_plot = [x1-0.9, x1, x1+0.9]
plt.plot([i for i in to_plot], [tang_line(i) for i in to_plot])
plt.show()
