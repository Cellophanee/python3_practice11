from numpy import *
import matplotlib.pyplot as plt
x = linspace(0, 5)
y = (x ** 1/2) * sin(10 * x)
plt.plot(x, y, 'r-', linewidth=3)
plt.axis([-1, 6, -4, 4])
plt.grid(linestyle='--', linewidth=1)
plt.title('2D Графік Гусюка Даніеля')
plt.legend(['(x^1/2)*sin(10*x)\nx=[0;5]'], loc='lower right')
plt.savefig('Husiuk_Daniel.png', dpi=300)
plt.show()