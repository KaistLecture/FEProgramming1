
import numpy as np
import random
import time

t0 = time.time()

n = 1000000
r = []
for i in range(n):
    r.append(random.normalvariate(0,1))

t1 = time.time()

nr = np.random.randn(n)

t2 = time.time()

print(t1-t0)
print(t2-t1)

    
              