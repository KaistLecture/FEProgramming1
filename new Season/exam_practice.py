d = dict()
for i in range(2,13):
    d[i] = []
    
for i in range(1,7):
    for j in range(1,7):
        d[i+j].append((i,j))

for x in d:
    print(x,d[x])
    
#%%
import numpy as np
n = 10000
x = np.random.random((n,10))
y = np.random.random((n,10))

#length = np.zeros((n,1))
length = []
for i in range(n):
    s = 0
    for j in range(10):
        if j==9:
            s += np.sqrt((x[i,j]-x[i,0])**2+(y[i,j]-y[i,0])**2)
        else:
            s += np.sqrt((x[i,j]-x[i,j+1])**2+(y[i,j]-y[i,j+1])**2)
    length.append(s)
length = np.array(length)


'''
dx = np.diff(x, axis=1)
dy = np.diff(y, axis=1)
length = np.sqrt(dx**2 + dy**2).sum(axis=1)
'''
import matplotlib.pyplot as plt
plt.hist(length,bins=30)
print(length.mean())
print(length.std())






