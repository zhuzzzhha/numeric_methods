import numpy as np
import matplotlib.pyplot as plt

N = 4     # число экспериментов
sigma = 3   # стандартное отклонение наблюдаемых значений
k = 0.5     # теоретическое значение параметра k
b = 2       # теоретическое значение параметра b

x = [0, 1, 2, 4]
y = [0, 1, 4, 2]

plt.scatter(x, y, s=2, c='blue')
plt.grid(True)
plt.show()

mx = x.sum()/N
my = y.sum()/N
a2 = np.dot(x.T, x)/N
a11 = np.dot(x.T, y)/N
 
kk = (a11 - mx*my)/(a2 - mx**2)
bb = my - kk*mx

ff = np.array([kk*z+bb for z in range(N)])

plt.plot(f)
plt.plot(ff, c='red')
