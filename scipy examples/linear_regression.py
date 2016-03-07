
from scipy.stats import linregress
import numpy as np

def f(x):
    return 2*x

x = np.random.randn(200)
y = f(x) + 0.3*np.random.randn(200)
gradient, intercept, r_value, p_value, std_err = linregress(x,y)

print("intercept = %g"%intercept)
print("slope = %g"%gradient)
print("r^2 = %g"%r_value**2)
print("p_value = %g"%p_value)
print("s.e. = %g"%std_err)
import matplotlib.pyplot as plt
plt.scatter(x,y,marker='+')
plt.xlim([-4,4])
plt.ylim([-8,8])

x1 = np.linspace(-4,4,200)
y1 = intercept + gradient * x1
plt.plot(x1,y1,'r-')
plt.show()

