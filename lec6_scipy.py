# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:12:06 2017

@author: Administrator
"""

from scipy.interpolate import interp1d
import numpy as np

x = np.linspace(-3,3,101)
y = np.sin(x)

import matplotlib.pyplot as plt
'''
plt.plot(x,y)

xx = x[::20]
yy = y[::20]
plt.plot(xx,yy,'r')

f = interp1d(xx,yy,kind="cubic")
xhat = f(x)
plt.plot(x,xhat,'.g')
'''
import scipy.stats as sst
p = sst.norm.pdf(x)
#plt.plot(x,p)

pp = sst.t.pdf(x,10)

#plt.plot(x,pp,'r')

import scipy.optimize as sop
def f(x):
    return x**2-10

a = sop.root(f,5)
print(a)

b = sop.minimize(f, 10)






