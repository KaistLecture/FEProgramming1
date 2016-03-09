
from numpy import arange, sin, pi, random, array
x = arange(0, 6e-2, 6e-2 / 30)
A, k, theta = 10, 1.0 / 3e-2, pi / 6
y_true = A * sin(2 * pi * k * x + theta)
y_meas = y_true + 2*random.randn(len(x))

def residuals(p, y, x):
    A, k, theta = p
    err = y - A * sin(2 * pi * k * x + theta)
    return err

from scipy.optimize import leastsq   
p0 = [8, 1 / 2.3e-2, pi / 3] #initial values
plsq = leastsq(residuals, p0, args=(y_meas, x))
print(plsq[0])

def peval(x, p):
    return p[0] * sin(2 * pi * p[1] * x + p[2])
    
import matplotlib.pyplot as plt
plt.plot(x, peval(x, plsq[0]),x,y_meas,'o',x,y_true)
plt.title('Least-squares fit to noisy data')
plt.legend(['Fit', 'Noisy', 'True'])
plt.show()