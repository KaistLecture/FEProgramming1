
import datetime
import scipy.stats as sst
import random
import math
import numpy as np
import time

def parseParams(params):
    s = params['underlying']
    k = params['strike']
    r = params['riskfree']
    q = params['dividend']
    t = (params['matDate'] - params['evalDate']).days / 365.0
    sigma = params['volatility']
    return (s,k,r,q,t,sigma)

def bsprice(params):
    (s,k,r,q,t,sigma) = parseParams(params)
    d1 = (math.log(s/k) + (r-q+0.5*sigma**2)*t) / (sigma*math.sqrt(t))
    d2 = d1 - sigma*math.sqrt(t)
    nd1 = sst.norm.cdf(d1)
    nd2 = sst.norm.cdf(d2)
    call = s*math.exp(-q*t)*nd1 - k*math.exp(-r*t)*nd2
    put =  k*math.exp(-r*t)*(1-nd2) - s*math.exp(-q*t)*(1-nd1)
    price = {"Call":call, "Put":put}
    return price

def mcprice(params):
    m = params['simnum']
    (s,k,r,q,t,sigma) = parseParams(params)
    c = [0]*m;  p=[0]*m;
    drift = (r-q-0.5*sigma**2)*t
    diffusion = sigma*math.sqrt(t)
    for i in range(m):
        e = random.gauss(0,1)
        st = s*math.exp(drift + diffusion*e)
        c[i] = max(st-k, 0.0)
        p[i] = max(k-st, 0.0)
    call = math.exp(-r*t) * sum(c) / m
    put  = math.exp(-r*t) * sum(p) / m
    price = {"Call":call, "Put":put}
    return price

def mcprice_numpy(params):
    m = params['simnum']
    (s,k,r,q,t,sigma) = parseParams(params)
    e = np.random.randn(m)
    s = s*np.exp((r-q-0.5*sigma**2)*t + sigma*np.sqrt(t)*e)
    payoff_call = np.where(s-k>0, s-k, 0.0)
    payoff_put = np.where(k-s>0, k-s, 0.0)
    call = np.exp(-r*t)*payoff_call.mean();
    put = np.exp(-r*t)*payoff_put.mean();
    price = {"Call":call, "Put":put}
    return price

f = open('optioninfo.txt', 'r')
info = f.readlines()
today = datetime.datetime.strptime(info[0][7:17],'%Y-%m-%d')
values = [today];
for i in range(1,5):
    values.append(float(info[i].rstrip("\n").split(": ")[-1]))
    
names = ['evalDate', 'underlying', 'riskfree', 'dividend', 'volatility']

while True:
    method = input("List (1) or NumPy (2) = ")
    if method=='1':  fun = mcprice;  break
    elif method=='2': fun = mcprice_numpy; break
    else: print("Wrong input")

t0 = time.time()
n = 53
params = dict(zip(names,values))
print('='*n)
print('{0:3s}{1:6s}{2:8s}{3:10s}{4:>12s}{5:>12s}'.format("No","Type","Strike","Mat","Analytic","MonteCarlo"))
print('-'*n)
for i in range(6,len(info)):
    c = info[i].rstrip("\n").split("|")
    optionType = c[-1]
    stk = float(c[2])
    mat = datetime.datetime.strptime(c[1],'%Y-%m-%d')
    params.update({'matDate':mat, 'strike':stk, 'simnum':1000000})
    price1 = bsprice(params)[optionType]
    price2 = fun(params)[optionType]
    print('{0:3s}{1:6s}{2:^8s}{3:10s}{4:>12.4f}{5:>12.4f}'.format(c[0],optionType,c[2],mat.strftime("%y/%b/%d"),price1,price2))
print('='*n)
print("computation time = %0.2fsec."%(time.time() - t0))

#%%
print(10)

#%%
print(20)

