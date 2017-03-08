import matplotlib.pyplot as plt
import numpy as np
x = np.arange(100)
y = np.random.randn(100)
z = np.cumsum(y)

plt.figure(0)
plt.plot(x, y, 'o-r')
plt.plot(x, z, 's:b')
plt.title(r"$\Delta x^2 + y^2 = \sqrt{z} $")
plt.xlabel("X")
plt.ylabel("return")
plt.legend(['AAA','cumsum'])

plt.figure(1)
plt.plot(np.random.rand(30,2))


fig, ax = plt.subplots(2,2,figsize=(6,8))
ax[0][0].plot(x,y)
ax[0][0].set_title("Plot1")

ax[0][1].hist(y)
ax[1][0].plot(z)
ax[1][0].set_title("Plot 2")
ax[1][1].hist(z)

plt.show()












