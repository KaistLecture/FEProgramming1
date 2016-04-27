import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

p = pd.read_excel("stockprice.xlsx")
p.index = p.pop('Date')
r = np.log(p).diff()
r.dropna(inplace=True)
print(r.describe())
print(r.corr())

pp = p / p.ix[0,:]
pp.plot(figsize=(6,3))

#weight: 투자비중
#ret: 종목별 일간로그수익률 데이터 (pandas.DataFrame)
#n: 시뮬레이션 회수
#res: 함수 실행 결과 시뮬레이션 시나리오별 포트폴리오 수익률 (n개)
def histSimulation(weight, ret, n):
    res = np.zeros(n)
    s = np.random.randint(0,len(ret),(n,20))
    for i in range(n):
        sampled = np.exp(ret.ix[s[i,:],:].sum())-1
        pr = np.dot(weight, sampled)
        res[i] = pr
    return res

def mnSimulation(weight, ret, n):
    res = np.zeros(n)
    for i in range(n):
        temp = np.random.multivariate_normal(ret.mean(), ret.cov(), 20)
        sampled = np.exp(temp.sum(axis=0))-1
        pr = np.dot(weight, sampled)
        res[i] = pr
    return res

def performSimulation(weight, ret, n, fun):
    res = fun(weight, ret, n)
    fig, ax = plt.subplots(1,1,figsize=(6,4))
    ax.hist(res, bins=50)
    temp = [res.mean(),res.std(),np.percentile(res,1),np.percentile(res,99)]
    xmax = res.max()
    t = "mean={0:.3%}\nstd={1:.3%}\n1% quantile={2:.3%}\n99% quantile={3:.3%}"
    ax.text(xmax+0.01, n/50, t.format(temp[0],temp[1],temp[2],temp[3]), fontsize=12)
    ax.set_xlim([res.min(), res.max()])
    ax.set_title(fun.__name__)
    fig.show()    
    
numOfStocks = 5
w = np.ones(numOfStocks) / numOfStocks
n = 10000

t0 = time.time()
performSimulation(w,r,n,histSimulation)
performSimulation(w,r,n,mnSimulation)
print("computation time = %0.3f" % (time.time()-t0))

