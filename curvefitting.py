import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0 , 4.0 ,8.2 , 10.3])
y = np.array([0.0, 1.2 ,2.8 , 5.6])
z = np.polyfit(x,y,'2')
z

p = np.poly1d(z)
xp = np.linspace(-2,12,100)
plt.plot(x, y, '.', xp, p(xp),'-')
plt.show()
