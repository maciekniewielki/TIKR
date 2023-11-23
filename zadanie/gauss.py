import numpy as np
import matplotlib.pyplot as plt

def gauss(x):
    return x

def plot_gauss():
    x = np.linspace(-4, 4, 200)
    y = gauss(x)
    plt.plot(x, y)
    plt.show()
