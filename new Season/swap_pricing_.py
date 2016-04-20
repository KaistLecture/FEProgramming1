import datetime as dt
from dateutil.relativedelta import relativedelta
from scipy.interpolate import interp1d
import math
import numpy as np

#yield curve loading
data = open("Yield_Curve.txt","r").readlines()
data = [a.rstrip("\n").split("\t") for a in data]
days, yields, dates = [], [], []
for d, y in data:
    date = dt.datetime.strptime(d,"%Y-%m-%d")
    dates.append(date)
    days.append((date-dates[0]).days)
    yields.append(float(y))
today = dates[0]

#functions
def act365(date1, date2):
    return (date2-date1).days / 365
def act360(date1, date2):
    return (date2-date1).days / 360
def spotRate(date, yieldCurve):
    days = (date-today).days
    return yieldCurve(days)
def df(date, yieldCurve):
    return math.exp(-spotRate(date,yieldCurve) 
    * act365(today,date))        
def fwdRate(date1, date2, daycounter, yieldCurve):
    return 1/daycounter(date1,date2)*(df(date1,yieldCurve) / df(date2,yieldCurve) -1)
    
def irs_pricing(today, swaptype, notional, effectiveDate, terminationDate, 
                fixedRate, fixedTenor, fixedDC, 
                indexTenor, spread, floatingTenor, floatingDC, lastFixing,
                yieldCurve):
                    c = 1 if swaptype.upper()=="PAY" else -1
                    #fixed leg
                    d = effectiveDate
                    d1 = d + fixedTenor
                    fixedCF = []
                    npv = 0
                    while d1<=terminationDate:
                        if d1>today:
                            cf = notional * fixedDC(d,d1) * fixedRate
                            fixedCF.append([d1, cf])
                            npv -= cf * df(d1, yieldCurve)
                        d = d1
                        d1 = d + fixedTenor
                    #floating leg
                    d = effectiveDate
                    d1 = d + floatingTenor
                    floatingCF = []
                    while d1<=terminationDate:
                        if d1>today:
                            rate = lastFixing if d<today else fwdRate(d,d1,floatingDC,yieldCurve)
                            cf = notional * floatingDC(d,d1) * rate  
                            floatingCF.append([d1, cf])
                            npv += cf * df(d1, yieldCurve)
                        d = d1
                        d1 = d + floatingTenor
                    return (c*npv, fixedCF, floatingCF)
                    



#input dates should be converted to the number of days from evaluation date
#a fake curve
yieldCurve = interp1d(days, yields)

df_vec = np.vectorize(df)
dfs = df_vec(dates,yieldCurve)
#yield curve plotting
'''
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2,1,figsize=(8,8))
ax[0].plot(dates,yields,"s-")
ax[0].set_title("Yield Curve")
ax[1].plot(dates,dfs,"d-")
ax[1].set_title("Discount Factor")
fig.show()
'''


#swap sample pricing
notional = 10000
swaptype = "Rec"
today = dt.datetime(2016, 3, 16)
effectiveDate = dt.datetime(2014, 1, 5)
terminationDate = dt.datetime(2029, 1, 5)
fixedRate = 0.02
fixedDC = act365
fixedTenor = relativedelta(months = 3)
indexTenor = relativedelta(months = 6)
spread = 0.001
floatingDC = act360
floatingTenor = relativedelta(months = 6)
lastFixing = 0.005

price = irs_pricing(today, swaptype, notional, effectiveDate, terminationDate, 
                    fixedRate, fixedTenor, fixedDC, 
                    indexTenor, spread, floatingTenor, floatingDC, lastFixing,
                    yieldCurve)
print("price = %.3f" % price[0])

import matplotlib.pyplot as plt
fig, ax = plt.subplots(2,1,figsize=(8,8))
fixed = np.array(price[1])
floating = np.array(price[2])
ax[0].bar(fixed[:,0],fixed[:,1], width=60)
ax[1].bar(floating[:,0], floating[:,1], width=60)
fig.show()















