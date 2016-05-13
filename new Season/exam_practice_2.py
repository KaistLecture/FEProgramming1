#(1)
import numpy as np
n = 10000
p1 = np.random.random((n,2))
p2 = np.random.random((n,2))
z = np.sqrt(((p1-p2)**2).sum(axis=1))
print("Prob(len>1)={0:.2%}".format((z>=1).sum() / n))

#%%
#(2)
import datetime as dt
import dateutil.relativedelta as dr
def schedule2Day(y,m,d):
    d = dt.datetime(y,m,d)
    d0 = dt.datetime(2016,5,1)
    t = dr.relativedelta(months=1)
    x = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    for i in range(12):
        dd = d+t*(i+1)
        n = (dd-d0).days
        print( dd.strftime("%Y/%m/%d"), x[n%7] )    

schedule2Day(2016,5,18)

#%%
#(3)
import numpy as np
import matplotlib.pyplot as plt
n = 10000
s0 = 10000
mu = 0
sigma = 0.4
corr = 0.5
cov = corr * sigma *sigma
mean = [mu,mu]
covMatrix = [[sigma**2,cov],[cov,sigma**2]]
r = np.random.multivariate_normal(mean,covMatrix,(3,n))
r3 = r.sum(axis=0)
plt.hist(r3,bins=30)
plt.show()
s1 = s0*np.exp(r3)
minS = s1.min(axis=1)
print("Prob(min>10000)={0:.2%}".format((minS>10000).sum() / n))

#%%
#(4)
import numpy as np
def psum(n):
    nums = np.arange(n+1)
    return (nums[:-2] * nums[1:-1] * nums[2:]).sum()    
print("sum = %d" % psum(10))

#%%
#(5)
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("data.xlsx")
data.index = data.pop('Date')
data.dropna(inplace=True)
r = data / data.shift(1)
#or
r1 = np.exp(np.log(data).diff())

r.dropna(inplace=True)
print("Corr=%0.4f" % r.corr().ix[1,0])

model = pd.ols(x=r.MSFT, y=r.AAPL)
alpha = model.beta.intercept
beta = model.beta.x
print("alpha = {0}  beta = {1}".format(alpha,beta))
x = np.array([0.85,1.15])
y = alpha + beta*x

fig, ax = plt.subplots(1,1)
ax.scatter(r.MSFT, r.AAPL, marker='.')
ax.plot(x,y,'r-')
ax.set_title("AAPL vs. MSFT")
ax.set_xlabel("MSFT")
ax.set_ylabel("AAPL")
fig.show()



