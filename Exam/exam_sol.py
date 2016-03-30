#Problem 1
'''
import random
import pandas as pd

def counter(N):
    d = {}
    for i in range(ord("A"),ord("Z")+1):
        d[chr(i)] = 0
    
    for i in range(N):
        s = chr(random.randint(ord("A"),ord("Z")))
        d[s] += 1
#        if s in d:
#            d[s] += 1
#        else:
#            d[s] = 1   
    return d

ss = counter(10)
sss = pd.Series(ss)
sss.plot(kind="bar")
'''
#%%
#Problem 4
'''
import pandas as pd
import numpy as np
data = pd.read_csv("Data4.csv")
data.index = pd.DatetimeIndex(data.pop("DATE"))
data2 = data.resample("M", how='last').dropna()

#data2["PAYEMS"]
data2.PAYEMS /= 1000
data2.DJIA = np.log(data2.DJIA) * 100
data2 = data2.diff()
print(data2.corr())

res = pd.ols(x=data2.PAYEMS, y=data2.DJIA)
print(res)
alpha = res.beta.intercept
beta = res.beta.x

x = np.linspace(-1,1,2)
y = alpha + beta*x

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
ax.scatter(data2.PAYEMS, data2.DJIA)
ax.plot(x,y,'r')
ax.set_xlim([-1,1])
tit = "$DJIA = %0.3f + %0.3f PAYEMS + \\epsilon$" % (alpha,beta)
ax.set_title(tit, fontsize=20)
fig.show()
'''
#%%
'''
import numpy as np
r = np.random.randn(100000,10)
rr = r.sum(axis=1)
print("Mean = {0}".format(rr.mean()))
print("Std = %g" % rr.std())

k = np.random.randn(100000,100)
kk = k.cumsum(1)
id = np.where(kk<=-2,1,0)
id2 = id * np.arange(1,101)
id3 = np.where(id2==0, 100, id2)
deftime = id3.min(1)
surv = (deftime==100).sum()

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
ax.hist(deftime, bins=100)
ax.set_title("# of Surv. = %d" % surv)
fig.show()
'''
#%%
from itertools import permutations
dist = open("Data2.txt").readlines()
n = len(dist)-1
d = []
for i in range(1, n+1):
    d.append([int(x) for x in dist[i].rstrip("\n").split(";")])

p = permutations(range(n))
minDist = 100000000
minPath = []
for path in p:
    l = d[path[-1]][path[0]]
    for i in range(n-1):
        l += d[path[i]][path[i+1]]
    if l<minDist:
        minDist = l
        minPath = [path]
    elif l==minDist:
        minPath.append(path)

for i in minPath:
    print([chr(x+ord("A")) for x in i])

print("Min. Dist = %d" % minDist)


















