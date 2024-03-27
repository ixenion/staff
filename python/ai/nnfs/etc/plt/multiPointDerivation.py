import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x**2

x = np.arange(0,5,0.001)
y = f(x)

plt.plot(x,y)

colors = ["k","g","r","b","c"]

def apx_tang_line(x, apx_derivative):
    return (apx_derivative*x) + b

for i in range(5):
    p2_delta = 0.0001
    x1 = i
    x2 = x1+p2_delta

    y1 = f(x1)
    y2 = f(x2)

    print((x1,y1), (x2,y2))
    apx_derivative = (y2-y1)/(x2-x1)
    print(f"Aproximate derivative for f(x) where x = {x1} is {apx_derivative}")
    b = y2 - (apx_derivative*x2)

    to_plot = [x1-0.6, x1, x1+0.6]
    plt.scatter(x1, y1, c=colors[i])
    plt.plot([point for point in to_plot], [apx_tang_line(point,apx_derivative) for point in to_plot], c=colors[i])

plt.show()
