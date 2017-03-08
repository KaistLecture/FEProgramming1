import numpy as np
import matplotlib.pyplot as plt
import time

t0 = time.time()
n = 100000
m = 10
x = np.random.rand(n, m)
y = np.random.rand(n, m)
x = np.c_[x, x[:,0]]
y = np.c_[y, y[:,0]]
s = np.sqrt(np.diff(x)**2 + np.diff(y)**2).sum(1)
print(s.mean(), s.std())

t1 = time.time()

def distance(x):
    return np.sqrt(np.dot(np.transpose(x),x))

result=np.zeros((100000,1))
for i in range(0,100000):
    data=np.random.rand(2,10)
    total_distance=distance(data[:,0]-data[:,9])
    for j in range(0,9):
        total_distance+=distance(data[:,j]-data[:,j+1])
    result[i,0]=total_distance
    
std = np.std(result)
mean = np.mean(result)
print(mean, std)

t2 = time.time()


print(t1-t0 , t2-t1)
'''
hist, bins=np.histogram(result,100)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
'''

